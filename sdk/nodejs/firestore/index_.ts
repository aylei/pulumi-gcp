// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Cloud Firestore indexes enable simple and complex queries against documents in a database.
 *  This resource manages composite indexes and not single
 * field indexes.
 *
 * To get more information about Index, see:
 *
 * * [API documentation](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/firestore/docs/query-data/indexing)
 *
 * ## Example Usage
 */
export class Index extends pulumi.CustomResource {
    /**
     * Get an existing Index resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IndexState, opts?: pulumi.CustomResourceOptions): Index {
        return new Index(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:firestore/index:Index';

    /**
     * Returns true if the given object is an instance of Index.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Index {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Index.__pulumiType;
    }

    /**
     * The collection being indexed.
     */
    public readonly collection!: pulumi.Output<string>;
    /**
     * The Firestore database id. Defaults to `"(default)"`.
     */
    public readonly database!: pulumi.Output<string | undefined>;
    /**
     * The fields supported by this index. The last field entry is always for
     * the field path `__name__`. If, on creation, `__name__` was not
     * specified as the last field, it will be added automatically with the
     * same direction as that of the last field defined. If the final field
     * in a composite index is not directional, the `__name__` will be
     * ordered `"ASCENDING"` (unless explicitly specified otherwise).  Structure is documented below.
     */
    public readonly fields!: pulumi.Output<outputs.firestore.IndexField[]>;
    /**
     * A server defined name for this index. Format:
     * 'projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}'
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The scope at which a query is run.
     */
    public readonly queryScope!: pulumi.Output<string | undefined>;

    /**
     * Create a Index resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IndexArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IndexArgs | IndexState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IndexState | undefined;
            inputs["collection"] = state ? state.collection : undefined;
            inputs["database"] = state ? state.database : undefined;
            inputs["fields"] = state ? state.fields : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["queryScope"] = state ? state.queryScope : undefined;
        } else {
            const args = argsOrState as IndexArgs | undefined;
            if (!args || args.collection === undefined) {
                throw new Error("Missing required property 'collection'");
            }
            if (!args || args.fields === undefined) {
                throw new Error("Missing required property 'fields'");
            }
            inputs["collection"] = args ? args.collection : undefined;
            inputs["database"] = args ? args.database : undefined;
            inputs["fields"] = args ? args.fields : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["queryScope"] = args ? args.queryScope : undefined;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Index.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Index resources.
 */
export interface IndexState {
    /**
     * The collection being indexed.
     */
    readonly collection?: pulumi.Input<string>;
    /**
     * The Firestore database id. Defaults to `"(default)"`.
     */
    readonly database?: pulumi.Input<string>;
    /**
     * The fields supported by this index. The last field entry is always for
     * the field path `__name__`. If, on creation, `__name__` was not
     * specified as the last field, it will be added automatically with the
     * same direction as that of the last field defined. If the final field
     * in a composite index is not directional, the `__name__` will be
     * ordered `"ASCENDING"` (unless explicitly specified otherwise).  Structure is documented below.
     */
    readonly fields?: pulumi.Input<pulumi.Input<inputs.firestore.IndexField>[]>;
    /**
     * A server defined name for this index. Format:
     * 'projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}'
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The scope at which a query is run.
     */
    readonly queryScope?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Index resource.
 */
export interface IndexArgs {
    /**
     * The collection being indexed.
     */
    readonly collection: pulumi.Input<string>;
    /**
     * The Firestore database id. Defaults to `"(default)"`.
     */
    readonly database?: pulumi.Input<string>;
    /**
     * The fields supported by this index. The last field entry is always for
     * the field path `__name__`. If, on creation, `__name__` was not
     * specified as the last field, it will be added automatically with the
     * same direction as that of the last field defined. If the final field
     * in a composite index is not directional, the `__name__` will be
     * ordered `"ASCENDING"` (unless explicitly specified otherwise).  Structure is documented below.
     */
    readonly fields: pulumi.Input<pulumi.Input<inputs.firestore.IndexField>[]>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The scope at which a query is run.
     */
    readonly queryScope?: pulumi.Input<string>;
}
