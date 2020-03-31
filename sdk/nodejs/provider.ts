// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as utilities from "./utilities";

/**
 * The provider type for the google-beta package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google-beta/blob/master/website/docs/index.html.markdown.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'gcp';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Provider.__pulumiType;
    }


    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        {
            inputs["accessContextManagerCustomEndpoint"] = args ? args.accessContextManagerCustomEndpoint : undefined;
            inputs["accessToken"] = args ? args.accessToken : undefined;
            inputs["appEngineCustomEndpoint"] = args ? args.appEngineCustomEndpoint : undefined;
            inputs["batching"] = pulumi.output(args ? args.batching : undefined).apply(JSON.stringify);
            inputs["bigQueryCustomEndpoint"] = args ? args.bigQueryCustomEndpoint : undefined;
            inputs["bigqueryDataTransferCustomEndpoint"] = args ? args.bigqueryDataTransferCustomEndpoint : undefined;
            inputs["bigqueryReservationCustomEndpoint"] = args ? args.bigqueryReservationCustomEndpoint : undefined;
            inputs["bigtableCustomEndpoint"] = args ? args.bigtableCustomEndpoint : undefined;
            inputs["billingCustomEndpoint"] = args ? args.billingCustomEndpoint : undefined;
            inputs["binaryAuthorizationCustomEndpoint"] = args ? args.binaryAuthorizationCustomEndpoint : undefined;
            inputs["cloudBillingCustomEndpoint"] = args ? args.cloudBillingCustomEndpoint : undefined;
            inputs["cloudBuildCustomEndpoint"] = args ? args.cloudBuildCustomEndpoint : undefined;
            inputs["cloudFunctionsCustomEndpoint"] = args ? args.cloudFunctionsCustomEndpoint : undefined;
            inputs["cloudIotCustomEndpoint"] = args ? args.cloudIotCustomEndpoint : undefined;
            inputs["cloudRunCustomEndpoint"] = args ? args.cloudRunCustomEndpoint : undefined;
            inputs["cloudSchedulerCustomEndpoint"] = args ? args.cloudSchedulerCustomEndpoint : undefined;
            inputs["cloudTasksCustomEndpoint"] = args ? args.cloudTasksCustomEndpoint : undefined;
            inputs["composerCustomEndpoint"] = args ? args.composerCustomEndpoint : undefined;
            inputs["computeBetaCustomEndpoint"] = args ? args.computeBetaCustomEndpoint : undefined;
            inputs["computeCustomEndpoint"] = args ? args.computeCustomEndpoint : undefined;
            inputs["containerAnalysisCustomEndpoint"] = args ? args.containerAnalysisCustomEndpoint : undefined;
            inputs["containerBetaCustomEndpoint"] = args ? args.containerBetaCustomEndpoint : undefined;
            inputs["containerCustomEndpoint"] = args ? args.containerCustomEndpoint : undefined;
            inputs["credentials"] = (args ? args.credentials : undefined) || utilities.getEnv("GOOGLE_CREDENTIALS", "GOOGLE_CLOUD_KEYFILE_JSON", "GCLOUD_KEYFILE_JSON");
            inputs["dataFusionCustomEndpoint"] = args ? args.dataFusionCustomEndpoint : undefined;
            inputs["dataflowCustomEndpoint"] = args ? args.dataflowCustomEndpoint : undefined;
            inputs["dataprocBetaCustomEndpoint"] = args ? args.dataprocBetaCustomEndpoint : undefined;
            inputs["dataprocCustomEndpoint"] = args ? args.dataprocCustomEndpoint : undefined;
            inputs["datastoreCustomEndpoint"] = args ? args.datastoreCustomEndpoint : undefined;
            inputs["deploymentManagerCustomEndpoint"] = args ? args.deploymentManagerCustomEndpoint : undefined;
            inputs["dialogflowCustomEndpoint"] = args ? args.dialogflowCustomEndpoint : undefined;
            inputs["dnsBetaCustomEndpoint"] = args ? args.dnsBetaCustomEndpoint : undefined;
            inputs["dnsCustomEndpoint"] = args ? args.dnsCustomEndpoint : undefined;
            inputs["filestoreCustomEndpoint"] = args ? args.filestoreCustomEndpoint : undefined;
            inputs["firebaseCustomEndpoint"] = args ? args.firebaseCustomEndpoint : undefined;
            inputs["firestoreCustomEndpoint"] = args ? args.firestoreCustomEndpoint : undefined;
            inputs["gameServicesCustomEndpoint"] = args ? args.gameServicesCustomEndpoint : undefined;
            inputs["healthcareCustomEndpoint"] = args ? args.healthcareCustomEndpoint : undefined;
            inputs["iamCredentialsCustomEndpoint"] = args ? args.iamCredentialsCustomEndpoint : undefined;
            inputs["iamCustomEndpoint"] = args ? args.iamCustomEndpoint : undefined;
            inputs["iapCustomEndpoint"] = args ? args.iapCustomEndpoint : undefined;
            inputs["identityPlatformCustomEndpoint"] = args ? args.identityPlatformCustomEndpoint : undefined;
            inputs["kmsCustomEndpoint"] = args ? args.kmsCustomEndpoint : undefined;
            inputs["loggingCustomEndpoint"] = args ? args.loggingCustomEndpoint : undefined;
            inputs["mlEngineCustomEndpoint"] = args ? args.mlEngineCustomEndpoint : undefined;
            inputs["monitoringCustomEndpoint"] = args ? args.monitoringCustomEndpoint : undefined;
            inputs["project"] = (args ? args.project : undefined) || utilities.getEnv("GOOGLE_PROJECT", "GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT", "CLOUDSDK_CORE_PROJECT");
            inputs["pubsubCustomEndpoint"] = args ? args.pubsubCustomEndpoint : undefined;
            inputs["redisCustomEndpoint"] = args ? args.redisCustomEndpoint : undefined;
            inputs["region"] = (args ? args.region : undefined) || utilities.getEnv("GOOGLE_REGION", "GCLOUD_REGION", "CLOUDSDK_COMPUTE_REGION");
            inputs["requestTimeout"] = args ? args.requestTimeout : undefined;
            inputs["resourceManagerCustomEndpoint"] = args ? args.resourceManagerCustomEndpoint : undefined;
            inputs["resourceManagerV2beta1CustomEndpoint"] = args ? args.resourceManagerV2beta1CustomEndpoint : undefined;
            inputs["runtimeConfigCustomEndpoint"] = args ? args.runtimeConfigCustomEndpoint : undefined;
            inputs["runtimeconfigCustomEndpoint"] = args ? args.runtimeconfigCustomEndpoint : undefined;
            inputs["scopes"] = pulumi.output(args ? args.scopes : undefined).apply(JSON.stringify);
            inputs["secretManagerCustomEndpoint"] = args ? args.secretManagerCustomEndpoint : undefined;
            inputs["securityCenterCustomEndpoint"] = args ? args.securityCenterCustomEndpoint : undefined;
            inputs["securityScannerCustomEndpoint"] = args ? args.securityScannerCustomEndpoint : undefined;
            inputs["serviceManagementCustomEndpoint"] = args ? args.serviceManagementCustomEndpoint : undefined;
            inputs["serviceNetworkingCustomEndpoint"] = args ? args.serviceNetworkingCustomEndpoint : undefined;
            inputs["serviceUsageCustomEndpoint"] = args ? args.serviceUsageCustomEndpoint : undefined;
            inputs["sourceRepoCustomEndpoint"] = args ? args.sourceRepoCustomEndpoint : undefined;
            inputs["spannerCustomEndpoint"] = args ? args.spannerCustomEndpoint : undefined;
            inputs["sqlCustomEndpoint"] = args ? args.sqlCustomEndpoint : undefined;
            inputs["storageCustomEndpoint"] = args ? args.storageCustomEndpoint : undefined;
            inputs["storageTransferCustomEndpoint"] = args ? args.storageTransferCustomEndpoint : undefined;
            inputs["tpuCustomEndpoint"] = args ? args.tpuCustomEndpoint : undefined;
            inputs["userProjectOverride"] = pulumi.output(args ? args.userProjectOverride : undefined).apply(JSON.stringify);
            inputs["vpcAccessCustomEndpoint"] = args ? args.vpcAccessCustomEndpoint : undefined;
            inputs["zone"] = (args ? args.zone : undefined) || utilities.getEnv("GOOGLE_ZONE", "GCLOUD_ZONE", "CLOUDSDK_COMPUTE_ZONE");
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Provider.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    readonly accessContextManagerCustomEndpoint?: pulumi.Input<string>;
    readonly accessToken?: pulumi.Input<string>;
    readonly appEngineCustomEndpoint?: pulumi.Input<string>;
    readonly batching?: pulumi.Input<inputs.ProviderBatching>;
    readonly bigQueryCustomEndpoint?: pulumi.Input<string>;
    readonly bigqueryDataTransferCustomEndpoint?: pulumi.Input<string>;
    readonly bigqueryReservationCustomEndpoint?: pulumi.Input<string>;
    readonly bigtableCustomEndpoint?: pulumi.Input<string>;
    readonly billingCustomEndpoint?: pulumi.Input<string>;
    readonly binaryAuthorizationCustomEndpoint?: pulumi.Input<string>;
    readonly cloudBillingCustomEndpoint?: pulumi.Input<string>;
    readonly cloudBuildCustomEndpoint?: pulumi.Input<string>;
    readonly cloudFunctionsCustomEndpoint?: pulumi.Input<string>;
    readonly cloudIotCustomEndpoint?: pulumi.Input<string>;
    readonly cloudRunCustomEndpoint?: pulumi.Input<string>;
    readonly cloudSchedulerCustomEndpoint?: pulumi.Input<string>;
    readonly cloudTasksCustomEndpoint?: pulumi.Input<string>;
    readonly composerCustomEndpoint?: pulumi.Input<string>;
    readonly computeBetaCustomEndpoint?: pulumi.Input<string>;
    readonly computeCustomEndpoint?: pulumi.Input<string>;
    readonly containerAnalysisCustomEndpoint?: pulumi.Input<string>;
    readonly containerBetaCustomEndpoint?: pulumi.Input<string>;
    readonly containerCustomEndpoint?: pulumi.Input<string>;
    readonly credentials?: pulumi.Input<string>;
    readonly dataFusionCustomEndpoint?: pulumi.Input<string>;
    readonly dataflowCustomEndpoint?: pulumi.Input<string>;
    readonly dataprocBetaCustomEndpoint?: pulumi.Input<string>;
    readonly dataprocCustomEndpoint?: pulumi.Input<string>;
    readonly datastoreCustomEndpoint?: pulumi.Input<string>;
    readonly deploymentManagerCustomEndpoint?: pulumi.Input<string>;
    readonly dialogflowCustomEndpoint?: pulumi.Input<string>;
    readonly dnsBetaCustomEndpoint?: pulumi.Input<string>;
    readonly dnsCustomEndpoint?: pulumi.Input<string>;
    readonly filestoreCustomEndpoint?: pulumi.Input<string>;
    readonly firebaseCustomEndpoint?: pulumi.Input<string>;
    readonly firestoreCustomEndpoint?: pulumi.Input<string>;
    readonly gameServicesCustomEndpoint?: pulumi.Input<string>;
    readonly healthcareCustomEndpoint?: pulumi.Input<string>;
    readonly iamCredentialsCustomEndpoint?: pulumi.Input<string>;
    readonly iamCustomEndpoint?: pulumi.Input<string>;
    readonly iapCustomEndpoint?: pulumi.Input<string>;
    readonly identityPlatformCustomEndpoint?: pulumi.Input<string>;
    readonly kmsCustomEndpoint?: pulumi.Input<string>;
    readonly loggingCustomEndpoint?: pulumi.Input<string>;
    readonly mlEngineCustomEndpoint?: pulumi.Input<string>;
    readonly monitoringCustomEndpoint?: pulumi.Input<string>;
    readonly project?: pulumi.Input<string>;
    readonly pubsubCustomEndpoint?: pulumi.Input<string>;
    readonly redisCustomEndpoint?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    readonly requestTimeout?: pulumi.Input<string>;
    readonly resourceManagerCustomEndpoint?: pulumi.Input<string>;
    readonly resourceManagerV2beta1CustomEndpoint?: pulumi.Input<string>;
    readonly runtimeConfigCustomEndpoint?: pulumi.Input<string>;
    readonly runtimeconfigCustomEndpoint?: pulumi.Input<string>;
    readonly scopes?: pulumi.Input<pulumi.Input<string>[]>;
    readonly secretManagerCustomEndpoint?: pulumi.Input<string>;
    readonly securityCenterCustomEndpoint?: pulumi.Input<string>;
    readonly securityScannerCustomEndpoint?: pulumi.Input<string>;
    readonly serviceManagementCustomEndpoint?: pulumi.Input<string>;
    readonly serviceNetworkingCustomEndpoint?: pulumi.Input<string>;
    readonly serviceUsageCustomEndpoint?: pulumi.Input<string>;
    readonly sourceRepoCustomEndpoint?: pulumi.Input<string>;
    readonly spannerCustomEndpoint?: pulumi.Input<string>;
    readonly sqlCustomEndpoint?: pulumi.Input<string>;
    readonly storageCustomEndpoint?: pulumi.Input<string>;
    readonly storageTransferCustomEndpoint?: pulumi.Input<string>;
    readonly tpuCustomEndpoint?: pulumi.Input<string>;
    readonly userProjectOverride?: pulumi.Input<boolean>;
    readonly vpcAccessCustomEndpoint?: pulumi.Input<string>;
    readonly zone?: pulumi.Input<string>;
}
