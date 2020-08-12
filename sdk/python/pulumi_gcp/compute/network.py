# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Network(pulumi.CustomResource):
    auto_create_subnetworks: pulumi.Output[bool]
    """
    When set to `true`, the network is created in "auto subnet mode" and
    it will create a subnet for each region automatically across the
    `10.128.0.0/9` address range.
    When set to `false`, the network is created in "custom subnet mode" so
    the user can explicitly connect subnetwork resources.
    """
    delete_default_routes_on_create: pulumi.Output[bool]
    """
    If set to `true`, default routes (`0.0.0.0/0`) will be deleted
    immediately after network creation. Defaults to `false`.
    """
    description: pulumi.Output[str]
    """
    An optional description of this resource. The resource must be
    recreated to modify this field.
    """
    gateway_ipv4: pulumi.Output[str]
    """
    The gateway address for default routing out of the network. This value is selected by GCP.
    """
    name: pulumi.Output[str]
    """
    Name of the resource. Provided by the client when the resource is
    created. The name must be 1-63 characters long, and comply with
    RFC1035. Specifically, the name must be 1-63 characters long and match
    the regular expression `a-z?` which means the
    first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last
    character, which cannot be a dash.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    routing_mode: pulumi.Output[str]
    """
    The network-wide routing mode to use. If set to `REGIONAL`, this
    network's cloud routers will only advertise routes with subnetworks
    of this network in the same region as the router. If set to `GLOBAL`,
    this network's cloud routers will advertise routes with all
    subnetworks of this network, across regions.
    Possible values are `REGIONAL` and `GLOBAL`.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    def __init__(__self__, resource_name, opts=None, auto_create_subnetworks=None, delete_default_routes_on_create=None, description=None, name=None, project=None, routing_mode=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a VPC network or legacy network resource on GCP.

        To get more information about Network, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/networks)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/vpc/docs/vpc)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_create_subnetworks: When set to `true`, the network is created in "auto subnet mode" and
               it will create a subnet for each region automatically across the
               `10.128.0.0/9` address range.
               When set to `false`, the network is created in "custom subnet mode" so
               the user can explicitly connect subnetwork resources.
        :param pulumi.Input[bool] delete_default_routes_on_create: If set to `true`, default routes (`0.0.0.0/0`) will be deleted
               immediately after network creation. Defaults to `false`.
        :param pulumi.Input[str] description: An optional description of this resource. The resource must be
               recreated to modify this field.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] routing_mode: The network-wide routing mode to use. If set to `REGIONAL`, this
               network's cloud routers will only advertise routes with subnetworks
               of this network in the same region as the router. If set to `GLOBAL`,
               this network's cloud routers will advertise routes with all
               subnetworks of this network, across regions.
               Possible values are `REGIONAL` and `GLOBAL`.
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

            __props__['auto_create_subnetworks'] = auto_create_subnetworks
            __props__['delete_default_routes_on_create'] = delete_default_routes_on_create
            __props__['description'] = description
            __props__['name'] = name
            __props__['project'] = project
            __props__['routing_mode'] = routing_mode
            __props__['gateway_ipv4'] = None
            __props__['self_link'] = None
        super(Network, __self__).__init__(
            'gcp:compute/network:Network',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, auto_create_subnetworks=None, delete_default_routes_on_create=None, description=None, gateway_ipv4=None, name=None, project=None, routing_mode=None, self_link=None):
        """
        Get an existing Network resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_create_subnetworks: When set to `true`, the network is created in "auto subnet mode" and
               it will create a subnet for each region automatically across the
               `10.128.0.0/9` address range.
               When set to `false`, the network is created in "custom subnet mode" so
               the user can explicitly connect subnetwork resources.
        :param pulumi.Input[bool] delete_default_routes_on_create: If set to `true`, default routes (`0.0.0.0/0`) will be deleted
               immediately after network creation. Defaults to `false`.
        :param pulumi.Input[str] description: An optional description of this resource. The resource must be
               recreated to modify this field.
        :param pulumi.Input[str] gateway_ipv4: The gateway address for default routing out of the network. This value is selected by GCP.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] routing_mode: The network-wide routing mode to use. If set to `REGIONAL`, this
               network's cloud routers will only advertise routes with subnetworks
               of this network in the same region as the router. If set to `GLOBAL`,
               this network's cloud routers will advertise routes with all
               subnetworks of this network, across regions.
               Possible values are `REGIONAL` and `GLOBAL`.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auto_create_subnetworks"] = auto_create_subnetworks
        __props__["delete_default_routes_on_create"] = delete_default_routes_on_create
        __props__["description"] = description
        __props__["gateway_ipv4"] = gateway_ipv4
        __props__["name"] = name
        __props__["project"] = project
        __props__["routing_mode"] = routing_mode
        __props__["self_link"] = self_link
        return Network(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
