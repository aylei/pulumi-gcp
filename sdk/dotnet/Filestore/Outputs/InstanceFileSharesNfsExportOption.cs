// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Filestore.Outputs
{

    [OutputType]
    public sealed class InstanceFileSharesNfsExportOption
    {
        /// <summary>
        /// Either READ_ONLY, for allowing only read requests on the exported directory,
        /// or READ_WRITE, for allowing both read and write requests. The default is READ_WRITE.
        /// Default value is `READ_WRITE`.
        /// Possible values are `READ_ONLY` and `READ_WRITE`.
        /// </summary>
        public readonly string? AccessMode;
        /// <summary>
        /// An integer representing the anonymous group id with a default value of 65534.
        /// Anon_gid may only be set with squashMode of ROOT_SQUASH. An error will be returned
        /// if this field is specified for other squashMode settings.
        /// </summary>
        public readonly int? AnonGid;
        /// <summary>
        /// An integer representing the anonymous user id with a default value of 65534.
        /// Anon_uid may only be set with squashMode of ROOT_SQUASH. An error will be returned
        /// if this field is specified for other squashMode settings.
        /// </summary>
        public readonly int? AnonUid;
        /// <summary>
        /// List of either IPv4 addresses, or ranges in CIDR notation which may mount the file share.
        /// Overlapping IP ranges are not allowed, both within and across NfsExportOptions. An error will be returned.
        /// The limit is 64 IP ranges/addresses for each FileShareConfig among all NfsExportOptions.
        /// </summary>
        public readonly ImmutableArray<string> IpRanges;
        /// <summary>
        /// Either NO_ROOT_SQUASH, for allowing root access on the exported directory, or ROOT_SQUASH,
        /// for not allowing root access. The default is NO_ROOT_SQUASH.
        /// Default value is `NO_ROOT_SQUASH`.
        /// Possible values are `NO_ROOT_SQUASH` and `ROOT_SQUASH`.
        /// </summary>
        public readonly string? SquashMode;

        [OutputConstructor]
        private InstanceFileSharesNfsExportOption(
            string? accessMode,

            int? anonGid,

            int? anonUid,

            ImmutableArray<string> ipRanges,

            string? squashMode)
        {
            AccessMode = accessMode;
            AnonGid = anonGid;
            AnonUid = anonUid;
            IpRanges = ipRanges;
            SquashMode = squashMode;
        }
    }
}
