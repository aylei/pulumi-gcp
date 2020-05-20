// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class RegionUrlMapTestGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of this test case.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Host portion of the URL.
        /// </summary>
        [Input("host", required: true)]
        public Input<string> Host { get; set; } = null!;

        /// <summary>
        /// Path portion of the URL.
        /// </summary>
        [Input("path", required: true)]
        public Input<string> Path { get; set; } = null!;

        /// <summary>
        /// A reference to expected RegionBackendService resource the given URL should be mapped to.
        /// </summary>
        [Input("service", required: true)]
        public Input<string> Service { get; set; } = null!;

        public RegionUrlMapTestGetArgs()
        {
        }
    }
}