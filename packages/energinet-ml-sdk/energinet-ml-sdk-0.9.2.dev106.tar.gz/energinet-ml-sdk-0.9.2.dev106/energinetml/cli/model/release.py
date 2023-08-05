#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[summary]
"""
import os
import tempfile
import zipfile

import click
import click_spinner
from azureml.core import Experiment as AzExperiment
from azureml.core import Run as AzRun
from azureml.core import Workspace

from energinetml.backend import default_backend as backend
from energinetml.cli.utils import discover_model
from energinetml.core.model import Model, TrainedModel

# -- CLI Command -------------------------------------------------------------


@click.command()
@discover_model()
@click.option(
    "--run-id",
    "-r",
    "run_id",
    type=str,
    required=False,
    default=None,
    help="Run ID to release",
)
def release(run_id: str, model: Model) -> None:
    """Release a model."""
    project = model.project

    workspace = backend.get_workspace(
        name=project.workspace_name,
        subscription_id=project.subscription_id,
        resource_group=project.resource_group,
    )

    if run_id is None:
        run_id = _get_run_id_if_omitted(workspace, model)

    run = AzRun.get(workspace=workspace, run_id=run_id)

    # -- Download files ------------------------------------------------------

    click.echo("Releasing model using Run ID: %s" % run_id)

    with tempfile.TemporaryDirectory() as temp_folder_path:

        # -- Download resources ----------------------------------------------

        # Download project snapshot (model.py, model.json, etc).
        # Snapshot is downloaded as a zip-archive.
        click.echo("Downloading model code snapshot")
        with click_spinner.spinner():
            snapshot_zip_path = run.restore_snapshot(path=temp_folder_path)

        # Download the trained model file (artifact).
        click.echo("Downloading trained model file")
        with click_spinner.spinner():
            # Trained model file path relative to model root
            trained_model_relative_path = model.get_relative_file_path(
                model.trained_model_path
            )

            # Absolute path where trained model file is downloaded to
            trained_model_absolute_path = os.path.join(
                temp_folder_path, trained_model_relative_path
            )

            # Download trained model file
            run.download_file(
                name=trained_model_relative_path,
                output_file_path=trained_model_absolute_path,
            )

        # -- Handle resources ------------------------------------------------

        # Instantiate TrainedModel object to test its existence and validity
        try:
            TrainedModel.load(trained_model_absolute_path)
        except Exception:
            # TODO Error handling
            click.echo("-" * 79)
            click.echo("Failed to load trained model, exception follows:")
            click.echo("-" * 79)
            raise

        # Add trained model file to existing archive
        click.echo("Archiving files")
        with click_spinner.spinner():
            z = zipfile.ZipFile(snapshot_zip_path, "a")
            z.write(
                filename=trained_model_absolute_path,
                arcname=trained_model_relative_path,
            )
            z.close()

        # -- Create Model ----------------------------------------------------

        # Can not use run.register_model() here, as its only able to copy
        # files from the Run's output folder, and we also want to package
        # the project files (from the restored snapshot).
        with click_spinner.spinner():
            model_tags = {k: v for k, v in run.tags.items() if not k.startswith("_")}
            model_tags.update({"run_id": run_id})

            model = backend.release_model(
                workspace=workspace,
                model_path=snapshot_zip_path,
                model_name=model.name,
                properties=run.properties,
                description="TODO Describe me!",
                run_id=run_id,
                tags=model_tags,
            )

            click.echo(f"Released new model {model.name} version {model.version}")


# -- Helper functions --------------------------------------------------------


def _get_run_id_if_omitted(workspace: Workspace, model: Model) -> str:
    """[summary]

    Args:
        workspace (Workspace): [description]
        model (Model): [description]

    Raises:
        click.Abort: [description]

    Returns:
        str: [description]
    """
    experiment = AzExperiment(workspace=workspace, name=model.experiment)

    latest_runs = list(AzRun.list(experiment=experiment))

    if not latest_runs:
        click.echo(f"No runs exists for experiment {model.experiment}")
        raise click.Abort()

    latest_run_id = latest_runs[0].id

    use_latest_run = click.confirm(
        (
            "You did not provide me with a Run ID. "
            f"Would you like to use the latest (Run ID: {latest_run_id})?"
        )
    )

    if use_latest_run is False:
        click.echo(
            "I do not know which run to release. Provide me with a "
            "Run ID using the -r/--run-id parameter."
        )
        raise click.Abort()

    return latest_run_id
