// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class ResourcePolicySnapshotSchedulePolicyScheduleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The policy will execute every nth day at the specified time.
        /// Structure is documented below.
        /// </summary>
        [Input("dailySchedule")]
        public Input<Inputs.ResourcePolicySnapshotSchedulePolicyScheduleDailyScheduleArgs>? DailySchedule { get; set; }

        /// <summary>
        /// The policy will execute every nth hour starting at the specified time.
        /// Structure is documented below.
        /// </summary>
        [Input("hourlySchedule")]
        public Input<Inputs.ResourcePolicySnapshotSchedulePolicyScheduleHourlyScheduleArgs>? HourlySchedule { get; set; }

        /// <summary>
        /// Allows specifying a snapshot time for each day of the week.
        /// Structure is documented below.
        /// </summary>
        [Input("weeklySchedule")]
        public Input<Inputs.ResourcePolicySnapshotSchedulePolicyScheduleWeeklyScheduleArgs>? WeeklySchedule { get; set; }

        public ResourcePolicySnapshotSchedulePolicyScheduleArgs()
        {
        }
    }
}
