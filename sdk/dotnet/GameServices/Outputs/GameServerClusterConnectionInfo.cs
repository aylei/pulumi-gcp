// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.GameServices.Outputs
{

    [OutputType]
    public sealed class GameServerClusterConnectionInfo
    {
        /// <summary>
        /// Reference of the GKE cluster where the game servers are installed.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.GameServerClusterConnectionInfoGkeClusterReference GkeClusterReference;
        /// <summary>
        /// Namespace designated on the game server cluster where the game server
        /// instances will be created. The namespace existence will be validated
        /// during creation.
        /// </summary>
        public readonly string Namespace;

        [OutputConstructor]
        private GameServerClusterConnectionInfo(
            Outputs.GameServerClusterConnectionInfoGkeClusterReference gkeClusterReference,

            string @namespace)
        {
            GkeClusterReference = gkeClusterReference;
            Namespace = @namespace;
        }
    }
}
