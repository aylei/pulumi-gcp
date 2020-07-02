// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Composer
{
    /// <summary>
    /// An environment for running orchestration tasks.
    /// 
    /// Environments run Apache Airflow software on Google infrastructure.
    /// 
    /// To get more information about Environments, see:
    /// 
    /// * [API documentation](https://cloud.google.com/composer/docs/reference/rest/)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/composer/docs)
    ///     * [Configuring Shared VPC for Composer Environments](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc)
    /// * [Apache Airflow Documentation](http://airflow.apache.org/)
    /// 
    /// &gt; **Warning:** We **STRONGLY** recommend  you read the [GCP guides](https://cloud.google.com/composer/docs/how-to)
    ///   as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure,
    ///   including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
    ///   This provider will not be able to automatically find or manage many of these underlying resources. In particular:
    ///   * It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some
    ///     errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
    ///     error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid
    ///     against GCP Cloud Composer before filing bugs against this provider.
    ///   * **Environments create Google Cloud Storage buckets that do not get cleaned up automatically** on environment
    ///     deletion. [More about Composer's use of Cloud Storage](https://cloud.google.com/composer/docs/concepts/cloud-storage).
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class Environment : Pulumi.CustomResource
    {
        /// <summary>
        /// Configuration parameters for this environment  Structure is documented below.
        /// </summary>
        [Output("config")]
        public Output<Outputs.EnvironmentConfig> Config { get; private set; } = null!;

        /// <summary>
        /// User-defined labels for this environment. The labels map can contain
        /// no more than 64 entries. Entries of the labels map are UTF8 strings
        /// that comply with the following restrictions:
        /// Label keys must be between 1 and 63 characters long and must conform
        /// to the following regular expression: `a-z?`.
        /// Label values must be between 0 and 63 characters long and must
        /// conform to the regular expression `(a-z?)?`.
        /// No more than 64 labels can be associated with a given environment.
        /// Both keys and values must be &lt;= 128 bytes in size.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Name of the environment
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The location or Compute Engine region for the environment.
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;


        /// <summary>
        /// Create a Environment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Environment(string name, EnvironmentArgs? args = null, CustomResourceOptions? options = null)
            : base("gcp:composer/environment:Environment", name, args ?? new EnvironmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Environment(string name, Input<string> id, EnvironmentState? state = null, CustomResourceOptions? options = null)
            : base("gcp:composer/environment:Environment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Environment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Environment Get(string name, Input<string> id, EnvironmentState? state = null, CustomResourceOptions? options = null)
        {
            return new Environment(name, id, state, options);
        }
    }

    public sealed class EnvironmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration parameters for this environment  Structure is documented below.
        /// </summary>
        [Input("config")]
        public Input<Inputs.EnvironmentConfigArgs>? Config { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// User-defined labels for this environment. The labels map can contain
        /// no more than 64 entries. Entries of the labels map are UTF8 strings
        /// that comply with the following restrictions:
        /// Label keys must be between 1 and 63 characters long and must conform
        /// to the following regular expression: `a-z?`.
        /// Label values must be between 0 and 63 characters long and must
        /// conform to the regular expression `(a-z?)?`.
        /// No more than 64 labels can be associated with a given environment.
        /// Both keys and values must be &lt;= 128 bytes in size.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Name of the environment
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The location or Compute Engine region for the environment.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public EnvironmentArgs()
        {
        }
    }

    public sealed class EnvironmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration parameters for this environment  Structure is documented below.
        /// </summary>
        [Input("config")]
        public Input<Inputs.EnvironmentConfigGetArgs>? Config { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// User-defined labels for this environment. The labels map can contain
        /// no more than 64 entries. Entries of the labels map are UTF8 strings
        /// that comply with the following restrictions:
        /// Label keys must be between 1 and 63 characters long and must conform
        /// to the following regular expression: `a-z?`.
        /// Label values must be between 0 and 63 characters long and must
        /// conform to the regular expression `(a-z?)?`.
        /// No more than 64 labels can be associated with a given environment.
        /// Both keys and values must be &lt;= 128 bytes in size.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Name of the environment
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The location or Compute Engine region for the environment.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public EnvironmentState()
        {
        }
    }
}
