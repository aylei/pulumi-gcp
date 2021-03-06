// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datastore

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Describes a composite index for Cloud Datastore.
//
// To get more information about Index, see:
//
// * [API documentation](https://cloud.google.com/datastore/docs/reference/admin/rest/v1/projects.indexes)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/datastore/docs/concepts/indexes)
//
// ## Example Usage
// ### Datastore Index
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp/datastore"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := datastore.NewDataStoreIndex(ctx, "_default", &datastore.DataStoreIndexArgs{
// 			Kind: pulumi.String("foo"),
// 			Properties: datastore.DataStoreIndexPropertyArray{
// 				&datastore.DataStoreIndexPropertyArgs{
// 					Direction: pulumi.String("ASCENDING"),
// 					Name:      pulumi.String("property_a"),
// 				},
// 				&datastore.DataStoreIndexPropertyArgs{
// 					Direction: pulumi.String("ASCENDING"),
// 					Name:      pulumi.String("property_b"),
// 				},
// 			},
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
// Index can be imported using any of these accepted formats
//
// ```sh
//  $ pulumi import gcp:datastore/dataStoreIndex:DataStoreIndex default projects/{{project}}/indexes/{{index_id}}
// ```
//
// ```sh
//  $ pulumi import gcp:datastore/dataStoreIndex:DataStoreIndex default {{project}}/{{index_id}}
// ```
//
// ```sh
//  $ pulumi import gcp:datastore/dataStoreIndex:DataStoreIndex default {{index_id}}
// ```
type DataStoreIndex struct {
	pulumi.CustomResourceState

	// Policy for including ancestors in the index.
	// Default value is `NONE`.
	// Possible values are `NONE` and `ALL_ANCESTORS`.
	Ancestor pulumi.StringPtrOutput `pulumi:"ancestor"`
	// The index id.
	IndexId pulumi.StringOutput `pulumi:"indexId"`
	// The entity kind which the index applies to.
	Kind pulumi.StringOutput `pulumi:"kind"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// An ordered list of properties to index on.
	// Structure is documented below.
	Properties DataStoreIndexPropertyArrayOutput `pulumi:"properties"`
}

// NewDataStoreIndex registers a new resource with the given unique name, arguments, and options.
func NewDataStoreIndex(ctx *pulumi.Context,
	name string, args *DataStoreIndexArgs, opts ...pulumi.ResourceOption) (*DataStoreIndex, error) {
	if args == nil || args.Kind == nil {
		return nil, errors.New("missing required argument 'Kind'")
	}
	if args == nil {
		args = &DataStoreIndexArgs{}
	}
	var resource DataStoreIndex
	err := ctx.RegisterResource("gcp:datastore/dataStoreIndex:DataStoreIndex", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataStoreIndex gets an existing DataStoreIndex resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataStoreIndex(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataStoreIndexState, opts ...pulumi.ResourceOption) (*DataStoreIndex, error) {
	var resource DataStoreIndex
	err := ctx.ReadResource("gcp:datastore/dataStoreIndex:DataStoreIndex", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataStoreIndex resources.
type dataStoreIndexState struct {
	// Policy for including ancestors in the index.
	// Default value is `NONE`.
	// Possible values are `NONE` and `ALL_ANCESTORS`.
	Ancestor *string `pulumi:"ancestor"`
	// The index id.
	IndexId *string `pulumi:"indexId"`
	// The entity kind which the index applies to.
	Kind *string `pulumi:"kind"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// An ordered list of properties to index on.
	// Structure is documented below.
	Properties []DataStoreIndexProperty `pulumi:"properties"`
}

type DataStoreIndexState struct {
	// Policy for including ancestors in the index.
	// Default value is `NONE`.
	// Possible values are `NONE` and `ALL_ANCESTORS`.
	Ancestor pulumi.StringPtrInput
	// The index id.
	IndexId pulumi.StringPtrInput
	// The entity kind which the index applies to.
	Kind pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// An ordered list of properties to index on.
	// Structure is documented below.
	Properties DataStoreIndexPropertyArrayInput
}

func (DataStoreIndexState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataStoreIndexState)(nil)).Elem()
}

type dataStoreIndexArgs struct {
	// Policy for including ancestors in the index.
	// Default value is `NONE`.
	// Possible values are `NONE` and `ALL_ANCESTORS`.
	Ancestor *string `pulumi:"ancestor"`
	// The entity kind which the index applies to.
	Kind string `pulumi:"kind"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// An ordered list of properties to index on.
	// Structure is documented below.
	Properties []DataStoreIndexProperty `pulumi:"properties"`
}

// The set of arguments for constructing a DataStoreIndex resource.
type DataStoreIndexArgs struct {
	// Policy for including ancestors in the index.
	// Default value is `NONE`.
	// Possible values are `NONE` and `ALL_ANCESTORS`.
	Ancestor pulumi.StringPtrInput
	// The entity kind which the index applies to.
	Kind pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// An ordered list of properties to index on.
	// Structure is documented below.
	Properties DataStoreIndexPropertyArrayInput
}

func (DataStoreIndexArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataStoreIndexArgs)(nil)).Elem()
}

type DataStoreIndexInput interface {
	pulumi.Input

	ToDataStoreIndexOutput() DataStoreIndexOutput
	ToDataStoreIndexOutputWithContext(ctx context.Context) DataStoreIndexOutput
}

func (DataStoreIndex) ElementType() reflect.Type {
	return reflect.TypeOf((*DataStoreIndex)(nil)).Elem()
}

func (i DataStoreIndex) ToDataStoreIndexOutput() DataStoreIndexOutput {
	return i.ToDataStoreIndexOutputWithContext(context.Background())
}

func (i DataStoreIndex) ToDataStoreIndexOutputWithContext(ctx context.Context) DataStoreIndexOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataStoreIndexOutput)
}

type DataStoreIndexOutput struct {
	*pulumi.OutputState
}

func (DataStoreIndexOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DataStoreIndexOutput)(nil)).Elem()
}

func (o DataStoreIndexOutput) ToDataStoreIndexOutput() DataStoreIndexOutput {
	return o
}

func (o DataStoreIndexOutput) ToDataStoreIndexOutputWithContext(ctx context.Context) DataStoreIndexOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DataStoreIndexOutput{})
}
