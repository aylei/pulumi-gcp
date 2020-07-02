# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Environment(pulumi.CustomResource):
    config: pulumi.Output[dict]
    """
    Configuration parameters for this environment  Structure is documented below.

      * `airflowUri` (`str`)
      * `dagGcsPrefix` (`str`)
      * `gkeCluster` (`str`)
      * `node_config` (`dict`) - The configuration used for the Kubernetes Engine cluster.  Structure is documented below.
        * `disk_size_gb` (`float`) - The disk size in GB used for node VMs. Minimum size is 20GB.
          If unspecified, defaults to 100GB. Cannot be updated.
        * `ip_allocation_policy` (`dict`) - Configuration for controlling how IPs are allocated in the GKE cluster.
          Structure is documented below.
          Cannot be updated.
          * `clusterIpv4CidrBlock` (`str`) - The IP address range used to allocate IP addresses to pods in the cluster.
            Set to blank to have GKE choose a range with the default size.
            Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
            Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
            (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
            Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
          * `clusterSecondaryRangeName` (`str`) - The name of the cluster's secondary range used to allocate IP addresses to pods.
            Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
            This field is applicable only when `use_ip_aliases` is true.
          * `servicesIpv4CidrBlock` (`str`) - The IP address range used to allocate IP addresses in this cluster.
            Set to blank to have GKE choose a range with the default size.
            Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
            Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
            (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
            Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
          * `servicesSecondaryRangeName` (`str`) - The name of the services' secondary range used to allocate IP addresses to the cluster.
            Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
            This field is applicable only when `use_ip_aliases` is true.
          * `useIpAliases` (`bool`) - Whether or not to enable Alias IPs in the GKE cluster. If true, a VPC-native cluster is created.
            Defaults to true if the `ip_allocation_block` is present in config.

        * `machine_type` (`str`) - The Compute Engine machine type used for cluster instances,
          specified as a name or relative resource name. For example:
          "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and
          region/zone.
        * `network` (`str`) - The Compute Engine network to be used for machine
          communications, specified as a self-link, relative resource name
          (e.g. "projects/{project}/global/networks/{network}"), by name.
        * `oauthScopes` (`list`) - The set of Google API scopes to be made available on all node
          VMs. Cannot be updated. If empty, defaults to
          `["https://www.googleapis.com/auth/cloud-platform"]`
        * `service_account` (`str`) - The Google Cloud Platform Service Account to be used by the
          node VMs. If a service account is not specified, the "default"
          Compute Engine service account is used. Cannot be updated. If given,
          note that the service account must have `roles/composer.worker`
          for any GCP resources created under the Cloud Composer Environment.
        * `subnetwork` (`str`) - The Compute Engine subnetwork to be used for machine
          communications, , specified as a self-link, relative resource name (e.g.
          "projects/{project}/regions/{region}/subnetworks/{subnetwork}"), or by name. If subnetwork is provided,
          network must also be provided and the subnetwork must belong to the enclosing environment's project and region.
        * `tags` (`list`) - The list of instance tags applied to all node VMs. Tags are
          used to identify valid sources or targets for network
          firewalls. Each tag within the list must comply with RFC1035.
          Cannot be updated.
        * `zone` (`str`) - The Compute Engine zone in which to deploy the VMs running the
          Apache Airflow software, specified as the zone name or
          relative resource name (e.g. "projects/{project}/zones/{zone}"). Must belong to the enclosing environment's project
          and region.

      * `node_count` (`float`) - The number of nodes in the Kubernetes Engine cluster that
        will be used to run this environment.
      * `privateEnvironmentConfig` (`dict`) - The configuration used for the Private IP Cloud Composer environment. Structure is documented below.
        * `cloudSqlIpv4CidrBlock` (`str`) - The CIDR block from which IP range in tenant project will be reserved for Cloud SQL. Needs to be disjoint from `web_server_ipv4_cidr_block`
        * `enablePrivateEndpoint` (`bool`) - -
          If true, access to the public endpoint of the GKE cluster is denied.
        * `masterIpv4CidrBlock` (`str`) - The IP range in CIDR notation to use for the hosted master network. This range is used
          for assigning internal IP addresses to the cluster master or set of masters and to the
          internal load balancer virtual IP. This range must not overlap with any other ranges
          in use within the cluster's network.
          If left blank, the default value of '172.16.0.0/28' is used.
        * `webServerIpv4CidrBlock` (`str`) - The CIDR block from which IP range for web server will be reserved. Needs to be disjoint from `master_ipv4_cidr_block` and `cloud_sql_ipv4_cidr_block`.

      * `softwareConfig` (`dict`) - The configuration settings for software inside the environment.  Structure is documented below.
        * `airflowConfigOverrides` (`dict`) - -
          (Optional) Apache Airflow configuration properties to override. Property keys contain the section and property names,
          separated by a hyphen, for example "core-dags_are_paused_at_creation".
        * `env_variables` (`dict`) - Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.
          Environment variable names must match the regular expression `[a-zA-Z_][a-zA-Z0-9_]*`.
          They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression
          `AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+`), and they cannot match any of the following reserved names:
          ```python
          import pulumi
          ```
        * `imageVersion` (`str`) - -
          The version of the software running in the environment. This encapsulates both the version of Cloud Composer
          functionality and the version of Apache Airflow. It must match the regular expression
          `composer-[0-9]+\.[0-9]+(\.[0-9]+)?-airflow-[0-9]+\.[0-9]+(\.[0-9]+.*)?`.
          The Cloud Composer portion of the version is a semantic version.
          The portion of the image version following 'airflow-' is an official Apache Airflow repository release name.
          See [documentation](https://cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments#softwareconfig)
          for allowed release names.
        * `pypiPackages` (`dict`) - Custom Python Package Index (PyPI) packages to be installed
          in the environment. Keys refer to the lowercase package name (e.g. "numpy"). Values are the lowercase extras and
          version specifier (e.g. "==1.12.0", "[devel,gcp_api]", "[devel]>=1.8.2, <1.9.2"). To specify a package without
          pinning it to a version specifier, use the empty string as the value.
        * `pythonVersion` (`str`) - -
          The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.
          Can be set to '2' or '3'. If not specified, the default is '2'. Cannot be updated.

      * `webServerNetworkAccessControl` (`dict`) - The network-level access control policy for the Airflow web server. If unspecified, no network-level access restrictions will be applied.
        * `allowedIpRanges` (`list`) - -
          A collection of allowed IP ranges with descriptions. Structure is documented below.
          * `description` (`str`) - A description of this ip range.
          * `value` (`str`) - IP address or range, defined using CIDR notation, of requests that this rule applies to.
            Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.
            IP range prefixes should be properly truncated. For example,
            `1.2.3.4/24` should be truncated to `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` should be truncated to `2001:db8::/32`.
    """
    labels: pulumi.Output[dict]
    """
    User-defined labels for this environment. The labels map can contain
    no more than 64 entries. Entries of the labels map are UTF8 strings
    that comply with the following restrictions:
    Label keys must be between 1 and 63 characters long and must conform
    to the following regular expression: `a-z?`.
    Label values must be between 0 and 63 characters long and must
    conform to the regular expression `(a-z?)?`.
    No more than 64 labels can be associated with a given environment.
    Both keys and values must be <= 128 bytes in size.
    """
    name: pulumi.Output[str]
    """
    Name of the environment
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    region: pulumi.Output[str]
    """
    The location or Compute Engine region for the environment.
    """
    def __init__(__self__, resource_name, opts=None, config=None, labels=None, name=None, project=None, region=None, __props__=None, __name__=None, __opts__=None):
        """
        An environment for running orchestration tasks.

        Environments run Apache Airflow software on Google infrastructure.

        To get more information about Environments, see:

        * [API documentation](https://cloud.google.com/composer/docs/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/composer/docs)
            * [Configuring Shared VPC for Composer Environments](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc)
        * [Apache Airflow Documentation](http://airflow.apache.org/)

        > **Warning:** We **STRONGLY** recommend  you read the [GCP guides](https://cloud.google.com/composer/docs/how-to)
          as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure,
          including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
          This provider will not be able to automatically find or manage many of these underlying resources. In particular:
          * It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some
            errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
            error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid
            against GCP Cloud Composer before filing bugs against this provider.
          * **Environments create Google Cloud Storage buckets that do not get cleaned up automatically** on environment
            deletion. [More about Composer's use of Cloud Storage](https://cloud.google.com/composer/docs/concepts/cloud-storage).

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] config: Configuration parameters for this environment  Structure is documented below.
        :param pulumi.Input[dict] labels: User-defined labels for this environment. The labels map can contain
               no more than 64 entries. Entries of the labels map are UTF8 strings
               that comply with the following restrictions:
               Label keys must be between 1 and 63 characters long and must conform
               to the following regular expression: `a-z?`.
               Label values must be between 0 and 63 characters long and must
               conform to the regular expression `(a-z?)?`.
               No more than 64 labels can be associated with a given environment.
               Both keys and values must be <= 128 bytes in size.
        :param pulumi.Input[str] name: Name of the environment
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The location or Compute Engine region for the environment.

        The **config** object supports the following:

          * `airflowUri` (`pulumi.Input[str]`)
          * `dagGcsPrefix` (`pulumi.Input[str]`)
          * `gkeCluster` (`pulumi.Input[str]`)
          * `node_config` (`pulumi.Input[dict]`) - The configuration used for the Kubernetes Engine cluster.  Structure is documented below.
            * `disk_size_gb` (`pulumi.Input[float]`) - The disk size in GB used for node VMs. Minimum size is 20GB.
              If unspecified, defaults to 100GB. Cannot be updated.
            * `ip_allocation_policy` (`pulumi.Input[dict]`) - Configuration for controlling how IPs are allocated in the GKE cluster.
              Structure is documented below.
              Cannot be updated.
              * `clusterIpv4CidrBlock` (`pulumi.Input[str]`) - The IP address range used to allocate IP addresses to pods in the cluster.
                Set to blank to have GKE choose a range with the default size.
                Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
                Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
                (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
                Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
              * `clusterSecondaryRangeName` (`pulumi.Input[str]`) - The name of the cluster's secondary range used to allocate IP addresses to pods.
                Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
                This field is applicable only when `use_ip_aliases` is true.
              * `servicesIpv4CidrBlock` (`pulumi.Input[str]`) - The IP address range used to allocate IP addresses in this cluster.
                Set to blank to have GKE choose a range with the default size.
                Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
                Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
                (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
                Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
              * `servicesSecondaryRangeName` (`pulumi.Input[str]`) - The name of the services' secondary range used to allocate IP addresses to the cluster.
                Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
                This field is applicable only when `use_ip_aliases` is true.
              * `useIpAliases` (`pulumi.Input[bool]`) - Whether or not to enable Alias IPs in the GKE cluster. If true, a VPC-native cluster is created.
                Defaults to true if the `ip_allocation_block` is present in config.

            * `machine_type` (`pulumi.Input[str]`) - The Compute Engine machine type used for cluster instances,
              specified as a name or relative resource name. For example:
              "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and
              region/zone.
            * `network` (`pulumi.Input[str]`) - The Compute Engine network to be used for machine
              communications, specified as a self-link, relative resource name
              (e.g. "projects/{project}/global/networks/{network}"), by name.
            * `oauthScopes` (`pulumi.Input[list]`) - The set of Google API scopes to be made available on all node
              VMs. Cannot be updated. If empty, defaults to
              `["https://www.googleapis.com/auth/cloud-platform"]`
            * `service_account` (`pulumi.Input[str]`) - The Google Cloud Platform Service Account to be used by the
              node VMs. If a service account is not specified, the "default"
              Compute Engine service account is used. Cannot be updated. If given,
              note that the service account must have `roles/composer.worker`
              for any GCP resources created under the Cloud Composer Environment.
            * `subnetwork` (`pulumi.Input[str]`) - The Compute Engine subnetwork to be used for machine
              communications, , specified as a self-link, relative resource name (e.g.
              "projects/{project}/regions/{region}/subnetworks/{subnetwork}"), or by name. If subnetwork is provided,
              network must also be provided and the subnetwork must belong to the enclosing environment's project and region.
            * `tags` (`pulumi.Input[list]`) - The list of instance tags applied to all node VMs. Tags are
              used to identify valid sources or targets for network
              firewalls. Each tag within the list must comply with RFC1035.
              Cannot be updated.
            * `zone` (`pulumi.Input[str]`) - The Compute Engine zone in which to deploy the VMs running the
              Apache Airflow software, specified as the zone name or
              relative resource name (e.g. "projects/{project}/zones/{zone}"). Must belong to the enclosing environment's project
              and region.

          * `node_count` (`pulumi.Input[float]`) - The number of nodes in the Kubernetes Engine cluster that
            will be used to run this environment.
          * `privateEnvironmentConfig` (`pulumi.Input[dict]`) - The configuration used for the Private IP Cloud Composer environment. Structure is documented below.
            * `cloudSqlIpv4CidrBlock` (`pulumi.Input[str]`) - The CIDR block from which IP range in tenant project will be reserved for Cloud SQL. Needs to be disjoint from `web_server_ipv4_cidr_block`
            * `enablePrivateEndpoint` (`pulumi.Input[bool]`) - -
              If true, access to the public endpoint of the GKE cluster is denied.
            * `masterIpv4CidrBlock` (`pulumi.Input[str]`) - The IP range in CIDR notation to use for the hosted master network. This range is used
              for assigning internal IP addresses to the cluster master or set of masters and to the
              internal load balancer virtual IP. This range must not overlap with any other ranges
              in use within the cluster's network.
              If left blank, the default value of '172.16.0.0/28' is used.
            * `webServerIpv4CidrBlock` (`pulumi.Input[str]`) - The CIDR block from which IP range for web server will be reserved. Needs to be disjoint from `master_ipv4_cidr_block` and `cloud_sql_ipv4_cidr_block`.

          * `softwareConfig` (`pulumi.Input[dict]`) - The configuration settings for software inside the environment.  Structure is documented below.
            * `airflowConfigOverrides` (`pulumi.Input[dict]`) - -
              (Optional) Apache Airflow configuration properties to override. Property keys contain the section and property names,
              separated by a hyphen, for example "core-dags_are_paused_at_creation".
            * `env_variables` (`pulumi.Input[dict]`) - Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.
              Environment variable names must match the regular expression `[a-zA-Z_][a-zA-Z0-9_]*`.
              They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression
              `AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+`), and they cannot match any of the following reserved names:
              ```python
              import pulumi
              ```
            * `imageVersion` (`pulumi.Input[str]`) - -
              The version of the software running in the environment. This encapsulates both the version of Cloud Composer
              functionality and the version of Apache Airflow. It must match the regular expression
              `composer-[0-9]+\.[0-9]+(\.[0-9]+)?-airflow-[0-9]+\.[0-9]+(\.[0-9]+.*)?`.
              The Cloud Composer portion of the version is a semantic version.
              The portion of the image version following 'airflow-' is an official Apache Airflow repository release name.
              See [documentation](https://cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments#softwareconfig)
              for allowed release names.
            * `pypiPackages` (`pulumi.Input[dict]`) - Custom Python Package Index (PyPI) packages to be installed
              in the environment. Keys refer to the lowercase package name (e.g. "numpy"). Values are the lowercase extras and
              version specifier (e.g. "==1.12.0", "[devel,gcp_api]", "[devel]>=1.8.2, <1.9.2"). To specify a package without
              pinning it to a version specifier, use the empty string as the value.
            * `pythonVersion` (`pulumi.Input[str]`) - -
              The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.
              Can be set to '2' or '3'. If not specified, the default is '2'. Cannot be updated.

          * `webServerNetworkAccessControl` (`pulumi.Input[dict]`) - The network-level access control policy for the Airflow web server. If unspecified, no network-level access restrictions will be applied.
            * `allowedIpRanges` (`pulumi.Input[list]`) - -
              A collection of allowed IP ranges with descriptions. Structure is documented below.
              * `description` (`pulumi.Input[str]`) - A description of this ip range.
              * `value` (`pulumi.Input[str]`) - IP address or range, defined using CIDR notation, of requests that this rule applies to.
                Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.
                IP range prefixes should be properly truncated. For example,
                `1.2.3.4/24` should be truncated to `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` should be truncated to `2001:db8::/32`.
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

            __props__['config'] = config
            __props__['labels'] = labels
            __props__['name'] = name
            __props__['project'] = project
            __props__['region'] = region
        super(Environment, __self__).__init__(
            'gcp:composer/environment:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, config=None, labels=None, name=None, project=None, region=None):
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] config: Configuration parameters for this environment  Structure is documented below.
        :param pulumi.Input[dict] labels: User-defined labels for this environment. The labels map can contain
               no more than 64 entries. Entries of the labels map are UTF8 strings
               that comply with the following restrictions:
               Label keys must be between 1 and 63 characters long and must conform
               to the following regular expression: `a-z?`.
               Label values must be between 0 and 63 characters long and must
               conform to the regular expression `(a-z?)?`.
               No more than 64 labels can be associated with a given environment.
               Both keys and values must be <= 128 bytes in size.
        :param pulumi.Input[str] name: Name of the environment
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The location or Compute Engine region for the environment.

        The **config** object supports the following:

          * `airflowUri` (`pulumi.Input[str]`)
          * `dagGcsPrefix` (`pulumi.Input[str]`)
          * `gkeCluster` (`pulumi.Input[str]`)
          * `node_config` (`pulumi.Input[dict]`) - The configuration used for the Kubernetes Engine cluster.  Structure is documented below.
            * `disk_size_gb` (`pulumi.Input[float]`) - The disk size in GB used for node VMs. Minimum size is 20GB.
              If unspecified, defaults to 100GB. Cannot be updated.
            * `ip_allocation_policy` (`pulumi.Input[dict]`) - Configuration for controlling how IPs are allocated in the GKE cluster.
              Structure is documented below.
              Cannot be updated.
              * `clusterIpv4CidrBlock` (`pulumi.Input[str]`) - The IP address range used to allocate IP addresses to pods in the cluster.
                Set to blank to have GKE choose a range with the default size.
                Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
                Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
                (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
                Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
              * `clusterSecondaryRangeName` (`pulumi.Input[str]`) - The name of the cluster's secondary range used to allocate IP addresses to pods.
                Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
                This field is applicable only when `use_ip_aliases` is true.
              * `servicesIpv4CidrBlock` (`pulumi.Input[str]`) - The IP address range used to allocate IP addresses in this cluster.
                Set to blank to have GKE choose a range with the default size.
                Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
                Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
                (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
                Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
              * `servicesSecondaryRangeName` (`pulumi.Input[str]`) - The name of the services' secondary range used to allocate IP addresses to the cluster.
                Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
                This field is applicable only when `use_ip_aliases` is true.
              * `useIpAliases` (`pulumi.Input[bool]`) - Whether or not to enable Alias IPs in the GKE cluster. If true, a VPC-native cluster is created.
                Defaults to true if the `ip_allocation_block` is present in config.

            * `machine_type` (`pulumi.Input[str]`) - The Compute Engine machine type used for cluster instances,
              specified as a name or relative resource name. For example:
              "projects/{project}/zones/{zone}/machineTypes/{machineType}". Must belong to the enclosing environment's project and
              region/zone.
            * `network` (`pulumi.Input[str]`) - The Compute Engine network to be used for machine
              communications, specified as a self-link, relative resource name
              (e.g. "projects/{project}/global/networks/{network}"), by name.
            * `oauthScopes` (`pulumi.Input[list]`) - The set of Google API scopes to be made available on all node
              VMs. Cannot be updated. If empty, defaults to
              `["https://www.googleapis.com/auth/cloud-platform"]`
            * `service_account` (`pulumi.Input[str]`) - The Google Cloud Platform Service Account to be used by the
              node VMs. If a service account is not specified, the "default"
              Compute Engine service account is used. Cannot be updated. If given,
              note that the service account must have `roles/composer.worker`
              for any GCP resources created under the Cloud Composer Environment.
            * `subnetwork` (`pulumi.Input[str]`) - The Compute Engine subnetwork to be used for machine
              communications, , specified as a self-link, relative resource name (e.g.
              "projects/{project}/regions/{region}/subnetworks/{subnetwork}"), or by name. If subnetwork is provided,
              network must also be provided and the subnetwork must belong to the enclosing environment's project and region.
            * `tags` (`pulumi.Input[list]`) - The list of instance tags applied to all node VMs. Tags are
              used to identify valid sources or targets for network
              firewalls. Each tag within the list must comply with RFC1035.
              Cannot be updated.
            * `zone` (`pulumi.Input[str]`) - The Compute Engine zone in which to deploy the VMs running the
              Apache Airflow software, specified as the zone name or
              relative resource name (e.g. "projects/{project}/zones/{zone}"). Must belong to the enclosing environment's project
              and region.

          * `node_count` (`pulumi.Input[float]`) - The number of nodes in the Kubernetes Engine cluster that
            will be used to run this environment.
          * `privateEnvironmentConfig` (`pulumi.Input[dict]`) - The configuration used for the Private IP Cloud Composer environment. Structure is documented below.
            * `cloudSqlIpv4CidrBlock` (`pulumi.Input[str]`) - The CIDR block from which IP range in tenant project will be reserved for Cloud SQL. Needs to be disjoint from `web_server_ipv4_cidr_block`
            * `enablePrivateEndpoint` (`pulumi.Input[bool]`) - -
              If true, access to the public endpoint of the GKE cluster is denied.
            * `masterIpv4CidrBlock` (`pulumi.Input[str]`) - The IP range in CIDR notation to use for the hosted master network. This range is used
              for assigning internal IP addresses to the cluster master or set of masters and to the
              internal load balancer virtual IP. This range must not overlap with any other ranges
              in use within the cluster's network.
              If left blank, the default value of '172.16.0.0/28' is used.
            * `webServerIpv4CidrBlock` (`pulumi.Input[str]`) - The CIDR block from which IP range for web server will be reserved. Needs to be disjoint from `master_ipv4_cidr_block` and `cloud_sql_ipv4_cidr_block`.

          * `softwareConfig` (`pulumi.Input[dict]`) - The configuration settings for software inside the environment.  Structure is documented below.
            * `airflowConfigOverrides` (`pulumi.Input[dict]`) - -
              (Optional) Apache Airflow configuration properties to override. Property keys contain the section and property names,
              separated by a hyphen, for example "core-dags_are_paused_at_creation".
            * `env_variables` (`pulumi.Input[dict]`) - Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.
              Environment variable names must match the regular expression `[a-zA-Z_][a-zA-Z0-9_]*`.
              They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression
              `AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+`), and they cannot match any of the following reserved names:
              ```python
              import pulumi
              ```
            * `imageVersion` (`pulumi.Input[str]`) - -
              The version of the software running in the environment. This encapsulates both the version of Cloud Composer
              functionality and the version of Apache Airflow. It must match the regular expression
              `composer-[0-9]+\.[0-9]+(\.[0-9]+)?-airflow-[0-9]+\.[0-9]+(\.[0-9]+.*)?`.
              The Cloud Composer portion of the version is a semantic version.
              The portion of the image version following 'airflow-' is an official Apache Airflow repository release name.
              See [documentation](https://cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments#softwareconfig)
              for allowed release names.
            * `pypiPackages` (`pulumi.Input[dict]`) - Custom Python Package Index (PyPI) packages to be installed
              in the environment. Keys refer to the lowercase package name (e.g. "numpy"). Values are the lowercase extras and
              version specifier (e.g. "==1.12.0", "[devel,gcp_api]", "[devel]>=1.8.2, <1.9.2"). To specify a package without
              pinning it to a version specifier, use the empty string as the value.
            * `pythonVersion` (`pulumi.Input[str]`) - -
              The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.
              Can be set to '2' or '3'. If not specified, the default is '2'. Cannot be updated.

          * `webServerNetworkAccessControl` (`pulumi.Input[dict]`) - The network-level access control policy for the Airflow web server. If unspecified, no network-level access restrictions will be applied.
            * `allowedIpRanges` (`pulumi.Input[list]`) - -
              A collection of allowed IP ranges with descriptions. Structure is documented below.
              * `description` (`pulumi.Input[str]`) - A description of this ip range.
              * `value` (`pulumi.Input[str]`) - IP address or range, defined using CIDR notation, of requests that this rule applies to.
                Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.
                IP range prefixes should be properly truncated. For example,
                `1.2.3.4/24` should be truncated to `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` should be truncated to `2001:db8::/32`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["config"] = config
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["project"] = project
        __props__["region"] = region
        return Environment(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
