// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package diagflow

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Represents an entity type. Entity types serve as a tool for extracting parameter values from natural language queries.
//
// To get more information about EntityType, see:
//
// * [API documentation](https://cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.entityTypes)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/dialogflow/docs/)
//
// ## Example Usage
type EntityType struct {
	pulumi.CustomResourceState

	// The name of this entity type to be displayed on the console.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Enables fuzzy entity extraction during classification.
	EnableFuzzyExtraction pulumi.BoolPtrOutput `pulumi:"enableFuzzyExtraction"`
	// The collection of entity entries associated with the entity type.  Structure is documented below.
	Entities EntityTypeEntityArrayOutput `pulumi:"entities"`
	// Indicates the kind of entity type.
	// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
	// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
	//   types can contain references to other entity types (with or without aliases).
	// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
	Kind pulumi.StringOutput `pulumi:"kind"`
	// The unique identifier of the entity type. Format: projects/<Project ID>/agent/entityTypes/<Entity type ID>.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
}

// NewEntityType registers a new resource with the given unique name, arguments, and options.
func NewEntityType(ctx *pulumi.Context,
	name string, args *EntityTypeArgs, opts ...pulumi.ResourceOption) (*EntityType, error) {
	if args == nil || args.DisplayName == nil {
		return nil, errors.New("missing required argument 'DisplayName'")
	}
	if args == nil || args.Kind == nil {
		return nil, errors.New("missing required argument 'Kind'")
	}
	if args == nil {
		args = &EntityTypeArgs{}
	}
	var resource EntityType
	err := ctx.RegisterResource("gcp:diagflow/entityType:EntityType", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEntityType gets an existing EntityType resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEntityType(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EntityTypeState, opts ...pulumi.ResourceOption) (*EntityType, error) {
	var resource EntityType
	err := ctx.ReadResource("gcp:diagflow/entityType:EntityType", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EntityType resources.
type entityTypeState struct {
	// The name of this entity type to be displayed on the console.
	DisplayName *string `pulumi:"displayName"`
	// Enables fuzzy entity extraction during classification.
	EnableFuzzyExtraction *bool `pulumi:"enableFuzzyExtraction"`
	// The collection of entity entries associated with the entity type.  Structure is documented below.
	Entities []EntityTypeEntity `pulumi:"entities"`
	// Indicates the kind of entity type.
	// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
	// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
	//   types can contain references to other entity types (with or without aliases).
	// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
	Kind *string `pulumi:"kind"`
	// The unique identifier of the entity type. Format: projects/<Project ID>/agent/entityTypes/<Entity type ID>.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}

type EntityTypeState struct {
	// The name of this entity type to be displayed on the console.
	DisplayName pulumi.StringPtrInput
	// Enables fuzzy entity extraction during classification.
	EnableFuzzyExtraction pulumi.BoolPtrInput
	// The collection of entity entries associated with the entity type.  Structure is documented below.
	Entities EntityTypeEntityArrayInput
	// Indicates the kind of entity type.
	// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
	// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
	//   types can contain references to other entity types (with or without aliases).
	// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
	Kind pulumi.StringPtrInput
	// The unique identifier of the entity type. Format: projects/<Project ID>/agent/entityTypes/<Entity type ID>.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
}

func (EntityTypeState) ElementType() reflect.Type {
	return reflect.TypeOf((*entityTypeState)(nil)).Elem()
}

type entityTypeArgs struct {
	// The name of this entity type to be displayed on the console.
	DisplayName string `pulumi:"displayName"`
	// Enables fuzzy entity extraction during classification.
	EnableFuzzyExtraction *bool `pulumi:"enableFuzzyExtraction"`
	// The collection of entity entries associated with the entity type.  Structure is documented below.
	Entities []EntityTypeEntity `pulumi:"entities"`
	// Indicates the kind of entity type.
	// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
	// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
	//   types can contain references to other entity types (with or without aliases).
	// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
	Kind string `pulumi:"kind"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}

// The set of arguments for constructing a EntityType resource.
type EntityTypeArgs struct {
	// The name of this entity type to be displayed on the console.
	DisplayName pulumi.StringInput
	// Enables fuzzy entity extraction during classification.
	EnableFuzzyExtraction pulumi.BoolPtrInput
	// The collection of entity entries associated with the entity type.  Structure is documented below.
	Entities EntityTypeEntityArrayInput
	// Indicates the kind of entity type.
	// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
	// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
	//   types can contain references to other entity types (with or without aliases).
	// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
	Kind pulumi.StringInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
}

func (EntityTypeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*entityTypeArgs)(nil)).Elem()
}
