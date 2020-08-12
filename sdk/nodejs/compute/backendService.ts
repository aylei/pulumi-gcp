// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A Backend Service defines a group of virtual machines that will serve
 * traffic for load balancing. This resource is a global backend service,
 * appropriate for external load balancing or self-managed internal load balancing.
 * For managed internal load balancing, use a regional backend service instead.
 *
 * Currently self-managed internal load balancing is only available in beta.
 *
 * To get more information about BackendService, see:
 *
 * * [API documentation](https://cloud.google.com/compute/docs/reference/v1/backendServices)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)
 *
 * ## Example Usage
 */
export class BackendService extends pulumi.CustomResource {
    /**
     * Get an existing BackendService resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BackendServiceState, opts?: pulumi.CustomResourceOptions): BackendService {
        return new BackendService(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/backendService:BackendService';

    /**
     * Returns true if the given object is an instance of BackendService.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BackendService {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BackendService.__pulumiType;
    }

    /**
     * Lifetime of cookies in seconds if sessionAffinity is
     * GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
     * only until the end of the browser session (or equivalent). The
     * maximum allowed value for TTL is one day.
     * When the load balancing scheme is INTERNAL, this field is not used.
     */
    public readonly affinityCookieTtlSec!: pulumi.Output<number | undefined>;
    /**
     * The set of backends that serve this BackendService.
     * Structure is documented below.
     */
    public readonly backends!: pulumi.Output<outputs.compute.BackendServiceBackend[] | undefined>;
    /**
     * Cloud CDN configuration for this BackendService.
     * Structure is documented below.
     */
    public readonly cdnPolicy!: pulumi.Output<outputs.compute.BackendServiceCdnPolicy>;
    /**
     * Settings controlling the volume of connections to a backend service. This field
     * is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
     * Structure is documented below.
     */
    public readonly circuitBreakers!: pulumi.Output<outputs.compute.BackendServiceCircuitBreakers | undefined>;
    /**
     * Time for which instance will be drained (not accept new
     * connections, but still work to finish started).
     */
    public readonly connectionDrainingTimeoutSec!: pulumi.Output<number | undefined>;
    /**
     * Consistent Hash-based load balancing can be used to provide soft session
     * affinity based on HTTP headers, cookies or other properties. This load balancing
     * policy is applicable only for HTTP connections. The affinity to a particular
     * destination host will be lost when one or more hosts are added/removed from the
     * destination service. This field specifies parameters that control consistent
     * hashing. This field only applies if the loadBalancingScheme is set to
     * INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
     * set to MAGLEV or RING_HASH.
     * Structure is documented below.
     */
    public readonly consistentHash!: pulumi.Output<outputs.compute.BackendServiceConsistentHash | undefined>;
    /**
     * Creation timestamp in RFC3339 text format.
     */
    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    /**
     * Headers that the HTTP/S load balancer should add to proxied
     * requests.
     */
    public readonly customRequestHeaders!: pulumi.Output<string[] | undefined>;
    /**
     * An optional description of this resource.
     * Provide this property when you create the resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * If true, enable Cloud CDN for this BackendService.
     */
    public readonly enableCdn!: pulumi.Output<boolean | undefined>;
    /**
     * Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
     */
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
     * for health checking this BackendService. Currently at most one health
     * check can be specified.
     * A health check must be specified unless the backend service uses an internet NEG as a backend.
     * For internal load balancing, a URL to a HealthCheck resource must be specified instead.
     */
    public readonly healthChecks!: pulumi.Output<string | undefined>;
    /**
     * Settings for enabling Cloud Identity Aware Proxy
     * Structure is documented below.
     */
    public readonly iap!: pulumi.Output<outputs.compute.BackendServiceIap | undefined>;
    /**
     * Indicates whether the backend service will be used with internal or
     * external load balancing. A backend service created for one type of
     * load balancing cannot be used with the other.
     * Default value is `EXTERNAL`.
     * Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
     */
    public readonly loadBalancingScheme!: pulumi.Output<string | undefined>;
    /**
     * The load balancing algorithm used within the scope of the locality.
     * The possible values are -
     * ROUND_ROBIN - This is a simple policy in which each healthy backend
     * is selected in round robin order.
     * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
     * hosts and picks the host which has fewer active requests.
     * RING_HASH - The ring/modulo hash load balancer implements consistent
     * hashing to backends. The algorithm has the property that the
     * addition/removal of a host from a set of N hosts only affects
     * 1/N of the requests.
     * RANDOM - The load balancer selects a random healthy host.
     * ORIGINAL_DESTINATION - Backend host is selected based on the client
     * connection metadata, i.e., connections are opened
     * to the same address as the destination address of
     * the incoming connection before the connection
     * was redirected to the load balancer.
     * MAGLEV - used as a drop in replacement for the ring hash load balancer.
     * Maglev is not as stable as ring hash but has faster table lookup
     * build times and host selection times. For more information about
     * Maglev, refer to https://ai.google/research/pubs/pub44824
     * This field is applicable only when the loadBalancingScheme is set to
     * INTERNAL_SELF_MANAGED.
     * Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
     */
    public readonly localityLbPolicy!: pulumi.Output<string | undefined>;
    /**
     * This field denotes the logging options for the load balancer traffic served by this backend service.
     * If logging is enabled, logs will be exported to Stackdriver.
     * Structure is documented below.
     */
    public readonly logConfig!: pulumi.Output<outputs.compute.BackendServiceLogConfig>;
    /**
     * Name of the cookie.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Settings controlling eviction of unhealthy hosts from the load balancing pool.
     * This field is applicable only when the loadBalancingScheme is set
     * to INTERNAL_SELF_MANAGED.
     * Structure is documented below.
     */
    public readonly outlierDetection!: pulumi.Output<outputs.compute.BackendServiceOutlierDetection | undefined>;
    /**
     * Name of backend port. The same name should appear in the instance
     * groups referenced by this service. Required when the load balancing
     * scheme is EXTERNAL.
     */
    public readonly portName!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The protocol this BackendService uses to communicate with backends.
     * The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
     * types and may result in errors if used with the GA API.
     * Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, and `SSL`.
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * The security policy associated with this backend service.
     */
    public readonly securityPolicy!: pulumi.Output<string | undefined>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    /**
     * Type of session affinity to use. The default is NONE. Session affinity is
     * not applicable if the protocol is UDP.
     * Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
     */
    public readonly sessionAffinity!: pulumi.Output<string>;
    /**
     * How many seconds to wait for the backend before considering it a
     * failed request. Default is 30 seconds. Valid range is [1, 86400].
     */
    public readonly timeoutSec!: pulumi.Output<number>;

    /**
     * Create a BackendService resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: BackendServiceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BackendServiceArgs | BackendServiceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as BackendServiceState | undefined;
            inputs["affinityCookieTtlSec"] = state ? state.affinityCookieTtlSec : undefined;
            inputs["backends"] = state ? state.backends : undefined;
            inputs["cdnPolicy"] = state ? state.cdnPolicy : undefined;
            inputs["circuitBreakers"] = state ? state.circuitBreakers : undefined;
            inputs["connectionDrainingTimeoutSec"] = state ? state.connectionDrainingTimeoutSec : undefined;
            inputs["consistentHash"] = state ? state.consistentHash : undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["customRequestHeaders"] = state ? state.customRequestHeaders : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enableCdn"] = state ? state.enableCdn : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["healthChecks"] = state ? state.healthChecks : undefined;
            inputs["iap"] = state ? state.iap : undefined;
            inputs["loadBalancingScheme"] = state ? state.loadBalancingScheme : undefined;
            inputs["localityLbPolicy"] = state ? state.localityLbPolicy : undefined;
            inputs["logConfig"] = state ? state.logConfig : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["outlierDetection"] = state ? state.outlierDetection : undefined;
            inputs["portName"] = state ? state.portName : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["protocol"] = state ? state.protocol : undefined;
            inputs["securityPolicy"] = state ? state.securityPolicy : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["sessionAffinity"] = state ? state.sessionAffinity : undefined;
            inputs["timeoutSec"] = state ? state.timeoutSec : undefined;
        } else {
            const args = argsOrState as BackendServiceArgs | undefined;
            inputs["affinityCookieTtlSec"] = args ? args.affinityCookieTtlSec : undefined;
            inputs["backends"] = args ? args.backends : undefined;
            inputs["cdnPolicy"] = args ? args.cdnPolicy : undefined;
            inputs["circuitBreakers"] = args ? args.circuitBreakers : undefined;
            inputs["connectionDrainingTimeoutSec"] = args ? args.connectionDrainingTimeoutSec : undefined;
            inputs["consistentHash"] = args ? args.consistentHash : undefined;
            inputs["customRequestHeaders"] = args ? args.customRequestHeaders : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["enableCdn"] = args ? args.enableCdn : undefined;
            inputs["healthChecks"] = args ? args.healthChecks : undefined;
            inputs["iap"] = args ? args.iap : undefined;
            inputs["loadBalancingScheme"] = args ? args.loadBalancingScheme : undefined;
            inputs["localityLbPolicy"] = args ? args.localityLbPolicy : undefined;
            inputs["logConfig"] = args ? args.logConfig : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["outlierDetection"] = args ? args.outlierDetection : undefined;
            inputs["portName"] = args ? args.portName : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["securityPolicy"] = args ? args.securityPolicy : undefined;
            inputs["sessionAffinity"] = args ? args.sessionAffinity : undefined;
            inputs["timeoutSec"] = args ? args.timeoutSec : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["fingerprint"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(BackendService.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BackendService resources.
 */
export interface BackendServiceState {
    /**
     * Lifetime of cookies in seconds if sessionAffinity is
     * GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
     * only until the end of the browser session (or equivalent). The
     * maximum allowed value for TTL is one day.
     * When the load balancing scheme is INTERNAL, this field is not used.
     */
    readonly affinityCookieTtlSec?: pulumi.Input<number>;
    /**
     * The set of backends that serve this BackendService.
     * Structure is documented below.
     */
    readonly backends?: pulumi.Input<pulumi.Input<inputs.compute.BackendServiceBackend>[]>;
    /**
     * Cloud CDN configuration for this BackendService.
     * Structure is documented below.
     */
    readonly cdnPolicy?: pulumi.Input<inputs.compute.BackendServiceCdnPolicy>;
    /**
     * Settings controlling the volume of connections to a backend service. This field
     * is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
     * Structure is documented below.
     */
    readonly circuitBreakers?: pulumi.Input<inputs.compute.BackendServiceCircuitBreakers>;
    /**
     * Time for which instance will be drained (not accept new
     * connections, but still work to finish started).
     */
    readonly connectionDrainingTimeoutSec?: pulumi.Input<number>;
    /**
     * Consistent Hash-based load balancing can be used to provide soft session
     * affinity based on HTTP headers, cookies or other properties. This load balancing
     * policy is applicable only for HTTP connections. The affinity to a particular
     * destination host will be lost when one or more hosts are added/removed from the
     * destination service. This field specifies parameters that control consistent
     * hashing. This field only applies if the loadBalancingScheme is set to
     * INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
     * set to MAGLEV or RING_HASH.
     * Structure is documented below.
     */
    readonly consistentHash?: pulumi.Input<inputs.compute.BackendServiceConsistentHash>;
    /**
     * Creation timestamp in RFC3339 text format.
     */
    readonly creationTimestamp?: pulumi.Input<string>;
    /**
     * Headers that the HTTP/S load balancer should add to proxied
     * requests.
     */
    readonly customRequestHeaders?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An optional description of this resource.
     * Provide this property when you create the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * If true, enable Cloud CDN for this BackendService.
     */
    readonly enableCdn?: pulumi.Input<boolean>;
    /**
     * Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
     */
    readonly fingerprint?: pulumi.Input<string>;
    /**
     * The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
     * for health checking this BackendService. Currently at most one health
     * check can be specified.
     * A health check must be specified unless the backend service uses an internet NEG as a backend.
     * For internal load balancing, a URL to a HealthCheck resource must be specified instead.
     */
    readonly healthChecks?: pulumi.Input<string>;
    /**
     * Settings for enabling Cloud Identity Aware Proxy
     * Structure is documented below.
     */
    readonly iap?: pulumi.Input<inputs.compute.BackendServiceIap>;
    /**
     * Indicates whether the backend service will be used with internal or
     * external load balancing. A backend service created for one type of
     * load balancing cannot be used with the other.
     * Default value is `EXTERNAL`.
     * Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
     */
    readonly loadBalancingScheme?: pulumi.Input<string>;
    /**
     * The load balancing algorithm used within the scope of the locality.
     * The possible values are -
     * ROUND_ROBIN - This is a simple policy in which each healthy backend
     * is selected in round robin order.
     * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
     * hosts and picks the host which has fewer active requests.
     * RING_HASH - The ring/modulo hash load balancer implements consistent
     * hashing to backends. The algorithm has the property that the
     * addition/removal of a host from a set of N hosts only affects
     * 1/N of the requests.
     * RANDOM - The load balancer selects a random healthy host.
     * ORIGINAL_DESTINATION - Backend host is selected based on the client
     * connection metadata, i.e., connections are opened
     * to the same address as the destination address of
     * the incoming connection before the connection
     * was redirected to the load balancer.
     * MAGLEV - used as a drop in replacement for the ring hash load balancer.
     * Maglev is not as stable as ring hash but has faster table lookup
     * build times and host selection times. For more information about
     * Maglev, refer to https://ai.google/research/pubs/pub44824
     * This field is applicable only when the loadBalancingScheme is set to
     * INTERNAL_SELF_MANAGED.
     * Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
     */
    readonly localityLbPolicy?: pulumi.Input<string>;
    /**
     * This field denotes the logging options for the load balancer traffic served by this backend service.
     * If logging is enabled, logs will be exported to Stackdriver.
     * Structure is documented below.
     */
    readonly logConfig?: pulumi.Input<inputs.compute.BackendServiceLogConfig>;
    /**
     * Name of the cookie.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Settings controlling eviction of unhealthy hosts from the load balancing pool.
     * This field is applicable only when the loadBalancingScheme is set
     * to INTERNAL_SELF_MANAGED.
     * Structure is documented below.
     */
    readonly outlierDetection?: pulumi.Input<inputs.compute.BackendServiceOutlierDetection>;
    /**
     * Name of backend port. The same name should appear in the instance
     * groups referenced by this service. Required when the load balancing
     * scheme is EXTERNAL.
     */
    readonly portName?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The protocol this BackendService uses to communicate with backends.
     * The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
     * types and may result in errors if used with the GA API.
     * Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, and `SSL`.
     */
    readonly protocol?: pulumi.Input<string>;
    /**
     * The security policy associated with this backend service.
     */
    readonly securityPolicy?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    /**
     * Type of session affinity to use. The default is NONE. Session affinity is
     * not applicable if the protocol is UDP.
     * Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
     */
    readonly sessionAffinity?: pulumi.Input<string>;
    /**
     * How many seconds to wait for the backend before considering it a
     * failed request. Default is 30 seconds. Valid range is [1, 86400].
     */
    readonly timeoutSec?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a BackendService resource.
 */
export interface BackendServiceArgs {
    /**
     * Lifetime of cookies in seconds if sessionAffinity is
     * GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
     * only until the end of the browser session (or equivalent). The
     * maximum allowed value for TTL is one day.
     * When the load balancing scheme is INTERNAL, this field is not used.
     */
    readonly affinityCookieTtlSec?: pulumi.Input<number>;
    /**
     * The set of backends that serve this BackendService.
     * Structure is documented below.
     */
    readonly backends?: pulumi.Input<pulumi.Input<inputs.compute.BackendServiceBackend>[]>;
    /**
     * Cloud CDN configuration for this BackendService.
     * Structure is documented below.
     */
    readonly cdnPolicy?: pulumi.Input<inputs.compute.BackendServiceCdnPolicy>;
    /**
     * Settings controlling the volume of connections to a backend service. This field
     * is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
     * Structure is documented below.
     */
    readonly circuitBreakers?: pulumi.Input<inputs.compute.BackendServiceCircuitBreakers>;
    /**
     * Time for which instance will be drained (not accept new
     * connections, but still work to finish started).
     */
    readonly connectionDrainingTimeoutSec?: pulumi.Input<number>;
    /**
     * Consistent Hash-based load balancing can be used to provide soft session
     * affinity based on HTTP headers, cookies or other properties. This load balancing
     * policy is applicable only for HTTP connections. The affinity to a particular
     * destination host will be lost when one or more hosts are added/removed from the
     * destination service. This field specifies parameters that control consistent
     * hashing. This field only applies if the loadBalancingScheme is set to
     * INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
     * set to MAGLEV or RING_HASH.
     * Structure is documented below.
     */
    readonly consistentHash?: pulumi.Input<inputs.compute.BackendServiceConsistentHash>;
    /**
     * Headers that the HTTP/S load balancer should add to proxied
     * requests.
     */
    readonly customRequestHeaders?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An optional description of this resource.
     * Provide this property when you create the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * If true, enable Cloud CDN for this BackendService.
     */
    readonly enableCdn?: pulumi.Input<boolean>;
    /**
     * The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
     * for health checking this BackendService. Currently at most one health
     * check can be specified.
     * A health check must be specified unless the backend service uses an internet NEG as a backend.
     * For internal load balancing, a URL to a HealthCheck resource must be specified instead.
     */
    readonly healthChecks?: pulumi.Input<string>;
    /**
     * Settings for enabling Cloud Identity Aware Proxy
     * Structure is documented below.
     */
    readonly iap?: pulumi.Input<inputs.compute.BackendServiceIap>;
    /**
     * Indicates whether the backend service will be used with internal or
     * external load balancing. A backend service created for one type of
     * load balancing cannot be used with the other.
     * Default value is `EXTERNAL`.
     * Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
     */
    readonly loadBalancingScheme?: pulumi.Input<string>;
    /**
     * The load balancing algorithm used within the scope of the locality.
     * The possible values are -
     * ROUND_ROBIN - This is a simple policy in which each healthy backend
     * is selected in round robin order.
     * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
     * hosts and picks the host which has fewer active requests.
     * RING_HASH - The ring/modulo hash load balancer implements consistent
     * hashing to backends. The algorithm has the property that the
     * addition/removal of a host from a set of N hosts only affects
     * 1/N of the requests.
     * RANDOM - The load balancer selects a random healthy host.
     * ORIGINAL_DESTINATION - Backend host is selected based on the client
     * connection metadata, i.e., connections are opened
     * to the same address as the destination address of
     * the incoming connection before the connection
     * was redirected to the load balancer.
     * MAGLEV - used as a drop in replacement for the ring hash load balancer.
     * Maglev is not as stable as ring hash but has faster table lookup
     * build times and host selection times. For more information about
     * Maglev, refer to https://ai.google/research/pubs/pub44824
     * This field is applicable only when the loadBalancingScheme is set to
     * INTERNAL_SELF_MANAGED.
     * Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
     */
    readonly localityLbPolicy?: pulumi.Input<string>;
    /**
     * This field denotes the logging options for the load balancer traffic served by this backend service.
     * If logging is enabled, logs will be exported to Stackdriver.
     * Structure is documented below.
     */
    readonly logConfig?: pulumi.Input<inputs.compute.BackendServiceLogConfig>;
    /**
     * Name of the cookie.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Settings controlling eviction of unhealthy hosts from the load balancing pool.
     * This field is applicable only when the loadBalancingScheme is set
     * to INTERNAL_SELF_MANAGED.
     * Structure is documented below.
     */
    readonly outlierDetection?: pulumi.Input<inputs.compute.BackendServiceOutlierDetection>;
    /**
     * Name of backend port. The same name should appear in the instance
     * groups referenced by this service. Required when the load balancing
     * scheme is EXTERNAL.
     */
    readonly portName?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The protocol this BackendService uses to communicate with backends.
     * The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
     * types and may result in errors if used with the GA API.
     * Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, and `SSL`.
     */
    readonly protocol?: pulumi.Input<string>;
    /**
     * The security policy associated with this backend service.
     */
    readonly securityPolicy?: pulumi.Input<string>;
    /**
     * Type of session affinity to use. The default is NONE. Session affinity is
     * not applicable if the protocol is UDP.
     * Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
     */
    readonly sessionAffinity?: pulumi.Input<string>;
    /**
     * How many seconds to wait for the backend before considering it a
     * failed request. Default is 30 seconds. Valid range is [1, 86400].
     */
    readonly timeoutSec?: pulumi.Input<number>;
}
