// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.OsConfig.Inputs
{

    public sealed class GuestPoliciesRecipeInstallStepArchiveExtractionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the relevant artifact in the recipe.
        /// </summary>
        [Input("artifactId", required: true)]
        public Input<string> ArtifactId { get; set; } = null!;

        /// <summary>
        /// Directory to extract archive to. Defaults to / on Linux or C:\ on Windows.
        /// </summary>
        [Input("destination")]
        public Input<string>? Destination { get; set; }

        /// <summary>
        /// The type of the archive to extract.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public GuestPoliciesRecipeInstallStepArchiveExtractionArgs()
        {
        }
    }
}