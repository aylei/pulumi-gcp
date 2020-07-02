// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Allows creation and management of a single binding within IAM policy for
 * an existing Google Cloud Platform Billing Account.
 *
 * > **Note:** This resource __must not__ be used in conjunction with
 *    `gcp.billing.AccountIamMember` for the __same role__ or they will fight over
 *    what your policy should be.
 *
 * > **Note:** On create, this resource will overwrite members of any existing roles.
 *     Use `pulumi import` and inspect the output to ensure
 *     your existing members are preserved.
 */
export class AccountIamBinding extends pulumi.CustomResource {
    /**
     * Get an existing AccountIamBinding resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountIamBindingState, opts?: pulumi.CustomResourceOptions): AccountIamBinding {
        return new AccountIamBinding(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:billing/accountIamBinding:AccountIamBinding';

    /**
     * Returns true if the given object is an instance of AccountIamBinding.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccountIamBinding {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccountIamBinding.__pulumiType;
    }

    /**
     * The billing account id.
     */
    public readonly billingAccountId!: pulumi.Output<string>;
    public readonly condition!: pulumi.Output<outputs.billing.AccountIamBindingCondition | undefined>;
    /**
     * (Computed) The etag of the billing account's IAM policy.
     */
    public /*out*/ readonly etag!: pulumi.Output<string>;
    /**
     * A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
     */
    public readonly members!: pulumi.Output<string[]>;
    /**
     * The role that should be applied.
     */
    public readonly role!: pulumi.Output<string>;

    /**
     * Create a AccountIamBinding resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccountIamBindingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AccountIamBindingArgs | AccountIamBindingState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AccountIamBindingState | undefined;
            inputs["billingAccountId"] = state ? state.billingAccountId : undefined;
            inputs["condition"] = state ? state.condition : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["members"] = state ? state.members : undefined;
            inputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as AccountIamBindingArgs | undefined;
            if (!args || args.billingAccountId === undefined) {
                throw new Error("Missing required property 'billingAccountId'");
            }
            if (!args || args.members === undefined) {
                throw new Error("Missing required property 'members'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            inputs["billingAccountId"] = args ? args.billingAccountId : undefined;
            inputs["condition"] = args ? args.condition : undefined;
            inputs["members"] = args ? args.members : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["etag"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AccountIamBinding.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AccountIamBinding resources.
 */
export interface AccountIamBindingState {
    /**
     * The billing account id.
     */
    readonly billingAccountId?: pulumi.Input<string>;
    readonly condition?: pulumi.Input<inputs.billing.AccountIamBindingCondition>;
    /**
     * (Computed) The etag of the billing account's IAM policy.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
     */
    readonly members?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The role that should be applied.
     */
    readonly role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AccountIamBinding resource.
 */
export interface AccountIamBindingArgs {
    /**
     * The billing account id.
     */
    readonly billingAccountId: pulumi.Input<string>;
    readonly condition?: pulumi.Input<inputs.billing.AccountIamBindingCondition>;
    /**
     * A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
     */
    readonly members: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The role that should be applied.
     */
    readonly role: pulumi.Input<string>;
}
