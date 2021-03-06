// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Adds existing resource policies to a disk. You can only add one policy
// which will be applied to this disk for scheduling snapshot creation.
//
// > **Note:** This resource does not support regional disks (`compute.RegionDisk`). For regional disks, please refer to the `compute.RegionDiskResourcePolicyAttachment` resource.
//
// ## Example Usage
// ### Disk Resource Policy Attachment Basic
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
// 		opt0 := "debian-9"
// 		opt1 := "debian-cloud"
// 		myImage, err := compute.LookupImage(ctx, &compute.LookupImageArgs{
// 			Family:  &opt0,
// 			Project: &opt1,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		ssd, err := compute.NewDisk(ctx, "ssd", &compute.DiskArgs{
// 			Image: pulumi.String(myImage.SelfLink),
// 			Size:  pulumi.Int(50),
// 			Type:  pulumi.String("pd-ssd"),
// 			Zone:  pulumi.String("us-central1-a"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewDiskResourcePolicyAttachment(ctx, "attachment", &compute.DiskResourcePolicyAttachmentArgs{
// 			Disk: ssd.Name,
// 			Zone: pulumi.String("us-central1-a"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewResourcePolicy(ctx, "policy", &compute.ResourcePolicyArgs{
// 			Region: pulumi.String("us-central1"),
// 			SnapshotSchedulePolicy: &compute.ResourcePolicySnapshotSchedulePolicyArgs{
// 				Schedule: &compute.ResourcePolicySnapshotSchedulePolicyScheduleArgs{
// 					DailySchedule: &compute.ResourcePolicySnapshotSchedulePolicyScheduleDailyScheduleArgs{
// 						DaysInCycle: pulumi.Int(1),
// 						StartTime:   pulumi.String("04:00"),
// 					},
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
// DiskResourcePolicyAttachment can be imported using any of these accepted formats
//
// ```sh
//  $ pulumi import gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment default projects/{{project}}/zones/{{zone}}/disks/{{disk}}/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment default {{project}}/{{zone}}/{{disk}}/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment default {{zone}}/{{disk}}/{{name}}
// ```
//
// ```sh
//  $ pulumi import gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment default {{disk}}/{{name}}
// ```
type DiskResourcePolicyAttachment struct {
	pulumi.CustomResourceState

	// The name of the disk in which the resource policies are attached to.
	Disk pulumi.StringOutput `pulumi:"disk"`
	// The resource policy to be attached to the disk for scheduling snapshot
	// creation. Do not specify the self link.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// A reference to the zone where the disk resides.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewDiskResourcePolicyAttachment registers a new resource with the given unique name, arguments, and options.
func NewDiskResourcePolicyAttachment(ctx *pulumi.Context,
	name string, args *DiskResourcePolicyAttachmentArgs, opts ...pulumi.ResourceOption) (*DiskResourcePolicyAttachment, error) {
	if args == nil || args.Disk == nil {
		return nil, errors.New("missing required argument 'Disk'")
	}
	if args == nil {
		args = &DiskResourcePolicyAttachmentArgs{}
	}
	var resource DiskResourcePolicyAttachment
	err := ctx.RegisterResource("gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDiskResourcePolicyAttachment gets an existing DiskResourcePolicyAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDiskResourcePolicyAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DiskResourcePolicyAttachmentState, opts ...pulumi.ResourceOption) (*DiskResourcePolicyAttachment, error) {
	var resource DiskResourcePolicyAttachment
	err := ctx.ReadResource("gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DiskResourcePolicyAttachment resources.
type diskResourcePolicyAttachmentState struct {
	// The name of the disk in which the resource policies are attached to.
	Disk *string `pulumi:"disk"`
	// The resource policy to be attached to the disk for scheduling snapshot
	// creation. Do not specify the self link.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// A reference to the zone where the disk resides.
	Zone *string `pulumi:"zone"`
}

type DiskResourcePolicyAttachmentState struct {
	// The name of the disk in which the resource policies are attached to.
	Disk pulumi.StringPtrInput
	// The resource policy to be attached to the disk for scheduling snapshot
	// creation. Do not specify the self link.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// A reference to the zone where the disk resides.
	Zone pulumi.StringPtrInput
}

func (DiskResourcePolicyAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*diskResourcePolicyAttachmentState)(nil)).Elem()
}

type diskResourcePolicyAttachmentArgs struct {
	// The name of the disk in which the resource policies are attached to.
	Disk string `pulumi:"disk"`
	// The resource policy to be attached to the disk for scheduling snapshot
	// creation. Do not specify the self link.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// A reference to the zone where the disk resides.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a DiskResourcePolicyAttachment resource.
type DiskResourcePolicyAttachmentArgs struct {
	// The name of the disk in which the resource policies are attached to.
	Disk pulumi.StringInput
	// The resource policy to be attached to the disk for scheduling snapshot
	// creation. Do not specify the self link.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// A reference to the zone where the disk resides.
	Zone pulumi.StringPtrInput
}

func (DiskResourcePolicyAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*diskResourcePolicyAttachmentArgs)(nil)).Elem()
}

type DiskResourcePolicyAttachmentInput interface {
	pulumi.Input

	ToDiskResourcePolicyAttachmentOutput() DiskResourcePolicyAttachmentOutput
	ToDiskResourcePolicyAttachmentOutputWithContext(ctx context.Context) DiskResourcePolicyAttachmentOutput
}

func (DiskResourcePolicyAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((*DiskResourcePolicyAttachment)(nil)).Elem()
}

func (i DiskResourcePolicyAttachment) ToDiskResourcePolicyAttachmentOutput() DiskResourcePolicyAttachmentOutput {
	return i.ToDiskResourcePolicyAttachmentOutputWithContext(context.Background())
}

func (i DiskResourcePolicyAttachment) ToDiskResourcePolicyAttachmentOutputWithContext(ctx context.Context) DiskResourcePolicyAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DiskResourcePolicyAttachmentOutput)
}

type DiskResourcePolicyAttachmentOutput struct {
	*pulumi.OutputState
}

func (DiskResourcePolicyAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DiskResourcePolicyAttachmentOutput)(nil)).Elem()
}

func (o DiskResourcePolicyAttachmentOutput) ToDiskResourcePolicyAttachmentOutput() DiskResourcePolicyAttachmentOutput {
	return o
}

func (o DiskResourcePolicyAttachmentOutput) ToDiskResourcePolicyAttachmentOutputWithContext(ctx context.Context) DiskResourcePolicyAttachmentOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DiskResourcePolicyAttachmentOutput{})
}
