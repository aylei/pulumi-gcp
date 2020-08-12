// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.PubSub.Inputs
{

    public sealed class SubscriptionPushConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("attributes")]
        private InputMap<string>? _attributes;

        /// <summary>
        /// Endpoint configuration attributes.
        /// Every endpoint has a set of API supported attributes that can
        /// be used to control different aspects of the message delivery.
        /// The currently supported attribute is x-goog-version, which you
        /// can use to change the format of the pushed message. This
        /// attribute indicates the version of the data expected by
        /// the endpoint. This controls the shape of the pushed message
        /// (i.e., its fields and metadata). The endpoint version is
        /// based on the version of the Pub/Sub API.
        /// If not present during the subscriptions.create call,
        /// it will default to the version of the API used to make
        /// such call. If not present during a subscriptions.modifyPushConfig
        /// call, its value will not be changed. subscriptions.get
        /// calls will always return a valid version, even if the
        /// subscription was created without this attribute.
        /// The possible values for this attribute are:
        /// - v1beta1: uses the push format defined in the v1beta1 Pub/Sub API.
        /// - v1 or v1beta2: uses the push format defined in the v1 Pub/Sub API.
        /// </summary>
        public InputMap<string> Attributes
        {
            get => _attributes ?? (_attributes = new InputMap<string>());
            set => _attributes = value;
        }

        /// <summary>
        /// If specified, Pub/Sub will generate and attach an OIDC JWT token as
        /// an Authorization header in the HTTP request for every pushed message.
        /// Structure is documented below.
        /// </summary>
        [Input("oidcToken")]
        public Input<Inputs.SubscriptionPushConfigOidcTokenGetArgs>? OidcToken { get; set; }

        /// <summary>
        /// A URL locating the endpoint to which messages should be pushed.
        /// For example, a Webhook endpoint might use
        /// "https://example.com/push".
        /// </summary>
        [Input("pushEndpoint", required: true)]
        public Input<string> PushEndpoint { get; set; } = null!;

        public SubscriptionPushConfigGetArgs()
        {
        }
    }
}
