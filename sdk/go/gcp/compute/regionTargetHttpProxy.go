// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Represents a RegionTargetHttpProxy resource, which is used by one or more
// forwarding rules to route incoming HTTP requests to a URL map.
//
// To get more information about RegionTargetHttpProxy, see:
//
// * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpProxies)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/compute/docs/load-balancing/http/target-proxies)
//
// ## Example Usage
// ### Region Target Http Proxy Basic
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/compute"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		defaultRegionHealthCheck, err := compute.NewRegionHealthCheck(ctx, "defaultRegionHealthCheck", &compute.RegionHealthCheckArgs{
// 			Region: pulumi.String("us-central1"),
// 			HttpHealthCheck: &compute.RegionHealthCheckHttpHealthCheckArgs{
// 				Port: pulumi.Int(80),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		defaultRegionBackendService, err := compute.NewRegionBackendService(ctx, "defaultRegionBackendService", &compute.RegionBackendServiceArgs{
// 			Region:     pulumi.String("us-central1"),
// 			Protocol:   pulumi.String("HTTP"),
// 			TimeoutSec: pulumi.Int(10),
// 			HealthChecks: pulumi.String(pulumi.String{
// 				defaultRegionHealthCheck.ID(),
// 			}),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		defaultRegionUrlMap, err := compute.NewRegionUrlMap(ctx, "defaultRegionUrlMap", &compute.RegionUrlMapArgs{
// 			Region:         pulumi.String("us-central1"),
// 			DefaultService: defaultRegionBackendService.ID(),
// 			HostRules: compute.RegionUrlMapHostRuleArray{
// 				&compute.RegionUrlMapHostRuleArgs{
// 					Hosts: pulumi.StringArray{
// 						pulumi.String("mysite.com"),
// 					},
// 					PathMatcher: pulumi.String("allpaths"),
// 				},
// 			},
// 			PathMatchers: compute.RegionUrlMapPathMatcherArray{
// 				&compute.RegionUrlMapPathMatcherArgs{
// 					Name:           pulumi.String("allpaths"),
// 					DefaultService: defaultRegionBackendService.ID(),
// 					PathRules: compute.RegionUrlMapPathMatcherPathRuleArray{
// 						&compute.RegionUrlMapPathMatcherPathRuleArgs{
// 							Paths: pulumi.StringArray{
// 								pulumi.String("/*"),
// 							},
// 							Service: defaultRegionBackendService.ID(),
// 						},
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewRegionTargetHttpProxy(ctx, "defaultRegionTargetHttpProxy", &compute.RegionTargetHttpProxyArgs{
// 			Region: pulumi.String("us-central1"),
// 			UrlMap: defaultRegionUrlMap.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Region Target Http Proxy Https Redirect
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/compute"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		defaultRegionUrlMap, err := compute.NewRegionUrlMap(ctx, "defaultRegionUrlMap", &compute.RegionUrlMapArgs{
// 			Region: pulumi.String("us-central1"),
// 			DefaultUrlRedirect: &compute.RegionUrlMapDefaultUrlRedirectArgs{
// 				HttpsRedirect: pulumi.Bool(true),
// 				StripQuery:    pulumi.Bool(false),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewRegionTargetHttpProxy(ctx, "defaultRegionTargetHttpProxy", &compute.RegionTargetHttpProxyArgs{
// 			Region: pulumi.String("us-central1"),
// 			UrlMap: defaultRegionUrlMap.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// RegionTargetHttpProxy can be imported using any of these accepted formats
//
// ```sh
//  $ pulumi import gcp:compute/regionTargetHttpProxy:RegionTargetHttpProxy default projects/{{project}}/regions/{{region}}/targetHttpProxies/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/regionTargetHttpProxy:RegionTargetHttpProxy default {{project}}/{{region}}/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/regionTargetHttpProxy:RegionTargetHttpProxy default {{region}}/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/regionTargetHttpProxy:RegionTargetHttpProxy default {{name}}
// ```
type RegionTargetHttpProxy struct {
	pulumi.CustomResourceState

	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// An optional description of this resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
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
	// The unique identifier for the resource.
	ProxyId pulumi.IntOutput `pulumi:"proxyId"`
	// The Region in which the created target https proxy should reside.
	// If it is not provided, the provider region is used.
	Region pulumi.StringOutput `pulumi:"region"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// A reference to the RegionUrlMap resource that defines the mapping from URL
	// to the BackendService.
	UrlMap pulumi.StringOutput `pulumi:"urlMap"`
}

// NewRegionTargetHttpProxy registers a new resource with the given unique name, arguments, and options.
func NewRegionTargetHttpProxy(ctx *pulumi.Context,
	name string, args *RegionTargetHttpProxyArgs, opts ...pulumi.ResourceOption) (*RegionTargetHttpProxy, error) {
	if args == nil || args.UrlMap == nil {
		return nil, errors.New("missing required argument 'UrlMap'")
	}
	if args == nil {
		args = &RegionTargetHttpProxyArgs{}
	}
	var resource RegionTargetHttpProxy
	err := ctx.RegisterResource("gcp:compute/regionTargetHttpProxy:RegionTargetHttpProxy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegionTargetHttpProxy gets an existing RegionTargetHttpProxy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegionTargetHttpProxy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegionTargetHttpProxyState, opts ...pulumi.ResourceOption) (*RegionTargetHttpProxy, error) {
	var resource RegionTargetHttpProxy
	err := ctx.ReadResource("gcp:compute/regionTargetHttpProxy:RegionTargetHttpProxy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RegionTargetHttpProxy resources.
type regionTargetHttpProxyState struct {
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp *string `pulumi:"creationTimestamp"`
	// An optional description of this resource.
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
	// The unique identifier for the resource.
	ProxyId *int `pulumi:"proxyId"`
	// The Region in which the created target https proxy should reside.
	// If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// A reference to the RegionUrlMap resource that defines the mapping from URL
	// to the BackendService.
	UrlMap *string `pulumi:"urlMap"`
}

type RegionTargetHttpProxyState struct {
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringPtrInput
	// An optional description of this resource.
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
	// The unique identifier for the resource.
	ProxyId pulumi.IntPtrInput
	// The Region in which the created target https proxy should reside.
	// If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// A reference to the RegionUrlMap resource that defines the mapping from URL
	// to the BackendService.
	UrlMap pulumi.StringPtrInput
}

func (RegionTargetHttpProxyState) ElementType() reflect.Type {
	return reflect.TypeOf((*regionTargetHttpProxyState)(nil)).Elem()
}

type regionTargetHttpProxyArgs struct {
	// An optional description of this resource.
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
	// The Region in which the created target https proxy should reside.
	// If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
	// A reference to the RegionUrlMap resource that defines the mapping from URL
	// to the BackendService.
	UrlMap string `pulumi:"urlMap"`
}

// The set of arguments for constructing a RegionTargetHttpProxy resource.
type RegionTargetHttpProxyArgs struct {
	// An optional description of this resource.
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
	// The Region in which the created target https proxy should reside.
	// If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
	// A reference to the RegionUrlMap resource that defines the mapping from URL
	// to the BackendService.
	UrlMap pulumi.StringInput
}

func (RegionTargetHttpProxyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*regionTargetHttpProxyArgs)(nil)).Elem()
}

type RegionTargetHttpProxyInput interface {
	pulumi.Input

	ToRegionTargetHttpProxyOutput() RegionTargetHttpProxyOutput
	ToRegionTargetHttpProxyOutputWithContext(ctx context.Context) RegionTargetHttpProxyOutput
}

func (RegionTargetHttpProxy) ElementType() reflect.Type {
	return reflect.TypeOf((*RegionTargetHttpProxy)(nil)).Elem()
}

func (i RegionTargetHttpProxy) ToRegionTargetHttpProxyOutput() RegionTargetHttpProxyOutput {
	return i.ToRegionTargetHttpProxyOutputWithContext(context.Background())
}

func (i RegionTargetHttpProxy) ToRegionTargetHttpProxyOutputWithContext(ctx context.Context) RegionTargetHttpProxyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegionTargetHttpProxyOutput)
}

type RegionTargetHttpProxyOutput struct {
	*pulumi.OutputState
}

func (RegionTargetHttpProxyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RegionTargetHttpProxyOutput)(nil)).Elem()
}

func (o RegionTargetHttpProxyOutput) ToRegionTargetHttpProxyOutput() RegionTargetHttpProxyOutput {
	return o
}

func (o RegionTargetHttpProxyOutput) ToRegionTargetHttpProxyOutputWithContext(ctx context.Context) RegionTargetHttpProxyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RegionTargetHttpProxyOutput{})
}
