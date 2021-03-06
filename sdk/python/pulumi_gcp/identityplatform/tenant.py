# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Tenant']


class Tenant(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_password_signup: Optional[pulumi.Input[bool]] = None,
                 disable_auth: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_email_link_signin: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Tenant configuration in a multi-tenant project.

        You must enable the
        [Google Identity Platform](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity) in
        the marketplace prior to using this resource.

        You must [enable multi-tenancy](https://cloud.google.com/identity-platform/docs/multi-tenancy-quickstart) via
        the Cloud Console prior to creating tenants.

        ## Example Usage
        ### Identity Platform Tenant Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        tenant = gcp.identityplatform.Tenant("tenant",
            allow_password_signup=True,
            display_name="tenant")
        ```

        ## Import

        Tenant can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:identityplatform/tenant:Tenant default projects/{{project}}/tenants/{{name}}
        ```

        ```sh
         $ pulumi import gcp:identityplatform/tenant:Tenant default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:identityplatform/tenant:Tenant default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_password_signup: Whether to allow email/password user authentication.
        :param pulumi.Input[bool] disable_auth: Whether authentication is disabled for the tenant. If true, the users under
               the disabled tenant are not allowed to sign-in. Admins of the disabled tenant
               are not able to manage its users.
        :param pulumi.Input[str] display_name: Human friendly display name of the tenant.
        :param pulumi.Input[bool] enable_email_link_signin: Whether to enable email link user authentication.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['allow_password_signup'] = allow_password_signup
            __props__['disable_auth'] = disable_auth
            if display_name is None:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            __props__['enable_email_link_signin'] = enable_email_link_signin
            __props__['project'] = project
            __props__['name'] = None
        super(Tenant, __self__).__init__(
            'gcp:identityplatform/tenant:Tenant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_password_signup: Optional[pulumi.Input[bool]] = None,
            disable_auth: Optional[pulumi.Input[bool]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            enable_email_link_signin: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'Tenant':
        """
        Get an existing Tenant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_password_signup: Whether to allow email/password user authentication.
        :param pulumi.Input[bool] disable_auth: Whether authentication is disabled for the tenant. If true, the users under
               the disabled tenant are not allowed to sign-in. Admins of the disabled tenant
               are not able to manage its users.
        :param pulumi.Input[str] display_name: Human friendly display name of the tenant.
        :param pulumi.Input[bool] enable_email_link_signin: Whether to enable email link user authentication.
        :param pulumi.Input[str] name: The name of the tenant that is generated by the server
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allow_password_signup"] = allow_password_signup
        __props__["disable_auth"] = disable_auth
        __props__["display_name"] = display_name
        __props__["enable_email_link_signin"] = enable_email_link_signin
        __props__["name"] = name
        __props__["project"] = project
        return Tenant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowPasswordSignup")
    def allow_password_signup(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to allow email/password user authentication.
        """
        return pulumi.get(self, "allow_password_signup")

    @property
    @pulumi.getter(name="disableAuth")
    def disable_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether authentication is disabled for the tenant. If true, the users under
        the disabled tenant are not allowed to sign-in. Admins of the disabled tenant
        are not able to manage its users.
        """
        return pulumi.get(self, "disable_auth")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Human friendly display name of the tenant.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableEmailLinkSignin")
    def enable_email_link_signin(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable email link user authentication.
        """
        return pulumi.get(self, "enable_email_link_signin")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the tenant that is generated by the server
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

