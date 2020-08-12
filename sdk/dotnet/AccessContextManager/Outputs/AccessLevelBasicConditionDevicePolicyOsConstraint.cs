// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AccessContextManager.Outputs
{

    [OutputType]
    public sealed class AccessLevelBasicConditionDevicePolicyOsConstraint
    {
        /// <summary>
        /// The minimum allowed OS version. If not set, any version
        /// of this OS satisfies the constraint.
        /// Format: "major.minor.patch" such as "10.5.301", "9.2.1".
        /// </summary>
        public readonly string? MinimumVersion;
        /// <summary>
        /// The operating system type of the device.
        /// Possible values are `OS_UNSPECIFIED`, `DESKTOP_MAC`, `DESKTOP_WINDOWS`, `DESKTOP_LINUX`, and `DESKTOP_CHROME_OS`.
        /// </summary>
        public readonly string OsType;

        [OutputConstructor]
        private AccessLevelBasicConditionDevicePolicyOsConstraint(
            string? minimumVersion,

            string osType)
        {
            MinimumVersion = minimumVersion;
            OsType = osType;
        }
    }
}
