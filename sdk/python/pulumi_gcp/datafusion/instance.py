# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Instance(pulumi.CustomResource):
    create_time: pulumi.Output[str]
    """
    The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
    """
    description: pulumi.Output[str]
    """
    An optional description of the instance.
    """
    enable_stackdriver_logging: pulumi.Output[bool]
    """
    Option to enable Stackdriver Logging.
    """
    enable_stackdriver_monitoring: pulumi.Output[bool]
    """
    Option to enable Stackdriver Monitoring.
    """
    labels: pulumi.Output[dict]
    """
    The resource labels for instance to use to annotate any related underlying resources,
    such as Compute Engine VMs.
    """
    name: pulumi.Output[str]
    """
    The ID of the instance or a fully qualified identifier for the instance.
    """
    network_config: pulumi.Output[dict]
    """
    Network configuration options. These are required when a private Data Fusion instance is to be created.
    Structure is documented below.

      * `ipAllocation` (`str`) - The IP range in CIDR notation to use for the managed Data Fusion instance
        nodes. This range must not overlap with any other ranges used in the Data Fusion instance network.
      * `network` (`str`) - Name of the network in the project with which the tenant project
        will be peered for executing pipelines. In case of shared VPC where the network resides in another host
        project the network should specified in the form of projects/{host-project-id}/global/networks/{network}
    """
    options: pulumi.Output[dict]
    """
    Map of additional options used to configure the behavior of Data Fusion instance.
    """
    private_instance: pulumi.Output[bool]
    """
    Specifies whether the Data Fusion instance should be private. If set to
    true, all Data Fusion nodes will have private IP addresses and will not be
    able to access the public internet.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    region: pulumi.Output[str]
    """
    The region of the Data Fusion instance.
    """
    service_account: pulumi.Output[str]
    """
    Service account which will be used to access resources in the customer project.
    """
    service_endpoint: pulumi.Output[str]
    """
    Endpoint on which the Data Fusion UI and REST APIs are accessible.
    """
    state: pulumi.Output[str]
    """
    The current state of this Data Fusion instance. - CREATING: Instance is being created - RUNNING: Instance is running and
    ready for requests - FAILED: Instance creation failed - DELETING: Instance is being deleted - UPGRADING: Instance is
    being upgraded - RESTARTING: Instance is being restarted
    """
    state_message: pulumi.Output[str]
    """
    Additional information about the current state of this Data Fusion instance if available.
    """
    type: pulumi.Output[str]
    """
    Represents the type of Data Fusion instance. Each type is configured with
    the default settings for processing and memory.
    - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines
    using point and click UI. However, there are certain limitations, such as fewer number
    of concurrent pipelines, no support for streaming pipelines, etc.
    - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more features
    available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
    Possible values are `BASIC` and `ENTERPRISE`.
    """
    update_time: pulumi.Output[str]
    """
    The time the instance was last updated in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
    """
    version: pulumi.Output[str]
    """
    Current version of the Data Fusion.
    """
    def __init__(__self__, resource_name, opts=None, description=None, enable_stackdriver_logging=None, enable_stackdriver_monitoring=None, labels=None, name=None, network_config=None, options=None, private_instance=None, project=None, region=None, type=None, version=None, __props__=None, __name__=None, __opts__=None):
        """
        Represents a Data Fusion instance.

        To get more information about Instance, see:

        * [API documentation](https://cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/data-fusion/docs/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of the instance.
        :param pulumi.Input[bool] enable_stackdriver_logging: Option to enable Stackdriver Logging.
        :param pulumi.Input[bool] enable_stackdriver_monitoring: Option to enable Stackdriver Monitoring.
        :param pulumi.Input[dict] labels: The resource labels for instance to use to annotate any related underlying resources,
               such as Compute Engine VMs.
        :param pulumi.Input[str] name: The ID of the instance or a fully qualified identifier for the instance.
        :param pulumi.Input[dict] network_config: Network configuration options. These are required when a private Data Fusion instance is to be created.
               Structure is documented below.
        :param pulumi.Input[dict] options: Map of additional options used to configure the behavior of Data Fusion instance.
        :param pulumi.Input[bool] private_instance: Specifies whether the Data Fusion instance should be private. If set to
               true, all Data Fusion nodes will have private IP addresses and will not be
               able to access the public internet.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region of the Data Fusion instance.
        :param pulumi.Input[str] type: Represents the type of Data Fusion instance. Each type is configured with
               the default settings for processing and memory.
               - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines
               using point and click UI. However, there are certain limitations, such as fewer number
               of concurrent pipelines, no support for streaming pipelines, etc.
               - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more features
               available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
               Possible values are `BASIC` and `ENTERPRISE`.
        :param pulumi.Input[str] version: Current version of the Data Fusion.

        The **network_config** object supports the following:

          * `ipAllocation` (`pulumi.Input[str]`) - The IP range in CIDR notation to use for the managed Data Fusion instance
            nodes. This range must not overlap with any other ranges used in the Data Fusion instance network.
          * `network` (`pulumi.Input[str]`) - Name of the network in the project with which the tenant project
            will be peered for executing pipelines. In case of shared VPC where the network resides in another host
            project the network should specified in the form of projects/{host-project-id}/global/networks/{network}
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['description'] = description
            __props__['enable_stackdriver_logging'] = enable_stackdriver_logging
            __props__['enable_stackdriver_monitoring'] = enable_stackdriver_monitoring
            __props__['labels'] = labels
            __props__['name'] = name
            __props__['network_config'] = network_config
            __props__['options'] = options
            __props__['private_instance'] = private_instance
            __props__['project'] = project
            __props__['region'] = region
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['version'] = version
            __props__['create_time'] = None
            __props__['service_account'] = None
            __props__['service_endpoint'] = None
            __props__['state'] = None
            __props__['state_message'] = None
            __props__['update_time'] = None
        super(Instance, __self__).__init__(
            'gcp:datafusion/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, create_time=None, description=None, enable_stackdriver_logging=None, enable_stackdriver_monitoring=None, labels=None, name=None, network_config=None, options=None, private_instance=None, project=None, region=None, service_account=None, service_endpoint=None, state=None, state_message=None, type=None, update_time=None, version=None):
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
        :param pulumi.Input[str] description: An optional description of the instance.
        :param pulumi.Input[bool] enable_stackdriver_logging: Option to enable Stackdriver Logging.
        :param pulumi.Input[bool] enable_stackdriver_monitoring: Option to enable Stackdriver Monitoring.
        :param pulumi.Input[dict] labels: The resource labels for instance to use to annotate any related underlying resources,
               such as Compute Engine VMs.
        :param pulumi.Input[str] name: The ID of the instance or a fully qualified identifier for the instance.
        :param pulumi.Input[dict] network_config: Network configuration options. These are required when a private Data Fusion instance is to be created.
               Structure is documented below.
        :param pulumi.Input[dict] options: Map of additional options used to configure the behavior of Data Fusion instance.
        :param pulumi.Input[bool] private_instance: Specifies whether the Data Fusion instance should be private. If set to
               true, all Data Fusion nodes will have private IP addresses and will not be
               able to access the public internet.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region of the Data Fusion instance.
        :param pulumi.Input[str] service_account: Service account which will be used to access resources in the customer project.
        :param pulumi.Input[str] service_endpoint: Endpoint on which the Data Fusion UI and REST APIs are accessible.
        :param pulumi.Input[str] state: The current state of this Data Fusion instance. - CREATING: Instance is being created - RUNNING: Instance is running and
               ready for requests - FAILED: Instance creation failed - DELETING: Instance is being deleted - UPGRADING: Instance is
               being upgraded - RESTARTING: Instance is being restarted
        :param pulumi.Input[str] state_message: Additional information about the current state of this Data Fusion instance if available.
        :param pulumi.Input[str] type: Represents the type of Data Fusion instance. Each type is configured with
               the default settings for processing and memory.
               - BASIC: Basic Data Fusion instance. In Basic type, the user will be able to create data pipelines
               using point and click UI. However, there are certain limitations, such as fewer number
               of concurrent pipelines, no support for streaming pipelines, etc.
               - ENTERPRISE: Enterprise Data Fusion instance. In Enterprise type, the user will have more features
               available, such as support for streaming pipelines, higher number of concurrent pipelines, etc.
               Possible values are `BASIC` and `ENTERPRISE`.
        :param pulumi.Input[str] update_time: The time the instance was last updated in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
        :param pulumi.Input[str] version: Current version of the Data Fusion.

        The **network_config** object supports the following:

          * `ipAllocation` (`pulumi.Input[str]`) - The IP range in CIDR notation to use for the managed Data Fusion instance
            nodes. This range must not overlap with any other ranges used in the Data Fusion instance network.
          * `network` (`pulumi.Input[str]`) - Name of the network in the project with which the tenant project
            will be peered for executing pipelines. In case of shared VPC where the network resides in another host
            project the network should specified in the form of projects/{host-project-id}/global/networks/{network}
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = create_time
        __props__["description"] = description
        __props__["enable_stackdriver_logging"] = enable_stackdriver_logging
        __props__["enable_stackdriver_monitoring"] = enable_stackdriver_monitoring
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["network_config"] = network_config
        __props__["options"] = options
        __props__["private_instance"] = private_instance
        __props__["project"] = project
        __props__["region"] = region
        __props__["service_account"] = service_account
        __props__["service_endpoint"] = service_endpoint
        __props__["state"] = state
        __props__["state_message"] = state_message
        __props__["type"] = type
        __props__["update_time"] = update_time
        __props__["version"] = version
        return Instance(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
