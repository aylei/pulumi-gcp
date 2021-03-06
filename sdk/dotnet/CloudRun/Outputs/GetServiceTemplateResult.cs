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
    public sealed class GetServiceTemplateResult
    {
        public readonly ImmutableArray<Outputs.GetServiceTemplateMetadataResult> Metadatas;
        public readonly ImmutableArray<Outputs.GetServiceTemplateSpecResult> Specs;

        [OutputConstructor]
        private GetServiceTemplateResult(
            ImmutableArray<Outputs.GetServiceTemplateMetadataResult> metadatas,

            ImmutableArray<Outputs.GetServiceTemplateSpecResult> specs)
        {
            Metadatas = metadatas;
            Specs = specs;
        }
    }
}
