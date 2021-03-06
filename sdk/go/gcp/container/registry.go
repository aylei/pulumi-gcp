// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package container

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Ensures that the Google Cloud Storage bucket that backs Google Container Registry exists. Creating this resource will create the backing bucket if it does not exist, or do nothing if the bucket already exists. Destroying this resource does *NOT* destroy the backing bucket. For more information see [the official documentation](https://cloud.google.com/container-registry/docs/overview)
//
// This resource can be used to ensure that the GCS bucket exists prior to assigning permissions. For more information see the [access control page](https://cloud.google.com/container-registry/docs/access-control) for GCR.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/container"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := container.NewRegistry(ctx, "registry", &container.RegistryArgs{
// 			Location: pulumi.String("EU"),
// 			Project:  pulumi.String("my-project"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// The `id` field of the `container.Registry` is the identifier of the storage bucket that backs GCR and can be used to assign permissions to the bucket.
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/container"
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/storage"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		registry, err := container.NewRegistry(ctx, "registry", &container.RegistryArgs{
// 			Project:  pulumi.String("my-project"),
// 			Location: pulumi.String("EU"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = storage.NewBucketIAMMember(ctx, "viewer", &storage.BucketIAMMemberArgs{
// 			Bucket: registry.ID(),
// 			Role:   pulumi.String("roles/storage.objectViewer"),
// 			Member: pulumi.String("user:jane@example.com"),
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
// This resource does not support import.
type Registry struct {
	pulumi.CustomResourceState

	// The URI of the created resource.
	BucketSelfLink pulumi.StringOutput `pulumi:"bucketSelfLink"`
	// The location of the registry. One of `ASIA`, `EU`, `US` or not specified. See [the official documentation](https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry) for more information on registry locations.
	Location pulumi.StringPtrOutput `pulumi:"location"`
	// The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
}

// NewRegistry registers a new resource with the given unique name, arguments, and options.
func NewRegistry(ctx *pulumi.Context,
	name string, args *RegistryArgs, opts ...pulumi.ResourceOption) (*Registry, error) {
	if args == nil {
		args = &RegistryArgs{}
	}
	var resource Registry
	err := ctx.RegisterResource("gcp:container/registry:Registry", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegistry gets an existing Registry resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegistry(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegistryState, opts ...pulumi.ResourceOption) (*Registry, error) {
	var resource Registry
	err := ctx.ReadResource("gcp:container/registry:Registry", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Registry resources.
type registryState struct {
	// The URI of the created resource.
	BucketSelfLink *string `pulumi:"bucketSelfLink"`
	// The location of the registry. One of `ASIA`, `EU`, `US` or not specified. See [the official documentation](https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry) for more information on registry locations.
	Location *string `pulumi:"location"`
	// The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}

type RegistryState struct {
	// The URI of the created resource.
	BucketSelfLink pulumi.StringPtrInput
	// The location of the registry. One of `ASIA`, `EU`, `US` or not specified. See [the official documentation](https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry) for more information on registry locations.
	Location pulumi.StringPtrInput
	// The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
}

func (RegistryState) ElementType() reflect.Type {
	return reflect.TypeOf((*registryState)(nil)).Elem()
}

type registryArgs struct {
	// The location of the registry. One of `ASIA`, `EU`, `US` or not specified. See [the official documentation](https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry) for more information on registry locations.
	Location *string `pulumi:"location"`
	// The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}

// The set of arguments for constructing a Registry resource.
type RegistryArgs struct {
	// The location of the registry. One of `ASIA`, `EU`, `US` or not specified. See [the official documentation](https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry) for more information on registry locations.
	Location pulumi.StringPtrInput
	// The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
}

func (RegistryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*registryArgs)(nil)).Elem()
}

type RegistryInput interface {
	pulumi.Input

	ToRegistryOutput() RegistryOutput
	ToRegistryOutputWithContext(ctx context.Context) RegistryOutput
}

func (Registry) ElementType() reflect.Type {
	return reflect.TypeOf((*Registry)(nil)).Elem()
}

func (i Registry) ToRegistryOutput() RegistryOutput {
	return i.ToRegistryOutputWithContext(context.Background())
}

func (i Registry) ToRegistryOutputWithContext(ctx context.Context) RegistryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegistryOutput)
}

type RegistryOutput struct {
	*pulumi.OutputState
}

func (RegistryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RegistryOutput)(nil)).Elem()
}

func (o RegistryOutput) ToRegistryOutput() RegistryOutput {
	return o
}

func (o RegistryOutput) ToRegistryOutputWithContext(ctx context.Context) RegistryOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RegistryOutput{})
}
