// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * OAuth brand data. Only "Organization Internal" brands can be created
 * programatically via API. To convert it into an external brands
 * please use the GCP Console.
 * 
 * 
 * > **Note:** Brands can be created only once for a Google Cloud Platform
 * project and cannot be deleted. Destroying a provider-managed Brand
 * will remove it from state but *will not delete the resource on the server.*
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/iap_brand.html.markdown.
 */
export class Brand extends pulumi.CustomResource {
    /**
     * Get an existing Brand resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BrandState, opts?: pulumi.CustomResourceOptions): Brand {
        return new Brand(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:iap/brand:Brand';

    /**
     * Returns true if the given object is an instance of Brand.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Brand {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Brand.__pulumiType;
    }

    /**
     * Application name displayed on OAuth consent screen.
     */
    public readonly applicationTitle!: pulumi.Output<string>;
    /**
     * Output only. Identifier of the brand, in the format 'projects/{project_number}/brands/{brand_id}'. NOTE: The brand
     * identification corresponds to the project number as only one brand per project can be created.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Whether the brand is only intended for usage inside the GSuite organization only.
     */
    public /*out*/ readonly orgInternalOnly!: pulumi.Output<boolean>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * Support email displayed on the OAuth consent screen. Can be either a user or group email. When a user email is
     * specified, the caller must be the user with the associated email address. When a group email is specified, the
     * caller can be either a user or a service account which is an owner of the specified group in Cloud Identity.
     */
    public readonly supportEmail!: pulumi.Output<string>;

    /**
     * Create a Brand resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BrandArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BrandArgs | BrandState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as BrandState | undefined;
            inputs["applicationTitle"] = state ? state.applicationTitle : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["orgInternalOnly"] = state ? state.orgInternalOnly : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["supportEmail"] = state ? state.supportEmail : undefined;
        } else {
            const args = argsOrState as BrandArgs | undefined;
            if (!args || args.applicationTitle === undefined) {
                throw new Error("Missing required property 'applicationTitle'");
            }
            if (!args || args.supportEmail === undefined) {
                throw new Error("Missing required property 'supportEmail'");
            }
            inputs["applicationTitle"] = args ? args.applicationTitle : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["supportEmail"] = args ? args.supportEmail : undefined;
            inputs["name"] = undefined /*out*/;
            inputs["orgInternalOnly"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Brand.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Brand resources.
 */
export interface BrandState {
    /**
     * Application name displayed on OAuth consent screen.
     */
    readonly applicationTitle?: pulumi.Input<string>;
    /**
     * Output only. Identifier of the brand, in the format 'projects/{project_number}/brands/{brand_id}'. NOTE: The brand
     * identification corresponds to the project number as only one brand per project can be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Whether the brand is only intended for usage inside the GSuite organization only.
     */
    readonly orgInternalOnly?: pulumi.Input<boolean>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Support email displayed on the OAuth consent screen. Can be either a user or group email. When a user email is
     * specified, the caller must be the user with the associated email address. When a group email is specified, the
     * caller can be either a user or a service account which is an owner of the specified group in Cloud Identity.
     */
    readonly supportEmail?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Brand resource.
 */
export interface BrandArgs {
    /**
     * Application name displayed on OAuth consent screen.
     */
    readonly applicationTitle: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Support email displayed on the OAuth consent screen. Can be either a user or group email. When a user email is
     * specified, the caller must be the user with the associated email address. When a group email is specified, the
     * caller can be either a user or a service account which is an owner of the specified group in Cloud Identity.
     */
    readonly supportEmail: pulumi.Input<string>;
}
