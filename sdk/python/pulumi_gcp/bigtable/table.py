# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Table(pulumi.CustomResource):
    column_families: pulumi.Output[list]
    """
    A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.

      * `family` (`str`) - The name of the column family.
    """
    instance_name: pulumi.Output[str]
    """
    The name of the Bigtable instance.
    """
    name: pulumi.Output[str]
    """
    The name of the table.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    split_keys: pulumi.Output[list]
    """
    A list of predefined keys to split the table on.
    !> **Warning:** Modifying the `split_keys` of an existing table will cause the provider
    to delete/recreate the entire `bigtable.Table` resource.
    """
    def __init__(__self__, resource_name, opts=None, column_families=None, instance_name=None, name=None, project=None, split_keys=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates a Google Cloud Bigtable table inside an instance. For more information see
        [the official documentation](https://cloud.google.com/bigtable/) and
        [API](https://cloud.google.com/bigtable/docs/go/reference).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] column_families: A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.
        :param pulumi.Input[str] instance_name: The name of the Bigtable instance.
        :param pulumi.Input[str] name: The name of the table.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[list] split_keys: A list of predefined keys to split the table on.
               !> **Warning:** Modifying the `split_keys` of an existing table will cause the provider
               to delete/recreate the entire `bigtable.Table` resource.

        The **column_families** object supports the following:

          * `family` (`pulumi.Input[str]`) - The name of the column family.
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

            __props__['column_families'] = column_families
            if instance_name is None:
                raise TypeError("Missing required property 'instance_name'")
            __props__['instance_name'] = instance_name
            __props__['name'] = name
            __props__['project'] = project
            __props__['split_keys'] = split_keys
        super(Table, __self__).__init__(
            'gcp:bigtable/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, column_families=None, instance_name=None, name=None, project=None, split_keys=None):
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] column_families: A group of columns within a table which share a common configuration. This can be specified multiple times. Structure is documented below.
        :param pulumi.Input[str] instance_name: The name of the Bigtable instance.
        :param pulumi.Input[str] name: The name of the table.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[list] split_keys: A list of predefined keys to split the table on.
               !> **Warning:** Modifying the `split_keys` of an existing table will cause the provider
               to delete/recreate the entire `bigtable.Table` resource.

        The **column_families** object supports the following:

          * `family` (`pulumi.Input[str]`) - The name of the column family.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["column_families"] = column_families
        __props__["instance_name"] = instance_name
        __props__["name"] = name
        __props__["project"] = project
        __props__["split_keys"] = split_keys
        return Table(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
