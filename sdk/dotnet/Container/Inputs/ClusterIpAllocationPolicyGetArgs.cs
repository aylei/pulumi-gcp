// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Container.Inputs
{

    public sealed class ClusterIpAllocationPolicyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address range for the cluster pod IPs.
        /// Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
        /// to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
        /// from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
        /// pick a specific range to use.
        /// </summary>
        [Input("clusterIpv4CidrBlock")]
        public Input<string>? ClusterIpv4CidrBlock { get; set; }

        /// <summary>
        /// The name of the existing secondary
        /// range in the cluster's subnetwork to use for pod IP addresses. Alternatively,
        /// `cluster_ipv4_cidr_block` can be used to automatically create a GKE-managed one.
        /// </summary>
        [Input("clusterSecondaryRangeName")]
        public Input<string>? ClusterSecondaryRangeName { get; set; }

        /// <summary>
        /// The IP address range of the services IPs in this cluster.
        /// Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
        /// to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
        /// from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
        /// pick a specific range to use.
        /// </summary>
        [Input("servicesIpv4CidrBlock")]
        public Input<string>? ServicesIpv4CidrBlock { get; set; }

        /// <summary>
        /// The name of the existing
        /// secondary range in the cluster's subnetwork to use for service `ClusterIP`s.
        /// Alternatively, `services_ipv4_cidr_block` can be used to automatically create a
        /// GKE-managed one.
        /// </summary>
        [Input("servicesSecondaryRangeName")]
        public Input<string>? ServicesSecondaryRangeName { get; set; }

        public ClusterIpAllocationPolicyGetArgs()
        {
        }
    }
}
