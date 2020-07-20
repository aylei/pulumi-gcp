// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.BigQuery.Outputs
{

    [OutputType]
    public sealed class TableExternalDataConfiguration
    {
        /// <summary>
        /// - Let BigQuery try to autodetect the schema
        /// and format of the table.
        /// </summary>
        public readonly bool Autodetect;
        /// <summary>
        /// The compression type of the data source.
        /// Valid values are "NONE" or "GZIP".
        /// </summary>
        public readonly string? Compression;
        /// <summary>
        /// Additional properties to set if
        /// `source_format` is set to "CSV". Structure is documented below.
        /// </summary>
        public readonly Outputs.TableExternalDataConfigurationCsvOptions? CsvOptions;
        /// <summary>
        /// Additional options if
        /// `source_format` is set to "GOOGLE_SHEETS". Structure is
        /// documented below.
        /// </summary>
        public readonly Outputs.TableExternalDataConfigurationGoogleSheetsOptions? GoogleSheetsOptions;
        /// <summary>
        /// When set, configures hive partitioning
        /// support. Not all storage formats support hive partitioning -- requesting hive
        /// partitioning on an unsupported format will lead to an error, as will providing
        /// an invalid specification.
        /// </summary>
        public readonly Outputs.TableExternalDataConfigurationHivePartitioningOptions? HivePartitioningOptions;
        /// <summary>
        /// Indicates if BigQuery should
        /// allow extra values that are not represented in the table schema.
        /// If true, the extra values are ignored. If false, records with
        /// extra columns are treated as bad records, and if there are too
        /// many bad records, an invalid error is returned in the job result.
        /// The default value is false.
        /// </summary>
        public readonly bool? IgnoreUnknownValues;
        /// <summary>
        /// The maximum number of bad records that
        /// BigQuery can ignore when reading data.
        /// </summary>
        public readonly int? MaxBadRecords;
        /// <summary>
        /// A JSON schema for the external table. Schema is required
        /// for CSV and JSON formats if autodetect is not on. Schema is disallowed
        /// for Google Cloud Bigtable, Cloud Datastore backups, Avro, ORC and Parquet formats.
        /// ~&gt;**NOTE**: Because this field expects a JSON string, any changes to the
        /// string will create a diff, even if the JSON itself hasn't changed.
        /// Furthermore drift for this field cannot not be detected because BigQuery
        /// only uses this schema to compute the effective schema for the table, therefore
        /// any changes on the configured value will force the table to be recreated.
        /// This schema is effectively only applied when creating a table from an external
        /// datasource, after creation the computed schema will be stored in
        /// `google_bigquery_table.schema`
        /// </summary>
        public readonly string? Schema;
        /// <summary>
        /// The data format. Supported values are:
        /// "CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET",
        /// and "DATSTORE_BACKUP". To use "GOOGLE_SHEETS"
        /// the `scopes` must include
        /// "https://www.googleapis.com/auth/drive.readonly".
        /// </summary>
        public readonly string SourceFormat;
        /// <summary>
        /// A list of the fully-qualified URIs that point to
        /// your data in Google Cloud.
        /// </summary>
        public readonly ImmutableArray<string> SourceUris;

        [OutputConstructor]
        private TableExternalDataConfiguration(
            bool autodetect,

            string? compression,

            Outputs.TableExternalDataConfigurationCsvOptions? csvOptions,

            Outputs.TableExternalDataConfigurationGoogleSheetsOptions? googleSheetsOptions,

            Outputs.TableExternalDataConfigurationHivePartitioningOptions? hivePartitioningOptions,

            bool? ignoreUnknownValues,

            int? maxBadRecords,

            string? schema,

            string sourceFormat,

            ImmutableArray<string> sourceUris)
        {
            Autodetect = autodetect;
            Compression = compression;
            CsvOptions = csvOptions;
            GoogleSheetsOptions = googleSheetsOptions;
            HivePartitioningOptions = hivePartitioningOptions;
            IgnoreUnknownValues = ignoreUnknownValues;
            MaxBadRecords = maxBadRecords;
            Schema = schema;
            SourceFormat = sourceFormat;
            SourceUris = sourceUris;
        }
    }
}
