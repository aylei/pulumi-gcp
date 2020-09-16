// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Represents a TargetInstance resource which defines an endpoint instance
// that terminates traffic of certain protocols. In particular, they are used
// in Protocol Forwarding, where forwarding rules can send packets to a
// non-NAT'ed target instance. Each target instance contains a single
// virtual machine instance that receives and handles traffic from the
// corresponding forwarding rules.
//
// To get more information about TargetInstance, see:
//
// * [API documentation](https://cloud.google.com/compute/docs/reference/v1/targetInstances)
// * How-to Guides
//     * [Using Protocol Forwarding](https://cloud.google.com/compute/docs/protocol-forwarding)
//
// ## Example Usage
type TargetInstance struct {
	pulumi.CustomResourceState

	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The Compute instance VM handling traffic for this target instance.
	// Accepts the instance self-link, relative path
	// (e.g. `projects/project/zones/zone/instances/instance`) or name. If
	// name is given, the zone will default to the given zone or
	// the provider-default zone and the project will default to the
	// provider-level project.
	Instance pulumi.StringOutput `pulumi:"instance"`
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name pulumi.StringOutput `pulumi:"name"`
	// NAT option controlling how IPs are NAT'ed to the instance.
	// Currently only NO_NAT (default value) is supported.
	// Default value is `NO_NAT`.
	// Possible values are `NO_NAT`.
	NatPolicy pulumi.StringPtrOutput `pulumi:"natPolicy"`
	// The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to
	// the network that the default network interface belongs to.
	Network pulumi.StringPtrOutput `pulumi:"network"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// URL of the zone where the target instance resides.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewTargetInstance registers a new resource with the given unique name, arguments, and options.
func NewTargetInstance(ctx *pulumi.Context,
	name string, args *TargetInstanceArgs, opts ...pulumi.ResourceOption) (*TargetInstance, error) {
	if args == nil || args.Instance == nil {
		return nil, errors.New("missing required argument 'Instance'")
	}
	if args == nil {
		args = &TargetInstanceArgs{}
	}
	var resource TargetInstance
	err := ctx.RegisterResource("gcp:compute/targetInstance:TargetInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTargetInstance gets an existing TargetInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTargetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TargetInstanceState, opts ...pulumi.ResourceOption) (*TargetInstance, error) {
	var resource TargetInstance
	err := ctx.ReadResource("gcp:compute/targetInstance:TargetInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TargetInstance resources.
type targetInstanceState struct {
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp *string `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// The Compute instance VM handling traffic for this target instance.
	// Accepts the instance self-link, relative path
	// (e.g. `projects/project/zones/zone/instances/instance`) or name. If
	// name is given, the zone will default to the given zone or
	// the provider-default zone and the project will default to the
	// provider-level project.
	Instance *string `pulumi:"instance"`
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// NAT option controlling how IPs are NAT'ed to the instance.
	// Currently only NO_NAT (default value) is supported.
	// Default value is `NO_NAT`.
	// Possible values are `NO_NAT`.
	NatPolicy *string `pulumi:"natPolicy"`
	// The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to
	// the network that the default network interface belongs to.
	Network *string `pulumi:"network"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// URL of the zone where the target instance resides.
	Zone *string `pulumi:"zone"`
}

type TargetInstanceState struct {
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringPtrInput
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// The Compute instance VM handling traffic for this target instance.
	// Accepts the instance self-link, relative path
	// (e.g. `projects/project/zones/zone/instances/instance`) or name. If
	// name is given, the zone will default to the given zone or
	// the provider-default zone and the project will default to the
	// provider-level project.
	Instance pulumi.StringPtrInput
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// NAT option controlling how IPs are NAT'ed to the instance.
	// Currently only NO_NAT (default value) is supported.
	// Default value is `NO_NAT`.
	// Possible values are `NO_NAT`.
	NatPolicy pulumi.StringPtrInput
	// The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to
	// the network that the default network interface belongs to.
	Network pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// URL of the zone where the target instance resides.
	Zone pulumi.StringPtrInput
}

func (TargetInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*targetInstanceState)(nil)).Elem()
}

type targetInstanceArgs struct {
	// An optional description of this resource.
	Description *string `pulumi:"description"`
	// The Compute instance VM handling traffic for this target instance.
	// Accepts the instance self-link, relative path
	// (e.g. `projects/project/zones/zone/instances/instance`) or name. If
	// name is given, the zone will default to the given zone or
	// the provider-default zone and the project will default to the
	// provider-level project.
	Instance string `pulumi:"instance"`
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// NAT option controlling how IPs are NAT'ed to the instance.
	// Currently only NO_NAT (default value) is supported.
	// Default value is `NO_NAT`.
	// Possible values are `NO_NAT`.
	NatPolicy *string `pulumi:"natPolicy"`
	// The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to
	// the network that the default network interface belongs to.
	Network *string `pulumi:"network"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// URL of the zone where the target instance resides.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a TargetInstance resource.
type TargetInstanceArgs struct {
	// An optional description of this resource.
	Description pulumi.StringPtrInput
	// The Compute instance VM handling traffic for this target instance.
	// Accepts the instance self-link, relative path
	// (e.g. `projects/project/zones/zone/instances/instance`) or name. If
	// name is given, the zone will default to the given zone or
	// the provider-default zone and the project will default to the
	// provider-level project.
	Instance pulumi.StringInput
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// NAT option controlling how IPs are NAT'ed to the instance.
	// Currently only NO_NAT (default value) is supported.
	// Default value is `NO_NAT`.
	// Possible values are `NO_NAT`.
	NatPolicy pulumi.StringPtrInput
	// The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to
	// the network that the default network interface belongs to.
	Network pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// URL of the zone where the target instance resides.
	Zone pulumi.StringPtrInput
}

func (TargetInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*targetInstanceArgs)(nil)).Elem()
}
