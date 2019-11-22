// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Organizations
{
    /// <summary>
    /// Allows management of Organization policies for a Google Organization. For more information see
    /// [the official
    /// documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
    /// [API](https://cloud.google.com/resource-manager/reference/rest/v1/organizations/setOrgPolicy).
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/organization_policy.html.markdown.
    /// </summary>
    public partial class Policy : Pulumi.CustomResource
    {
        /// <summary>
        /// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
        /// </summary>
        [Output("booleanPolicy")]
        public Output<Outputs.PolicyBooleanPolicy?> BooleanPolicy { get; private set; } = null!;

        /// <summary>
        /// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
        /// </summary>
        [Output("constraint")]
        public Output<string> Constraint { get; private set; } = null!;

        /// <summary>
        /// (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
        /// </summary>
        [Output("listPolicy")]
        public Output<Outputs.PolicyListPolicy?> ListPolicy { get; private set; } = null!;

        /// <summary>
        /// The numeric ID of the organization to set the policy for.
        /// </summary>
        [Output("orgId")]
        public Output<string> OrgId { get; private set; } = null!;

        /// <summary>
        /// A restore policy is a constraint to restore the default policy. Structure is documented below.
        /// </summary>
        [Output("restorePolicy")]
        public Output<Outputs.PolicyRestorePolicy?> RestorePolicy { get; private set; } = null!;

        /// <summary>
        /// (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
        /// </summary>
        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;

        /// <summary>
        /// Version of the Policy. Default version is 0.
        /// </summary>
        [Output("version")]
        public Output<int> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Policy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Policy(string name, PolicyArgs args, CustomResourceOptions? options = null)
            : base("gcp:organizations/policy:Policy", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Policy(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
            : base("gcp:organizations/policy:Policy", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Policy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Policy Get(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new Policy(name, id, state, options);
        }
    }

    public sealed class PolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
        /// </summary>
        [Input("booleanPolicy")]
        public Input<Inputs.PolicyBooleanPolicyArgs>? BooleanPolicy { get; set; }

        /// <summary>
        /// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
        /// </summary>
        [Input("constraint", required: true)]
        public Input<string> Constraint { get; set; } = null!;

        /// <summary>
        /// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
        /// </summary>
        [Input("listPolicy")]
        public Input<Inputs.PolicyListPolicyArgs>? ListPolicy { get; set; }

        /// <summary>
        /// The numeric ID of the organization to set the policy for.
        /// </summary>
        [Input("orgId", required: true)]
        public Input<string> OrgId { get; set; } = null!;

        /// <summary>
        /// A restore policy is a constraint to restore the default policy. Structure is documented below.
        /// </summary>
        [Input("restorePolicy")]
        public Input<Inputs.PolicyRestorePolicyArgs>? RestorePolicy { get; set; }

        /// <summary>
        /// Version of the Policy. Default version is 0.
        /// </summary>
        [Input("version")]
        public Input<int>? Version { get; set; }

        public PolicyArgs()
        {
        }
    }

    public sealed class PolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A boolean policy is a constraint that is either enforced or not. Structure is documented below.
        /// </summary>
        [Input("booleanPolicy")]
        public Input<Inputs.PolicyBooleanPolicyGetArgs>? BooleanPolicy { get; set; }

        /// <summary>
        /// The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
        /// </summary>
        [Input("constraint")]
        public Input<string>? Constraint { get; set; }

        /// <summary>
        /// (Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
        /// </summary>
        [Input("listPolicy")]
        public Input<Inputs.PolicyListPolicyGetArgs>? ListPolicy { get; set; }

        /// <summary>
        /// The numeric ID of the organization to set the policy for.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// A restore policy is a constraint to restore the default policy. Structure is documented below.
        /// </summary>
        [Input("restorePolicy")]
        public Input<Inputs.PolicyRestorePolicyGetArgs>? RestorePolicy { get; set; }

        /// <summary>
        /// (Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
        /// </summary>
        [Input("updateTime")]
        public Input<string>? UpdateTime { get; set; }

        /// <summary>
        /// Version of the Policy. Default version is 0.
        /// </summary>
        [Input("version")]
        public Input<int>? Version { get; set; }

        public PolicyState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class PolicyBooleanPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("enforced", required: true)]
        public Input<bool> Enforced { get; set; } = null!;

        public PolicyBooleanPolicyArgs()
        {
        }
    }

    public sealed class PolicyBooleanPolicyGetArgs : Pulumi.ResourceArgs
    {
        [Input("enforced", required: true)]
        public Input<bool> Enforced { get; set; } = null!;

        public PolicyBooleanPolicyGetArgs()
        {
        }
    }

    public sealed class PolicyListPolicyAllowArgs : Pulumi.ResourceArgs
    {
        [Input("all")]
        public Input<bool>? All { get; set; }

        [Input("values")]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public PolicyListPolicyAllowArgs()
        {
        }
    }

    public sealed class PolicyListPolicyAllowGetArgs : Pulumi.ResourceArgs
    {
        [Input("all")]
        public Input<bool>? All { get; set; }

        [Input("values")]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public PolicyListPolicyAllowGetArgs()
        {
        }
    }

    public sealed class PolicyListPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("allow")]
        public Input<PolicyListPolicyAllowArgs>? Allow { get; set; }

        [Input("deny")]
        public Input<PolicyListPolicyDenyArgs>? Deny { get; set; }

        [Input("inheritFromParent")]
        public Input<bool>? InheritFromParent { get; set; }

        [Input("suggestedValue")]
        public Input<string>? SuggestedValue { get; set; }

        public PolicyListPolicyArgs()
        {
        }
    }

    public sealed class PolicyListPolicyDenyArgs : Pulumi.ResourceArgs
    {
        [Input("all")]
        public Input<bool>? All { get; set; }

        [Input("values")]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public PolicyListPolicyDenyArgs()
        {
        }
    }

    public sealed class PolicyListPolicyDenyGetArgs : Pulumi.ResourceArgs
    {
        [Input("all")]
        public Input<bool>? All { get; set; }

        [Input("values")]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public PolicyListPolicyDenyGetArgs()
        {
        }
    }

    public sealed class PolicyListPolicyGetArgs : Pulumi.ResourceArgs
    {
        [Input("allow")]
        public Input<PolicyListPolicyAllowGetArgs>? Allow { get; set; }

        [Input("deny")]
        public Input<PolicyListPolicyDenyGetArgs>? Deny { get; set; }

        [Input("inheritFromParent")]
        public Input<bool>? InheritFromParent { get; set; }

        [Input("suggestedValue")]
        public Input<string>? SuggestedValue { get; set; }

        public PolicyListPolicyGetArgs()
        {
        }
    }

    public sealed class PolicyRestorePolicyArgs : Pulumi.ResourceArgs
    {
        [Input("default", required: true)]
        public Input<bool> Default { get; set; } = null!;

        public PolicyRestorePolicyArgs()
        {
        }
    }

    public sealed class PolicyRestorePolicyGetArgs : Pulumi.ResourceArgs
    {
        [Input("default", required: true)]
        public Input<bool> Default { get; set; } = null!;

        public PolicyRestorePolicyGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class PolicyBooleanPolicy
    {
        public readonly bool Enforced;

        [OutputConstructor]
        private PolicyBooleanPolicy(bool enforced)
        {
            Enforced = enforced;
        }
    }

    [OutputType]
    public sealed class PolicyListPolicy
    {
        public readonly PolicyListPolicyAllow? Allow;
        public readonly PolicyListPolicyDeny? Deny;
        public readonly bool? InheritFromParent;
        public readonly string SuggestedValue;

        [OutputConstructor]
        private PolicyListPolicy(
            PolicyListPolicyAllow? allow,
            PolicyListPolicyDeny? deny,
            bool? inheritFromParent,
            string suggestedValue)
        {
            Allow = allow;
            Deny = deny;
            InheritFromParent = inheritFromParent;
            SuggestedValue = suggestedValue;
        }
    }

    [OutputType]
    public sealed class PolicyListPolicyAllow
    {
        public readonly bool? All;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private PolicyListPolicyAllow(
            bool? all,
            ImmutableArray<string> values)
        {
            All = all;
            Values = values;
        }
    }

    [OutputType]
    public sealed class PolicyListPolicyDeny
    {
        public readonly bool? All;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private PolicyListPolicyDeny(
            bool? all,
            ImmutableArray<string> values)
        {
            All = all;
            Values = values;
        }
    }

    [OutputType]
    public sealed class PolicyRestorePolicy
    {
        public readonly bool Default;

        [OutputConstructor]
        private PolicyRestorePolicy(bool @default)
        {
            Default = @default;
        }
    }
    }
}