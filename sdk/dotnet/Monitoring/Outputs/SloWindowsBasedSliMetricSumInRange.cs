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
    public sealed class SloWindowsBasedSliMetricSumInRange
    {
        /// <summary>
        /// Range of numerical values. The computed good_service
        /// will be the count of values x in the Distribution such
        /// that range.min &lt;= x &lt; range.max. inclusive of min and
        /// exclusive of max. Open ranges can be defined by setting
        /// just one of min or max. Summed value `X` should satisfy
        /// `range.min &lt;= X &lt; range.max` for a good window.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.SloWindowsBasedSliMetricSumInRangeRange Range;
        /// <summary>
        /// A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters)
        /// specifying the TimeSeries to use for evaluating window
        /// quality. The provided TimeSeries must have
        /// ValueType = INT64 or ValueType = DOUBLE and
        /// MetricKind = GAUGE.
        /// Summed value `X` should satisfy
        /// `range.min &lt;= X &lt; range.max` for a good window.
        /// </summary>
        public readonly string TimeSeries;

        [OutputConstructor]
        private SloWindowsBasedSliMetricSumInRange(
            Outputs.SloWindowsBasedSliMetricSumInRangeRange range,

            string timeSeries)
        {
            Range = range;
            TimeSeries = timeSeries;
        }
    }
}
