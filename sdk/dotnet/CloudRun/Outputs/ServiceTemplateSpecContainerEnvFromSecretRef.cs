// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudRun.Outputs
{

    [OutputType]
    public sealed class ServiceTemplateSpecContainerEnvFromSecretRef
    {
        /// <summary>
        /// The Secret to select from.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReference? LocalObjectReference;
        /// <summary>
        /// Specify whether the Secret must be defined
        /// </summary>
        public readonly bool? Optional;

        [OutputConstructor]
        private ServiceTemplateSpecContainerEnvFromSecretRef(
            Outputs.ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReference? localObjectReference,

            bool? optional)
        {
            LocalObjectReference = localObjectReference;
            Optional = optional;
        }
    }
}
