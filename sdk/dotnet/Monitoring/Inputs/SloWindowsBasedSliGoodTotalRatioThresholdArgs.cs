// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class SloWindowsBasedSliGoodTotalRatioThresholdArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Basic SLI to evaluate to judge window quality.
        /// Structure is documented below.
        /// </summary>
        [Input("basicSliPerformance")]
        public Input<Inputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceArgs>? BasicSliPerformance { get; set; }

        /// <summary>
        /// Request-based SLI to evaluate to judge window quality.
        /// Structure is documented below.
        /// </summary>
        [Input("performance")]
        public Input<Inputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceArgs>? Performance { get; set; }

        /// <summary>
        /// A duration string, e.g. 10s.
        /// Good service is defined to be the count of requests made to
        /// this service that return in no more than threshold.
        /// </summary>
        [Input("threshold")]
        public Input<double>? Threshold { get; set; }

        public SloWindowsBasedSliGoodTotalRatioThresholdArgs()
        {
        }
    }
}
