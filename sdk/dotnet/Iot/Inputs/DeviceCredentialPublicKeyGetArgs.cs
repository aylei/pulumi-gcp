// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Iot.Inputs
{

    public sealed class DeviceCredentialPublicKeyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The format of the key.
        /// </summary>
        [Input("format", required: true)]
        public Input<string> Format { get; set; } = null!;

        /// <summary>
        /// The key data.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        public DeviceCredentialPublicKeyGetArgs()
        {
        }
    }
}
