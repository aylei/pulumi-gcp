// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Kms.Outputs
{

    [OutputType]
    public sealed class GetKMSCryptoKeyVersionTemplateResult
    {
        public readonly string Algorithm;
        public readonly string ProtectionLevel;

        [OutputConstructor]
        private GetKMSCryptoKeyVersionTemplateResult(
            string algorithm,

            string protectionLevel)
        {
            Algorithm = algorithm;
            ProtectionLevel = protectionLevel;
        }
    }
}
