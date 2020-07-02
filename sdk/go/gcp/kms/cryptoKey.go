// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// A `CryptoKey` represents a logical key that can be used for cryptographic operations.
//
// > **Note:** CryptoKeys cannot be deleted from Google Cloud Platform.
// Destroying a provider-managed CryptoKey will remove it from state
// and delete all CryptoKeyVersions, rendering the key unusable, but *will
// not delete the resource on the server.* When the provider destroys these keys,
// any data previously encrypted with these keys will be irrecoverable.
// For this reason, it is strongly recommended that you add lifecycle hooks
// to the resource to prevent accidental destruction.
//
// To get more information about CryptoKey, see:
//
// * [API documentation](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)
// * How-to Guides
//     * [Creating a key](https://cloud.google.com/kms/docs/creating-keys#create_a_key)
//
// ## Example Usage
type CryptoKey struct {
	pulumi.CustomResourceState

	// The KeyRing that this key belongs to.
	// Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'`.
	KeyRing pulumi.StringOutput `pulumi:"keyRing"`
	// Labels with user-defined metadata to apply to this resource.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The resource name for the CryptoKey.
	Name pulumi.StringOutput `pulumi:"name"`
	// The immutable purpose of this CryptoKey. See the
	// [purpose reference](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
	// for possible inputs.
	Purpose pulumi.StringPtrOutput `pulumi:"purpose"`
	// Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
	// The first rotation will take place after the specified period. The rotation period has
	// the format of a decimal number with up to 9 fractional digits, followed by the
	// letter `s` (seconds). It must be greater than a day (ie, 86400).
	RotationPeriod pulumi.StringPtrOutput `pulumi:"rotationPeriod"`
	SelfLink       pulumi.StringOutput    `pulumi:"selfLink"`
	// A template describing settings for new crypto key versions.  Structure is documented below.
	VersionTemplate CryptoKeyVersionTemplateOutput `pulumi:"versionTemplate"`
}

// NewCryptoKey registers a new resource with the given unique name, arguments, and options.
func NewCryptoKey(ctx *pulumi.Context,
	name string, args *CryptoKeyArgs, opts ...pulumi.ResourceOption) (*CryptoKey, error) {
	if args == nil || args.KeyRing == nil {
		return nil, errors.New("missing required argument 'KeyRing'")
	}
	if args == nil {
		args = &CryptoKeyArgs{}
	}
	var resource CryptoKey
	err := ctx.RegisterResource("gcp:kms/cryptoKey:CryptoKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCryptoKey gets an existing CryptoKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCryptoKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CryptoKeyState, opts ...pulumi.ResourceOption) (*CryptoKey, error) {
	var resource CryptoKey
	err := ctx.ReadResource("gcp:kms/cryptoKey:CryptoKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CryptoKey resources.
type cryptoKeyState struct {
	// The KeyRing that this key belongs to.
	// Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'`.
	KeyRing *string `pulumi:"keyRing"`
	// Labels with user-defined metadata to apply to this resource.
	Labels map[string]string `pulumi:"labels"`
	// The resource name for the CryptoKey.
	Name *string `pulumi:"name"`
	// The immutable purpose of this CryptoKey. See the
	// [purpose reference](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
	// for possible inputs.
	Purpose *string `pulumi:"purpose"`
	// Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
	// The first rotation will take place after the specified period. The rotation period has
	// the format of a decimal number with up to 9 fractional digits, followed by the
	// letter `s` (seconds). It must be greater than a day (ie, 86400).
	RotationPeriod *string `pulumi:"rotationPeriod"`
	SelfLink       *string `pulumi:"selfLink"`
	// A template describing settings for new crypto key versions.  Structure is documented below.
	VersionTemplate *CryptoKeyVersionTemplate `pulumi:"versionTemplate"`
}

type CryptoKeyState struct {
	// The KeyRing that this key belongs to.
	// Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'`.
	KeyRing pulumi.StringPtrInput
	// Labels with user-defined metadata to apply to this resource.
	Labels pulumi.StringMapInput
	// The resource name for the CryptoKey.
	Name pulumi.StringPtrInput
	// The immutable purpose of this CryptoKey. See the
	// [purpose reference](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
	// for possible inputs.
	Purpose pulumi.StringPtrInput
	// Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
	// The first rotation will take place after the specified period. The rotation period has
	// the format of a decimal number with up to 9 fractional digits, followed by the
	// letter `s` (seconds). It must be greater than a day (ie, 86400).
	RotationPeriod pulumi.StringPtrInput
	SelfLink       pulumi.StringPtrInput
	// A template describing settings for new crypto key versions.  Structure is documented below.
	VersionTemplate CryptoKeyVersionTemplatePtrInput
}

func (CryptoKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*cryptoKeyState)(nil)).Elem()
}

type cryptoKeyArgs struct {
	// The KeyRing that this key belongs to.
	// Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'`.
	KeyRing string `pulumi:"keyRing"`
	// Labels with user-defined metadata to apply to this resource.
	Labels map[string]string `pulumi:"labels"`
	// The resource name for the CryptoKey.
	Name *string `pulumi:"name"`
	// The immutable purpose of this CryptoKey. See the
	// [purpose reference](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
	// for possible inputs.
	Purpose *string `pulumi:"purpose"`
	// Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
	// The first rotation will take place after the specified period. The rotation period has
	// the format of a decimal number with up to 9 fractional digits, followed by the
	// letter `s` (seconds). It must be greater than a day (ie, 86400).
	RotationPeriod *string `pulumi:"rotationPeriod"`
	// A template describing settings for new crypto key versions.  Structure is documented below.
	VersionTemplate *CryptoKeyVersionTemplate `pulumi:"versionTemplate"`
}

// The set of arguments for constructing a CryptoKey resource.
type CryptoKeyArgs struct {
	// The KeyRing that this key belongs to.
	// Format: `'projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}'`.
	KeyRing pulumi.StringInput
	// Labels with user-defined metadata to apply to this resource.
	Labels pulumi.StringMapInput
	// The resource name for the CryptoKey.
	Name pulumi.StringPtrInput
	// The immutable purpose of this CryptoKey. See the
	// [purpose reference](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
	// for possible inputs.
	Purpose pulumi.StringPtrInput
	// Every time this period passes, generate a new CryptoKeyVersion and set it as the primary.
	// The first rotation will take place after the specified period. The rotation period has
	// the format of a decimal number with up to 9 fractional digits, followed by the
	// letter `s` (seconds). It must be greater than a day (ie, 86400).
	RotationPeriod pulumi.StringPtrInput
	// A template describing settings for new crypto key versions.  Structure is documented below.
	VersionTemplate CryptoKeyVersionTemplatePtrInput
}

func (CryptoKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cryptoKeyArgs)(nil)).Elem()
}
