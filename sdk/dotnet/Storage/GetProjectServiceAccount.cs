// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Storage
{
    public static class GetProjectServiceAccount
    {
        /// <summary>
        /// Get the email address of a project's unique Google Cloud Storage service account.
        /// 
        /// Each Google Cloud project has a unique service account for use with Google Cloud Storage. Only this
        /// special service account can be used to set up `gcp.storage.Notification` resources.
        /// 
        /// For more information see
        /// [the API reference](https://cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount).
        /// </summary>
        public static Task<GetProjectServiceAccountResult> InvokeAsync(GetProjectServiceAccountArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProjectServiceAccountResult>("gcp:storage/getProjectServiceAccount:getProjectServiceAccount", args ?? new GetProjectServiceAccountArgs(), options.WithVersion());
    }


    public sealed class GetProjectServiceAccountArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The project the unique service account was created for. If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// The project the lookup originates from. This field is used if you are making the request
        /// from a different account than the one you are finding the service account for.
        /// </summary>
        [Input("userProject")]
        public string? UserProject { get; set; }

        public GetProjectServiceAccountArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetProjectServiceAccountResult
    {
        /// <summary>
        /// The email address of the service account. This value is often used to refer to the service account
        /// in order to grant IAM permissions.
        /// </summary>
        public readonly string EmailAddress;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Project;
        public readonly string? UserProject;

        [OutputConstructor]
        private GetProjectServiceAccountResult(
            string emailAddress,

            string id,

            string project,

            string? userProject)
        {
            EmailAddress = emailAddress;
            Id = id;
            Project = project;
            UserProject = userProject;
        }
    }
}
