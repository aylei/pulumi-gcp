# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GCPolicyMaxAgeArgs',
    'GCPolicyMaxVersionArgs',
    'InstanceClusterArgs',
    'InstanceIamBindingConditionArgs',
    'InstanceIamMemberConditionArgs',
    'TableColumnFamilyArgs',
    'TableIamBindingConditionArgs',
    'TableIamMemberConditionArgs',
]

@pulumi.input_type
class GCPolicyMaxAgeArgs:
    def __init__(__self__, *,
                 days: pulumi.Input[int]):
        """
        :param pulumi.Input[int] days: Number of days before applying GC policy.
        """
        pulumi.set(__self__, "days", days)

    @property
    @pulumi.getter
    def days(self) -> pulumi.Input[int]:
        """
        Number of days before applying GC policy.
        """
        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: pulumi.Input[int]):
        pulumi.set(self, "days", value)


@pulumi.input_type
class GCPolicyMaxVersionArgs:
    def __init__(__self__, *,
                 number: pulumi.Input[int]):
        """
        :param pulumi.Input[int] number: Number of version before applying the GC policy.
        """
        pulumi.set(__self__, "number", number)

    @property
    @pulumi.getter
    def number(self) -> pulumi.Input[int]:
        """
        Number of version before applying the GC policy.
        """
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: pulumi.Input[int]):
        pulumi.set(self, "number", value)


@pulumi.input_type
class InstanceClusterArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 zone: pulumi.Input[str],
                 num_nodes: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cluster_id: The ID of the Cloud Bigtable cluster.
        :param pulumi.Input[str] zone: The zone to create the Cloud Bigtable cluster in. Each
               cluster must have a different zone in the same region. Zones that support
               Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).
        :param pulumi.Input[int] num_nodes: The number of nodes in your Cloud Bigtable cluster.
               Required, with a minimum of `1` for a `PRODUCTION` instance. Must be left unset
               for a `DEVELOPMENT` instance.
        :param pulumi.Input[str] storage_type: The storage type to use. One of `"SSD"` or
               `"HDD"`. Defaults to `"SSD"`.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "zone", zone)
        if num_nodes is not None:
            pulumi.set(__self__, "num_nodes", num_nodes)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Cloud Bigtable cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Input[str]:
        """
        The zone to create the Cloud Bigtable cluster in. Each
        cluster must have a different zone in the same region. Zones that support
        Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone", value)

    @property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes in your Cloud Bigtable cluster.
        Required, with a minimum of `1` for a `PRODUCTION` instance. Must be left unset
        for a `DEVELOPMENT` instance.
        """
        return pulumi.get(self, "num_nodes")

    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_nodes", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        The storage type to use. One of `"SSD"` or
        `"HDD"`. Defaults to `"SSD"`.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)


@pulumi.input_type
class InstanceIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class InstanceIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class TableColumnFamilyArgs:
    def __init__(__self__, *,
                 family: pulumi.Input[str]):
        """
        :param pulumi.Input[str] family: The name of the column family.
        """
        pulumi.set(__self__, "family", family)

    @property
    @pulumi.getter
    def family(self) -> pulumi.Input[str]:
        """
        The name of the column family.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: pulumi.Input[str]):
        pulumi.set(self, "family", value)


@pulumi.input_type
class TableIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class TableIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


