// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AppEngine.Inputs
{

    public sealed class EngineSplitTrafficSplitArgs : Pulumi.ResourceArgs
    {
        [Input("allocations", required: true)]
        private InputMap<string>? _allocations;

        /// <summary>
        /// Mapping from version IDs within the service to fractional (0.000, 1] allocations of traffic for that version. Each version can be specified only once, but some versions in the service may not have any traffic allocation. Services that have traffic allocated cannot be deleted until either the service is deleted or their traffic allocation is removed. Allocations must sum to 1. Up to two decimal place precision is supported for IP-based splits and up to three decimal places is supported for cookie-based splits.
        /// </summary>
        public InputMap<string> Allocations
        {
            get => _allocations ?? (_allocations = new InputMap<string>());
            set => _allocations = value;
        }

        /// <summary>
        /// Mechanism used to determine which version a request is sent to. The traffic selection algorithm will be stable for either type until allocations are changed.
        /// </summary>
        [Input("shardBy")]
        public Input<string>? ShardBy { get; set; }

        public EngineSplitTrafficSplitArgs()
        {
        }
    }
}