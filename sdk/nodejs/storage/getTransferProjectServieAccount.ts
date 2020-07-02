// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve Storage Transfer service account for this project
 */
export function getTransferProjectServieAccount(args?: GetTransferProjectServieAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetTransferProjectServieAccountResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("gcp:storage/getTransferProjectServieAccount:getTransferProjectServieAccount", {
        "project": args.project,
    }, opts);
}

/**
 * A collection of arguments for invoking getTransferProjectServieAccount.
 */
export interface GetTransferProjectServieAccountArgs {
    /**
     * The project ID. If it is not provided, the provider project is used.
     */
    readonly project?: string;
}

/**
 * A collection of values returned by getTransferProjectServieAccount.
 */
export interface GetTransferProjectServieAccountResult {
    /**
     * Email address of the default service account used by Storage Transfer Jobs running in this project
     */
    readonly email: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly project: string;
}
