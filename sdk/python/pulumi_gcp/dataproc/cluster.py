# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Cluster']


class Cluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_config: Optional[pulumi.Input[pulumi.InputType['ClusterClusterConfigArgs']]] = None,
                 graceful_decommission_timeout: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Cloud Dataproc cluster resource within GCP. For more information see
        [the official dataproc documentation](https://cloud.google.com/dataproc/).

        !> **Warning:** Due to limitations of the API, all arguments except
        `labels`,`cluster_config.worker_config.num_instances` and `cluster_config.preemptible_worker_config.num_instances` are non-updatable. Changing others will cause recreation of the
        whole cluster!

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        simplecluster = gcp.dataproc.Cluster("simplecluster", region="us-central1")
        ```
        ### Advanced

        ```python
        import pulumi
        import pulumi_gcp as gcp

        mycluster = gcp.dataproc.Cluster("mycluster",
            cluster_config=gcp.dataproc.ClusterClusterConfigArgs(
                gce_cluster_config=gcp.dataproc.ClusterClusterConfigGceClusterConfigArgs(
                    service_account_scopes=[
                        "https://www.googleapis.com/auth/monitoring",
                        "useraccounts-ro",
                        "storage-rw",
                        "logging-write",
                    ],
                    tags=[
                        "foo",
                        "bar",
                    ],
                ),
                initialization_actions=[gcp.dataproc.ClusterClusterConfigInitializationActionArgs(
                    script="gs://dataproc-initialization-actions/stackdriver/stackdriver.sh",
                    timeout_sec=500,
                )],
                master_config=gcp.dataproc.ClusterClusterConfigMasterConfigArgs(
                    disk_config=gcp.dataproc.ClusterClusterConfigMasterConfigDiskConfigArgs(
                        boot_disk_size_gb=15,
                        boot_disk_type="pd-ssd",
                    ),
                    machine_type="e2-medium",
                    num_instances=1,
                ),
                preemptible_worker_config=gcp.dataproc.ClusterClusterConfigPreemptibleWorkerConfigArgs(
                    num_instances=0,
                ),
                software_config=gcp.dataproc.ClusterClusterConfigSoftwareConfigArgs(
                    image_version="1.3.7-deb9",
                    override_properties={
                        "dataproc:dataproc.allow.zero.workers": "true",
                    },
                ),
                staging_bucket="dataproc-staging-bucket",
                worker_config={
                    "diskConfig": {
                        "boot_disk_size_gb": 15,
                        "numLocalSsds": 1,
                    },
                    "machine_type": "e2-medium",
                    "min_cpu_platform": "Intel Skylake",
                    "numInstances": 2,
                },
            ),
            graceful_decommission_timeout="120s",
            labels={
                "foo": "bar",
            },
            region="us-central1")
        ```
        ### Using A GPU Accelerator

        ```python
        import pulumi
        import pulumi_gcp as gcp

        accelerated_cluster = gcp.dataproc.Cluster("acceleratedCluster",
            cluster_config=gcp.dataproc.ClusterClusterConfigArgs(
                gce_cluster_config=gcp.dataproc.ClusterClusterConfigGceClusterConfigArgs(
                    zone="us-central1-a",
                ),
                master_config=gcp.dataproc.ClusterClusterConfigMasterConfigArgs(
                    accelerators=[gcp.dataproc.ClusterClusterConfigMasterConfigAcceleratorArgs(
                        accelerator_count=1,
                        accelerator_type="nvidia-tesla-k80",
                    )],
                ),
            ),
            region="us-central1")
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClusterClusterConfigArgs']] cluster_config: Allows you to configure various aspects of the cluster.
               Structure defined below.
        :param pulumi.Input[str] graceful_decommission_timeout: The timeout duration which allows graceful decomissioning when you change the number of worker nodes directly through a
               terraform apply
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The list of labels (key/value pairs) to be applied to
               instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
               which is the name of the cluster.
        :param pulumi.Input[str] name: The name of the cluster, unique within the project and
               zone.
        :param pulumi.Input[str] project: The ID of the project in which the `cluster` will exist. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region in which the cluster and associated nodes will be created in.
               Defaults to `global`.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['cluster_config'] = cluster_config
            __props__['graceful_decommission_timeout'] = graceful_decommission_timeout
            __props__['labels'] = labels
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
        super(Cluster, __self__).__init__(
            'gcp:dataproc/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_config: Optional[pulumi.Input[pulumi.InputType['ClusterClusterConfigArgs']]] = None,
            graceful_decommission_timeout: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClusterClusterConfigArgs']] cluster_config: Allows you to configure various aspects of the cluster.
               Structure defined below.
        :param pulumi.Input[str] graceful_decommission_timeout: The timeout duration which allows graceful decomissioning when you change the number of worker nodes directly through a
               terraform apply
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The list of labels (key/value pairs) to be applied to
               instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
               which is the name of the cluster.
        :param pulumi.Input[str] name: The name of the cluster, unique within the project and
               zone.
        :param pulumi.Input[str] project: The ID of the project in which the `cluster` will exist. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region in which the cluster and associated nodes will be created in.
               Defaults to `global`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_config"] = cluster_config
        __props__["graceful_decommission_timeout"] = graceful_decommission_timeout
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["project"] = project
        __props__["region"] = region
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> pulumi.Output['outputs.ClusterClusterConfig']:
        """
        Allows you to configure various aspects of the cluster.
        Structure defined below.
        """
        return pulumi.get(self, "cluster_config")

    @property
    @pulumi.getter(name="gracefulDecommissionTimeout")
    def graceful_decommission_timeout(self) -> pulumi.Output[Optional[str]]:
        """
        The timeout duration which allows graceful decomissioning when you change the number of worker nodes directly through a
        terraform apply
        """
        return pulumi.get(self, "graceful_decommission_timeout")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The list of labels (key/value pairs) to be applied to
        instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
        which is the name of the cluster.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the cluster, unique within the project and
        zone.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the `cluster` will exist. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region in which the cluster and associated nodes will be created in.
        Defaults to `global`.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

