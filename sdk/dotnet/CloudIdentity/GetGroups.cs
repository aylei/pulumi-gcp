// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudIdentity
{
    public static class GetGroups
    {
        /// <summary>
        /// Use this data source to get list of the Cloud Identity Groups under a customer or namespace.
        /// 
        /// https://cloud.google.com/identity/docs/concepts/overview#groups
        /// </summary>
        public static Task<GetGroupsResult> InvokeAsync(GetGroupsArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetGroupsResult>("gcp:cloudidentity/getGroups:getGroups", args ?? new GetGroupsArgs(), options.WithVersion());
    }


    public sealed class GetGroupsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The parent resource under which to list all Groups. Must be of the form identitysources/{identity_source_id} for external- identity-mapped groups or customers/{customer_id} for Google Groups.
        /// </summary>
        [Input("parent", required: true)]
        public string Parent { get; set; } = null!;

        public GetGroupsArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetGroupsResult
    {
        /// <summary>
        /// The list of groups under the provided customer or namespace. Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetGroupsGroupResult> Groups;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Parent;

        [OutputConstructor]
        private GetGroupsResult(
            ImmutableArray<Outputs.GetGroupsGroupResult> groups,

            string id,

            string parent)
        {
            Groups = groups;
            Id = id;
            Parent = parent;
        }
    }
}