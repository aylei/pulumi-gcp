# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Repository(pulumi.CustomResource):
    create_time: pulumi.Output[str]
    """
    The time when the repository was created.
    """
    description: pulumi.Output[str]
    """
    The user-provided description of the repository.
    """
    format: pulumi.Output[str]
    """
    The format of packages that are stored in the repoitory.
    """
    labels: pulumi.Output[dict]
    """
    Labels with user-defined metadata.
    This field may contain up to 64 entries. Label keys and values may be no
    longer than 63 characters. Label keys must begin with a lowercase letter
    and may only contain lowercase letters, numeric characters, underscores,
    and dashes.
    """
    location: pulumi.Output[str]
    """
    The name of the location this repository is located in.
    """
    name: pulumi.Output[str]
    """
    The name of the repository, for example: "projects/p1/locations/us-central1/repositories/repo1"
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    repository_id: pulumi.Output[str]
    """
    The last part of the repository name, for example:
    "repo1"
    """
    update_time: pulumi.Output[str]
    """
    The time when the repository was last updated.
    """
    def __init__(__self__, resource_name, opts=None, description=None, format=None, labels=None, location=None, project=None, repository_id=None, __props__=None, __name__=None, __opts__=None):
        """
        A repository for storing artifacts

        To get more information about Repository, see:

        * [API documentation](https://cloud.google.com/artifact-registry/docs/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/artifact-registry/docs/overview)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The user-provided description of the repository.
        :param pulumi.Input[str] format: The format of packages that are stored in the repoitory.
        :param pulumi.Input[dict] labels: Labels with user-defined metadata.
               This field may contain up to 64 entries. Label keys and values may be no
               longer than 63 characters. Label keys must begin with a lowercase letter
               and may only contain lowercase letters, numeric characters, underscores,
               and dashes.
        :param pulumi.Input[str] location: The name of the location this repository is located in.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] repository_id: The last part of the repository name, for example:
               "repo1"
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
            if format is None:
                raise TypeError("Missing required property 'format'")
            __props__['format'] = format
            __props__['labels'] = labels
            __props__['location'] = location
            __props__['project'] = project
            if repository_id is None:
                raise TypeError("Missing required property 'repository_id'")
            __props__['repository_id'] = repository_id
            __props__['create_time'] = None
            __props__['name'] = None
            __props__['update_time'] = None
        super(Repository, __self__).__init__(
            'gcp:artifactregistry/repository:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, create_time=None, description=None, format=None, labels=None, location=None, name=None, project=None, repository_id=None, update_time=None):
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The time when the repository was created.
        :param pulumi.Input[str] description: The user-provided description of the repository.
        :param pulumi.Input[str] format: The format of packages that are stored in the repoitory.
        :param pulumi.Input[dict] labels: Labels with user-defined metadata.
               This field may contain up to 64 entries. Label keys and values may be no
               longer than 63 characters. Label keys must begin with a lowercase letter
               and may only contain lowercase letters, numeric characters, underscores,
               and dashes.
        :param pulumi.Input[str] location: The name of the location this repository is located in.
        :param pulumi.Input[str] name: The name of the repository, for example: "projects/p1/locations/us-central1/repositories/repo1"
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] repository_id: The last part of the repository name, for example:
               "repo1"
        :param pulumi.Input[str] update_time: The time when the repository was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_time"] = create_time
        __props__["description"] = description
        __props__["format"] = format
        __props__["labels"] = labels
        __props__["location"] = location
        __props__["name"] = name
        __props__["project"] = project
        __props__["repository_id"] = repository_id
        __props__["update_time"] = update_time
        return Repository(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
