// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The ObjectAccessControls resources represent the Access Control Lists
 * (ACLs) for objects within Google Cloud Storage. ACLs let you specify
 * who has access to your data and to what extent.
 * 
 * There are two roles that can be assigned to an entity:
 * 
 * READERs can get an object, though the acl property will not be revealed.
 * OWNERs are READERs, and they can get the acl property, update an object,
 * and call all objectAccessControls methods on the object. The owner of an
 * object is always an OWNER.
 * For more information, see Access Control, with the caveat that this API
 * uses READER and OWNER instead of READ and FULL_CONTROL.
 * 
 * 
 * To get more information about ObjectAccessControl, see:
 * 
 * * [API documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/storage/docs/access-control/create-manage-lists)
 * 
 * ## Example Usage - Storage Object Access Control Public Object
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const bucket = new gcp.storage.Bucket("bucket", {});
 * const object = new gcp.storage.BucketObject("object", {
 *     bucket: bucket.name,
 *     source: new pulumi.asset.FileArchive("../static/img/header-logo.png"),
 * });
 * const publicRule = new gcp.storage.ObjectAccessControl("public_rule", {
 *     bucket: bucket.name,
 *     entity: "allUsers",
 *     object: object.outputName,
 *     role: "READER",
 * });
 * ```
 */
export class ObjectAccessControl extends pulumi.CustomResource {
    /**
     * Get an existing ObjectAccessControl resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ObjectAccessControlState, opts?: pulumi.CustomResourceOptions): ObjectAccessControl {
        return new ObjectAccessControl(name, <any>state, { ...opts, id: id });
    }

    public readonly bucket: pulumi.Output<string>;
    public /*out*/ readonly domain: pulumi.Output<string>;
    public /*out*/ readonly email: pulumi.Output<string>;
    public readonly entity: pulumi.Output<string>;
    public /*out*/ readonly entityId: pulumi.Output<string>;
    public /*out*/ readonly generation: pulumi.Output<number>;
    public readonly object: pulumi.Output<string>;
    public /*out*/ readonly projectTeam: pulumi.Output<{ projectNumber?: string, team?: string }>;
    public readonly role: pulumi.Output<string>;

    /**
     * Create a ObjectAccessControl resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ObjectAccessControlArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ObjectAccessControlArgs | ObjectAccessControlState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ObjectAccessControlState = argsOrState as ObjectAccessControlState | undefined;
            inputs["bucket"] = state ? state.bucket : undefined;
            inputs["domain"] = state ? state.domain : undefined;
            inputs["email"] = state ? state.email : undefined;
            inputs["entity"] = state ? state.entity : undefined;
            inputs["entityId"] = state ? state.entityId : undefined;
            inputs["generation"] = state ? state.generation : undefined;
            inputs["object"] = state ? state.object : undefined;
            inputs["projectTeam"] = state ? state.projectTeam : undefined;
            inputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as ObjectAccessControlArgs | undefined;
            if (!args || args.bucket === undefined) {
                throw new Error("Missing required property 'bucket'");
            }
            if (!args || args.entity === undefined) {
                throw new Error("Missing required property 'entity'");
            }
            if (!args || args.object === undefined) {
                throw new Error("Missing required property 'object'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            inputs["bucket"] = args ? args.bucket : undefined;
            inputs["entity"] = args ? args.entity : undefined;
            inputs["object"] = args ? args.object : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["domain"] = undefined /*out*/;
            inputs["email"] = undefined /*out*/;
            inputs["entityId"] = undefined /*out*/;
            inputs["generation"] = undefined /*out*/;
            inputs["projectTeam"] = undefined /*out*/;
        }
        super("gcp:storage/objectAccessControl:ObjectAccessControl", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ObjectAccessControl resources.
 */
export interface ObjectAccessControlState {
    readonly bucket?: pulumi.Input<string>;
    readonly domain?: pulumi.Input<string>;
    readonly email?: pulumi.Input<string>;
    readonly entity?: pulumi.Input<string>;
    readonly entityId?: pulumi.Input<string>;
    readonly generation?: pulumi.Input<number>;
    readonly object?: pulumi.Input<string>;
    readonly projectTeam?: pulumi.Input<{ projectNumber?: pulumi.Input<string>, team?: pulumi.Input<string> }>;
    readonly role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ObjectAccessControl resource.
 */
export interface ObjectAccessControlArgs {
    readonly bucket: pulumi.Input<string>;
    readonly entity: pulumi.Input<string>;
    readonly object: pulumi.Input<string>;
    readonly role: pulumi.Input<string>;
}
