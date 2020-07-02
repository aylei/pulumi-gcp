# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class GameServerDeploymentRollout(pulumi.CustomResource):
    default_game_server_config: pulumi.Output[str]
    """
    This field points to the game server config that is
    applied by default to all realms and clusters. For example,
    `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
    """
    deployment_id: pulumi.Output[str]
    """
    The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
    """
    game_server_config_overrides: pulumi.Output[list]
    """
    The game_server_config_overrides contains the per game server config
    overrides. The overrides are processed in the order they are listed. As
    soon as a match is found for a cluster, the rest of the list is not
    processed.  Structure is documented below.

      * `configVersion` (`str`) - Version of the configuration.
      * `realmsSelector` (`dict`) - Selection by realms.  Structure is documented below.
        * `realms` (`list`) - List of realms to match against.
    """
    name: pulumi.Output[str]
    """
    The resource id of the game server deployment eg:
    'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    def __init__(__self__, resource_name, opts=None, default_game_server_config=None, deployment_id=None, game_server_config_overrides=None, project=None, __props__=None, __name__=None, __opts__=None):
        """
        This represents the rollout state. This is part of the game server
        deployment.

        To get more information about GameServerDeploymentRollout, see:

        * [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/GameServerDeploymentRollout)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/game-servers/docs)

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_game_server_config: This field points to the game server config that is
               applied by default to all realms and clusters. For example,
               `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        :param pulumi.Input[str] deployment_id: The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        :param pulumi.Input[list] game_server_config_overrides: The game_server_config_overrides contains the per game server config
               overrides. The overrides are processed in the order they are listed. As
               soon as a match is found for a cluster, the rest of the list is not
               processed.  Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        The **game_server_config_overrides** object supports the following:

          * `configVersion` (`pulumi.Input[str]`) - Version of the configuration.
          * `realmsSelector` (`pulumi.Input[dict]`) - Selection by realms.  Structure is documented below.
            * `realms` (`pulumi.Input[list]`) - List of realms to match against.
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

            if default_game_server_config is None:
                raise TypeError("Missing required property 'default_game_server_config'")
            __props__['default_game_server_config'] = default_game_server_config
            if deployment_id is None:
                raise TypeError("Missing required property 'deployment_id'")
            __props__['deployment_id'] = deployment_id
            __props__['game_server_config_overrides'] = game_server_config_overrides
            __props__['project'] = project
            __props__['name'] = None
        super(GameServerDeploymentRollout, __self__).__init__(
            'gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, default_game_server_config=None, deployment_id=None, game_server_config_overrides=None, name=None, project=None):
        """
        Get an existing GameServerDeploymentRollout resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_game_server_config: This field points to the game server config that is
               applied by default to all realms and clusters. For example,
               `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        :param pulumi.Input[str] deployment_id: The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        :param pulumi.Input[list] game_server_config_overrides: The game_server_config_overrides contains the per game server config
               overrides. The overrides are processed in the order they are listed. As
               soon as a match is found for a cluster, the rest of the list is not
               processed.  Structure is documented below.
        :param pulumi.Input[str] name: The resource id of the game server deployment eg:
               'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.

        The **game_server_config_overrides** object supports the following:

          * `configVersion` (`pulumi.Input[str]`) - Version of the configuration.
          * `realmsSelector` (`pulumi.Input[dict]`) - Selection by realms.  Structure is documented below.
            * `realms` (`pulumi.Input[list]`) - List of realms to match against.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["default_game_server_config"] = default_game_server_config
        __props__["deployment_id"] = deployment_id
        __props__["game_server_config_overrides"] = game_server_config_overrides
        __props__["name"] = name
        __props__["project"] = project
        return GameServerDeploymentRollout(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
