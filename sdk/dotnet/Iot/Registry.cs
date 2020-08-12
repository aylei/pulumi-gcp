// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Iot
{
    /// <summary>
    /// A Google Cloud IoT Core device registry.
    /// 
    /// To get more information about DeviceRegistry, see:
    /// 
    /// * [API documentation](https://cloud.google.com/iot/docs/reference/cloudiot/rest/)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/iot/docs/)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class Registry : Pulumi.CustomResource
    {
        /// <summary>
        /// List of public key certificates to authenticate devices.
        /// The structure is documented below.
        /// </summary>
        [Output("credentials")]
        public Output<ImmutableArray<Outputs.RegistryCredential>> Credentials { get; private set; } = null!;

        /// <summary>
        /// List of configurations for event notifications, such as PubSub topics
        /// to publish device events to.
        /// Structure is documented below.
        /// </summary>
        [Output("eventNotificationConfigs")]
        public Output<ImmutableArray<Outputs.RegistryEventNotificationConfigItem>> EventNotificationConfigs { get; private set; } = null!;

        /// <summary>
        /// Activate or deactivate HTTP.
        /// The structure is documented below.
        /// </summary>
        [Output("httpConfig")]
        public Output<Outputs.RegistryHttpConfig> HttpConfig { get; private set; } = null!;

        /// <summary>
        /// The default logging verbosity for activity from devices in this
        /// registry. Specifies which events should be written to logs. For
        /// example, if the LogLevel is ERROR, only events that terminate in
        /// errors will be logged. LogLevel is inclusive; enabling INFO logging
        /// will also enable ERROR logging.
        /// Default value is `NONE`.
        /// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
        /// </summary>
        [Output("logLevel")]
        public Output<string?> LogLevel { get; private set; } = null!;

        /// <summary>
        /// Activate or deactivate MQTT.
        /// The structure is documented below.
        /// </summary>
        [Output("mqttConfig")]
        public Output<Outputs.RegistryMqttConfig> MqttConfig { get; private set; } = null!;

        /// <summary>
        /// A unique name for the resource, required by device registry.
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
        /// The region in which the created registry should reside.
        /// If it is not provided, the provider region is used.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// A PubSub topic to publish device state updates.
        /// The structure is documented below.
        /// </summary>
        [Output("stateNotificationConfig")]
        public Output<Outputs.RegistryStateNotificationConfig?> StateNotificationConfig { get; private set; } = null!;


        /// <summary>
        /// Create a Registry resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Registry(string name, RegistryArgs? args = null, CustomResourceOptions? options = null)
            : base("gcp:iot/registry:Registry", name, args ?? new RegistryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Registry(string name, Input<string> id, RegistryState? state = null, CustomResourceOptions? options = null)
            : base("gcp:iot/registry:Registry", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                Aliases =
                {
                    new Alias { Type = "gcp:kms/registry:Registry"},
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Registry resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Registry Get(string name, Input<string> id, RegistryState? state = null, CustomResourceOptions? options = null)
        {
            return new Registry(name, id, state, options);
        }
    }

    public sealed class RegistryArgs : Pulumi.ResourceArgs
    {
        [Input("credentials")]
        private InputList<Inputs.RegistryCredentialArgs>? _credentials;

        /// <summary>
        /// List of public key certificates to authenticate devices.
        /// The structure is documented below.
        /// </summary>
        public InputList<Inputs.RegistryCredentialArgs> Credentials
        {
            get => _credentials ?? (_credentials = new InputList<Inputs.RegistryCredentialArgs>());
            set => _credentials = value;
        }

        [Input("eventNotificationConfigs")]
        private InputList<Inputs.RegistryEventNotificationConfigItemArgs>? _eventNotificationConfigs;

        /// <summary>
        /// List of configurations for event notifications, such as PubSub topics
        /// to publish device events to.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.RegistryEventNotificationConfigItemArgs> EventNotificationConfigs
        {
            get => _eventNotificationConfigs ?? (_eventNotificationConfigs = new InputList<Inputs.RegistryEventNotificationConfigItemArgs>());
            set => _eventNotificationConfigs = value;
        }

        /// <summary>
        /// Activate or deactivate HTTP.
        /// The structure is documented below.
        /// </summary>
        [Input("httpConfig")]
        public Input<Inputs.RegistryHttpConfigArgs>? HttpConfig { get; set; }

        /// <summary>
        /// The default logging verbosity for activity from devices in this
        /// registry. Specifies which events should be written to logs. For
        /// example, if the LogLevel is ERROR, only events that terminate in
        /// errors will be logged. LogLevel is inclusive; enabling INFO logging
        /// will also enable ERROR logging.
        /// Default value is `NONE`.
        /// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
        /// </summary>
        [Input("logLevel")]
        public Input<string>? LogLevel { get; set; }

        /// <summary>
        /// Activate or deactivate MQTT.
        /// The structure is documented below.
        /// </summary>
        [Input("mqttConfig")]
        public Input<Inputs.RegistryMqttConfigArgs>? MqttConfig { get; set; }

        /// <summary>
        /// A unique name for the resource, required by device registry.
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
        /// The region in which the created registry should reside.
        /// If it is not provided, the provider region is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// A PubSub topic to publish device state updates.
        /// The structure is documented below.
        /// </summary>
        [Input("stateNotificationConfig")]
        public Input<Inputs.RegistryStateNotificationConfigArgs>? StateNotificationConfig { get; set; }

        public RegistryArgs()
        {
        }
    }

    public sealed class RegistryState : Pulumi.ResourceArgs
    {
        [Input("credentials")]
        private InputList<Inputs.RegistryCredentialGetArgs>? _credentials;

        /// <summary>
        /// List of public key certificates to authenticate devices.
        /// The structure is documented below.
        /// </summary>
        public InputList<Inputs.RegistryCredentialGetArgs> Credentials
        {
            get => _credentials ?? (_credentials = new InputList<Inputs.RegistryCredentialGetArgs>());
            set => _credentials = value;
        }

        [Input("eventNotificationConfigs")]
        private InputList<Inputs.RegistryEventNotificationConfigItemGetArgs>? _eventNotificationConfigs;

        /// <summary>
        /// List of configurations for event notifications, such as PubSub topics
        /// to publish device events to.
        /// Structure is documented below.
        /// </summary>
        public InputList<Inputs.RegistryEventNotificationConfigItemGetArgs> EventNotificationConfigs
        {
            get => _eventNotificationConfigs ?? (_eventNotificationConfigs = new InputList<Inputs.RegistryEventNotificationConfigItemGetArgs>());
            set => _eventNotificationConfigs = value;
        }

        /// <summary>
        /// Activate or deactivate HTTP.
        /// The structure is documented below.
        /// </summary>
        [Input("httpConfig")]
        public Input<Inputs.RegistryHttpConfigGetArgs>? HttpConfig { get; set; }

        /// <summary>
        /// The default logging verbosity for activity from devices in this
        /// registry. Specifies which events should be written to logs. For
        /// example, if the LogLevel is ERROR, only events that terminate in
        /// errors will be logged. LogLevel is inclusive; enabling INFO logging
        /// will also enable ERROR logging.
        /// Default value is `NONE`.
        /// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
        /// </summary>
        [Input("logLevel")]
        public Input<string>? LogLevel { get; set; }

        /// <summary>
        /// Activate or deactivate MQTT.
        /// The structure is documented below.
        /// </summary>
        [Input("mqttConfig")]
        public Input<Inputs.RegistryMqttConfigGetArgs>? MqttConfig { get; set; }

        /// <summary>
        /// A unique name for the resource, required by device registry.
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
        /// The region in which the created registry should reside.
        /// If it is not provided, the provider region is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// A PubSub topic to publish device state updates.
        /// The structure is documented below.
        /// </summary>
        [Input("stateNotificationConfig")]
        public Input<Inputs.RegistryStateNotificationConfigGetArgs>? StateNotificationConfig { get; set; }

        public RegistryState()
        {
        }
    }
}
