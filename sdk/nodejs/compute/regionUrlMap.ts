// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * UrlMaps are used to route requests to a backend service based on rules
 * that you define for the host and path of an incoming URL.
 *
 * ## Example Usage
 */
export class RegionUrlMap extends pulumi.CustomResource {
    /**
     * Get an existing RegionUrlMap resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegionUrlMapState, opts?: pulumi.CustomResourceOptions): RegionUrlMap {
        return new RegionUrlMap(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/regionUrlMap:RegionUrlMap';

    /**
     * Returns true if the given object is an instance of RegionUrlMap.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RegionUrlMap {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RegionUrlMap.__pulumiType;
    }

    /**
     * Creation timestamp in RFC3339 text format.
     */
    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    /**
     * A reference to a RegionBackendService resource. This will be used if
     * none of the pathRules defined by this PathMatcher is matched by
     * the URL's path portion.
     */
    public readonly defaultService!: pulumi.Output<string | undefined>;
    /**
     * When none of the specified hostRules match, the request is redirected to a URL specified
     * by defaultUrlRedirect. If defaultUrlRedirect is specified, defaultService or
     * defaultRouteAction must not be set.
     * Structure is documented below.
     */
    public readonly defaultUrlRedirect!: pulumi.Output<outputs.compute.RegionUrlMapDefaultUrlRedirect | undefined>;
    /**
     * Description of this test case.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Fingerprint of this resource. This field is used internally during updates of this resource.
     */
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * The list of HostRules to use against the URL.
     * Structure is documented below.
     */
    public readonly hostRules!: pulumi.Output<outputs.compute.RegionUrlMapHostRule[] | undefined>;
    /**
     * The unique identifier for the resource.
     */
    public /*out*/ readonly mapId!: pulumi.Output<number>;
    /**
     * The name of the query parameter to match. The query parameter must exist in the
     * request, in the absence of which the request match fails.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The name of the PathMatcher to use to match the path portion of
     * the URL if the hostRule matches the URL's host portion.
     */
    public readonly pathMatchers!: pulumi.Output<outputs.compute.RegionUrlMapPathMatcher[] | undefined>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The Region in which the url map should reside.
     * If it is not provided, the provider region is used.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    /**
     * The list of expected URL mappings. Requests to update this UrlMap will
     * succeed only if all of the test cases pass.
     * Structure is documented below.
     */
    public readonly tests!: pulumi.Output<outputs.compute.RegionUrlMapTest[] | undefined>;

    /**
     * Create a RegionUrlMap resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: RegionUrlMapArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RegionUrlMapArgs | RegionUrlMapState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RegionUrlMapState | undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["defaultService"] = state ? state.defaultService : undefined;
            inputs["defaultUrlRedirect"] = state ? state.defaultUrlRedirect : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["hostRules"] = state ? state.hostRules : undefined;
            inputs["mapId"] = state ? state.mapId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["pathMatchers"] = state ? state.pathMatchers : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["tests"] = state ? state.tests : undefined;
        } else {
            const args = argsOrState as RegionUrlMapArgs | undefined;
            inputs["defaultService"] = args ? args.defaultService : undefined;
            inputs["defaultUrlRedirect"] = args ? args.defaultUrlRedirect : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["hostRules"] = args ? args.hostRules : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["pathMatchers"] = args ? args.pathMatchers : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["tests"] = args ? args.tests : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["fingerprint"] = undefined /*out*/;
            inputs["mapId"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RegionUrlMap.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RegionUrlMap resources.
 */
export interface RegionUrlMapState {
    /**
     * Creation timestamp in RFC3339 text format.
     */
    readonly creationTimestamp?: pulumi.Input<string>;
    /**
     * A reference to a RegionBackendService resource. This will be used if
     * none of the pathRules defined by this PathMatcher is matched by
     * the URL's path portion.
     */
    readonly defaultService?: pulumi.Input<string>;
    /**
     * When none of the specified hostRules match, the request is redirected to a URL specified
     * by defaultUrlRedirect. If defaultUrlRedirect is specified, defaultService or
     * defaultRouteAction must not be set.
     * Structure is documented below.
     */
    readonly defaultUrlRedirect?: pulumi.Input<inputs.compute.RegionUrlMapDefaultUrlRedirect>;
    /**
     * Description of this test case.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Fingerprint of this resource. This field is used internally during updates of this resource.
     */
    readonly fingerprint?: pulumi.Input<string>;
    /**
     * The list of HostRules to use against the URL.
     * Structure is documented below.
     */
    readonly hostRules?: pulumi.Input<pulumi.Input<inputs.compute.RegionUrlMapHostRule>[]>;
    /**
     * The unique identifier for the resource.
     */
    readonly mapId?: pulumi.Input<number>;
    /**
     * The name of the query parameter to match. The query parameter must exist in the
     * request, in the absence of which the request match fails.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the PathMatcher to use to match the path portion of
     * the URL if the hostRule matches the URL's host portion.
     */
    readonly pathMatchers?: pulumi.Input<pulumi.Input<inputs.compute.RegionUrlMapPathMatcher>[]>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The Region in which the url map should reside.
     * If it is not provided, the provider region is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    /**
     * The list of expected URL mappings. Requests to update this UrlMap will
     * succeed only if all of the test cases pass.
     * Structure is documented below.
     */
    readonly tests?: pulumi.Input<pulumi.Input<inputs.compute.RegionUrlMapTest>[]>;
}

/**
 * The set of arguments for constructing a RegionUrlMap resource.
 */
export interface RegionUrlMapArgs {
    /**
     * A reference to a RegionBackendService resource. This will be used if
     * none of the pathRules defined by this PathMatcher is matched by
     * the URL's path portion.
     */
    readonly defaultService?: pulumi.Input<string>;
    /**
     * When none of the specified hostRules match, the request is redirected to a URL specified
     * by defaultUrlRedirect. If defaultUrlRedirect is specified, defaultService or
     * defaultRouteAction must not be set.
     * Structure is documented below.
     */
    readonly defaultUrlRedirect?: pulumi.Input<inputs.compute.RegionUrlMapDefaultUrlRedirect>;
    /**
     * Description of this test case.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The list of HostRules to use against the URL.
     * Structure is documented below.
     */
    readonly hostRules?: pulumi.Input<pulumi.Input<inputs.compute.RegionUrlMapHostRule>[]>;
    /**
     * The name of the query parameter to match. The query parameter must exist in the
     * request, in the absence of which the request match fails.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the PathMatcher to use to match the path portion of
     * the URL if the hostRule matches the URL's host portion.
     */
    readonly pathMatchers?: pulumi.Input<pulumi.Input<inputs.compute.RegionUrlMapPathMatcher>[]>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The Region in which the url map should reside.
     * If it is not provided, the provider region is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The list of expected URL mappings. Requests to update this UrlMap will
     * succeed only if all of the test cases pass.
     * Structure is documented below.
     */
    readonly tests?: pulumi.Input<pulumi.Input<inputs.compute.RegionUrlMapTest>[]>;
}
