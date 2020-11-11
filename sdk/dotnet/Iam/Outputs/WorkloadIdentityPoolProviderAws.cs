// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Iam.Outputs
{

    [OutputType]
    public sealed class WorkloadIdentityPoolProviderAws
    {
        /// <summary>
        /// The AWS account ID.
        /// </summary>
        public readonly string AccountId;

        [OutputConstructor]
        private WorkloadIdentityPoolProviderAws(string accountId)
        {
            AccountId = accountId;
        }
    }
}
