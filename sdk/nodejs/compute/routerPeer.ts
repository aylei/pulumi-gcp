// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * BGP information that must be configured into the routing stack to
 * establish BGP peering. This information must specify the peer ASN
 * and either the interface name, IP address, or peer IP address.
 * Please refer to RFC4273.
 *
 * To get more information about RouterBgpPeer, see:
 *
 * * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/routers)
 * * How-to Guides
 *     * [Google Cloud Router](https://cloud.google.com/router/docs/)
 *
 * ## Example Usage
 */
export class RouterPeer extends pulumi.CustomResource {
    /**
     * Get an existing RouterPeer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterPeerState, opts?: pulumi.CustomResourceOptions): RouterPeer {
        return new RouterPeer(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/routerPeer:RouterPeer';

    /**
     * Returns true if the given object is an instance of RouterPeer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RouterPeer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RouterPeer.__pulumiType;
    }

    /**
     * User-specified flag to indicate which mode to use for advertisement.
     * Valid values of this enum field are: `DEFAULT`, `CUSTOM`
     */
    public readonly advertiseMode!: pulumi.Output<string | undefined>;
    /**
     * User-specified list of prefix groups to advertise in custom
     * mode, which can take one of the following options:
     * * `ALL_SUBNETS`: Advertises all available subnets, including peer VPC subnets.
     * * `ALL_VPC_SUBNETS`: Advertises the router's own VPC subnets.
     * * `ALL_PEER_VPC_SUBNETS`: Advertises peer subnets of the router's VPC network.
     */
    public readonly advertisedGroups!: pulumi.Output<string[] | undefined>;
    /**
     * User-specified list of individual IP ranges to advertise in
     * custom mode. This field can only be populated if advertiseMode
     * is `CUSTOM` and is advertised to all peers of the router. These IP
     * ranges will be advertised in addition to any specified groups.
     * Leave this field blank to advertise no custom IP ranges.  Structure is documented below.
     */
    public readonly advertisedIpRanges!: pulumi.Output<outputs.compute.RouterPeerAdvertisedIpRange[] | undefined>;
    /**
     * The priority of routes advertised to this BGP peer.
     * Where there is more than one matching route of maximum
     * length, the routes with the lowest priority value win.
     */
    public readonly advertisedRoutePriority!: pulumi.Output<number | undefined>;
    /**
     * Name of the interface the BGP peer is associated with.
     */
    public readonly interface!: pulumi.Output<string>;
    /**
     * IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
     */
    public /*out*/ readonly ipAddress!: pulumi.Output<string>;
    /**
     * The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
     * you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
     * specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
     * of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
     */
    public /*out*/ readonly managementType!: pulumi.Output<string>;
    /**
     * Name of this BGP peer. The name must be 1-63 characters long,
     * and comply with RFC1035. Specifically, the name must be 1-63 characters
     * long and match the regular expression `a-z?` which
     * means the first character must be a lowercase letter, and all
     * following characters must be a dash, lowercase letter, or digit,
     * except the last character, which cannot be a dash.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Peer BGP Autonomous System Number (ASN).
     * Each BGP interface may use a different value.
     */
    public readonly peerAsn!: pulumi.Output<number>;
    /**
     * IP address of the BGP interface outside Google Cloud Platform.
     * Only IPv4 is supported.
     */
    public readonly peerIpAddress!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * Region where the router and BgpPeer reside.
     * If it is not provided, the provider region is used.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The name of the Cloud Router in which this BgpPeer will be configured.
     */
    public readonly router!: pulumi.Output<string>;

    /**
     * Create a RouterPeer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RouterPeerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RouterPeerArgs | RouterPeerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RouterPeerState | undefined;
            inputs["advertiseMode"] = state ? state.advertiseMode : undefined;
            inputs["advertisedGroups"] = state ? state.advertisedGroups : undefined;
            inputs["advertisedIpRanges"] = state ? state.advertisedIpRanges : undefined;
            inputs["advertisedRoutePriority"] = state ? state.advertisedRoutePriority : undefined;
            inputs["interface"] = state ? state.interface : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["managementType"] = state ? state.managementType : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["peerAsn"] = state ? state.peerAsn : undefined;
            inputs["peerIpAddress"] = state ? state.peerIpAddress : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["router"] = state ? state.router : undefined;
        } else {
            const args = argsOrState as RouterPeerArgs | undefined;
            if (!args || args.interface === undefined) {
                throw new Error("Missing required property 'interface'");
            }
            if (!args || args.peerAsn === undefined) {
                throw new Error("Missing required property 'peerAsn'");
            }
            if (!args || args.peerIpAddress === undefined) {
                throw new Error("Missing required property 'peerIpAddress'");
            }
            if (!args || args.router === undefined) {
                throw new Error("Missing required property 'router'");
            }
            inputs["advertiseMode"] = args ? args.advertiseMode : undefined;
            inputs["advertisedGroups"] = args ? args.advertisedGroups : undefined;
            inputs["advertisedIpRanges"] = args ? args.advertisedIpRanges : undefined;
            inputs["advertisedRoutePriority"] = args ? args.advertisedRoutePriority : undefined;
            inputs["interface"] = args ? args.interface : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["peerAsn"] = args ? args.peerAsn : undefined;
            inputs["peerIpAddress"] = args ? args.peerIpAddress : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["router"] = args ? args.router : undefined;
            inputs["ipAddress"] = undefined /*out*/;
            inputs["managementType"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RouterPeer.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RouterPeer resources.
 */
export interface RouterPeerState {
    /**
     * User-specified flag to indicate which mode to use for advertisement.
     * Valid values of this enum field are: `DEFAULT`, `CUSTOM`
     */
    readonly advertiseMode?: pulumi.Input<string>;
    /**
     * User-specified list of prefix groups to advertise in custom
     * mode, which can take one of the following options:
     * * `ALL_SUBNETS`: Advertises all available subnets, including peer VPC subnets.
     * * `ALL_VPC_SUBNETS`: Advertises the router's own VPC subnets.
     * * `ALL_PEER_VPC_SUBNETS`: Advertises peer subnets of the router's VPC network.
     */
    readonly advertisedGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * User-specified list of individual IP ranges to advertise in
     * custom mode. This field can only be populated if advertiseMode
     * is `CUSTOM` and is advertised to all peers of the router. These IP
     * ranges will be advertised in addition to any specified groups.
     * Leave this field blank to advertise no custom IP ranges.  Structure is documented below.
     */
    readonly advertisedIpRanges?: pulumi.Input<pulumi.Input<inputs.compute.RouterPeerAdvertisedIpRange>[]>;
    /**
     * The priority of routes advertised to this BGP peer.
     * Where there is more than one matching route of maximum
     * length, the routes with the lowest priority value win.
     */
    readonly advertisedRoutePriority?: pulumi.Input<number>;
    /**
     * Name of the interface the BGP peer is associated with.
     */
    readonly interface?: pulumi.Input<string>;
    /**
     * IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
     * you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
     * specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
     * of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
     */
    readonly managementType?: pulumi.Input<string>;
    /**
     * Name of this BGP peer. The name must be 1-63 characters long,
     * and comply with RFC1035. Specifically, the name must be 1-63 characters
     * long and match the regular expression `a-z?` which
     * means the first character must be a lowercase letter, and all
     * following characters must be a dash, lowercase letter, or digit,
     * except the last character, which cannot be a dash.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Peer BGP Autonomous System Number (ASN).
     * Each BGP interface may use a different value.
     */
    readonly peerAsn?: pulumi.Input<number>;
    /**
     * IP address of the BGP interface outside Google Cloud Platform.
     * Only IPv4 is supported.
     */
    readonly peerIpAddress?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Region where the router and BgpPeer reside.
     * If it is not provided, the provider region is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The name of the Cloud Router in which this BgpPeer will be configured.
     */
    readonly router?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RouterPeer resource.
 */
export interface RouterPeerArgs {
    /**
     * User-specified flag to indicate which mode to use for advertisement.
     * Valid values of this enum field are: `DEFAULT`, `CUSTOM`
     */
    readonly advertiseMode?: pulumi.Input<string>;
    /**
     * User-specified list of prefix groups to advertise in custom
     * mode, which can take one of the following options:
     * * `ALL_SUBNETS`: Advertises all available subnets, including peer VPC subnets.
     * * `ALL_VPC_SUBNETS`: Advertises the router's own VPC subnets.
     * * `ALL_PEER_VPC_SUBNETS`: Advertises peer subnets of the router's VPC network.
     */
    readonly advertisedGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * User-specified list of individual IP ranges to advertise in
     * custom mode. This field can only be populated if advertiseMode
     * is `CUSTOM` and is advertised to all peers of the router. These IP
     * ranges will be advertised in addition to any specified groups.
     * Leave this field blank to advertise no custom IP ranges.  Structure is documented below.
     */
    readonly advertisedIpRanges?: pulumi.Input<pulumi.Input<inputs.compute.RouterPeerAdvertisedIpRange>[]>;
    /**
     * The priority of routes advertised to this BGP peer.
     * Where there is more than one matching route of maximum
     * length, the routes with the lowest priority value win.
     */
    readonly advertisedRoutePriority?: pulumi.Input<number>;
    /**
     * Name of the interface the BGP peer is associated with.
     */
    readonly interface: pulumi.Input<string>;
    /**
     * Name of this BGP peer. The name must be 1-63 characters long,
     * and comply with RFC1035. Specifically, the name must be 1-63 characters
     * long and match the regular expression `a-z?` which
     * means the first character must be a lowercase letter, and all
     * following characters must be a dash, lowercase letter, or digit,
     * except the last character, which cannot be a dash.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Peer BGP Autonomous System Number (ASN).
     * Each BGP interface may use a different value.
     */
    readonly peerAsn: pulumi.Input<number>;
    /**
     * IP address of the BGP interface outside Google Cloud Platform.
     * Only IPv4 is supported.
     */
    readonly peerIpAddress: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Region where the router and BgpPeer reside.
     * If it is not provided, the provider region is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The name of the Cloud Router in which this BgpPeer will be configured.
     */
    readonly router: pulumi.Input<string>;
}
