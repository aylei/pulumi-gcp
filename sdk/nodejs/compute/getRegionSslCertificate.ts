// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Get info about a Region Google Compute SSL Certificate from its name.
 */
export function getRegionSslCertificate(args: GetRegionSslCertificateArgs, opts?: pulumi.InvokeOptions): Promise<GetRegionSslCertificateResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("gcp:compute/getRegionSslCertificate:getRegionSslCertificate", {
        "name": args.name,
        "project": args.project,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegionSslCertificate.
 */
export interface GetRegionSslCertificateArgs {
    /**
     * The name of the certificate.
     */
    readonly name: string;
    /**
     * The project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: string;
    /**
     * The region in which the resource belongs. If it
     * is not provided, the provider region is used.
     */
    readonly region?: string;
}

/**
 * A collection of values returned by getRegionSslCertificate.
 */
export interface GetRegionSslCertificateResult {
    readonly certificate: string;
    readonly certificateId: number;
    readonly creationTimestamp: string;
    readonly description: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly namePrefix: string;
    readonly privateKey: string;
    readonly project?: string;
    readonly region?: string;
    readonly selfLink: string;
}