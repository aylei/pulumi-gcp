// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudScheduler.Inputs
{

    public sealed class JobHttpTargetOauthTokenArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// OAuth scope to be used for generating OAuth access token. If not specified,
        /// "https://www.googleapis.com/auth/cloud-platform" will be used.
        /// </summary>
        [Input("scope")]
        public Input<string>? Scope { get; set; }

        /// <summary>
        /// Service account email to be used for generating OAuth token.
        /// The service account must be within the same project as the job.
        /// </summary>
        [Input("serviceAccountEmail", required: true)]
        public Input<string> ServiceAccountEmail { get; set; } = null!;

        public JobHttpTargetOauthTokenArgs()
        {
        }
    }
}