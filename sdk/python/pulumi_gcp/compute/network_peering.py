# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class NetworkPeering(pulumi.CustomResource):
    export_custom_routes: pulumi.Output[bool]
    """
    Whether to export the custom routes to the peer network. Defaults to `false`.
    """
    export_subnet_routes_with_public_ip: pulumi.Output[bool]
    """
    Whether subnet routes with public IP range are exported. The default value is true, all subnet routes are exported. The IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always exported to peers and are not controlled by this field.
    """
    import_custom_routes: pulumi.Output[bool]
    """
    Whether to export the custom routes from the peer network. Defaults to `false`.
    """
    import_subnet_routes_with_public_ip: pulumi.Output[bool]
    """
    Whether subnet routes with public IP range are imported. The default value is false. The IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always imported from peers and are not controlled by this field.
    """
    name: pulumi.Output[str]
    """
    Name of the peering.
    """
    network: pulumi.Output[str]
    """
    The primary network of the peering.
    """
    peer_network: pulumi.Output[str]
    """
    The peer network in the peering. The peer network
    may belong to a different project.
    """
    state: pulumi.Output[str]
    """
    State for the peering, either `ACTIVE` or `INACTIVE`. The peering is
    `ACTIVE` when there's a matching configuration in the peer network.
    """
    state_details: pulumi.Output[str]
    """
    Details about the current state of the peering.
    """
    def __init__(__self__, resource_name, opts=None, export_custom_routes=None, export_subnet_routes_with_public_ip=None, import_custom_routes=None, import_subnet_routes_with_public_ip=None, name=None, network=None, peer_network=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a network peering within GCE. For more information see
        [the official documentation](https://cloud.google.com/compute/docs/vpc/vpc-peering)
        and
        [API](https://cloud.google.com/compute/docs/reference/latest/networks).

        > Both network must create a peering with each other for the peering
        to be functional.

        > Subnets IP ranges across peered VPC networks cannot overlap.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] export_custom_routes: Whether to export the custom routes to the peer network. Defaults to `false`.
        :param pulumi.Input[bool] export_subnet_routes_with_public_ip: Whether subnet routes with public IP range are exported. The default value is true, all subnet routes are exported. The IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always exported to peers and are not controlled by this field.
        :param pulumi.Input[bool] import_custom_routes: Whether to export the custom routes from the peer network. Defaults to `false`.
        :param pulumi.Input[bool] import_subnet_routes_with_public_ip: Whether subnet routes with public IP range are imported. The default value is false. The IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always imported from peers and are not controlled by this field.
        :param pulumi.Input[str] name: Name of the peering.
        :param pulumi.Input[str] network: The primary network of the peering.
        :param pulumi.Input[str] peer_network: The peer network in the peering. The peer network
               may belong to a different project.
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

            __props__['export_custom_routes'] = export_custom_routes
            __props__['export_subnet_routes_with_public_ip'] = export_subnet_routes_with_public_ip
            __props__['import_custom_routes'] = import_custom_routes
            __props__['import_subnet_routes_with_public_ip'] = import_subnet_routes_with_public_ip
            __props__['name'] = name
            if network is None:
                raise TypeError("Missing required property 'network'")
            __props__['network'] = network
            if peer_network is None:
                raise TypeError("Missing required property 'peer_network'")
            __props__['peer_network'] = peer_network
            __props__['state'] = None
            __props__['state_details'] = None
        super(NetworkPeering, __self__).__init__(
            'gcp:compute/networkPeering:NetworkPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, export_custom_routes=None, export_subnet_routes_with_public_ip=None, import_custom_routes=None, import_subnet_routes_with_public_ip=None, name=None, network=None, peer_network=None, state=None, state_details=None):
        """
        Get an existing NetworkPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] export_custom_routes: Whether to export the custom routes to the peer network. Defaults to `false`.
        :param pulumi.Input[bool] export_subnet_routes_with_public_ip: Whether subnet routes with public IP range are exported. The default value is true, all subnet routes are exported. The IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always exported to peers and are not controlled by this field.
        :param pulumi.Input[bool] import_custom_routes: Whether to export the custom routes from the peer network. Defaults to `false`.
        :param pulumi.Input[bool] import_subnet_routes_with_public_ip: Whether subnet routes with public IP range are imported. The default value is false. The IPv4 special-use ranges (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are always imported from peers and are not controlled by this field.
        :param pulumi.Input[str] name: Name of the peering.
        :param pulumi.Input[str] network: The primary network of the peering.
        :param pulumi.Input[str] peer_network: The peer network in the peering. The peer network
               may belong to a different project.
        :param pulumi.Input[str] state: State for the peering, either `ACTIVE` or `INACTIVE`. The peering is
               `ACTIVE` when there's a matching configuration in the peer network.
        :param pulumi.Input[str] state_details: Details about the current state of the peering.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["export_custom_routes"] = export_custom_routes
        __props__["export_subnet_routes_with_public_ip"] = export_subnet_routes_with_public_ip
        __props__["import_custom_routes"] = import_custom_routes
        __props__["import_subnet_routes_with_public_ip"] = import_subnet_routes_with_public_ip
        __props__["name"] = name
        __props__["network"] = network
        __props__["peer_network"] = peer_network
        __props__["state"] = state
        __props__["state_details"] = state_details
        return NetworkPeering(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
