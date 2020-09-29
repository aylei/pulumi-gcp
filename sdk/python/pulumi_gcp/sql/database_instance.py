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

__all__ = ['DatabaseInstance']


class DatabaseInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_version: Optional[pulumi.Input[str]] = None,
                 encryption_key_name: Optional[pulumi.Input[str]] = None,
                 master_instance_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 replica_configuration: Optional[pulumi.Input[pulumi.InputType['DatabaseInstanceReplicaConfigurationArgs']]] = None,
                 root_password: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[pulumi.InputType['DatabaseInstanceSettingsArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
        or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).

        > **NOTE on `sql.DatabaseInstance`:** - First-generation instances have been
        deprecated and should no longer be created, see [upgrade docs](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
        for more details.
        To upgrade your First-generation instance, update your config that the instance has
        * `settings.ip_configuration.ipv4_enabled=true`
        * `settings.backup_configuration.enabled=true`
        * `settings.backup_configuration.binary_log_enabled=true`.\
          Apply the config, then upgrade the instance in the console as described in the documentation.
          Once upgraded, update the following attributes in your config to the correct value according to
          the above documentation:
        * `region`
        * `database_version` (if applicable)
        * `tier`\
          Remove any fields that are not applicable to Second-generation instances:
        * `settings.crash_safe_replication`
        * `settings.replication_type`
        * `settings.authorized_gae_applications`
          And change values to appropriate values for Second-generation instances for:
        * `activation_policy` ("ON_DEMAND" is no longer an option)
        * `pricing_plan` ("PER_USE" is now the only valid option)
          Change `settings.backup_configuration.enabled` attribute back to its desired value and apply as necessary.

        > **NOTE on `sql.DatabaseInstance`:** - Second-generation instances include a
        default 'root'@'%' user with no password. This user will be deleted by the provider on
        instance creation. You should use `sql.User` to define a custom user with
        a restricted host and strong password.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_version: The MySQL, PostgreSQL or
               SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
               `MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `SQLSERVER_2017_STANDARD`,
               `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
               [Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
               includes an up-to-date reference of supported versions.
        :param pulumi.Input[str] encryption_key_name: The full path to the encryption key used for the CMEK disk encryption.  Setting
               up disk encryption currently requires manual steps outside of this provider.
               The provided key must be in the same region as the SQL instance.  In order
               to use this feature, a special kind of service account must be created and
               granted permission on this key.  This step can currently only be done
               manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
               That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
               key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
        :param pulumi.Input[str] master_instance_name: The name of the instance that will act as
               the master in the replication setup. Note, this requires the master to have
               `binary_log_enabled` set, as well as existing backups.
        :param pulumi.Input[str] name: A name for this whitelist entry.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] region: The region the instance will sit in. Note, Cloud SQL is not
               available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
               A valid region must be provided to use this resource. If a region is not provided in the resource definition,
               the provider region will be used instead, but this will be an apply-time error for instances if the provider
               region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
               make sure you understand this.
        :param pulumi.Input[pulumi.InputType['DatabaseInstanceReplicaConfigurationArgs']] replica_configuration: The configuration for replication. The
               configuration is detailed below.
        :param pulumi.Input[str] root_password: Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
        :param pulumi.Input[pulumi.InputType['DatabaseInstanceSettingsArgs']] settings: The settings to use for the database. The
               configuration is detailed below.
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

            __props__['database_version'] = database_version
            __props__['encryption_key_name'] = encryption_key_name
            __props__['master_instance_name'] = master_instance_name
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
            __props__['replica_configuration'] = replica_configuration
            __props__['root_password'] = root_password
            if settings is None:
                raise TypeError("Missing required property 'settings'")
            __props__['settings'] = settings
            __props__['connection_name'] = None
            __props__['first_ip_address'] = None
            __props__['ip_addresses'] = None
            __props__['private_ip_address'] = None
            __props__['public_ip_address'] = None
            __props__['self_link'] = None
            __props__['server_ca_certs'] = None
            __props__['service_account_email_address'] = None
        super(DatabaseInstance, __self__).__init__(
            'gcp:sql/databaseInstance:DatabaseInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connection_name: Optional[pulumi.Input[str]] = None,
            database_version: Optional[pulumi.Input[str]] = None,
            encryption_key_name: Optional[pulumi.Input[str]] = None,
            first_ip_address: Optional[pulumi.Input[str]] = None,
            ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseInstanceIpAddressArgs']]]]] = None,
            master_instance_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_ip_address: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            public_ip_address: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            replica_configuration: Optional[pulumi.Input[pulumi.InputType['DatabaseInstanceReplicaConfigurationArgs']]] = None,
            root_password: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            server_ca_certs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatabaseInstanceServerCaCertArgs']]]]] = None,
            service_account_email_address: Optional[pulumi.Input[str]] = None,
            settings: Optional[pulumi.Input[pulumi.InputType['DatabaseInstanceSettingsArgs']]] = None) -> 'DatabaseInstance':
        """
        Get an existing DatabaseInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_name: The connection name of the instance to be used in
               connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
        :param pulumi.Input[str] database_version: The MySQL, PostgreSQL or
               SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
               `MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `SQLSERVER_2017_STANDARD`,
               `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
               [Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
               includes an up-to-date reference of supported versions.
        :param pulumi.Input[str] encryption_key_name: The full path to the encryption key used for the CMEK disk encryption.  Setting
               up disk encryption currently requires manual steps outside of this provider.
               The provided key must be in the same region as the SQL instance.  In order
               to use this feature, a special kind of service account must be created and
               granted permission on this key.  This step can currently only be done
               manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
               That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
               key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
        :param pulumi.Input[str] first_ip_address: The first IPv4 address of any type assigned.
        :param pulumi.Input[str] master_instance_name: The name of the instance that will act as
               the master in the replication setup. Note, this requires the master to have
               `binary_log_enabled` set, as well as existing backups.
        :param pulumi.Input[str] name: A name for this whitelist entry.
        :param pulumi.Input[str] private_ip_address: The first private (`PRIVATE`) IPv4 address assigned.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] public_ip_address: The first public (`PRIMARY`) IPv4 address assigned.
        :param pulumi.Input[str] region: The region the instance will sit in. Note, Cloud SQL is not
               available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
               A valid region must be provided to use this resource. If a region is not provided in the resource definition,
               the provider region will be used instead, but this will be an apply-time error for instances if the provider
               region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
               make sure you understand this.
        :param pulumi.Input[pulumi.InputType['DatabaseInstanceReplicaConfigurationArgs']] replica_configuration: The configuration for replication. The
               configuration is detailed below.
        :param pulumi.Input[str] root_password: Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[str] service_account_email_address: The service account email address assigned to the
               instance.
        :param pulumi.Input[pulumi.InputType['DatabaseInstanceSettingsArgs']] settings: The settings to use for the database. The
               configuration is detailed below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["connection_name"] = connection_name
        __props__["database_version"] = database_version
        __props__["encryption_key_name"] = encryption_key_name
        __props__["first_ip_address"] = first_ip_address
        __props__["ip_addresses"] = ip_addresses
        __props__["master_instance_name"] = master_instance_name
        __props__["name"] = name
        __props__["private_ip_address"] = private_ip_address
        __props__["project"] = project
        __props__["public_ip_address"] = public_ip_address
        __props__["region"] = region
        __props__["replica_configuration"] = replica_configuration
        __props__["root_password"] = root_password
        __props__["self_link"] = self_link
        __props__["server_ca_certs"] = server_ca_certs
        __props__["service_account_email_address"] = service_account_email_address
        __props__["settings"] = settings
        return DatabaseInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Output[str]:
        """
        The connection name of the instance to be used in
        connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
        """
        return pulumi.get(self, "connection_name")

    @property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> pulumi.Output[Optional[str]]:
        """
        The MySQL, PostgreSQL or
        SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
        `MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `SQLSERVER_2017_STANDARD`,
        `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
        [Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
        includes an up-to-date reference of supported versions.
        """
        return pulumi.get(self, "database_version")

    @property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> pulumi.Output[str]:
        """
        The full path to the encryption key used for the CMEK disk encryption.  Setting
        up disk encryption currently requires manual steps outside of this provider.
        The provided key must be in the same region as the SQL instance.  In order
        to use this feature, a special kind of service account must be created and
        granted permission on this key.  This step can currently only be done
        manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
        That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
        key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
        """
        return pulumi.get(self, "encryption_key_name")

    @property
    @pulumi.getter(name="firstIpAddress")
    def first_ip_address(self) -> pulumi.Output[str]:
        """
        The first IPv4 address of any type assigned.
        """
        return pulumi.get(self, "first_ip_address")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence['outputs.DatabaseInstanceIpAddress']]:
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter(name="masterInstanceName")
    def master_instance_name(self) -> pulumi.Output[str]:
        """
        The name of the instance that will act as
        the master in the replication setup. Note, this requires the master to have
        `binary_log_enabled` set, as well as existing backups.
        """
        return pulumi.get(self, "master_instance_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name for this whitelist entry.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[str]:
        """
        The first private (`PRIVATE`) IPv4 address assigned.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> pulumi.Output[str]:
        """
        The first public (`PRIMARY`) IPv4 address assigned.
        """
        return pulumi.get(self, "public_ip_address")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region the instance will sit in. Note, Cloud SQL is not
        available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
        A valid region must be provided to use this resource. If a region is not provided in the resource definition,
        the provider region will be used instead, but this will be an apply-time error for instances if the provider
        region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
        make sure you understand this.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="replicaConfiguration")
    def replica_configuration(self) -> pulumi.Output['outputs.DatabaseInstanceReplicaConfiguration']:
        """
        The configuration for replication. The
        configuration is detailed below.
        """
        return pulumi.get(self, "replica_configuration")

    @property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> pulumi.Output[Optional[str]]:
        """
        Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
        """
        return pulumi.get(self, "root_password")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(self) -> pulumi.Output[Sequence['outputs.DatabaseInstanceServerCaCert']]:
        return pulumi.get(self, "server_ca_certs")

    @property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> pulumi.Output[str]:
        """
        The service account email address assigned to the
        instance.
        """
        return pulumi.get(self, "service_account_email_address")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output['outputs.DatabaseInstanceSettings']:
        """
        The settings to use for the database. The
        configuration is detailed below.
        """
        return pulumi.get(self, "settings")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

