// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A description of the conditions under which some aspect of your system is
 * considered to be "unhealthy" and the ways to notify people or services
 * about this state.
 *
 * To get more information about AlertPolicy, see:
 *
 * * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/monitoring/alerts/)
 *
 * ## Example Usage
 */
export class AlertPolicy extends pulumi.CustomResource {
    /**
     * Get an existing AlertPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertPolicyState, opts?: pulumi.CustomResourceOptions): AlertPolicy {
        return new AlertPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:monitoring/alertPolicy:AlertPolicy';

    /**
     * Returns true if the given object is an instance of AlertPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AlertPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AlertPolicy.__pulumiType;
    }

    /**
     * How to combine the results of multiple conditions to
     * determine if an incident should be opened.
     */
    public readonly combiner!: pulumi.Output<string>;
    /**
     * A list of conditions for the policy. The conditions are combined by
     * AND or OR according to the combiner field. If the combined conditions
     * evaluate to true, then an incident is created. A policy can have from
     * one to six conditions.  Structure is documented below.
     */
    public readonly conditions!: pulumi.Output<outputs.monitoring.AlertPolicyCondition[]>;
    /**
     * A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
     * ignored.
     */
    public /*out*/ readonly creationRecord!: pulumi.Output<outputs.monitoring.AlertPolicyCreationRecord>;
    /**
     * A short name or phrase used to identify the
     * condition in dashboards, notifications, and
     * incidents. To avoid confusion, don't use the same
     * display name for multiple conditions in the same
     * policy.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * A short name or phrase used to identify the policy in dashboards,
     * notifications, and incidents. To avoid confusion, don't use the same
     * display name for multiple policies in the same project. The name is
     * limited to 512 Unicode characters.  Structure is documented below.
     */
    public readonly documentation!: pulumi.Output<outputs.monitoring.AlertPolicyDocumentation | undefined>;
    /**
     * Whether or not the policy is enabled. The default is true.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * -
     * The unique resource name for this condition.
     * Its syntax is:
     * projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
     * [CONDITION_ID] is assigned by Stackdriver Monitoring when
     * the condition is created as part of a new or updated alerting
     * policy.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Identifies the notification channels to which notifications should be
     * sent when incidents are opened or closed or when new violations occur
     * on an already opened incident. Each element of this array corresponds
     * to the name field in each of the NotificationChannel objects that are
     * returned from the notificationChannels.list method. The syntax of the
     * entries in this field is
     * `projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]`
     */
    public readonly notificationChannels!: pulumi.Output<string[] | undefined>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * This field is intended to be used for organizing and identifying the AlertPolicy
     * objects.The field can contain up to 64 entries. Each key and value is limited
     * to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
     * can contain only lowercase letters, numerals, underscores, and dashes. Keys
     * must begin with a letter.
     */
    public readonly userLabels!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a AlertPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AlertPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AlertPolicyArgs | AlertPolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AlertPolicyState | undefined;
            inputs["combiner"] = state ? state.combiner : undefined;
            inputs["conditions"] = state ? state.conditions : undefined;
            inputs["creationRecord"] = state ? state.creationRecord : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["documentation"] = state ? state.documentation : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["notificationChannels"] = state ? state.notificationChannels : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["userLabels"] = state ? state.userLabels : undefined;
        } else {
            const args = argsOrState as AlertPolicyArgs | undefined;
            if (!args || args.combiner === undefined) {
                throw new Error("Missing required property 'combiner'");
            }
            if (!args || args.conditions === undefined) {
                throw new Error("Missing required property 'conditions'");
            }
            if (!args || args.displayName === undefined) {
                throw new Error("Missing required property 'displayName'");
            }
            inputs["combiner"] = args ? args.combiner : undefined;
            inputs["conditions"] = args ? args.conditions : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["documentation"] = args ? args.documentation : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["notificationChannels"] = args ? args.notificationChannels : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["userLabels"] = args ? args.userLabels : undefined;
            inputs["creationRecord"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AlertPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AlertPolicy resources.
 */
export interface AlertPolicyState {
    /**
     * How to combine the results of multiple conditions to
     * determine if an incident should be opened.
     */
    readonly combiner?: pulumi.Input<string>;
    /**
     * A list of conditions for the policy. The conditions are combined by
     * AND or OR according to the combiner field. If the combined conditions
     * evaluate to true, then an incident is created. A policy can have from
     * one to six conditions.  Structure is documented below.
     */
    readonly conditions?: pulumi.Input<pulumi.Input<inputs.monitoring.AlertPolicyCondition>[]>;
    /**
     * A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
     * ignored.
     */
    readonly creationRecord?: pulumi.Input<inputs.monitoring.AlertPolicyCreationRecord>;
    /**
     * A short name or phrase used to identify the
     * condition in dashboards, notifications, and
     * incidents. To avoid confusion, don't use the same
     * display name for multiple conditions in the same
     * policy.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * A short name or phrase used to identify the policy in dashboards,
     * notifications, and incidents. To avoid confusion, don't use the same
     * display name for multiple policies in the same project. The name is
     * limited to 512 Unicode characters.  Structure is documented below.
     */
    readonly documentation?: pulumi.Input<inputs.monitoring.AlertPolicyDocumentation>;
    /**
     * Whether or not the policy is enabled. The default is true.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * -
     * The unique resource name for this condition.
     * Its syntax is:
     * projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
     * [CONDITION_ID] is assigned by Stackdriver Monitoring when
     * the condition is created as part of a new or updated alerting
     * policy.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Identifies the notification channels to which notifications should be
     * sent when incidents are opened or closed or when new violations occur
     * on an already opened incident. Each element of this array corresponds
     * to the name field in each of the NotificationChannel objects that are
     * returned from the notificationChannels.list method. The syntax of the
     * entries in this field is
     * `projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]`
     */
    readonly notificationChannels?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * This field is intended to be used for organizing and identifying the AlertPolicy
     * objects.The field can contain up to 64 entries. Each key and value is limited
     * to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
     * can contain only lowercase letters, numerals, underscores, and dashes. Keys
     * must begin with a letter.
     */
    readonly userLabels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a AlertPolicy resource.
 */
export interface AlertPolicyArgs {
    /**
     * How to combine the results of multiple conditions to
     * determine if an incident should be opened.
     */
    readonly combiner: pulumi.Input<string>;
    /**
     * A list of conditions for the policy. The conditions are combined by
     * AND or OR according to the combiner field. If the combined conditions
     * evaluate to true, then an incident is created. A policy can have from
     * one to six conditions.  Structure is documented below.
     */
    readonly conditions: pulumi.Input<pulumi.Input<inputs.monitoring.AlertPolicyCondition>[]>;
    /**
     * A short name or phrase used to identify the
     * condition in dashboards, notifications, and
     * incidents. To avoid confusion, don't use the same
     * display name for multiple conditions in the same
     * policy.
     */
    readonly displayName: pulumi.Input<string>;
    /**
     * A short name or phrase used to identify the policy in dashboards,
     * notifications, and incidents. To avoid confusion, don't use the same
     * display name for multiple policies in the same project. The name is
     * limited to 512 Unicode characters.  Structure is documented below.
     */
    readonly documentation?: pulumi.Input<inputs.monitoring.AlertPolicyDocumentation>;
    /**
     * Whether or not the policy is enabled. The default is true.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Identifies the notification channels to which notifications should be
     * sent when incidents are opened or closed or when new violations occur
     * on an already opened incident. Each element of this array corresponds
     * to the name field in each of the NotificationChannel objects that are
     * returned from the notificationChannels.list method. The syntax of the
     * entries in this field is
     * `projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]`
     */
    readonly notificationChannels?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * This field is intended to be used for organizing and identifying the AlertPolicy
     * objects.The field can contain up to 64 entries. Each key and value is limited
     * to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
     * can contain only lowercase letters, numerals, underscores, and dashes. Keys
     * must begin with a letter.
     */
    readonly userLabels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
