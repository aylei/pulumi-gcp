// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Tags are used to attach custom metadata to Data Catalog resources. Tags conform to the specifications within their tag template.
 *
 * See [Data Catalog IAM](https://cloud.google.com/data-catalog/docs/concepts/iam) for information on the permissions needed to create or view tags.
 *
 * To get more information about Tag, see:
 *
 * * [API documentation](https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.tags)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/data-catalog/docs)
 *
 * ## Example Usage
 */
export class Tag extends pulumi.CustomResource {
    /**
     * Get an existing Tag resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TagState, opts?: pulumi.CustomResourceOptions): Tag {
        return new Tag(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:datacatalog/tag:Tag';

    /**
     * Returns true if the given object is an instance of Tag.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Tag {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Tag.__pulumiType;
    }

    /**
     * Resources like Entry can have schemas associated with them. This scope allows users to attach tags to an
     * individual column based on that schema.
     * For attaching a tag to a nested column, use `.` to separate the column names. Example:
     * `outer_column.inner_column`
     */
    public readonly column!: pulumi.Output<string | undefined>;
    /**
     * This maps the ID of a tag field to the value of and additional information about that field.
     * Valid field IDs are defined by the tag's template. A tag must have at least 1 field and at most 500 fields.
     * Structure is documented below.
     */
    public readonly fields!: pulumi.Output<outputs.datacatalog.TagField[]>;
    /**
     * The resource name of the tag in URL format. Example:
     * projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}/tags/{tag_id} or
     * projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/tags/{tag_id} where tag_id is a system-generated
     * identifier. Note that this Tag may not actually be stored in the location in this name.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The name of the parent this tag is attached to. This can be the name of an entry or an entry group. If an entry group, the tag will be attached to
     * all entries in that group.
     */
    public readonly parent!: pulumi.Output<string | undefined>;
    /**
     * The resource name of the tag template that this tag uses. Example:
     * projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}
     * This field cannot be modified after creation.
     */
    public readonly template!: pulumi.Output<string>;
    /**
     * The display name of the tag template.
     */
    public /*out*/ readonly templateDisplayname!: pulumi.Output<string>;

    /**
     * Create a Tag resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TagArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TagArgs | TagState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TagState | undefined;
            inputs["column"] = state ? state.column : undefined;
            inputs["fields"] = state ? state.fields : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["parent"] = state ? state.parent : undefined;
            inputs["template"] = state ? state.template : undefined;
            inputs["templateDisplayname"] = state ? state.templateDisplayname : undefined;
        } else {
            const args = argsOrState as TagArgs | undefined;
            if (!args || args.fields === undefined) {
                throw new Error("Missing required property 'fields'");
            }
            if (!args || args.template === undefined) {
                throw new Error("Missing required property 'template'");
            }
            inputs["column"] = args ? args.column : undefined;
            inputs["fields"] = args ? args.fields : undefined;
            inputs["parent"] = args ? args.parent : undefined;
            inputs["template"] = args ? args.template : undefined;
            inputs["name"] = undefined /*out*/;
            inputs["templateDisplayname"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Tag.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Tag resources.
 */
export interface TagState {
    /**
     * Resources like Entry can have schemas associated with them. This scope allows users to attach tags to an
     * individual column based on that schema.
     * For attaching a tag to a nested column, use `.` to separate the column names. Example:
     * `outer_column.inner_column`
     */
    readonly column?: pulumi.Input<string>;
    /**
     * This maps the ID of a tag field to the value of and additional information about that field.
     * Valid field IDs are defined by the tag's template. A tag must have at least 1 field and at most 500 fields.
     * Structure is documented below.
     */
    readonly fields?: pulumi.Input<pulumi.Input<inputs.datacatalog.TagField>[]>;
    /**
     * The resource name of the tag in URL format. Example:
     * projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}/tags/{tag_id} or
     * projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/tags/{tag_id} where tag_id is a system-generated
     * identifier. Note that this Tag may not actually be stored in the location in this name.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the parent this tag is attached to. This can be the name of an entry or an entry group. If an entry group, the tag will be attached to
     * all entries in that group.
     */
    readonly parent?: pulumi.Input<string>;
    /**
     * The resource name of the tag template that this tag uses. Example:
     * projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}
     * This field cannot be modified after creation.
     */
    readonly template?: pulumi.Input<string>;
    /**
     * The display name of the tag template.
     */
    readonly templateDisplayname?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Tag resource.
 */
export interface TagArgs {
    /**
     * Resources like Entry can have schemas associated with them. This scope allows users to attach tags to an
     * individual column based on that schema.
     * For attaching a tag to a nested column, use `.` to separate the column names. Example:
     * `outer_column.inner_column`
     */
    readonly column?: pulumi.Input<string>;
    /**
     * This maps the ID of a tag field to the value of and additional information about that field.
     * Valid field IDs are defined by the tag's template. A tag must have at least 1 field and at most 500 fields.
     * Structure is documented below.
     */
    readonly fields: pulumi.Input<pulumi.Input<inputs.datacatalog.TagField>[]>;
    /**
     * The name of the parent this tag is attached to. This can be the name of an entry or an entry group. If an entry group, the tag will be attached to
     * all entries in that group.
     */
    readonly parent?: pulumi.Input<string>;
    /**
     * The resource name of the tag template that this tag uses. Example:
     * projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}
     * This field cannot be modified after creation.
     */
    readonly template: pulumi.Input<string>;
}
