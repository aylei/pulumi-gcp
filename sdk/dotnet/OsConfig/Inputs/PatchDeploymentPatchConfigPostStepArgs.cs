// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.OsConfig.Inputs
{

    public sealed class PatchDeploymentPatchConfigPostStepArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ExecStepConfig for all Linux VMs targeted by the PatchJob.
        /// Structure is documented below.
        /// </summary>
        [Input("linuxExecStepConfig")]
        public Input<Inputs.PatchDeploymentPatchConfigPostStepLinuxExecStepConfigArgs>? LinuxExecStepConfig { get; set; }

        /// <summary>
        /// The ExecStepConfig for all Windows VMs targeted by the PatchJob.
        /// Structure is documented below.
        /// </summary>
        [Input("windowsExecStepConfig")]
        public Input<Inputs.PatchDeploymentPatchConfigPostStepWindowsExecStepConfigArgs>? WindowsExecStepConfig { get; set; }

        public PatchDeploymentPatchConfigPostStepArgs()
        {
        }
    }
}
