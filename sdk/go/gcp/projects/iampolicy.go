// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package projects

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Four different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:
//
// * `projects.IAMPolicy`: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.
// * `projects.IAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.
// * `projects.IAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.
// * `projects.IAMAuditConfig`: Authoritative for a given service. Updates the IAM policy to enable audit logging for the given service.
//
// > **Note:** `projects.IAMPolicy` **cannot** be used in conjunction with `projects.IAMBinding`, `projects.IAMMember`, or `projects.IAMAuditConfig` or they will fight over what your policy should be.
//
// > **Note:** `projects.IAMBinding` resources **can be** used in conjunction with `projects.IAMMember` resources **only if** they do not grant privilege to the same role.
type IAMPolicy struct {
	pulumi.CustomResourceState

	// (Computed) The etag of the project's IAM policy.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// The `organizations.getIAMPolicy` data source that represents
	// the IAM policy that will be applied to the project. The policy will be
	// merged with any existing policy applied to the project.
	PolicyData pulumi.StringOutput `pulumi:"policyData"`
	// The project ID. If not specified for `projects.IAMBinding`, `projects.IAMMember`, or `projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
	// Required for `projects.IAMPolicy` - you must explicitly set the project, and it
	// will not be inferred from the provider.
	Project pulumi.StringOutput `pulumi:"project"`
}

// NewIAMPolicy registers a new resource with the given unique name, arguments, and options.
func NewIAMPolicy(ctx *pulumi.Context,
	name string, args *IAMPolicyArgs, opts ...pulumi.ResourceOption) (*IAMPolicy, error) {
	if args == nil || args.PolicyData == nil {
		return nil, errors.New("missing required argument 'PolicyData'")
	}
	if args == nil || args.Project == nil {
		return nil, errors.New("missing required argument 'Project'")
	}
	if args == nil {
		args = &IAMPolicyArgs{}
	}
	var resource IAMPolicy
	err := ctx.RegisterResource("gcp:projects/iAMPolicy:IAMPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIAMPolicy gets an existing IAMPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIAMPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IAMPolicyState, opts ...pulumi.ResourceOption) (*IAMPolicy, error) {
	var resource IAMPolicy
	err := ctx.ReadResource("gcp:projects/iAMPolicy:IAMPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IAMPolicy resources.
type iampolicyState struct {
	// (Computed) The etag of the project's IAM policy.
	Etag *string `pulumi:"etag"`
	// The `organizations.getIAMPolicy` data source that represents
	// the IAM policy that will be applied to the project. The policy will be
	// merged with any existing policy applied to the project.
	PolicyData *string `pulumi:"policyData"`
	// The project ID. If not specified for `projects.IAMBinding`, `projects.IAMMember`, or `projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
	// Required for `projects.IAMPolicy` - you must explicitly set the project, and it
	// will not be inferred from the provider.
	Project *string `pulumi:"project"`
}

type IAMPolicyState struct {
	// (Computed) The etag of the project's IAM policy.
	Etag pulumi.StringPtrInput
	// The `organizations.getIAMPolicy` data source that represents
	// the IAM policy that will be applied to the project. The policy will be
	// merged with any existing policy applied to the project.
	PolicyData pulumi.StringPtrInput
	// The project ID. If not specified for `projects.IAMBinding`, `projects.IAMMember`, or `projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
	// Required for `projects.IAMPolicy` - you must explicitly set the project, and it
	// will not be inferred from the provider.
	Project pulumi.StringPtrInput
}

func (IAMPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*iampolicyState)(nil)).Elem()
}

type iampolicyArgs struct {
	// The `organizations.getIAMPolicy` data source that represents
	// the IAM policy that will be applied to the project. The policy will be
	// merged with any existing policy applied to the project.
	PolicyData string `pulumi:"policyData"`
	// The project ID. If not specified for `projects.IAMBinding`, `projects.IAMMember`, or `projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
	// Required for `projects.IAMPolicy` - you must explicitly set the project, and it
	// will not be inferred from the provider.
	Project string `pulumi:"project"`
}

// The set of arguments for constructing a IAMPolicy resource.
type IAMPolicyArgs struct {
	// The `organizations.getIAMPolicy` data source that represents
	// the IAM policy that will be applied to the project. The policy will be
	// merged with any existing policy applied to the project.
	PolicyData pulumi.StringInput
	// The project ID. If not specified for `projects.IAMBinding`, `projects.IAMMember`, or `projects.IAMAuditConfig`, uses the ID of the project configured with the provider.
	// Required for `projects.IAMPolicy` - you must explicitly set the project, and it
	// will not be inferred from the provider.
	Project pulumi.StringInput
}

func (IAMPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*iampolicyArgs)(nil)).Elem()
}
