// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Storage.Outputs
{

    [OutputType]
    public sealed class TransferJobTransferSpecAwsS3DataSource
    {
        /// <summary>
        /// AWS credentials block.
        /// </summary>
        public readonly Outputs.TransferJobTransferSpecAwsS3DataSourceAwsAccessKey AwsAccessKey;
        /// <summary>
        /// S3 Bucket name.
        /// </summary>
        public readonly string BucketName;

        [OutputConstructor]
        private TransferJobTransferSpecAwsS3DataSource(
            Outputs.TransferJobTransferSpecAwsS3DataSourceAwsAccessKey awsAccessKey,

            string bucketName)
        {
            AwsAccessKey = awsAccessKey;
            BucketName = bucketName;
        }
    }
}
