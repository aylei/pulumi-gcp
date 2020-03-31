# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class FlexibleAppVersion(pulumi.CustomResource):
    api_config: pulumi.Output[dict]
    """
    Serving configuration for Google Cloud Endpoints.

      * `authFailAction` (`str`)
      * `login` (`str`)
      * `script` (`str`)
      * `securityLevel` (`str`)
      * `url` (`str`)
    """
    automatic_scaling: pulumi.Output[dict]
    """
    Automatic scaling is based on request rate, response latencies, and other application metrics.

      * `coolDownPeriod` (`str`)
      * `cpuUtilization` (`dict`)
        * `aggregationWindowLength` (`str`)
        * `targetUtilization` (`float`)

      * `diskUtilization` (`dict`)
        * `targetReadBytesPerSecond` (`float`)
        * `targetReadOpsPerSecond` (`float`)
        * `targetWriteBytesPerSecond` (`float`)
        * `targetWriteOpsPerSecond` (`float`)

      * `maxConcurrentRequests` (`float`)
      * `maxIdleInstances` (`float`)
      * `maxPendingLatency` (`str`)
      * `maxTotalInstances` (`float`)
      * `minIdleInstances` (`float`)
      * `minPendingLatency` (`str`)
      * `minTotalInstances` (`float`)
      * `networkUtilization` (`dict`)
        * `targetReceivedBytesPerSecond` (`float`)
        * `targetReceivedPacketsPerSecond` (`float`)
        * `targetSentBytesPerSecond` (`float`)
        * `targetSentPacketsPerSecond` (`float`)

      * `requestUtilization` (`dict`)
        * `targetConcurrentRequests` (`float`)
        * `targetRequestCountPerSecond` (`str`)
    """
    beta_settings: pulumi.Output[dict]
    """
    Metadata settings that are supplied to this version to enable beta runtime features.
    """
    default_expiration: pulumi.Output[str]
    """
    Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
    StaticFilesHandler does not specify its own expiration time.
    """
    delete_service_on_destroy: pulumi.Output[bool]
    """
    If set to `true`, the service will be deleted if it is the last version.    
    """
    deployment: pulumi.Output[dict]
    """
    Code and application artifacts that make up this version.

      * `cloudBuildOptions` (`dict`)
        * `appYamlPath` (`str`)
        * `cloudBuildTimeout` (`str`)

      * `container` (`dict`)
        * `image` (`str`)

      * `files` (`list`)
        * `name` (`str`) - The identifier for this object. Format specified above.
        * `sha1Sum` (`str`)
        * `sourceUrl` (`str`)

      * `zip` (`dict`)
        * `filesCount` (`float`)
        * `sourceUrl` (`str`)
    """
    endpoints_api_service: pulumi.Output[dict]
    """
    Code and application artifacts that make up this version.

      * `config_id` (`str`)
      * `disableTraceSampling` (`bool`)
      * `name` (`str`) - The identifier for this object. Format specified above.
      * `rolloutStrategy` (`str`)
    """
    entrypoint: pulumi.Output[dict]
    """
    The entrypoint for the application.

      * `shell` (`str`)
    """
    env_variables: pulumi.Output[dict]
    """
    Environment variables available to the application. As these are not returned in the API request, Terraform will not
    detect any changes made outside of the Terraform config.
    """
    inbound_services: pulumi.Output[list]
    """
    Before an application can receive email or XMPP messages, the application must be configured to enable the service.
    """
    instance_class: pulumi.Output[str]
    """
    Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
    B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
    """
    liveness_check: pulumi.Output[dict]
    """
    Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.

      * `checkInterval` (`str`)
      * `failureThreshold` (`float`)
      * `host` (`str`)
      * `initialDelay` (`str`)
      * `path` (`str`)
      * `successThreshold` (`float`)
      * `timeout` (`str`)
    """
    manual_scaling: pulumi.Output[dict]
    """
    A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
    its memory over time.

      * `instances` (`float`)
    """
    name: pulumi.Output[str]
    """
    The identifier for this object. Format specified above.
    """
    network: pulumi.Output[dict]
    """
    Extra network settings

      * `forwardedPorts` (`list`)
      * `instanceTag` (`str`)
      * `name` (`str`) - The identifier for this object. Format specified above.
      * `session_affinity` (`bool`)
      * `subnetwork` (`str`)
    """
    nobuild_files_regex: pulumi.Output[str]
    """
    Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
    """
    noop_on_destroy: pulumi.Output[bool]
    """
    If set to `true`, the application version will not be deleted.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    readiness_check: pulumi.Output[dict]
    """
    Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.

      * `appStartTimeout` (`str`)
      * `checkInterval` (`str`)
      * `failureThreshold` (`float`)
      * `host` (`str`)
      * `path` (`str`)
      * `successThreshold` (`float`)
      * `timeout` (`str`)
    """
    resources: pulumi.Output[dict]
    """
    Machine resources for a version.

      * `cpu` (`float`)
      * `diskGb` (`float`)
      * `memoryGb` (`float`)
      * `volumes` (`list`)
        * `name` (`str`) - The identifier for this object. Format specified above.
        * `sizeGb` (`float`)
        * `volumeType` (`str`)
    """
    runtime: pulumi.Output[str]
    """
    Desired runtime. Example python27.
    """
    runtime_api_version: pulumi.Output[str]
    """
    The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
    https://cloud.google.com/appengine/docs/standard//config/appref
    """
    runtime_channel: pulumi.Output[str]
    """
    The channel of the runtime to use. Only available for some runtimes.
    """
    runtime_main_executable_path: pulumi.Output[str]
    """
    The path or name of the app's main executable.
    """
    service: pulumi.Output[str]
    """
    AppEngine service resource
    """
    serving_status: pulumi.Output[str]
    """
    Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
    Defaults to SERVING.
    """
    version_id: pulumi.Output[str]
    """
    Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
    numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
    """
    vpc_access_connector: pulumi.Output[dict]
    """
    Enables VPC connectivity for standard apps.

      * `name` (`str`) - The identifier for this object. Format specified above.
    """
    def __init__(__self__, resource_name, opts=None, api_config=None, automatic_scaling=None, beta_settings=None, default_expiration=None, delete_service_on_destroy=None, deployment=None, endpoints_api_service=None, entrypoint=None, env_variables=None, inbound_services=None, instance_class=None, liveness_check=None, manual_scaling=None, network=None, nobuild_files_regex=None, noop_on_destroy=None, project=None, readiness_check=None, resources=None, runtime=None, runtime_api_version=None, runtime_channel=None, runtime_main_executable_path=None, service=None, serving_status=None, version_id=None, vpc_access_connector=None, __props__=None, __name__=None, __opts__=None):
        """
        Flexible App Version resource to create a new version of flexible GAE Application. Based on Google Compute Engine,
        the App Engine flexible environment automatically scales your app up and down while also balancing the load.
        Learn about the differences between the standard environment and the flexible environment
        at https://cloud.google.com/appengine/docs/the-appengine-environments.


        To get more information about FlexibleAppVersion, see:

        * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/appengine/docs/flexible)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_flexible_app_version.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] api_config: Serving configuration for Google Cloud Endpoints.
        :param pulumi.Input[dict] automatic_scaling: Automatic scaling is based on request rate, response latencies, and other application metrics.
        :param pulumi.Input[dict] beta_settings: Metadata settings that are supplied to this version to enable beta runtime features.
        :param pulumi.Input[str] default_expiration: Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
               StaticFilesHandler does not specify its own expiration time.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.    
        :param pulumi.Input[dict] deployment: Code and application artifacts that make up this version.
        :param pulumi.Input[dict] endpoints_api_service: Code and application artifacts that make up this version.
        :param pulumi.Input[dict] entrypoint: The entrypoint for the application.
        :param pulumi.Input[dict] env_variables: Environment variables available to the application. As these are not returned in the API request, Terraform will not
               detect any changes made outside of the Terraform config.
        :param pulumi.Input[list] inbound_services: Before an application can receive email or XMPP messages, the application must be configured to enable the service.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
               B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
        :param pulumi.Input[dict] liveness_check: Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
        :param pulumi.Input[dict] manual_scaling: A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
               its memory over time.
        :param pulumi.Input[dict] network: Extra network settings
        :param pulumi.Input[str] nobuild_files_regex: Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[dict] readiness_check: Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
        :param pulumi.Input[dict] resources: Machine resources for a version.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
               https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] runtime_channel: The channel of the runtime to use. Only available for some runtimes.
        :param pulumi.Input[str] runtime_main_executable_path: The path or name of the app's main executable.
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[str] serving_status: Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
               Defaults to SERVING.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
               numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
        :param pulumi.Input[dict] vpc_access_connector: Enables VPC connectivity for standard apps.

        The **api_config** object supports the following:

          * `authFailAction` (`pulumi.Input[str]`)
          * `login` (`pulumi.Input[str]`)
          * `script` (`pulumi.Input[str]`)
          * `securityLevel` (`pulumi.Input[str]`)
          * `url` (`pulumi.Input[str]`)

        The **automatic_scaling** object supports the following:

          * `coolDownPeriod` (`pulumi.Input[str]`)
          * `cpuUtilization` (`pulumi.Input[dict]`)
            * `aggregationWindowLength` (`pulumi.Input[str]`)
            * `targetUtilization` (`pulumi.Input[float]`)

          * `diskUtilization` (`pulumi.Input[dict]`)
            * `targetReadBytesPerSecond` (`pulumi.Input[float]`)
            * `targetReadOpsPerSecond` (`pulumi.Input[float]`)
            * `targetWriteBytesPerSecond` (`pulumi.Input[float]`)
            * `targetWriteOpsPerSecond` (`pulumi.Input[float]`)

          * `maxConcurrentRequests` (`pulumi.Input[float]`)
          * `maxIdleInstances` (`pulumi.Input[float]`)
          * `maxPendingLatency` (`pulumi.Input[str]`)
          * `maxTotalInstances` (`pulumi.Input[float]`)
          * `minIdleInstances` (`pulumi.Input[float]`)
          * `minPendingLatency` (`pulumi.Input[str]`)
          * `minTotalInstances` (`pulumi.Input[float]`)
          * `networkUtilization` (`pulumi.Input[dict]`)
            * `targetReceivedBytesPerSecond` (`pulumi.Input[float]`)
            * `targetReceivedPacketsPerSecond` (`pulumi.Input[float]`)
            * `targetSentBytesPerSecond` (`pulumi.Input[float]`)
            * `targetSentPacketsPerSecond` (`pulumi.Input[float]`)

          * `requestUtilization` (`pulumi.Input[dict]`)
            * `targetConcurrentRequests` (`pulumi.Input[float]`)
            * `targetRequestCountPerSecond` (`pulumi.Input[str]`)

        The **deployment** object supports the following:

          * `cloudBuildOptions` (`pulumi.Input[dict]`)
            * `appYamlPath` (`pulumi.Input[str]`)
            * `cloudBuildTimeout` (`pulumi.Input[str]`)

          * `container` (`pulumi.Input[dict]`)
            * `image` (`pulumi.Input[str]`)

          * `files` (`pulumi.Input[list]`)
            * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
            * `sha1Sum` (`pulumi.Input[str]`)
            * `sourceUrl` (`pulumi.Input[str]`)

          * `zip` (`pulumi.Input[dict]`)
            * `filesCount` (`pulumi.Input[float]`)
            * `sourceUrl` (`pulumi.Input[str]`)

        The **endpoints_api_service** object supports the following:

          * `config_id` (`pulumi.Input[str]`)
          * `disableTraceSampling` (`pulumi.Input[bool]`)
          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
          * `rolloutStrategy` (`pulumi.Input[str]`)

        The **entrypoint** object supports the following:

          * `shell` (`pulumi.Input[str]`)

        The **liveness_check** object supports the following:

          * `checkInterval` (`pulumi.Input[str]`)
          * `failureThreshold` (`pulumi.Input[float]`)
          * `host` (`pulumi.Input[str]`)
          * `initialDelay` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `successThreshold` (`pulumi.Input[float]`)
          * `timeout` (`pulumi.Input[str]`)

        The **manual_scaling** object supports the following:

          * `instances` (`pulumi.Input[float]`)

        The **network** object supports the following:

          * `forwardedPorts` (`pulumi.Input[list]`)
          * `instanceTag` (`pulumi.Input[str]`)
          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
          * `session_affinity` (`pulumi.Input[bool]`)
          * `subnetwork` (`pulumi.Input[str]`)

        The **readiness_check** object supports the following:

          * `appStartTimeout` (`pulumi.Input[str]`)
          * `checkInterval` (`pulumi.Input[str]`)
          * `failureThreshold` (`pulumi.Input[float]`)
          * `host` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `successThreshold` (`pulumi.Input[float]`)
          * `timeout` (`pulumi.Input[str]`)

        The **resources** object supports the following:

          * `cpu` (`pulumi.Input[float]`)
          * `diskGb` (`pulumi.Input[float]`)
          * `memoryGb` (`pulumi.Input[float]`)
          * `volumes` (`pulumi.Input[list]`)
            * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
            * `sizeGb` (`pulumi.Input[float]`)
            * `volumeType` (`pulumi.Input[str]`)

        The **vpc_access_connector** object supports the following:

          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
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

            __props__['api_config'] = api_config
            __props__['automatic_scaling'] = automatic_scaling
            __props__['beta_settings'] = beta_settings
            __props__['default_expiration'] = default_expiration
            __props__['delete_service_on_destroy'] = delete_service_on_destroy
            __props__['deployment'] = deployment
            __props__['endpoints_api_service'] = endpoints_api_service
            __props__['entrypoint'] = entrypoint
            __props__['env_variables'] = env_variables
            __props__['inbound_services'] = inbound_services
            __props__['instance_class'] = instance_class
            if liveness_check is None:
                raise TypeError("Missing required property 'liveness_check'")
            __props__['liveness_check'] = liveness_check
            __props__['manual_scaling'] = manual_scaling
            __props__['network'] = network
            __props__['nobuild_files_regex'] = nobuild_files_regex
            __props__['noop_on_destroy'] = noop_on_destroy
            __props__['project'] = project
            if readiness_check is None:
                raise TypeError("Missing required property 'readiness_check'")
            __props__['readiness_check'] = readiness_check
            __props__['resources'] = resources
            if runtime is None:
                raise TypeError("Missing required property 'runtime'")
            __props__['runtime'] = runtime
            __props__['runtime_api_version'] = runtime_api_version
            __props__['runtime_channel'] = runtime_channel
            __props__['runtime_main_executable_path'] = runtime_main_executable_path
            __props__['service'] = service
            __props__['serving_status'] = serving_status
            __props__['version_id'] = version_id
            __props__['vpc_access_connector'] = vpc_access_connector
            __props__['name'] = None
        super(FlexibleAppVersion, __self__).__init__(
            'gcp:appengine/flexibleAppVersion:FlexibleAppVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, api_config=None, automatic_scaling=None, beta_settings=None, default_expiration=None, delete_service_on_destroy=None, deployment=None, endpoints_api_service=None, entrypoint=None, env_variables=None, inbound_services=None, instance_class=None, liveness_check=None, manual_scaling=None, name=None, network=None, nobuild_files_regex=None, noop_on_destroy=None, project=None, readiness_check=None, resources=None, runtime=None, runtime_api_version=None, runtime_channel=None, runtime_main_executable_path=None, service=None, serving_status=None, version_id=None, vpc_access_connector=None):
        """
        Get an existing FlexibleAppVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] api_config: Serving configuration for Google Cloud Endpoints.
        :param pulumi.Input[dict] automatic_scaling: Automatic scaling is based on request rate, response latencies, and other application metrics.
        :param pulumi.Input[dict] beta_settings: Metadata settings that are supplied to this version to enable beta runtime features.
        :param pulumi.Input[str] default_expiration: Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
               StaticFilesHandler does not specify its own expiration time.
        :param pulumi.Input[bool] delete_service_on_destroy: If set to `true`, the service will be deleted if it is the last version.    
        :param pulumi.Input[dict] deployment: Code and application artifacts that make up this version.
        :param pulumi.Input[dict] endpoints_api_service: Code and application artifacts that make up this version.
        :param pulumi.Input[dict] entrypoint: The entrypoint for the application.
        :param pulumi.Input[dict] env_variables: Environment variables available to the application. As these are not returned in the API request, Terraform will not
               detect any changes made outside of the Terraform config.
        :param pulumi.Input[list] inbound_services: Before an application can receive email or XMPP messages, the application must be configured to enable the service.
        :param pulumi.Input[str] instance_class: Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
               B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.
        :param pulumi.Input[dict] liveness_check: Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.
        :param pulumi.Input[dict] manual_scaling: A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
               its memory over time.
        :param pulumi.Input[str] name: The identifier for this object. Format specified above.
        :param pulumi.Input[dict] network: Extra network settings
        :param pulumi.Input[str] nobuild_files_regex: Files that match this pattern will not be built into this version. Only applicable for Go runtimes.
        :param pulumi.Input[bool] noop_on_destroy: If set to `true`, the application version will not be deleted.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[dict] readiness_check: Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.
        :param pulumi.Input[dict] resources: Machine resources for a version.
        :param pulumi.Input[str] runtime: Desired runtime. Example python27.
        :param pulumi.Input[str] runtime_api_version: The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
               https://cloud.google.com/appengine/docs/standard//config/appref
        :param pulumi.Input[str] runtime_channel: The channel of the runtime to use. Only available for some runtimes.
        :param pulumi.Input[str] runtime_main_executable_path: The path or name of the app's main executable.
        :param pulumi.Input[str] service: AppEngine service resource
        :param pulumi.Input[str] serving_status: Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
               Defaults to SERVING.
        :param pulumi.Input[str] version_id: Relative name of the version within the service. For example, 'v1'. Version names can contain only lowercase letters,
               numbers, or hyphens. Reserved names,"default", "latest", and any name with the prefix "ah-".
        :param pulumi.Input[dict] vpc_access_connector: Enables VPC connectivity for standard apps.

        The **api_config** object supports the following:

          * `authFailAction` (`pulumi.Input[str]`)
          * `login` (`pulumi.Input[str]`)
          * `script` (`pulumi.Input[str]`)
          * `securityLevel` (`pulumi.Input[str]`)
          * `url` (`pulumi.Input[str]`)

        The **automatic_scaling** object supports the following:

          * `coolDownPeriod` (`pulumi.Input[str]`)
          * `cpuUtilization` (`pulumi.Input[dict]`)
            * `aggregationWindowLength` (`pulumi.Input[str]`)
            * `targetUtilization` (`pulumi.Input[float]`)

          * `diskUtilization` (`pulumi.Input[dict]`)
            * `targetReadBytesPerSecond` (`pulumi.Input[float]`)
            * `targetReadOpsPerSecond` (`pulumi.Input[float]`)
            * `targetWriteBytesPerSecond` (`pulumi.Input[float]`)
            * `targetWriteOpsPerSecond` (`pulumi.Input[float]`)

          * `maxConcurrentRequests` (`pulumi.Input[float]`)
          * `maxIdleInstances` (`pulumi.Input[float]`)
          * `maxPendingLatency` (`pulumi.Input[str]`)
          * `maxTotalInstances` (`pulumi.Input[float]`)
          * `minIdleInstances` (`pulumi.Input[float]`)
          * `minPendingLatency` (`pulumi.Input[str]`)
          * `minTotalInstances` (`pulumi.Input[float]`)
          * `networkUtilization` (`pulumi.Input[dict]`)
            * `targetReceivedBytesPerSecond` (`pulumi.Input[float]`)
            * `targetReceivedPacketsPerSecond` (`pulumi.Input[float]`)
            * `targetSentBytesPerSecond` (`pulumi.Input[float]`)
            * `targetSentPacketsPerSecond` (`pulumi.Input[float]`)

          * `requestUtilization` (`pulumi.Input[dict]`)
            * `targetConcurrentRequests` (`pulumi.Input[float]`)
            * `targetRequestCountPerSecond` (`pulumi.Input[str]`)

        The **deployment** object supports the following:

          * `cloudBuildOptions` (`pulumi.Input[dict]`)
            * `appYamlPath` (`pulumi.Input[str]`)
            * `cloudBuildTimeout` (`pulumi.Input[str]`)

          * `container` (`pulumi.Input[dict]`)
            * `image` (`pulumi.Input[str]`)

          * `files` (`pulumi.Input[list]`)
            * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
            * `sha1Sum` (`pulumi.Input[str]`)
            * `sourceUrl` (`pulumi.Input[str]`)

          * `zip` (`pulumi.Input[dict]`)
            * `filesCount` (`pulumi.Input[float]`)
            * `sourceUrl` (`pulumi.Input[str]`)

        The **endpoints_api_service** object supports the following:

          * `config_id` (`pulumi.Input[str]`)
          * `disableTraceSampling` (`pulumi.Input[bool]`)
          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
          * `rolloutStrategy` (`pulumi.Input[str]`)

        The **entrypoint** object supports the following:

          * `shell` (`pulumi.Input[str]`)

        The **liveness_check** object supports the following:

          * `checkInterval` (`pulumi.Input[str]`)
          * `failureThreshold` (`pulumi.Input[float]`)
          * `host` (`pulumi.Input[str]`)
          * `initialDelay` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `successThreshold` (`pulumi.Input[float]`)
          * `timeout` (`pulumi.Input[str]`)

        The **manual_scaling** object supports the following:

          * `instances` (`pulumi.Input[float]`)

        The **network** object supports the following:

          * `forwardedPorts` (`pulumi.Input[list]`)
          * `instanceTag` (`pulumi.Input[str]`)
          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
          * `session_affinity` (`pulumi.Input[bool]`)
          * `subnetwork` (`pulumi.Input[str]`)

        The **readiness_check** object supports the following:

          * `appStartTimeout` (`pulumi.Input[str]`)
          * `checkInterval` (`pulumi.Input[str]`)
          * `failureThreshold` (`pulumi.Input[float]`)
          * `host` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `successThreshold` (`pulumi.Input[float]`)
          * `timeout` (`pulumi.Input[str]`)

        The **resources** object supports the following:

          * `cpu` (`pulumi.Input[float]`)
          * `diskGb` (`pulumi.Input[float]`)
          * `memoryGb` (`pulumi.Input[float]`)
          * `volumes` (`pulumi.Input[list]`)
            * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
            * `sizeGb` (`pulumi.Input[float]`)
            * `volumeType` (`pulumi.Input[str]`)

        The **vpc_access_connector** object supports the following:

          * `name` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_config"] = api_config
        __props__["automatic_scaling"] = automatic_scaling
        __props__["beta_settings"] = beta_settings
        __props__["default_expiration"] = default_expiration
        __props__["delete_service_on_destroy"] = delete_service_on_destroy
        __props__["deployment"] = deployment
        __props__["endpoints_api_service"] = endpoints_api_service
        __props__["entrypoint"] = entrypoint
        __props__["env_variables"] = env_variables
        __props__["inbound_services"] = inbound_services
        __props__["instance_class"] = instance_class
        __props__["liveness_check"] = liveness_check
        __props__["manual_scaling"] = manual_scaling
        __props__["name"] = name
        __props__["network"] = network
        __props__["nobuild_files_regex"] = nobuild_files_regex
        __props__["noop_on_destroy"] = noop_on_destroy
        __props__["project"] = project
        __props__["readiness_check"] = readiness_check
        __props__["resources"] = resources
        __props__["runtime"] = runtime
        __props__["runtime_api_version"] = runtime_api_version
        __props__["runtime_channel"] = runtime_channel
        __props__["runtime_main_executable_path"] = runtime_main_executable_path
        __props__["service"] = service
        __props__["serving_status"] = serving_status
        __props__["version_id"] = version_id
        __props__["vpc_access_connector"] = vpc_access_connector
        return FlexibleAppVersion(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

