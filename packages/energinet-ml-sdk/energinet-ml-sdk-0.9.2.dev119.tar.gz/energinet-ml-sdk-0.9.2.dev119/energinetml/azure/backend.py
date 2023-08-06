#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[summary]
"""
import re
from functools import cached_property
from typing import List

import azureml
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azureml._common.exceptions import AzureMLException
from azureml.core import ComputeTarget, Environment, Experiment
from azureml.core import Model as AzureMLModel
from azureml.core import RunConfiguration, ScriptRunConfig, Workspace
from azureml.core.authentication import AzureCliAuthentication
from azureml.core.compute import AmlCompute
from azureml.core.conda_dependencies import CondaDependencies

from energinetml.core.backend import AbstractBackend
from energinetml.core.model import Model as EnerginetMLModel
from energinetml.settings import (
    CLUSTER_IDLE_SECONDS_BEFORE_SCALEDOWN,
    PACKAGE_NAME,
    PYTHON_VERSION,
)

from .submitting import AzureSubmitContext
from .training import AzureCloudTrainingContext, AzureLocalTrainingContext


class AzureBackend(AbstractBackend):
    def parse_azureml_exception(
        self, e: AzureMLException
    ) -> AbstractBackend.BackendException:
        """Extracts error message from AzureMLException and
        returns a BackendException.

        Args:
            e (AzureMLException): [description]

        Returns:
            AbstractBackend.BackendException: [description]
        """
        msg = str(e)
        matches = re.findall(r'"message":"([^"]+)"', msg)
        if matches:
            return self.BackendException(matches[0])
        else:
            return self.BackendException(msg)

    @cached_property
    def _credential(self) -> AzureCliAuthentication:
        """[summary]

        Returns:
            AzureCliAuthentication: [description]
        """
        return AzureCliAuthentication()

    def get_available_subscriptions(self) -> List[str]:
        """[summary]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            List[str]: [description]
        """
        subscription_client = SubscriptionClient(self._credential)
        try:
            return list(subscription_client.subscriptions.list())
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)

    def get_available_resource_groups(self, subscription_id: str) -> List[str]:
        """[summary]

        Args:
            subscription_id (str): [description]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            List[str]: [description]
        """
        resource_client = ResourceManagementClient(self._credential, subscription_id)
        try:
            return list(resource_client.resource_groups.list())
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)

    # -- Workspaces ----------------------------------------------------------

    def get_available_workspaces(
        self, subscription_id: str, resource_group: str
    ) -> List[Workspace]:
        """[summary]

        Args:
            subscription_id (str): [description]
            resource_group (str): [description]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            List[Workspace]: [description]
        """
        try:
            workspaces_mapped = Workspace.list(
                auth=self._credential,
                subscription_id=subscription_id,
                resource_group=resource_group,
            )
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)

        workspaces = []

        for workspace_list in workspaces_mapped.values():
            workspaces.extend(workspace_list)

        return workspaces

    def get_available_workspace_names(
        self, subscription_id: str, resource_group: str
    ) -> List[str]:
        """[summary]

        Args:
            subscription_id (str): [description]
            resource_group (str): [description]

        Returns:
            List[str]: [description]
        """
        available_workspaces = self.get_available_workspaces(
            subscription_id=subscription_id, resource_group=resource_group
        )

        return [w.name for w in available_workspaces]

    def get_workspace(
        self, subscription_id: str, resource_group: str, name: str
    ) -> Workspace:
        """[summary]

        Args:
            subscription_id (str): [description]
            resource_group (str): [description]
            name (str): [description]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            Workspace: [description]
        """
        try:
            return Workspace.get(
                auth=self._credential,
                subscription_id=subscription_id,
                resource_group=resource_group,
                name=name,
            )
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)

    # -- Compute clusters ----------------------------------------------------

    def get_compute_clusters(self, workspace: Workspace) -> List[AmlCompute]:
        """[summary]

        Args:
            workspace (Workspace): [description]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            List[AmlCompute]: [description]
        """
        try:
            return AmlCompute.list(workspace=workspace)
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)

    def get_available_vm_sizes(self, workspace: Workspace) -> List[str]:
        """[summary]

        Args:
            workspace (Workspace): [description]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            List[str]: [description]
        """
        try:
            return AmlCompute.supported_vmsizes(workspace=workspace)
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)

    def create_compute_cluster(
        self,
        workspace: Workspace,
        name: str,
        vm_size: str,
        min_nodes: int,
        max_nodes: int,
        vnet_resource_group_name: str,
        vnet_name: str,
        subnet_name: str,
    ) -> None:
        """[summary]

        Args:
            workspace (Workspace): [description]
            name (str): [description]
            vm_size (str): [description]
            min_nodes (int): [description]
            max_nodes (int): [description]
            vnet_resource_group_name (str): [description]
            vnet_name (str): [description]
            subnet_name (str): [description]

        Raises:
            self.parse_azureml_exception: [description]
        """

        compute_config = AmlCompute.provisioning_configuration(
            vm_size=vm_size,
            min_nodes=min_nodes,
            max_nodes=max_nodes,
            vnet_resourcegroup_name=vnet_resource_group_name,
            vnet_name=vnet_name,
            subnet_name=subnet_name,
            idle_seconds_before_scaledown=CLUSTER_IDLE_SECONDS_BEFORE_SCALEDOWN,
        )

        try:
            ComputeTarget.create(workspace, name, compute_config).wait_for_completion(
                show_output=False
            )
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)

    # -- Contexts ------------------------------------------------------------

    def get_local_training_context(
        self, force_download: bool
    ) -> AzureLocalTrainingContext:
        """[summary]

        Args:
            force_download (bool): [description]

        Returns:
            AzureLocalTrainingContext: [description]
        """
        return AzureLocalTrainingContext(self, force_download)

    def get_cloud_training_context(self) -> AzureCloudTrainingContext:
        """[summary]

        Returns:
            AzureCloudTrainingContext: [description]
        """
        return AzureCloudTrainingContext()

    def submit_model(
        self, model: EnerginetMLModel, params: List[str]
    ) -> AzureSubmitContext:
        """[summary]

        Args:
            model (Model): [description]
            params (List[str]): [description]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            AzureSubmitContext: [description]
        """
        cd = CondaDependencies()
        cd.set_python_version(PYTHON_VERSION)

        # Project requirements (from requirements.txt)
        for requirement in model.requirements:
            cd.add_pip_package(requirement.line)

        # Python environment
        env = Environment(model.requirements.get(PACKAGE_NAME).line)
        env.python.conda_dependencies = cd

        compute_config = RunConfiguration()
        compute_config.target = model.compute_target
        compute_config.environment = env

        workspace = self.get_workspace(
            name=model.project.workspace_name,
            subscription_id=model.project.subscription_id,
            resource_group=model.project.resource_group,
        )

        experiment = Experiment(workspace=workspace, name=model.experiment)

        with model.temporary_folder() as path:
            config = ScriptRunConfig(
                source_directory=path,
                script=model.SCRIPT_FILE_NAME,
                arguments=["model", "train", "--cloud-mode"] + list(params),
                run_config=compute_config,
            )

            try:
                run = experiment.submit(config)
            except azureml._common.exceptions.AzureMLException as e:
                raise self.parse_azureml_exception(e)

            return AzureSubmitContext(model, run)

    def release_model(
        self, workspace: Workspace, model_path: str, model_name: str, **kwargs
    ) -> AzureMLModel:
        """[summary]

        Args:
            workspace (Workspace): [description]
            model_path (str): [description]
            model_name (str): [description]

        Raises:
            self.parse_azureml_exception: [description]

        Returns:
            AzureMLModel: [description]
        """
        try:
            asset = AzureMLModel._create_asset(
                workspace.service_context, model_path, model_name, None
            )

            return AzureMLModel._register_with_asset(
                workspace=workspace, model_name=model_name, asset_id=asset.id, **kwargs
            )
        except azureml._common.exceptions.AzureMLException as e:
            raise self.parse_azureml_exception(e)
