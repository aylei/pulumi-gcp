// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

export class IAMMember extends pulumi.CustomResource {
    /**
     * Get an existing IAMMember resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IAMMemberState): IAMMember {
        return new IAMMember(name, <any>state, { id });
    }

    public /*out*/ readonly etag: pulumi.Output<string>;
    public readonly member: pulumi.Output<string>;
    public readonly project: pulumi.Output<string | undefined>;
    public readonly role: pulumi.Output<string>;

    /**
     * Create a IAMMember resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IAMMemberArgs, opts?: pulumi.ResourceOptions)
    constructor(name: string, argsOrState?: IAMMemberArgs | IAMMemberState, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: IAMMemberState = argsOrState as IAMMemberState | undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["member"] = state ? state.member : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as IAMMemberArgs | undefined;
            if (!args || args.member === undefined) {
                throw new Error("Missing required property 'member'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            inputs["member"] = args ? args.member : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        super("gcp:projects/iAMMember:IAMMember", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IAMMember resources.
 */
export interface IAMMemberState {
    readonly etag?: pulumi.Input<string>;
    readonly member?: pulumi.Input<string>;
    readonly project?: pulumi.Input<string>;
    readonly role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IAMMember resource.
 */
export interface IAMMemberArgs {
    readonly member: pulumi.Input<string>;
    readonly project?: pulumi.Input<string>;
    readonly role: pulumi.Input<string>;
}