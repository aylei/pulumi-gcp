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
    public sealed class GetServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceResult
    {
        /// <summary>
        /// The name of the Cloud Run Service.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceResult(string name)
        {
            Name = name;
        }
    }
}
