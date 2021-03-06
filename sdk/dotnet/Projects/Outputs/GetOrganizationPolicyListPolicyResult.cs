// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Projects.Outputs
{

    [OutputType]
    public sealed class GetOrganizationPolicyListPolicyResult
    {
        public readonly ImmutableArray<Outputs.GetOrganizationPolicyListPolicyAllowResult> Allows;
        public readonly ImmutableArray<Outputs.GetOrganizationPolicyListPolicyDenyResult> Denies;
        public readonly bool InheritFromParent;
        public readonly string SuggestedValue;

        [OutputConstructor]
        private GetOrganizationPolicyListPolicyResult(
            ImmutableArray<Outputs.GetOrganizationPolicyListPolicyAllowResult> allows,

            ImmutableArray<Outputs.GetOrganizationPolicyListPolicyDenyResult> denies,

            bool inheritFromParent,

            string suggestedValue)
        {
            Allows = allows;
            Denies = denies;
            InheritFromParent = inheritFromParent;
            SuggestedValue = suggestedValue;
        }
    }
}
