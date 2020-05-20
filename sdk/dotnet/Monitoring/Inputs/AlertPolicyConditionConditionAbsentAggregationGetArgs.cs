// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class AlertPolicyConditionConditionAbsentAggregationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The alignment period for per-time
        /// series alignment. If present,
        /// alignmentPeriod must be at least
        /// 60 seconds. After per-time series
        /// alignment, each time series will
        /// contain data points only on the
        /// period boundaries. If
        /// perSeriesAligner is not specified
        /// or equals ALIGN_NONE, then this
        /// field is ignored. If
        /// perSeriesAligner is specified and
        /// does not equal ALIGN_NONE, then
        /// this field must be defined;
        /// otherwise an error is returned.
        /// </summary>
        [Input("alignmentPeriod")]
        public Input<string>? AlignmentPeriod { get; set; }

        /// <summary>
        /// The approach to be used to combine
        /// time series. Not all reducer
        /// functions may be applied to all
        /// time series, depending on the
        /// metric type and the value type of
        /// the original time series.
        /// Reduction may change the metric
        /// type of value type of the time
        /// series.Time series data must be
        /// aligned in order to perform cross-
        /// time series reduction. If
        /// crossSeriesReducer is specified,
        /// then perSeriesAligner must be
        /// specified and not equal ALIGN_NONE
        /// and alignmentPeriod must be
        /// specified; otherwise, an error is
        /// returned.
        /// </summary>
        [Input("crossSeriesReducer")]
        public Input<string>? CrossSeriesReducer { get; set; }

        [Input("groupByFields")]
        private InputList<string>? _groupByFields;

        /// <summary>
        /// The set of fields to preserve when
        /// crossSeriesReducer is specified.
        /// The groupByFields determine how
        /// the time series are partitioned
        /// into subsets prior to applying the
        /// aggregation function. Each subset
        /// contains time series that have the
        /// same value for each of the
        /// grouping fields. Each individual
        /// time series is a member of exactly
        /// one subset. The crossSeriesReducer
        /// is applied to each subset of time
        /// series. It is not possible to
        /// reduce across different resource
        /// types, so this field implicitly
        /// contains resource.type. Fields not
        /// specified in groupByFields are
        /// aggregated away. If groupByFields
        /// is not specified and all the time
        /// series have the same resource
        /// type, then the time series are
        /// aggregated into a single output
        /// time series. If crossSeriesReducer
        /// is not defined, this field is
        /// ignored.
        /// </summary>
        public InputList<string> GroupByFields
        {
            get => _groupByFields ?? (_groupByFields = new InputList<string>());
            set => _groupByFields = value;
        }

        /// <summary>
        /// The approach to be used to align
        /// individual time series. Not all
        /// alignment functions may be applied
        /// to all time series, depending on
        /// the metric type and value type of
        /// the original time series.
        /// Alignment may change the metric
        /// type or the value type of the time
        /// series.Time series data must be
        /// aligned in order to perform cross-
        /// time series reduction. If
        /// crossSeriesReducer is specified,
        /// then perSeriesAligner must be
        /// specified and not equal ALIGN_NONE
        /// and alignmentPeriod must be
        /// specified; otherwise, an error is
        /// returned.
        /// </summary>
        [Input("perSeriesAligner")]
        public Input<string>? PerSeriesAligner { get; set; }

        public AlertPolicyConditionConditionAbsentAggregationGetArgs()
        {
        }
    }
}