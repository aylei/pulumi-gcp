// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Organizations.Outputs
{

    [OutputType]
    public sealed class AccessApprovalSettingsEnrolledService
    {
        public readonly string CloudProduct;
        public readonly string? EnrollmentLevel;

        [OutputConstructor]
        private AccessApprovalSettingsEnrolledService(
            string cloudProduct,

            string? enrollmentLevel)
        {
            CloudProduct = cloudProduct;
            EnrollmentLevel = enrollmentLevel;
        }
    }
}
