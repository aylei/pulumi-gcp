// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Container
{
    public static class GetCluster
    {
        /// <summary>
        /// Get info about a GKE cluster from its name and location.
        /// </summary>
        public static Task<GetClusterResult> InvokeAsync(GetClusterArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClusterResult>("gcp:container/getCluster:getCluster", args ?? new GetClusterArgs(), options.WithVersion());
    }


    public sealed class GetClusterArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The location (zone or region) this cluster has been
        /// created in. One of `location`, `region`, `zone`, or a provider-level `zone` must
        /// be specified.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// The name of the cluster.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The project in which the resource belongs. If it
        /// is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public string? Project { get; set; }

        /// <summary>
        /// The region this cluster has been created in. Deprecated
        /// in favour of `location`.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        /// <summary>
        /// The zone this cluster has been created in. Deprecated in
        /// favour of `location`.
        /// </summary>
        [Input("zone")]
        public string? Zone { get; set; }

        public GetClusterArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetClusterResult
    {
        public readonly ImmutableArray<string> AdditionalZones;
        public readonly ImmutableArray<Outputs.GetClusterAddonsConfigResult> AddonsConfigs;
        public readonly ImmutableArray<Outputs.GetClusterAuthenticatorGroupsConfigResult> AuthenticatorGroupsConfigs;
        public readonly ImmutableArray<Outputs.GetClusterClusterAutoscalingResult> ClusterAutoscalings;
        public readonly string ClusterIpv4Cidr;
        public readonly ImmutableArray<Outputs.GetClusterClusterTelemetryResult> ClusterTelemetries;
        public readonly ImmutableArray<Outputs.GetClusterDatabaseEncryptionResult> DatabaseEncryptions;
        public readonly int DefaultMaxPodsPerNode;
        public readonly ImmutableArray<Outputs.GetClusterDefaultSnatStatusResult> DefaultSnatStatuses;
        public readonly string Description;
        public readonly bool EnableBinaryAuthorization;
        public readonly bool EnableIntranodeVisibility;
        public readonly bool EnableKubernetesAlpha;
        public readonly bool EnableLegacyAbac;
        public readonly bool EnableShieldedNodes;
        public readonly bool EnableTpu;
        public readonly string Endpoint;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly int InitialNodeCount;
        public readonly ImmutableArray<string> InstanceGroupUrls;
        public readonly ImmutableArray<Outputs.GetClusterIpAllocationPolicyResult> IpAllocationPolicies;
        public readonly string LabelFingerprint;
        public readonly string? Location;
        public readonly string LoggingService;
        public readonly ImmutableArray<Outputs.GetClusterMaintenancePolicyResult> MaintenancePolicies;
        public readonly ImmutableArray<Outputs.GetClusterMasterAuthorizedNetworksConfigResult> MasterAuthorizedNetworksConfigs;
        public readonly ImmutableArray<Outputs.GetClusterMasterAuthResult> MasterAuths;
        public readonly string MasterVersion;
        public readonly string MinMasterVersion;
        public readonly string MonitoringService;
        public readonly string Name;
        public readonly string Network;
        public readonly ImmutableArray<Outputs.GetClusterNetworkPolicyResult> NetworkPolicies;
        public readonly string NetworkingMode;
        public readonly ImmutableArray<Outputs.GetClusterNodeConfigResult> NodeConfigs;
        public readonly ImmutableArray<string> NodeLocations;
        public readonly ImmutableArray<Outputs.GetClusterNodePoolResult> NodePools;
        public readonly string NodeVersion;
        public readonly string Operation;
        public readonly ImmutableArray<Outputs.GetClusterPodSecurityPolicyConfigResult> PodSecurityPolicyConfigs;
        public readonly ImmutableArray<Outputs.GetClusterPrivateClusterConfigResult> PrivateClusterConfigs;
        public readonly string? Project;
        public readonly string? Region;
        public readonly ImmutableArray<Outputs.GetClusterReleaseChannelResult> ReleaseChannels;
        public readonly bool RemoveDefaultNodePool;
        public readonly ImmutableDictionary<string, string> ResourceLabels;
        public readonly ImmutableArray<Outputs.GetClusterResourceUsageExportConfigResult> ResourceUsageExportConfigs;
        public readonly string SelfLink;
        public readonly string ServicesIpv4Cidr;
        public readonly string Subnetwork;
        public readonly string TpuIpv4CidrBlock;
        public readonly ImmutableArray<Outputs.GetClusterVerticalPodAutoscalingResult> VerticalPodAutoscalings;
        public readonly ImmutableArray<Outputs.GetClusterWorkloadIdentityConfigResult> WorkloadIdentityConfigs;
        public readonly string? Zone;

        [OutputConstructor]
        private GetClusterResult(
            ImmutableArray<string> additionalZones,

            ImmutableArray<Outputs.GetClusterAddonsConfigResult> addonsConfigs,

            ImmutableArray<Outputs.GetClusterAuthenticatorGroupsConfigResult> authenticatorGroupsConfigs,

            ImmutableArray<Outputs.GetClusterClusterAutoscalingResult> clusterAutoscalings,

            string clusterIpv4Cidr,

            ImmutableArray<Outputs.GetClusterClusterTelemetryResult> clusterTelemetries,

            ImmutableArray<Outputs.GetClusterDatabaseEncryptionResult> databaseEncryptions,

            int defaultMaxPodsPerNode,

            ImmutableArray<Outputs.GetClusterDefaultSnatStatusResult> defaultSnatStatuses,

            string description,

            bool enableBinaryAuthorization,

            bool enableIntranodeVisibility,

            bool enableKubernetesAlpha,

            bool enableLegacyAbac,

            bool enableShieldedNodes,

            bool enableTpu,

            string endpoint,

            string id,

            int initialNodeCount,

            ImmutableArray<string> instanceGroupUrls,

            ImmutableArray<Outputs.GetClusterIpAllocationPolicyResult> ipAllocationPolicies,

            string labelFingerprint,

            string? location,

            string loggingService,

            ImmutableArray<Outputs.GetClusterMaintenancePolicyResult> maintenancePolicies,

            ImmutableArray<Outputs.GetClusterMasterAuthorizedNetworksConfigResult> masterAuthorizedNetworksConfigs,

            ImmutableArray<Outputs.GetClusterMasterAuthResult> masterAuths,

            string masterVersion,

            string minMasterVersion,

            string monitoringService,

            string name,

            string network,

            ImmutableArray<Outputs.GetClusterNetworkPolicyResult> networkPolicies,

            string networkingMode,

            ImmutableArray<Outputs.GetClusterNodeConfigResult> nodeConfigs,

            ImmutableArray<string> nodeLocations,

            ImmutableArray<Outputs.GetClusterNodePoolResult> nodePools,

            string nodeVersion,

            string operation,

            ImmutableArray<Outputs.GetClusterPodSecurityPolicyConfigResult> podSecurityPolicyConfigs,

            ImmutableArray<Outputs.GetClusterPrivateClusterConfigResult> privateClusterConfigs,

            string? project,

            string? region,

            ImmutableArray<Outputs.GetClusterReleaseChannelResult> releaseChannels,

            bool removeDefaultNodePool,

            ImmutableDictionary<string, string> resourceLabels,

            ImmutableArray<Outputs.GetClusterResourceUsageExportConfigResult> resourceUsageExportConfigs,

            string selfLink,

            string servicesIpv4Cidr,

            string subnetwork,

            string tpuIpv4CidrBlock,

            ImmutableArray<Outputs.GetClusterVerticalPodAutoscalingResult> verticalPodAutoscalings,

            ImmutableArray<Outputs.GetClusterWorkloadIdentityConfigResult> workloadIdentityConfigs,

            string? zone)
        {
            AdditionalZones = additionalZones;
            AddonsConfigs = addonsConfigs;
            AuthenticatorGroupsConfigs = authenticatorGroupsConfigs;
            ClusterAutoscalings = clusterAutoscalings;
            ClusterIpv4Cidr = clusterIpv4Cidr;
            ClusterTelemetries = clusterTelemetries;
            DatabaseEncryptions = databaseEncryptions;
            DefaultMaxPodsPerNode = defaultMaxPodsPerNode;
            DefaultSnatStatuses = defaultSnatStatuses;
            Description = description;
            EnableBinaryAuthorization = enableBinaryAuthorization;
            EnableIntranodeVisibility = enableIntranodeVisibility;
            EnableKubernetesAlpha = enableKubernetesAlpha;
            EnableLegacyAbac = enableLegacyAbac;
            EnableShieldedNodes = enableShieldedNodes;
            EnableTpu = enableTpu;
            Endpoint = endpoint;
            Id = id;
            InitialNodeCount = initialNodeCount;
            InstanceGroupUrls = instanceGroupUrls;
            IpAllocationPolicies = ipAllocationPolicies;
            LabelFingerprint = labelFingerprint;
            Location = location;
            LoggingService = loggingService;
            MaintenancePolicies = maintenancePolicies;
            MasterAuthorizedNetworksConfigs = masterAuthorizedNetworksConfigs;
            MasterAuths = masterAuths;
            MasterVersion = masterVersion;
            MinMasterVersion = minMasterVersion;
            MonitoringService = monitoringService;
            Name = name;
            Network = network;
            NetworkPolicies = networkPolicies;
            NetworkingMode = networkingMode;
            NodeConfigs = nodeConfigs;
            NodeLocations = nodeLocations;
            NodePools = nodePools;
            NodeVersion = nodeVersion;
            Operation = operation;
            PodSecurityPolicyConfigs = podSecurityPolicyConfigs;
            PrivateClusterConfigs = privateClusterConfigs;
            Project = project;
            Region = region;
            ReleaseChannels = releaseChannels;
            RemoveDefaultNodePool = removeDefaultNodePool;
            ResourceLabels = resourceLabels;
            ResourceUsageExportConfigs = resourceUsageExportConfigs;
            SelfLink = selfLink;
            ServicesIpv4Cidr = servicesIpv4Cidr;
            Subnetwork = subnetwork;
            TpuIpv4CidrBlock = tpuIpv4CidrBlock;
            VerticalPodAutoscalings = verticalPodAutoscalings;
            WorkloadIdentityConfigs = workloadIdentityConfigs;
            Zone = zone;
        }
    }
}
