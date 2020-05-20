// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Composer.Inputs
{

    public sealed class EnvironmentConfigNodeConfigIpAllocationPolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address range used to allocate IP addresses to pods in the cluster.
        /// Set to blank to have GKE choose a range with the default size.
        /// Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
        /// Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
        /// (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
        /// Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
        /// </summary>
        [Input("clusterIpv4CidrBlock")]
        public Input<string>? ClusterIpv4CidrBlock { get; set; }

        /// <summary>
        /// The name of the cluster's secondary range used to allocate IP addresses to pods.
        /// Specify either `cluster_secondary_range_name` or `cluster_ipv4_cidr_block` but not both.
        /// This field is applicable only when `use_ip_aliases` is true.
        /// </summary>
        [Input("clusterSecondaryRangeName")]
        public Input<string>? ClusterSecondaryRangeName { get; set; }

        /// <summary>
        /// The IP address range used to allocate IP addresses in this cluster.
        /// Set to blank to have GKE choose a range with the default size.
        /// Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
        /// Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
        /// (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
        /// Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
        /// </summary>
        [Input("servicesIpv4CidrBlock")]
        public Input<string>? ServicesIpv4CidrBlock { get; set; }

        /// <summary>
        /// The name of the services' secondary range used to allocate IP addresses to the cluster.
        /// Specify either `services_secondary_range_name` or `services_ipv4_cidr_block` but not both.
        /// This field is applicable only when `use_ip_aliases` is true.
        /// </summary>
        [Input("servicesSecondaryRangeName")]
        public Input<string>? ServicesSecondaryRangeName { get; set; }

        /// <summary>
        /// Whether or not to enable Alias IPs in the GKE cluster. If true, a VPC-native cluster is created.
        /// Defaults to true if the `ip_allocation_block` is present in config.
        /// </summary>
        [Input("useIpAliases", required: true)]
        public Input<bool> UseIpAliases { get; set; } = null!;

        public EnvironmentConfigNodeConfigIpAllocationPolicyArgs()
        {
        }
    }
}