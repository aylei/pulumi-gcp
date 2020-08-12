// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.IdentityPlatform.Inputs
{

    public sealed class InboundSamlConfigIdpConfigArgs : Pulumi.ResourceArgs
    {
        [Input("idpCertificates", required: true)]
        private InputList<Inputs.InboundSamlConfigIdpConfigIdpCertificateArgs>? _idpCertificates;

        /// <summary>
        /// The IdP's certificate data to verify the signature in the SAMLResponse issued by the IDP.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.InboundSamlConfigIdpConfigIdpCertificateArgs> IdpCertificates
        {
            get => _idpCertificates ?? (_idpCertificates = new InputList<Inputs.InboundSamlConfigIdpConfigIdpCertificateArgs>());
            set => _idpCertificates = value;
        }

        /// <summary>
        /// Unique identifier for all SAML entities
        /// </summary>
        [Input("idpEntityId", required: true)]
        public Input<string> IdpEntityId { get; set; } = null!;

        /// <summary>
        /// Indicates if outbounding SAMLRequest should be signed.
        /// </summary>
        [Input("signRequest")]
        public Input<bool>? SignRequest { get; set; }

        /// <summary>
        /// URL to send Authentication request to.
        /// </summary>
        [Input("ssoUrl", required: true)]
        public Input<string> SsoUrl { get; set; } = null!;

        public InboundSamlConfigIdpConfigArgs()
        {
        }
    }
}
