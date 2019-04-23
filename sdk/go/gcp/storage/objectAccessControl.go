// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package storage

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The ObjectAccessControls resources represent the Access Control Lists
// (ACLs) for objects within Google Cloud Storage. ACLs let you specify
// who has access to your data and to what extent.
// 
// There are two roles that can be assigned to an entity:
// 
// READERs can get an object, though the acl property will not be revealed.
// OWNERs are READERs, and they can get the acl property, update an object,
// and call all objectAccessControls methods on the object. The owner of an
// object is always an OWNER.
// For more information, see Access Control, with the caveat that this API
// uses READER and OWNER instead of READ and FULL_CONTROL.
// 
// 
// To get more information about ObjectAccessControl, see:
// 
// * [API documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/storage/docs/access-control/create-manage-lists)
type ObjectAccessControl struct {
	s *pulumi.ResourceState
}

// NewObjectAccessControl registers a new resource with the given unique name, arguments, and options.
func NewObjectAccessControl(ctx *pulumi.Context,
	name string, args *ObjectAccessControlArgs, opts ...pulumi.ResourceOpt) (*ObjectAccessControl, error) {
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil || args.Entity == nil {
		return nil, errors.New("missing required argument 'Entity'")
	}
	if args == nil || args.Object == nil {
		return nil, errors.New("missing required argument 'Object'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bucket"] = nil
		inputs["entity"] = nil
		inputs["object"] = nil
		inputs["role"] = nil
	} else {
		inputs["bucket"] = args.Bucket
		inputs["entity"] = args.Entity
		inputs["object"] = args.Object
		inputs["role"] = args.Role
	}
	inputs["domain"] = nil
	inputs["email"] = nil
	inputs["entityId"] = nil
	inputs["generation"] = nil
	inputs["projectTeam"] = nil
	s, err := ctx.RegisterResource("gcp:storage/objectAccessControl:ObjectAccessControl", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ObjectAccessControl{s: s}, nil
}

// GetObjectAccessControl gets an existing ObjectAccessControl resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetObjectAccessControl(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ObjectAccessControlState, opts ...pulumi.ResourceOpt) (*ObjectAccessControl, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bucket"] = state.Bucket
		inputs["domain"] = state.Domain
		inputs["email"] = state.Email
		inputs["entity"] = state.Entity
		inputs["entityId"] = state.EntityId
		inputs["generation"] = state.Generation
		inputs["object"] = state.Object
		inputs["projectTeam"] = state.ProjectTeam
		inputs["role"] = state.Role
	}
	s, err := ctx.ReadResource("gcp:storage/objectAccessControl:ObjectAccessControl", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ObjectAccessControl{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ObjectAccessControl) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ObjectAccessControl) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *ObjectAccessControl) Bucket() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bucket"])
}

func (r *ObjectAccessControl) Domain() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["domain"])
}

func (r *ObjectAccessControl) Email() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["email"])
}

func (r *ObjectAccessControl) Entity() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["entity"])
}

func (r *ObjectAccessControl) EntityId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["entityId"])
}

func (r *ObjectAccessControl) Generation() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["generation"])
}

func (r *ObjectAccessControl) Object() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["object"])
}

func (r *ObjectAccessControl) ProjectTeam() *pulumi.Output {
	return r.s.State["projectTeam"]
}

func (r *ObjectAccessControl) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// Input properties used for looking up and filtering ObjectAccessControl resources.
type ObjectAccessControlState struct {
	Bucket interface{}
	Domain interface{}
	Email interface{}
	Entity interface{}
	EntityId interface{}
	Generation interface{}
	Object interface{}
	ProjectTeam interface{}
	Role interface{}
}

// The set of arguments for constructing a ObjectAccessControl resource.
type ObjectAccessControlArgs struct {
	Bucket interface{}
	Entity interface{}
	Object interface{}
	Role interface{}
}
