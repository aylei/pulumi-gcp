# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetGroupMembershipsResult:
    """
    A collection of values returned by getGroupMemberships.
    """
    def __init__(__self__, group=None, id=None, memberships=None):
        if group and not isinstance(group, str):
            raise TypeError("Expected argument 'group' to be a str")
        __self__.group = group
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if memberships and not isinstance(memberships, list):
            raise TypeError("Expected argument 'memberships' to be a list")
        __self__.memberships = memberships
        """
        The list of memberships under the given group. Structure is documented below.
        """
class AwaitableGetGroupMembershipsResult(GetGroupMembershipsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupMembershipsResult(
            group=self.group,
            id=self.id,
            memberships=self.memberships)

def get_group_memberships(group=None,opts=None):
    """
    Use this data source to get list of the Cloud Identity Group Memberships within a given Group.

    https://cloud.google.com/identity/docs/concepts/overview#memberships


    :param str group: The parent Group resource under which to lookup the Membership names. Must be of the form groups/{group_id}.
    """
    __args__ = dict()


    __args__['group'] = group
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:cloudidentity/getGroupMemberships:getGroupMemberships', __args__, opts=opts).value

    return AwaitableGetGroupMembershipsResult(
        group=__ret__.get('group'),
        id=__ret__.get('id'),
        memberships=__ret__.get('memberships'))