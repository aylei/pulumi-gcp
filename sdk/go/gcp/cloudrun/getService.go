// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudrun

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information about a Google Cloud Run. For more information see
// the [official documentation](https://cloud.google.com/run/docs/)
// and [API](https://cloud.google.com/run/docs/apis).
func LookupService(ctx *pulumi.Context, args *LookupServiceArgs, opts ...pulumi.InvokeOption) (*LookupServiceResult, error) {
	var rv LookupServiceResult
	err := ctx.Invoke("gcp:cloudrun/getService:getService", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getService.
type LookupServiceArgs struct {
	// The location of the cloud run instance. eg us-central1
	Location string `pulumi:"location"`
	// The name of the Cloud Run Service.
	Name string `pulumi:"name"`
	// The project in which the resource belongs. If it
	// is not provided, the provider project is used.
	Project *string `pulumi:"project"`
}

// A collection of values returned by getService.
type LookupServiceResult struct {
	AutogenerateRevisionName bool `pulumi:"autogenerateRevisionName"`
	// The provider-assigned unique ID for this managed resource.
	Id        string               `pulumi:"id"`
	Location  string               `pulumi:"location"`
	Metadatas []GetServiceMetadata `pulumi:"metadatas"`
	Name      string               `pulumi:"name"`
	Project   *string              `pulumi:"project"`
	Statuses  []GetServiceStatus   `pulumi:"statuses"`
	Templates []GetServiceTemplate `pulumi:"templates"`
	Traffics  []GetServiceTraffic  `pulumi:"traffics"`
}
