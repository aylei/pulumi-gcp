// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datacatalog

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// ## Import
//
// For all import syntaxes, the "resource in question" can take any of the following forms* projects/{{project}}/locations/{{region}}/taxonomies/{{taxonomy}} * {{project}}/{{region}}/{{taxonomy}} * {{region}}/{{taxonomy}} * {{taxonomy}} Any variables not passed in the import command will be taken from the provider configuration. Data catalog taxonomy IAM resources can be imported using the resource identifiers, role, and member. IAM member imports use space-delimited identifiersthe resource in question, the role, and the member identity, e.g.
//
// ```sh
//  $ pulumi import gcp:datacatalog/taxonomyIamBinding:TaxonomyIamBinding editor "projects/{{project}}/locations/{{region}}/taxonomies/{{taxonomy}} roles/viewer user:jane@example.com"
// ```
//
//  IAM binding imports use space-delimited identifiersthe resource in question and the role, e.g.
//
// ```sh
//  $ pulumi import gcp:datacatalog/taxonomyIamBinding:TaxonomyIamBinding editor "projects/{{project}}/locations/{{region}}/taxonomies/{{taxonomy}} roles/viewer"
// ```
//
//  IAM policy imports use the identifier of the resource in question, e.g.
//
// ```sh
//  $ pulumi import gcp:datacatalog/taxonomyIamBinding:TaxonomyIamBinding editor projects/{{project}}/locations/{{region}}/taxonomies/{{taxonomy}}
// ```
//
//  -> **Custom Roles**If you're importing a IAM resource with a custom role, make sure to use the
//
// full name of the custom role, e.g. `[projects/my-project|organizations/my-org]/roles/my-custom-role`.
type TaxonomyIamBinding struct {
	pulumi.CustomResourceState

	Condition TaxonomyIamBindingConditionPtrOutput `pulumi:"condition"`
	// (Computed) The etag of the IAM policy.
	Etag    pulumi.StringOutput      `pulumi:"etag"`
	Members pulumi.StringArrayOutput `pulumi:"members"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	Region  pulumi.StringOutput `pulumi:"region"`
	// The role that should be applied. Only one
	// `datacatalog.TaxonomyIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringOutput `pulumi:"role"`
	// Used to find the parent resource to bind the IAM policy to
	Taxonomy pulumi.StringOutput `pulumi:"taxonomy"`
}

// NewTaxonomyIamBinding registers a new resource with the given unique name, arguments, and options.
func NewTaxonomyIamBinding(ctx *pulumi.Context,
	name string, args *TaxonomyIamBindingArgs, opts ...pulumi.ResourceOption) (*TaxonomyIamBinding, error) {
	if args == nil || args.Members == nil {
		return nil, errors.New("missing required argument 'Members'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	if args == nil || args.Taxonomy == nil {
		return nil, errors.New("missing required argument 'Taxonomy'")
	}
	if args == nil {
		args = &TaxonomyIamBindingArgs{}
	}
	var resource TaxonomyIamBinding
	err := ctx.RegisterResource("gcp:datacatalog/taxonomyIamBinding:TaxonomyIamBinding", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTaxonomyIamBinding gets an existing TaxonomyIamBinding resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTaxonomyIamBinding(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TaxonomyIamBindingState, opts ...pulumi.ResourceOption) (*TaxonomyIamBinding, error) {
	var resource TaxonomyIamBinding
	err := ctx.ReadResource("gcp:datacatalog/taxonomyIamBinding:TaxonomyIamBinding", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TaxonomyIamBinding resources.
type taxonomyIamBindingState struct {
	Condition *TaxonomyIamBindingCondition `pulumi:"condition"`
	// (Computed) The etag of the IAM policy.
	Etag    *string  `pulumi:"etag"`
	Members []string `pulumi:"members"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	Region  *string `pulumi:"region"`
	// The role that should be applied. Only one
	// `datacatalog.TaxonomyIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role *string `pulumi:"role"`
	// Used to find the parent resource to bind the IAM policy to
	Taxonomy *string `pulumi:"taxonomy"`
}

type TaxonomyIamBindingState struct {
	Condition TaxonomyIamBindingConditionPtrInput
	// (Computed) The etag of the IAM policy.
	Etag    pulumi.StringPtrInput
	Members pulumi.StringArrayInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	Region  pulumi.StringPtrInput
	// The role that should be applied. Only one
	// `datacatalog.TaxonomyIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringPtrInput
	// Used to find the parent resource to bind the IAM policy to
	Taxonomy pulumi.StringPtrInput
}

func (TaxonomyIamBindingState) ElementType() reflect.Type {
	return reflect.TypeOf((*taxonomyIamBindingState)(nil)).Elem()
}

type taxonomyIamBindingArgs struct {
	Condition *TaxonomyIamBindingCondition `pulumi:"condition"`
	Members   []string                     `pulumi:"members"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project *string `pulumi:"project"`
	Region  *string `pulumi:"region"`
	// The role that should be applied. Only one
	// `datacatalog.TaxonomyIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role string `pulumi:"role"`
	// Used to find the parent resource to bind the IAM policy to
	Taxonomy string `pulumi:"taxonomy"`
}

// The set of arguments for constructing a TaxonomyIamBinding resource.
type TaxonomyIamBindingArgs struct {
	Condition TaxonomyIamBindingConditionPtrInput
	Members   pulumi.StringArrayInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
	Project pulumi.StringPtrInput
	Region  pulumi.StringPtrInput
	// The role that should be applied. Only one
	// `datacatalog.TaxonomyIamBinding` can be used per role. Note that custom roles must be of the format
	// `[projects|organizations]/{parent-name}/roles/{role-name}`.
	Role pulumi.StringInput
	// Used to find the parent resource to bind the IAM policy to
	Taxonomy pulumi.StringInput
}

func (TaxonomyIamBindingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*taxonomyIamBindingArgs)(nil)).Elem()
}

type TaxonomyIamBindingInput interface {
	pulumi.Input

	ToTaxonomyIamBindingOutput() TaxonomyIamBindingOutput
	ToTaxonomyIamBindingOutputWithContext(ctx context.Context) TaxonomyIamBindingOutput
}

func (TaxonomyIamBinding) ElementType() reflect.Type {
	return reflect.TypeOf((*TaxonomyIamBinding)(nil)).Elem()
}

func (i TaxonomyIamBinding) ToTaxonomyIamBindingOutput() TaxonomyIamBindingOutput {
	return i.ToTaxonomyIamBindingOutputWithContext(context.Background())
}

func (i TaxonomyIamBinding) ToTaxonomyIamBindingOutputWithContext(ctx context.Context) TaxonomyIamBindingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TaxonomyIamBindingOutput)
}

type TaxonomyIamBindingOutput struct {
	*pulumi.OutputState
}

func (TaxonomyIamBindingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TaxonomyIamBindingOutput)(nil)).Elem()
}

func (o TaxonomyIamBindingOutput) ToTaxonomyIamBindingOutput() TaxonomyIamBindingOutput {
	return o
}

func (o TaxonomyIamBindingOutput) ToTaxonomyIamBindingOutputWithContext(ctx context.Context) TaxonomyIamBindingOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TaxonomyIamBindingOutput{})
}
