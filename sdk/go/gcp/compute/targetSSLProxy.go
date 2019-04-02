// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Represents a TargetSslProxy resource, which is used by one or more
// global forwarding rule to route incoming SSL requests to a backend
// service.
// 
// 
// To get more information about TargetSslProxy, see:
// 
// * [API documentation](https://cloud.google.com/compute/docs/reference/v1/targetSslProxies)
// * How-to Guides
//     * [Setting Up SSL proxy for Google Cloud Load Balancing](https://cloud.google.com/compute/docs/load-balancing/tcp-ssl/)
// 
// <div class = "oics-button" style="float: right; margin: 0 0 -15px">
//   <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_ssl_proxy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
//     <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
//   </a>
// </div>
type TargetSSLProxy struct {
	s *pulumi.ResourceState
}

// NewTargetSSLProxy registers a new resource with the given unique name, arguments, and options.
func NewTargetSSLProxy(ctx *pulumi.Context,
	name string, args *TargetSSLProxyArgs, opts ...pulumi.ResourceOpt) (*TargetSSLProxy, error) {
	if args == nil || args.BackendService == nil {
		return nil, errors.New("missing required argument 'BackendService'")
	}
	if args == nil || args.SslCertificates == nil {
		return nil, errors.New("missing required argument 'SslCertificates'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["backendService"] = nil
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["project"] = nil
		inputs["proxyHeader"] = nil
		inputs["sslCertificates"] = nil
		inputs["sslPolicy"] = nil
	} else {
		inputs["backendService"] = args.BackendService
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["project"] = args.Project
		inputs["proxyHeader"] = args.ProxyHeader
		inputs["sslCertificates"] = args.SslCertificates
		inputs["sslPolicy"] = args.SslPolicy
	}
	inputs["creationTimestamp"] = nil
	inputs["proxyId"] = nil
	inputs["selfLink"] = nil
	s, err := ctx.RegisterResource("gcp:compute/targetSSLProxy:TargetSSLProxy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TargetSSLProxy{s: s}, nil
}

// GetTargetSSLProxy gets an existing TargetSSLProxy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTargetSSLProxy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TargetSSLProxyState, opts ...pulumi.ResourceOpt) (*TargetSSLProxy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["backendService"] = state.BackendService
		inputs["creationTimestamp"] = state.CreationTimestamp
		inputs["description"] = state.Description
		inputs["name"] = state.Name
		inputs["project"] = state.Project
		inputs["proxyHeader"] = state.ProxyHeader
		inputs["proxyId"] = state.ProxyId
		inputs["selfLink"] = state.SelfLink
		inputs["sslCertificates"] = state.SslCertificates
		inputs["sslPolicy"] = state.SslPolicy
	}
	s, err := ctx.ReadResource("gcp:compute/targetSSLProxy:TargetSSLProxy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TargetSSLProxy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *TargetSSLProxy) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *TargetSSLProxy) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *TargetSSLProxy) BackendService() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["backendService"])
}

func (r *TargetSSLProxy) CreationTimestamp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["creationTimestamp"])
}

func (r *TargetSSLProxy) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

func (r *TargetSSLProxy) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The ID of the project in which the resource belongs.
// If it is not provided, the provider project is used.
func (r *TargetSSLProxy) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

func (r *TargetSSLProxy) ProxyHeader() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["proxyHeader"])
}

func (r *TargetSSLProxy) ProxyId() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["proxyId"])
}

// The URI of the created resource.
func (r *TargetSSLProxy) SelfLink() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["selfLink"])
}

func (r *TargetSSLProxy) SslCertificates() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["sslCertificates"])
}

func (r *TargetSSLProxy) SslPolicy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["sslPolicy"])
}

// Input properties used for looking up and filtering TargetSSLProxy resources.
type TargetSSLProxyState struct {
	BackendService interface{}
	CreationTimestamp interface{}
	Description interface{}
	Name interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
	ProxyHeader interface{}
	ProxyId interface{}
	// The URI of the created resource.
	SelfLink interface{}
	SslCertificates interface{}
	SslPolicy interface{}
}

// The set of arguments for constructing a TargetSSLProxy resource.
type TargetSSLProxyArgs struct {
	BackendService interface{}
	Description interface{}
	Name interface{}
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project interface{}
	ProxyHeader interface{}
	SslCertificates interface{}
	SslPolicy interface{}
}
