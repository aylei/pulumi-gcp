# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Agent(pulumi.CustomResource):
    api_version: pulumi.Output[str]
    """
    API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query
    different service endpoints for different API versions. However, bots connectors and webhook calls will follow
    the specified API version.
    * API_VERSION_V1: Legacy V1 API.
    * API_VERSION_V2: V2 API.
    * API_VERSION_V2_BETA_1: V2beta1 API.
    """
    avatar_uri: pulumi.Output[str]
    """
    The URI of the agent's avatar, which are used throughout the Dialogflow console. When an image URL is entered
    into this field, the Dialogflow will save the image in the backend. The address of the backend image returned
    from the API will be shown in the [avatarUriBackend] field.
    """
    avatar_uri_backend: pulumi.Output[str]
    """
    The URI of the agent's avatar as returned from the API. Output only. To provide an image URL for the agent avatar, the
    [avatarUri] field can be used.
    """
    classification_threshold: pulumi.Output[float]
    """
    To filter out false positive results and still get variety in matched natural language inputs for your agent,
    you can tune the machine learning classification threshold. If the returned score value is less than the threshold
    value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be
    triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the
    default of 0.3 is used.
    """
    default_language_code: pulumi.Output[str]
    """
    The default language of the agent as a language tag. [See Language Support](https://cloud.google.com/dialogflow/docs/reference/language)
    for a list of the currently supported language codes. This field cannot be updated after creation.
    """
    description: pulumi.Output[str]
    """
    The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.
    """
    display_name: pulumi.Output[str]
    """
    The name of this agent.
    """
    enable_logging: pulumi.Output[bool]
    """
    Determines whether this agent should log conversation queries.
    """
    match_mode: pulumi.Output[str]
    """
    Determines how intents are detected from user queries.
    * MATCH_MODE_HYBRID: Best for agents with a small number of examples in intents and/or wide use of templates
    syntax and composite entities.
    * MATCH_MODE_ML_ONLY: Can be used for agents with a large number of examples in intents, especially the ones
    using @sys.any or very large developer entities.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    supported_language_codes: pulumi.Output[list]
    """
    The list of all languages supported by this agent (except for the defaultLanguageCode).
    """
    tier: pulumi.Output[str]
    """
    The agent tier. If not specified, TIER_STANDARD is assumed.
    * TIER_STANDARD: Standard tier.
    * TIER_ENTERPRISE: Enterprise tier (Essentials).
    * TIER_ENTERPRISE_PLUS: Enterprise tier (Plus).
    NOTE: Due to consistency issues, the provider will not read this field from the API. Drift is possible between
    the the provider state and Dialogflow if the agent tier is changed outside of the provider.
    """
    time_zone: pulumi.Output[str]
    """
    The time zone of this agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York,
    Europe/Paris.
    """
    def __init__(__self__, resource_name, opts=None, api_version=None, avatar_uri=None, classification_threshold=None, default_language_code=None, description=None, display_name=None, enable_logging=None, match_mode=None, project=None, supported_language_codes=None, tier=None, time_zone=None, __props__=None, __name__=None, __opts__=None):
        """
        A Dialogflow agent is a virtual agent that handles conversations with your end-users. It is a natural language
        understanding module that understands the nuances of human language. Dialogflow translates end-user text or audio
        during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow
        agent to handle the types of conversations required for your system.

        To get more information about Agent, see:

        * [API documentation](https://cloud.google.com/dialogflow/docs/reference/rest/v2/projects/agent)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/dialogflow/docs/)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query
               different service endpoints for different API versions. However, bots connectors and webhook calls will follow
               the specified API version.
               * API_VERSION_V1: Legacy V1 API.
               * API_VERSION_V2: V2 API.
               * API_VERSION_V2_BETA_1: V2beta1 API.
        :param pulumi.Input[str] avatar_uri: The URI of the agent's avatar, which are used throughout the Dialogflow console. When an image URL is entered
               into this field, the Dialogflow will save the image in the backend. The address of the backend image returned
               from the API will be shown in the [avatarUriBackend] field.
        :param pulumi.Input[float] classification_threshold: To filter out false positive results and still get variety in matched natural language inputs for your agent,
               you can tune the machine learning classification threshold. If the returned score value is less than the threshold
               value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be
               triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the
               default of 0.3 is used.
        :param pulumi.Input[str] default_language_code: The default language of the agent as a language tag. [See Language Support](https://cloud.google.com/dialogflow/docs/reference/language)
               for a list of the currently supported language codes. This field cannot be updated after creation.
        :param pulumi.Input[str] description: The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.
        :param pulumi.Input[str] display_name: The name of this agent.
        :param pulumi.Input[bool] enable_logging: Determines whether this agent should log conversation queries.
        :param pulumi.Input[str] match_mode: Determines how intents are detected from user queries.
               * MATCH_MODE_HYBRID: Best for agents with a small number of examples in intents and/or wide use of templates
               syntax and composite entities.
               * MATCH_MODE_ML_ONLY: Can be used for agents with a large number of examples in intents, especially the ones
               using @sys.any or very large developer entities.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] supported_language_codes: The list of all languages supported by this agent (except for the defaultLanguageCode).
        :param pulumi.Input[str] tier: The agent tier. If not specified, TIER_STANDARD is assumed.
               * TIER_STANDARD: Standard tier.
               * TIER_ENTERPRISE: Enterprise tier (Essentials).
               * TIER_ENTERPRISE_PLUS: Enterprise tier (Plus).
               NOTE: Due to consistency issues, the provider will not read this field from the API. Drift is possible between
               the the provider state and Dialogflow if the agent tier is changed outside of the provider.
        :param pulumi.Input[str] time_zone: The time zone of this agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York,
               Europe/Paris.
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

            __props__['api_version'] = api_version
            __props__['avatar_uri'] = avatar_uri
            __props__['classification_threshold'] = classification_threshold
            if default_language_code is None:
                raise TypeError("Missing required property 'default_language_code'")
            __props__['default_language_code'] = default_language_code
            __props__['description'] = description
            if display_name is None:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            __props__['enable_logging'] = enable_logging
            __props__['match_mode'] = match_mode
            __props__['project'] = project
            __props__['supported_language_codes'] = supported_language_codes
            __props__['tier'] = tier
            if time_zone is None:
                raise TypeError("Missing required property 'time_zone'")
            __props__['time_zone'] = time_zone
            __props__['avatar_uri_backend'] = None
        super(Agent, __self__).__init__(
            'gcp:diagflow/agent:Agent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, api_version=None, avatar_uri=None, avatar_uri_backend=None, classification_threshold=None, default_language_code=None, description=None, display_name=None, enable_logging=None, match_mode=None, project=None, supported_language_codes=None, tier=None, time_zone=None):
        """
        Get an existing Agent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: API version displayed in Dialogflow console. If not specified, V2 API is assumed. Clients are free to query
               different service endpoints for different API versions. However, bots connectors and webhook calls will follow
               the specified API version.
               * API_VERSION_V1: Legacy V1 API.
               * API_VERSION_V2: V2 API.
               * API_VERSION_V2_BETA_1: V2beta1 API.
        :param pulumi.Input[str] avatar_uri: The URI of the agent's avatar, which are used throughout the Dialogflow console. When an image URL is entered
               into this field, the Dialogflow will save the image in the backend. The address of the backend image returned
               from the API will be shown in the [avatarUriBackend] field.
        :param pulumi.Input[str] avatar_uri_backend: The URI of the agent's avatar as returned from the API. Output only. To provide an image URL for the agent avatar, the
               [avatarUri] field can be used.
        :param pulumi.Input[float] classification_threshold: To filter out false positive results and still get variety in matched natural language inputs for your agent,
               you can tune the machine learning classification threshold. If the returned score value is less than the threshold
               value, then a fallback intent will be triggered or, if there are no fallback intents defined, no intent will be
               triggered. The score values range from 0.0 (completely uncertain) to 1.0 (completely certain). If set to 0.0, the
               default of 0.3 is used.
        :param pulumi.Input[str] default_language_code: The default language of the agent as a language tag. [See Language Support](https://cloud.google.com/dialogflow/docs/reference/language)
               for a list of the currently supported language codes. This field cannot be updated after creation.
        :param pulumi.Input[str] description: The description of this agent. The maximum length is 500 characters. If exceeded, the request is rejected.
        :param pulumi.Input[str] display_name: The name of this agent.
        :param pulumi.Input[bool] enable_logging: Determines whether this agent should log conversation queries.
        :param pulumi.Input[str] match_mode: Determines how intents are detected from user queries.
               * MATCH_MODE_HYBRID: Best for agents with a small number of examples in intents and/or wide use of templates
               syntax and composite entities.
               * MATCH_MODE_ML_ONLY: Can be used for agents with a large number of examples in intents, especially the ones
               using @sys.any or very large developer entities.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] supported_language_codes: The list of all languages supported by this agent (except for the defaultLanguageCode).
        :param pulumi.Input[str] tier: The agent tier. If not specified, TIER_STANDARD is assumed.
               * TIER_STANDARD: Standard tier.
               * TIER_ENTERPRISE: Enterprise tier (Essentials).
               * TIER_ENTERPRISE_PLUS: Enterprise tier (Plus).
               NOTE: Due to consistency issues, the provider will not read this field from the API. Drift is possible between
               the the provider state and Dialogflow if the agent tier is changed outside of the provider.
        :param pulumi.Input[str] time_zone: The time zone of this agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York,
               Europe/Paris.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_version"] = api_version
        __props__["avatar_uri"] = avatar_uri
        __props__["avatar_uri_backend"] = avatar_uri_backend
        __props__["classification_threshold"] = classification_threshold
        __props__["default_language_code"] = default_language_code
        __props__["description"] = description
        __props__["display_name"] = display_name
        __props__["enable_logging"] = enable_logging
        __props__["match_mode"] = match_mode
        __props__["project"] = project
        __props__["supported_language_codes"] = supported_language_codes
        __props__["tier"] = tier
        __props__["time_zone"] = time_zone
        return Agent(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
