// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.BigQuery.Inputs
{

    public sealed class ConnectionCloudSqlCredentialGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Password for database.
        /// **Note**: This property is sensitive and will not be displayed in the plan.
        /// </summary>
        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        /// <summary>
        /// Username for database.
        /// </summary>
        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public ConnectionCloudSqlCredentialGetArgs()
        {
        }
    }
}
