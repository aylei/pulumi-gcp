// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Kms
{
    public static class GetKMSCryptoKey
    {
        /// <summary>
        /// Provides access to a Google Cloud Platform KMS CryptoKey. For more information see
        /// [the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#key)
        /// and
        /// [API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys).
        /// 
        /// A CryptoKey is an interface to key material which can be used to encrypt and decrypt data. A CryptoKey belongs to a
        /// Google Cloud KMS KeyRing.
        /// </summary>
        public static Task<GetKMSCryptoKeyResult> InvokeAsync(GetKMSCryptoKeyArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetKMSCryptoKeyResult>("gcp:kms/getKMSCryptoKey:getKMSCryptoKey", args ?? new GetKMSCryptoKeyArgs(), options.WithVersion());
    }


    public sealed class GetKMSCryptoKeyArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The `self_link` of the Google Cloud Platform KeyRing to which the key belongs.
        /// </summary>
        [Input("keyRing", required: true)]
        public string KeyRing { get; set; } = null!;

        /// <summary>
        /// The CryptoKey's name.
        /// A CryptoKey’s name belonging to the specified Google Cloud Platform KeyRing and match the regular expression `[a-zA-Z0-9_-]{1,63}`
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetKMSCryptoKeyArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetKMSCryptoKeyResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string KeyRing;
        public readonly ImmutableDictionary<string, string> Labels;
        public readonly string Name;
        /// <summary>
        /// Defines the cryptographic capabilities of the key.
        /// </summary>
        public readonly string Purpose;
        /// <summary>
        /// Every time this period passes, generate a new CryptoKeyVersion and set it as
        /// the primary. The first rotation will take place after the specified period. The rotation period has the format
        /// of a decimal number with up to 9 fractional digits, followed by the letter s (seconds).
        /// </summary>
        public readonly string RotationPeriod;
        /// <summary>
        /// The self link of the created CryptoKey. Its format is `projects/{projectId}/locations/{location}/keyRings/{keyRingName}/cryptoKeys/{cryptoKeyName}`.
        /// </summary>
        public readonly string SelfLink;
        public readonly ImmutableArray<Outputs.GetKMSCryptoKeyVersionTemplateResult> VersionTemplates;

        [OutputConstructor]
        private GetKMSCryptoKeyResult(
            string id,

            string keyRing,

            ImmutableDictionary<string, string> labels,

            string name,

            string purpose,

            string rotationPeriod,

            string selfLink,

            ImmutableArray<Outputs.GetKMSCryptoKeyVersionTemplateResult> versionTemplates)
        {
            Id = id;
            KeyRing = keyRing;
            Labels = labels;
            Name = name;
            Purpose = purpose;
            RotationPeriod = rotationPeriod;
            SelfLink = selfLink;
            VersionTemplates = versionTemplates;
        }
    }
}
