// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Outputs
{

    [OutputType]
    public sealed class NodeGroupAutoscalingPolicy
    {
        /// <summary>
        /// Maximum size of the node group. Set to a value less than or equal
        /// to 100 and greater than or equal to min-nodes.
        /// </summary>
        public readonly int? MaxNodes;
        /// <summary>
        /// Minimum size of the node group. Must be less
        /// than or equal to max-nodes. The default value is 0.
        /// </summary>
        public readonly int? MinNodes;
        /// <summary>
        /// The autoscaling mode. Set to one of the following:
        /// - OFF: Disables the autoscaler.
        /// - ON: Enables scaling in and scaling out.
        /// - ONLY_SCALE_OUT: Enables only scaling out.
        /// You must use this mode if your node groups are configured to
        /// restart their hosted VMs on minimal servers.
        /// </summary>
        public readonly string? Mode;

        [OutputConstructor]
        private NodeGroupAutoscalingPolicy(
            int? maxNodes,

            int? minNodes,

            string? mode)
        {
            MaxNodes = maxNodes;
            MinNodes = minNodes;
            Mode = mode;
        }
    }
}