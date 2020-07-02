# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class DomainMapping(pulumi.CustomResource):
    domain_name: pulumi.Output[str]
    """
    Relative name of the domain serving the application. Example: example.com.
    """
    name: pulumi.Output[str]
    """
    Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.
    """
    override_strategy: pulumi.Output[str]
    """
    Whether the domain creation should override any existing mappings for this domain.
    By default, overrides are rejected.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    resource_records: pulumi.Output[list]
    """
    The resource records required to configure this domain mapping. These records must be added to the domain's DNS
    configuration in order to serve the application via this domain mapping.

      * `name` (`str`)
      * `rrdata` (`str`)
      * `type` (`str`)
    """
    ssl_settings: pulumi.Output[dict]
    """
    SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.  Structure is documented below.

      * `certificate_id` (`str`) - ID of the AuthorizedCertificate resource configuring SSL for the application. Clearing this field will
        remove SSL support.
        By default, a managed certificate is automatically created for every domain mapping. To omit SSL support
        or to configure SSL manually, specify `SslManagementType.MANUAL` on a `CREATE` or `UPDATE` request. You must be
        authorized to administer the `AuthorizedCertificate` resource to manually map it to a DomainMapping resource.
        Example: 12345.
      * `pendingManagedCertificateId` (`str`) - -
        ID of the managed `AuthorizedCertificate` resource currently being provisioned, if applicable. Until the new
        managed certificate has been successfully provisioned, the previous SSL state will be preserved. Once the
        provisioning process completes, the `certificateId` field will reflect the new managed certificate and this
        field will be left empty. To remove SSL support while there is still a pending managed certificate, clear the
        `certificateId` field with an update request.
      * `sslManagementType` (`str`) - SSL management type for this domain. If `AUTOMATIC`, a managed certificate is automatically provisioned.
        If `MANUAL`, `certificateId` must be manually specified in order to configure SSL for this domain.
    """
    def __init__(__self__, resource_name, opts=None, domain_name=None, override_strategy=None, project=None, ssl_settings=None, __props__=None, __name__=None, __opts__=None):
        """
        A domain serving an App Engine application.

        To get more information about DomainMapping, see:

        * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Relative name of the domain serving the application. Example: example.com.
        :param pulumi.Input[str] override_strategy: Whether the domain creation should override any existing mappings for this domain.
               By default, overrides are rejected.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[dict] ssl_settings: SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.  Structure is documented below.

        The **ssl_settings** object supports the following:

          * `certificate_id` (`pulumi.Input[str]`) - ID of the AuthorizedCertificate resource configuring SSL for the application. Clearing this field will
            remove SSL support.
            By default, a managed certificate is automatically created for every domain mapping. To omit SSL support
            or to configure SSL manually, specify `SslManagementType.MANUAL` on a `CREATE` or `UPDATE` request. You must be
            authorized to administer the `AuthorizedCertificate` resource to manually map it to a DomainMapping resource.
            Example: 12345.
          * `pendingManagedCertificateId` (`pulumi.Input[str]`) - -
            ID of the managed `AuthorizedCertificate` resource currently being provisioned, if applicable. Until the new
            managed certificate has been successfully provisioned, the previous SSL state will be preserved. Once the
            provisioning process completes, the `certificateId` field will reflect the new managed certificate and this
            field will be left empty. To remove SSL support while there is still a pending managed certificate, clear the
            `certificateId` field with an update request.
          * `sslManagementType` (`pulumi.Input[str]`) - SSL management type for this domain. If `AUTOMATIC`, a managed certificate is automatically provisioned.
            If `MANUAL`, `certificateId` must be manually specified in order to configure SSL for this domain.
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

            if domain_name is None:
                raise TypeError("Missing required property 'domain_name'")
            __props__['domain_name'] = domain_name
            __props__['override_strategy'] = override_strategy
            __props__['project'] = project
            __props__['ssl_settings'] = ssl_settings
            __props__['name'] = None
            __props__['resource_records'] = None
        super(DomainMapping, __self__).__init__(
            'gcp:appengine/domainMapping:DomainMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, domain_name=None, name=None, override_strategy=None, project=None, resource_records=None, ssl_settings=None):
        """
        Get an existing DomainMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Relative name of the domain serving the application. Example: example.com.
        :param pulumi.Input[str] name: Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.
        :param pulumi.Input[str] override_strategy: Whether the domain creation should override any existing mappings for this domain.
               By default, overrides are rejected.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] resource_records: The resource records required to configure this domain mapping. These records must be added to the domain's DNS
               configuration in order to serve the application via this domain mapping.
        :param pulumi.Input[dict] ssl_settings: SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.  Structure is documented below.

        The **resource_records** object supports the following:

          * `name` (`pulumi.Input[str]`)
          * `rrdata` (`pulumi.Input[str]`)
          * `type` (`pulumi.Input[str]`)

        The **ssl_settings** object supports the following:

          * `certificate_id` (`pulumi.Input[str]`) - ID of the AuthorizedCertificate resource configuring SSL for the application. Clearing this field will
            remove SSL support.
            By default, a managed certificate is automatically created for every domain mapping. To omit SSL support
            or to configure SSL manually, specify `SslManagementType.MANUAL` on a `CREATE` or `UPDATE` request. You must be
            authorized to administer the `AuthorizedCertificate` resource to manually map it to a DomainMapping resource.
            Example: 12345.
          * `pendingManagedCertificateId` (`pulumi.Input[str]`) - -
            ID of the managed `AuthorizedCertificate` resource currently being provisioned, if applicable. Until the new
            managed certificate has been successfully provisioned, the previous SSL state will be preserved. Once the
            provisioning process completes, the `certificateId` field will reflect the new managed certificate and this
            field will be left empty. To remove SSL support while there is still a pending managed certificate, clear the
            `certificateId` field with an update request.
          * `sslManagementType` (`pulumi.Input[str]`) - SSL management type for this domain. If `AUTOMATIC`, a managed certificate is automatically provisioned.
            If `MANUAL`, `certificateId` must be manually specified in order to configure SSL for this domain.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["domain_name"] = domain_name
        __props__["name"] = name
        __props__["override_strategy"] = override_strategy
        __props__["project"] = project
        __props__["resource_records"] = resource_records
        __props__["ssl_settings"] = ssl_settings
        return DomainMapping(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
