// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class ResourcePolicySnapshotSchedulePolicyScheduleWeeklyScheduleDayOfWeekGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The day of the week to create the snapshot. e.g. MONDAY
        /// Possible values are `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, and `SUNDAY`.
        /// </summary>
        [Input("day", required: true)]
        public Input<string> Day { get; set; } = null!;

        /// <summary>
        /// Time within the window to start the operations.
        /// It must be in format "HH:MM", where HH : [00-23] and MM : [00-00] GMT.
        /// </summary>
        [Input("startTime", required: true)]
        public Input<string> StartTime { get; set; } = null!;

        public ResourcePolicySnapshotSchedulePolicyScheduleWeeklyScheduleDayOfWeekGetArgs()
        {
        }
    }
}
