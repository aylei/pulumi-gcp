// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Outputs
{

    [OutputType]
    public sealed class SloRequestBasedSliDistributionCutRange
    {
        /// <summary>
        /// max value for the range (inclusive). If not given,
        /// will be set to "infinity", defining an open range
        /// "&gt;= range.min"
        /// </summary>
        public readonly double? Max;
        /// <summary>
        /// Min value for the range (inclusive). If not given,
        /// will be set to "-infinity", defining an open range
        /// "&lt; range.max"
        /// </summary>
        public readonly double? Min;

        [OutputConstructor]
        private SloRequestBasedSliDistributionCutRange(
            double? max,

            double? min)
        {
            Max = max;
            Min = min;
        }
    }
}
