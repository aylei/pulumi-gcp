// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Three different resources help you manage IAM policies on bigtable tables. Each of these resources serves a different use case:
 *
 * * `gcp.bigtable.TableIamPolicy`: Authoritative. Sets the IAM policy for the tables and replaces any existing policy already attached.
 * * `gcp.bigtable.TableIamBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the table are preserved.
 * * `gcp.bigtable.TableIamMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the table are preserved.
 *
 * > **Note:** `gcp.bigtable.TableIamPolicy` **cannot** be used in conjunction with `gcp.bigtable.TableIamBinding` and `gcp.bigtable.TableIamMember` or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the table as `gcp.bigtable.TableIamPolicy` replaces the entire policy.
 *
 * > **Note:** `gcp.bigtable.TableIamBinding` resources **can be** used in conjunction with `gcp.bigtable.TableIamMember` resources **only if** they do not grant privilege to the same role.
 */
export class TableIamBinding extends pulumi.CustomResource {
    /**
     * Get an existing TableIamBinding resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableIamBindingState, opts?: pulumi.CustomResourceOptions): TableIamBinding {
        return new TableIamBinding(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:bigtable/tableIamBinding:TableIamBinding';

    /**
     * Returns true if the given object is an instance of TableIamBinding.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TableIamBinding {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TableIamBinding.__pulumiType;
    }

    public readonly condition!: pulumi.Output<outputs.bigtable.TableIamBindingCondition | undefined>;
    /**
     * (Computed) The etag of the tables's IAM policy.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * The name or relative resource id of the instance that owns the table.
     */
    public readonly instance!: pulumi.Output<string>;
    public readonly members!: pulumi.Output<string[]>;
    public readonly project!: pulumi.Output<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.bigtable.TableIamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`. Read more about roles [here](https://cloud.google.com/bigtable/docs/access-control#roles).
     */
    public readonly role!: pulumi.Output<string>;
    /**
     * The name or relative resource id of the table to manage IAM policies for.
     */
    public readonly table!: pulumi.Output<string>;

    /**
     * Create a TableIamBinding resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TableIamBindingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TableIamBindingArgs | TableIamBindingState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TableIamBindingState | undefined;
            inputs["condition"] = state ? state.condition : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["instance"] = state ? state.instance : undefined;
            inputs["members"] = state ? state.members : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["role"] = state ? state.role : undefined;
            inputs["table"] = state ? state.table : undefined;
        } else {
            const args = argsOrState as TableIamBindingArgs | undefined;
            if (!args || args.instance === undefined) {
                throw new Error("Missing required property 'instance'");
            }
            if (!args || args.members === undefined) {
                throw new Error("Missing required property 'members'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            if (!args || args.table === undefined) {
                throw new Error("Missing required property 'table'");
            }
            inputs["condition"] = args ? args.condition : undefined;
            inputs["instance"] = args ? args.instance : undefined;
            inputs["members"] = args ? args.members : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["table"] = args ? args.table : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(TableIamBinding.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TableIamBinding resources.
 */
export interface TableIamBindingState {
    readonly condition?: pulumi.Input<inputs.bigtable.TableIamBindingCondition>;
    /**
     * (Computed) The etag of the tables's IAM policy.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * The name or relative resource id of the instance that owns the table.
     */
    readonly instance?: pulumi.Input<string>;
    readonly members?: pulumi.Input<pulumi.Input<string>[]>;
    readonly project?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.bigtable.TableIamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`. Read more about roles [here](https://cloud.google.com/bigtable/docs/access-control#roles).
     */
    readonly role?: pulumi.Input<string>;
    /**
     * The name or relative resource id of the table to manage IAM policies for.
     */
    readonly table?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TableIamBinding resource.
 */
export interface TableIamBindingArgs {
    readonly condition?: pulumi.Input<inputs.bigtable.TableIamBindingCondition>;
    /**
     * The name or relative resource id of the instance that owns the table.
     */
    readonly instance: pulumi.Input<string>;
    readonly members: pulumi.Input<pulumi.Input<string>[]>;
    readonly project?: pulumi.Input<string>;
    /**
     * The role that should be applied. Only one
     * `gcp.bigtable.TableIamBinding` can be used per role. Note that custom roles must be of the format
     * `[projects|organizations]/{parent-name}/roles/{role-name}`. Read more about roles [here](https://cloud.google.com/bigtable/docs/access-control#roles).
     */
    readonly role: pulumi.Input<string>;
    /**
     * The name or relative resource id of the table to manage IAM policies for.
     */
    readonly table: pulumi.Input<string>;
}
