# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class SSLCertificate(pulumi.CustomResource):
    certificate: pulumi.Output[str]
    """
    The certificate in PEM format.
    The certificate chain must be no greater than 5 certs long.
    The chain must include at least one intermediate cert.
    **Note**: This property is sensitive and will not be displayed in the plan.
    """
    certificate_id: pulumi.Output[float]
    """
    The unique identifier for the resource.
    """
    creation_timestamp: pulumi.Output[str]
    """
    Creation timestamp in RFC3339 text format.
    """
    description: pulumi.Output[str]
    """
    An optional description of this resource.
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
    name_prefix: pulumi.Output[str]
    """
    Creates a unique name beginning with the
    specified prefix. Conflicts with `name`.
    """
    private_key: pulumi.Output[str]
    """
    The write-only private key in PEM format.
    **Note**: This property is sensitive and will not be displayed in the plan.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    def __init__(__self__, resource_name, opts=None, certificate=None, description=None, name=None, name_prefix=None, private_key=None, project=None, __props__=None, __name__=None, __opts__=None):
        """
        An SslCertificate resource, used for HTTPS load balancing. This resource
        provides a mechanism to upload an SSL key and certificate to
        the load balancer to serve secure connections from the user.

        To get more information about SslCertificate, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)

        > **Warning:** All arguments including `certificate` and `private_key` will be stored in the raw
        state as plain-text. [Read more about secrets in state](https://www.pulumi.com/docs/intro/concepts/programming-model/#secrets).

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
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

            if certificate is None:
                raise TypeError("Missing required property 'certificate'")
            __props__['certificate'] = certificate
            __props__['description'] = description
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            if private_key is None:
                raise TypeError("Missing required property 'private_key'")
            __props__['private_key'] = private_key
            __props__['project'] = project
            __props__['certificate_id'] = None
            __props__['creation_timestamp'] = None
            __props__['self_link'] = None
        super(SSLCertificate, __self__).__init__(
            'gcp:compute/sSLCertificate:SSLCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, certificate=None, certificate_id=None, creation_timestamp=None, description=None, name=None, name_prefix=None, private_key=None, project=None, self_link=None):
        """
        Get an existing SSLCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: The certificate in PEM format.
               The certificate chain must be no greater than 5 certs long.
               The chain must include at least one intermediate cert.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[float] certificate_id: The unique identifier for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key: The write-only private key in PEM format.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["certificate"] = certificate
        __props__["certificate_id"] = certificate_id
        __props__["creation_timestamp"] = creation_timestamp
        __props__["description"] = description
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["private_key"] = private_key
        __props__["project"] = project
        __props__["self_link"] = self_link
        return SSLCertificate(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
