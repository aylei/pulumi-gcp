// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Enables the Google Compute Engine
// [Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
// feature for a project, assigning it as a Shared VPC service project associated
// with a given host project.
// 
// For more information, see,
// [the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
// where the Shared VPC feature is referred to by its former name "XPN".
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_shared_vpc_service_project.html.markdown.
type SharedVPCServiceProject struct {
	pulumi.CustomResourceState

	// The ID of a host project to associate.
	HostProject pulumi.StringOutput `pulumi:"hostProject"`
	// The ID of the project that will serve as a Shared VPC service project.
	ServiceProject pulumi.StringOutput `pulumi:"serviceProject"`
}

// NewSharedVPCServiceProject registers a new resource with the given unique name, arguments, and options.
func NewSharedVPCServiceProject(ctx *pulumi.Context,
	name string, args *SharedVPCServiceProjectArgs, opts ...pulumi.ResourceOption) (*SharedVPCServiceProject, error) {
	if args == nil || args.HostProject == nil {
		return nil, errors.New("missing required argument 'HostProject'")
	}
	if args == nil || args.ServiceProject == nil {
		return nil, errors.New("missing required argument 'ServiceProject'")
	}
	if args == nil {
		args = &SharedVPCServiceProjectArgs{}
	}
	var resource SharedVPCServiceProject
	err := ctx.RegisterResource("gcp:compute/sharedVPCServiceProject:SharedVPCServiceProject", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSharedVPCServiceProject gets an existing SharedVPCServiceProject resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSharedVPCServiceProject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SharedVPCServiceProjectState, opts ...pulumi.ResourceOption) (*SharedVPCServiceProject, error) {
	var resource SharedVPCServiceProject
	err := ctx.ReadResource("gcp:compute/sharedVPCServiceProject:SharedVPCServiceProject", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SharedVPCServiceProject resources.
type sharedVPCServiceProjectState struct {
	// The ID of a host project to associate.
	HostProject *string `pulumi:"hostProject"`
	// The ID of the project that will serve as a Shared VPC service project.
	ServiceProject *string `pulumi:"serviceProject"`
}

type SharedVPCServiceProjectState struct {
	// The ID of a host project to associate.
	HostProject pulumi.StringPtrInput
	// The ID of the project that will serve as a Shared VPC service project.
	ServiceProject pulumi.StringPtrInput
}

func (SharedVPCServiceProjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*sharedVPCServiceProjectState)(nil)).Elem()
}

type sharedVPCServiceProjectArgs struct {
	// The ID of a host project to associate.
	HostProject string `pulumi:"hostProject"`
	// The ID of the project that will serve as a Shared VPC service project.
	ServiceProject string `pulumi:"serviceProject"`
}

// The set of arguments for constructing a SharedVPCServiceProject resource.
type SharedVPCServiceProjectArgs struct {
	// The ID of a host project to associate.
	HostProject pulumi.StringInput
	// The ID of the project that will serve as a Shared VPC service project.
	ServiceProject pulumi.StringInput
}

func (SharedVPCServiceProjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sharedVPCServiceProjectArgs)(nil)).Elem()
}

