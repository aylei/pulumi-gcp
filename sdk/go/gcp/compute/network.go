// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a VPC network or legacy network resource on GCP.
//
// To get more information about Network, see:
//
// * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/networks)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/vpc/docs/vpc)
//
// ## Example Usage
type Network struct {
	pulumi.CustomResourceState

	// When set to `true`, the network is created in "auto subnet mode" and
	// it will create a subnet for each region automatically across the
	// `10.128.0.0/9` address range.
	// When set to `false`, the network is created in "custom subnet mode" so
	// the user can explicitly connect subnetwork resources.
	AutoCreateSubnetworks pulumi.BoolPtrOutput `pulumi:"autoCreateSubnetworks"`
	// If set to `true`, default routes (`0.0.0.0/0`) will be deleted
	// immediately after network creation. Defaults to `false`.
	DeleteDefaultRoutesOnCreate pulumi.BoolPtrOutput `pulumi:"deleteDefaultRoutesOnCreate"`
	// An optional description of this resource. The resource must be
	// recreated to modify this field.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The gateway address for default routing out of the network. This value is selected by GCP.
	GatewayIpv4 pulumi.StringOutput `pulumi:"gatewayIpv4"`
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The network-wide routing mode to use. If set to `REGIONAL`, this
	// network's cloud routers will only advertise routes with subnetworks
	// of this network in the same region as the router. If set to `GLOBAL`,
	// this network's cloud routers will advertise routes with all
	// subnetworks of this network, across regions.
	RoutingMode pulumi.StringOutput `pulumi:"routingMode"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
}

// NewNetwork registers a new resource with the given unique name, arguments, and options.
func NewNetwork(ctx *pulumi.Context,
	name string, args *NetworkArgs, opts ...pulumi.ResourceOption) (*Network, error) {
	if args == nil {
		args = &NetworkArgs{}
	}
	var resource Network
	err := ctx.RegisterResource("gcp:compute/network:Network", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetwork gets an existing Network resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkState, opts ...pulumi.ResourceOption) (*Network, error) {
	var resource Network
	err := ctx.ReadResource("gcp:compute/network:Network", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Network resources.
type networkState struct {
	// When set to `true`, the network is created in "auto subnet mode" and
	// it will create a subnet for each region automatically across the
	// `10.128.0.0/9` address range.
	// When set to `false`, the network is created in "custom subnet mode" so
	// the user can explicitly connect subnetwork resources.
	AutoCreateSubnetworks *bool `pulumi:"autoCreateSubnetworks"`
	// If set to `true`, default routes (`0.0.0.0/0`) will be deleted
	// immediately after network creation. Defaults to `false`.
	DeleteDefaultRoutesOnCreate *bool `pulumi:"deleteDefaultRoutesOnCreate"`
	// An optional description of this resource. The resource must be
	// recreated to modify this field.
	Description *string `pulumi:"description"`
	// The gateway address for default routing out of the network. This value is selected by GCP.
	GatewayIpv4 *string `pulumi:"gatewayIpv4"`
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The network-wide routing mode to use. If set to `REGIONAL`, this
	// network's cloud routers will only advertise routes with subnetworks
	// of this network in the same region as the router. If set to `GLOBAL`,
	// this network's cloud routers will advertise routes with all
	// subnetworks of this network, across regions.
	RoutingMode *string `pulumi:"routingMode"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
}

type NetworkState struct {
	// When set to `true`, the network is created in "auto subnet mode" and
	// it will create a subnet for each region automatically across the
	// `10.128.0.0/9` address range.
	// When set to `false`, the network is created in "custom subnet mode" so
	// the user can explicitly connect subnetwork resources.
	AutoCreateSubnetworks pulumi.BoolPtrInput
	// If set to `true`, default routes (`0.0.0.0/0`) will be deleted
	// immediately after network creation. Defaults to `false`.
	DeleteDefaultRoutesOnCreate pulumi.BoolPtrInput
	// An optional description of this resource. The resource must be
	// recreated to modify this field.
	Description pulumi.StringPtrInput
	// The gateway address for default routing out of the network. This value is selected by GCP.
	GatewayIpv4 pulumi.StringPtrInput
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The network-wide routing mode to use. If set to `REGIONAL`, this
	// network's cloud routers will only advertise routes with subnetworks
	// of this network in the same region as the router. If set to `GLOBAL`,
	// this network's cloud routers will advertise routes with all
	// subnetworks of this network, across regions.
	RoutingMode pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
}

func (NetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkState)(nil)).Elem()
}

type networkArgs struct {
	// When set to `true`, the network is created in "auto subnet mode" and
	// it will create a subnet for each region automatically across the
	// `10.128.0.0/9` address range.
	// When set to `false`, the network is created in "custom subnet mode" so
	// the user can explicitly connect subnetwork resources.
	AutoCreateSubnetworks *bool `pulumi:"autoCreateSubnetworks"`
	// If set to `true`, default routes (`0.0.0.0/0`) will be deleted
	// immediately after network creation. Defaults to `false`.
	DeleteDefaultRoutesOnCreate *bool `pulumi:"deleteDefaultRoutesOnCreate"`
	// An optional description of this resource. The resource must be
	// recreated to modify this field.
	Description *string `pulumi:"description"`
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The network-wide routing mode to use. If set to `REGIONAL`, this
	// network's cloud routers will only advertise routes with subnetworks
	// of this network in the same region as the router. If set to `GLOBAL`,
	// this network's cloud routers will advertise routes with all
	// subnetworks of this network, across regions.
	RoutingMode *string `pulumi:"routingMode"`
}

// The set of arguments for constructing a Network resource.
type NetworkArgs struct {
	// When set to `true`, the network is created in "auto subnet mode" and
	// it will create a subnet for each region automatically across the
	// `10.128.0.0/9` address range.
	// When set to `false`, the network is created in "custom subnet mode" so
	// the user can explicitly connect subnetwork resources.
	AutoCreateSubnetworks pulumi.BoolPtrInput
	// If set to `true`, default routes (`0.0.0.0/0`) will be deleted
	// immediately after network creation. Defaults to `false`.
	DeleteDefaultRoutesOnCreate pulumi.BoolPtrInput
	// An optional description of this resource. The resource must be
	// recreated to modify this field.
	Description pulumi.StringPtrInput
	// Name of the resource. Provided by the client when the resource is
	// created. The name must be 1-63 characters long, and comply with
	// RFC1035. Specifically, the name must be 1-63 characters long and match
	// the regular expression `a-z?` which means the
	// first character must be a lowercase letter, and all following
	// characters must be a dash, lowercase letter, or digit, except the last
	// character, which cannot be a dash.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The network-wide routing mode to use. If set to `REGIONAL`, this
	// network's cloud routers will only advertise routes with subnetworks
	// of this network in the same region as the router. If set to `GLOBAL`,
	// this network's cloud routers will advertise routes with all
	// subnetworks of this network, across regions.
	RoutingMode pulumi.StringPtrInput
}

func (NetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkArgs)(nil)).Elem()
}
