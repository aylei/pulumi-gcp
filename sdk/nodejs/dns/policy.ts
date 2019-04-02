// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * A policy is a collection of DNS rules applied to one or more Virtual
 * Private Cloud resources.
 * 
 * > **Warning:** This resource is in beta, and should be used with the terraform-provider-google-beta provider.
 * See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta resources.
 * 
 * To get more information about Policy, see:
 * 
 * * [API documentation](https://cloud.google.com/dns/docs/reference/v1beta2/policies)
 * * How-to Guides
 *     * [Using DNS server policies](https://cloud.google.com/dns/zones/#using-dns-server-policies)
 * 
 * <div class = "oics-button" style="float: right; margin: 0 0 -15px">
 *   <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=dns_policy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
 *     <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
 *   </a>
 * </div>
 */
export class Policy extends pulumi.CustomResource {
    /**
     * Get an existing Policy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState, opts?: pulumi.CustomResourceOptions): Policy {
        return new Policy(name, <any>state, { ...opts, id: id });
    }

    public readonly alternativeNameServerConfig: pulumi.Output<{ targetNameServers?: { ipv4Address?: string }[] } | undefined>;
    public readonly description: pulumi.Output<string | undefined>;
    public readonly enableInboundForwarding: pulumi.Output<boolean | undefined>;
    public readonly name: pulumi.Output<string>;
    public readonly networks: pulumi.Output<{ networkUrl?: string }[] | undefined>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project: pulumi.Output<string>;

    /**
     * Create a Policy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PolicyArgs | PolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: PolicyState = argsOrState as PolicyState | undefined;
            inputs["alternativeNameServerConfig"] = state ? state.alternativeNameServerConfig : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enableInboundForwarding"] = state ? state.enableInboundForwarding : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networks"] = state ? state.networks : undefined;
            inputs["project"] = state ? state.project : undefined;
        } else {
            const args = argsOrState as PolicyArgs | undefined;
            inputs["alternativeNameServerConfig"] = args ? args.alternativeNameServerConfig : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["enableInboundForwarding"] = args ? args.enableInboundForwarding : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networks"] = args ? args.networks : undefined;
            inputs["project"] = args ? args.project : undefined;
        }
        super("gcp:dns/policy:Policy", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Policy resources.
 */
export interface PolicyState {
    readonly alternativeNameServerConfig?: pulumi.Input<{ targetNameServers?: pulumi.Input<pulumi.Input<{ ipv4Address?: pulumi.Input<string> }>[]> }>;
    readonly description?: pulumi.Input<string>;
    readonly enableInboundForwarding?: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly networks?: pulumi.Input<pulumi.Input<{ networkUrl?: pulumi.Input<string> }>[]>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Policy resource.
 */
export interface PolicyArgs {
    readonly alternativeNameServerConfig?: pulumi.Input<{ targetNameServers?: pulumi.Input<pulumi.Input<{ ipv4Address?: pulumi.Input<string> }>[]> }>;
    readonly description?: pulumi.Input<string>;
    readonly enableInboundForwarding?: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly networks?: pulumi.Input<pulumi.Input<{ networkUrl?: pulumi.Input<string> }>[]>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
}
