// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudbuild

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Configuration for an automated build in response to source repository changes.
// 
// 
// To get more information about Trigger, see:
// 
// * [API documentation](https://cloud.google.com/cloud-build/docs/api/reference/rest/)
// * How-to Guides
//     * [Automating builds using build triggers](https://cloud.google.com/cloud-build/docs/running-builds/automate-builds)
type Trigger struct {
	s *pulumi.ResourceState
}

// NewTrigger registers a new resource with the given unique name, arguments, and options.
func NewTrigger(ctx *pulumi.Context,
	name string, args *TriggerArgs, opts ...pulumi.ResourceOpt) (*Trigger, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["build"] = nil
		inputs["description"] = nil
		inputs["disabled"] = nil
		inputs["filename"] = nil
		inputs["ignoredFiles"] = nil
		inputs["includedFiles"] = nil
		inputs["project"] = nil
		inputs["substitutions"] = nil
		inputs["triggerTemplate"] = nil
	} else {
		inputs["build"] = args.Build
		inputs["description"] = args.Description
		inputs["disabled"] = args.Disabled
		inputs["filename"] = args.Filename
		inputs["ignoredFiles"] = args.IgnoredFiles
		inputs["includedFiles"] = args.IncludedFiles
		inputs["project"] = args.Project
		inputs["substitutions"] = args.Substitutions
		inputs["triggerTemplate"] = args.TriggerTemplate
	}
	inputs["createTime"] = nil
	inputs["triggerId"] = nil
	s, err := ctx.RegisterResource("gcp:cloudbuild/trigger:Trigger", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Trigger{s: s}, nil
}

// GetTrigger gets an existing Trigger resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTrigger(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TriggerState, opts ...pulumi.ResourceOpt) (*Trigger, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["build"] = state.Build
		inputs["createTime"] = state.CreateTime
		inputs["description"] = state.Description
		inputs["disabled"] = state.Disabled
		inputs["filename"] = state.Filename
		inputs["ignoredFiles"] = state.IgnoredFiles
		inputs["includedFiles"] = state.IncludedFiles
		inputs["project"] = state.Project
		inputs["substitutions"] = state.Substitutions
		inputs["triggerId"] = state.TriggerId
		inputs["triggerTemplate"] = state.TriggerTemplate
	}
	s, err := ctx.ReadResource("gcp:cloudbuild/trigger:Trigger", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Trigger{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Trigger) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Trigger) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *Trigger) Build() *pulumi.Output {
	return r.s.State["build"]
}

func (r *Trigger) CreateTime() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["createTime"])
}

func (r *Trigger) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

func (r *Trigger) Disabled() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["disabled"])
}

func (r *Trigger) Filename() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["filename"])
}

func (r *Trigger) IgnoredFiles() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["ignoredFiles"])
}

func (r *Trigger) IncludedFiles() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["includedFiles"])
}

// The ID of the project in which the resource belongs.
// If it is not provided, the provider project is used.
func (r *Trigger) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

func (r *Trigger) Substitutions() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["substitutions"])
}

func (r *Trigger) TriggerId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["triggerId"])
}

func (r *Trigger) TriggerTemplate() *pulumi.Output {
	return r.s.State["triggerTemplate"]
}

// Input properties used for looking up and filtering Trigger resources.
type TriggerState struct {
	Build interface{}
	CreateTime interface{}
	Description interface{}
	Disabled interface{}
	Filename interface{}
	IgnoredFiles interface{}
	IncludedFiles interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
	Substitutions interface{}
	TriggerId interface{}
	TriggerTemplate interface{}
}

// The set of arguments for constructing a Trigger resource.
type TriggerArgs struct {
	Build interface{}
	Description interface{}
	Disabled interface{}
	Filename interface{}
	IgnoredFiles interface{}
	IncludedFiles interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
	Substitutions interface{}
	TriggerTemplate interface{}
}
