// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Outputs
{

    [OutputType]
    public sealed class RegionBackendServiceConsistentHashHttpCookie
    {
        /// <summary>
        /// Name of the cookie.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Path to set for the cookie.
        /// </summary>
        public readonly string? Path;
        /// <summary>
        /// Lifetime of the cookie.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.RegionBackendServiceConsistentHashHttpCookieTtl? Ttl;

        [OutputConstructor]
        private RegionBackendServiceConsistentHashHttpCookie(
            string? name,

            string? path,

            Outputs.RegionBackendServiceConsistentHashHttpCookieTtl? ttl)
        {
            Name = name;
            Path = path;
            Ttl = ttl;
        }
    }
}
