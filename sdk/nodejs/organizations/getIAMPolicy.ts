// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Generates an IAM policy document that may be referenced by and applied to
 * other Google Cloud Platform resources, such as the `google_project` resource.
 * 
 * ```
 * data "google_iam_policy" "admin" {
 *   binding {
 *     role = "roles/compute.instanceAdmin"
 * 
 *     members = [
 *       "serviceAccount:your-custom-sa@your-project.iam.gserviceaccount.com",
 *     ]
 *   }
 * 
 *   binding {
 *     role = "roles/storage.objectViewer"
 * 
 *     members = [
 *       "user:jane@example.com",
 *     ]
 *   }
 * }
 * ```
 * 
 * This data source is used to define IAM policies to apply to other resources.
 * Currently, defining a policy through a datasource and referencing that policy
 * from another resource is the only way to apply an IAM policy to a resource.
 * 
 * **Note:** Several restrictions apply when setting IAM policies through this API.
 * See the [setIamPolicy docs](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)
 * for a list of these restrictions.
 */
export function getIAMPolicy(args: GetIAMPolicyArgs): Promise<GetIAMPolicyResult> {
    return pulumi.runtime.invoke("gcp:organizations/getIAMPolicy:getIAMPolicy", {
        "bindings": args.bindings,
    });
}

/**
 * A collection of arguments for invoking getIAMPolicy.
 */
export interface GetIAMPolicyArgs {
    /**
     * A nested configuration block (described below)
     * defining a binding to be included in the policy document. Multiple
     * `binding` arguments are supported.
     */
    readonly bindings: pulumi.Input<{ members: pulumi.Input<pulumi.Input<string>[]>, role: pulumi.Input<string> }[]>;
}

/**
 * A collection of values returned by getIAMPolicy.
 */
export interface GetIAMPolicyResult {
    /**
     * The above bindings serialized in a format suitable for
     * referencing from a resource that supports IAM.
     */
    readonly policyData: string;
}