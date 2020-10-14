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

__all__ = ['PerInstanceConfig']


class PerInstanceConfig(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_group_manager: Optional[pulumi.Input[str]] = None,
                 minimal_action: Optional[pulumi.Input[str]] = None,
                 most_disruptive_allowed_action: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preserved_state: Optional[pulumi.Input[pulumi.InputType['PerInstanceConfigPreservedStateArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remove_instance_state_on_destroy: Optional[pulumi.Input[bool]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A config defined for a single managed instance that belongs to an instance group manager. It preserves the instance name
        across instance group manager operations and can define stateful disks or metadata that are unique to the instance.

        To get more information about PerInstanceConfig, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/instance-groups/stateful-migs#per-instance_configs)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_group_manager: The instance group manager this instance config is part of.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input[pulumi.InputType['PerInstanceConfigPreservedStateArgs']] preserved_state: The preserved state for this instance.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        :param pulumi.Input[str] zone: Zone where the containing instance group manager is located
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

            if instance_group_manager is None:
                raise TypeError("Missing required property 'instance_group_manager'")
            __props__['instance_group_manager'] = instance_group_manager
            __props__['minimal_action'] = minimal_action
            __props__['most_disruptive_allowed_action'] = most_disruptive_allowed_action
            __props__['name'] = name
            __props__['preserved_state'] = preserved_state
            __props__['project'] = project
            __props__['remove_instance_state_on_destroy'] = remove_instance_state_on_destroy
            if zone is None:
                raise TypeError("Missing required property 'zone'")
            __props__['zone'] = zone
        super(PerInstanceConfig, __self__).__init__(
            'gcp:compute/perInstanceConfig:PerInstanceConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_group_manager: Optional[pulumi.Input[str]] = None,
            minimal_action: Optional[pulumi.Input[str]] = None,
            most_disruptive_allowed_action: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            preserved_state: Optional[pulumi.Input[pulumi.InputType['PerInstanceConfigPreservedStateArgs']]] = None,
            project: Optional[pulumi.Input[str]] = None,
            remove_instance_state_on_destroy: Optional[pulumi.Input[bool]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'PerInstanceConfig':
        """
        Get an existing PerInstanceConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_group_manager: The instance group manager this instance config is part of.
        :param pulumi.Input[str] minimal_action: The minimal action to perform on the instance during an update.
               Default is `NONE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] most_disruptive_allowed_action: The most disruptive action to perform on the instance during an update.
               Default is `REPLACE`. Possible values are:
               * REPLACE
               * RESTART
               * REFRESH
               * NONE
        :param pulumi.Input[str] name: The name for this per-instance config and its corresponding instance.
        :param pulumi.Input[pulumi.InputType['PerInstanceConfigPreservedStateArgs']] preserved_state: The preserved state for this instance.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[bool] remove_instance_state_on_destroy: When true, deleting this config will immediately remove any specified state from the underlying instance.
               When false, deleting this config will *not* immediately remove any state from the underlying instance.
               State will be removed on the next instance recreation or update.
        :param pulumi.Input[str] zone: Zone where the containing instance group manager is located
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["instance_group_manager"] = instance_group_manager
        __props__["minimal_action"] = minimal_action
        __props__["most_disruptive_allowed_action"] = most_disruptive_allowed_action
        __props__["name"] = name
        __props__["preserved_state"] = preserved_state
        __props__["project"] = project
        __props__["remove_instance_state_on_destroy"] = remove_instance_state_on_destroy
        __props__["zone"] = zone
        return PerInstanceConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceGroupManager")
    def instance_group_manager(self) -> pulumi.Output[str]:
        """
        The instance group manager this instance config is part of.
        """
        return pulumi.get(self, "instance_group_manager")

    @property
    @pulumi.getter(name="minimalAction")
    def minimal_action(self) -> pulumi.Output[Optional[str]]:
        """
        The minimal action to perform on the instance during an update.
        Default is `NONE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "minimal_action")

    @property
    @pulumi.getter(name="mostDisruptiveAllowedAction")
    def most_disruptive_allowed_action(self) -> pulumi.Output[Optional[str]]:
        """
        The most disruptive action to perform on the instance during an update.
        Default is `REPLACE`. Possible values are:
        * REPLACE
        * RESTART
        * REFRESH
        * NONE
        """
        return pulumi.get(self, "most_disruptive_allowed_action")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for this per-instance config and its corresponding instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preservedState")
    def preserved_state(self) -> pulumi.Output[Optional['outputs.PerInstanceConfigPreservedState']]:
        """
        The preserved state for this instance.
        Structure is documented below.
        """
        return pulumi.get(self, "preserved_state")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="removeInstanceStateOnDestroy")
    def remove_instance_state_on_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        When true, deleting this config will immediately remove any specified state from the underlying instance.
        When false, deleting this config will *not* immediately remove any state from the underlying instance.
        State will be removed on the next instance recreation or update.
        """
        return pulumi.get(self, "remove_instance_state_on_destroy")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        Zone where the containing instance group manager is located
        """
        return pulumi.get(self, "zone")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

