// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class SloWindowsBasedSliMetricMeanInRangeRangeGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// max value for the range (inclusive). If not given,
        /// will be set to "infinity", defining an open range
        /// "&gt;= range.min"
        /// </summary>
        [Input("max")]
        public Input<double>? Max { get; set; }

        /// <summary>
        /// Min value for the range (inclusive). If not given,
        /// will be set to "-infinity", defining an open range
        /// "&lt; range.max"
        /// </summary>
        [Input("min")]
        public Input<double>? Min { get; set; }

        public SloWindowsBasedSliMetricMeanInRangeRangeGetArgs()
        {
        }
    }
}
