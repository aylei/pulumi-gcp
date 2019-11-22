// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Healthcare
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/healthcare_fhir_store.html.markdown.
    /// </summary>
    public partial class FhirStore : Pulumi.CustomResource
    {
        /// <summary>
        /// Identifies the dataset addressed by this request. Must be in the format
        /// 'projects/{project}/locations/{location}/datasets/{dataset}'
        /// </summary>
        [Output("dataset")]
        public Output<string> Dataset { get; private set; } = null!;

        /// <summary>
        /// Whether to disable referential integrity in this FHIR store. This field is immutable after FHIR store
        /// creation. The default value is false, meaning that the API will enforce referential integrity and fail the
        /// requests that will result in inconsistent state in the FHIR store. When this field is set to true, the API
        /// will skip referential integrity check. Consequently, operations that rely on references, such as
        /// Patient.get$everything, will not return all the results if broken references exist. ** Changing this
        /// property may recreate the FHIR store (removing all data) **
        /// </summary>
        [Output("disableReferentialIntegrity")]
        public Output<bool?> DisableReferentialIntegrity { get; private set; } = null!;

        /// <summary>
        /// Whether to disable resource versioning for this FHIR store. This field can not be changed after the creation
        /// of FHIR store. If set to false, which is the default behavior, all write operations will cause historical
        /// versions to be recorded automatically. The historical versions can be fetched through the history APIs, but
        /// cannot be updated. If set to true, no historical versions will be kept. The server will send back errors for
        /// attempts to read the historical versions. ** Changing this property may recreate the FHIR store (removing
        /// all data) **
        /// </summary>
        [Output("disableResourceVersioning")]
        public Output<bool?> DisableResourceVersioning { get; private set; } = null!;

        /// <summary>
        /// Whether to allow the bulk import API to accept history bundles and directly insert historical resource
        /// versions into the FHIR store. Importing resource histories creates resource interactions that appear to have
        /// occurred in the past, which clients may not want to allow. If set to false, history bundles within an import
        /// will fail with an error. ** Changing this property may recreate the FHIR store (removing all data) ** **
        /// This property can be changed manually in the Google Cloud Healthcare admin console without recreating the
        /// FHIR store **
        /// </summary>
        [Output("enableHistoryImport")]
        public Output<bool?> EnableHistoryImport { get; private set; } = null!;

        /// <summary>
        /// Whether this FHIR store has the updateCreate capability. This determines if the client can use an Update
        /// operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through
        /// the Create operation and attempts to Update a non-existent resource will return errors. Please treat the
        /// audit logs with appropriate levels of care if client-specified resource IDs contain sensitive data such as
        /// patient identifiers, those IDs will be part of the FHIR resource path recorded in Cloud audit logs and Cloud
        /// Pub/Sub notifications.
        /// </summary>
        [Output("enableUpdateCreate")]
        public Output<bool?> EnableUpdateCreate { get; private set; } = null!;

        /// <summary>
        /// User-supplied key-value pairs used to organize FHIR stores. Label keys must be between 1 and 63 characters
        /// long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
        /// [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters
        /// long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
        /// [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object
        /// containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// The resource name for the FhirStore. ** Changing this property may recreate the FHIR store (removing all
        /// data) **
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// A nested object resource
        /// </summary>
        [Output("notificationConfig")]
        public Output<Outputs.FhirStoreNotificationConfig?> NotificationConfig { get; private set; } = null!;

        /// <summary>
        /// The fully qualified name of this dataset
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;


        /// <summary>
        /// Create a FhirStore resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FhirStore(string name, FhirStoreArgs args, CustomResourceOptions? options = null)
            : base("gcp:healthcare/fhirStore:FhirStore", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private FhirStore(string name, Input<string> id, FhirStoreState? state = null, CustomResourceOptions? options = null)
            : base("gcp:healthcare/fhirStore:FhirStore", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing FhirStore resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FhirStore Get(string name, Input<string> id, FhirStoreState? state = null, CustomResourceOptions? options = null)
        {
            return new FhirStore(name, id, state, options);
        }
    }

    public sealed class FhirStoreArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Identifies the dataset addressed by this request. Must be in the format
        /// 'projects/{project}/locations/{location}/datasets/{dataset}'
        /// </summary>
        [Input("dataset", required: true)]
        public Input<string> Dataset { get; set; } = null!;

        /// <summary>
        /// Whether to disable referential integrity in this FHIR store. This field is immutable after FHIR store
        /// creation. The default value is false, meaning that the API will enforce referential integrity and fail the
        /// requests that will result in inconsistent state in the FHIR store. When this field is set to true, the API
        /// will skip referential integrity check. Consequently, operations that rely on references, such as
        /// Patient.get$everything, will not return all the results if broken references exist. ** Changing this
        /// property may recreate the FHIR store (removing all data) **
        /// </summary>
        [Input("disableReferentialIntegrity")]
        public Input<bool>? DisableReferentialIntegrity { get; set; }

        /// <summary>
        /// Whether to disable resource versioning for this FHIR store. This field can not be changed after the creation
        /// of FHIR store. If set to false, which is the default behavior, all write operations will cause historical
        /// versions to be recorded automatically. The historical versions can be fetched through the history APIs, but
        /// cannot be updated. If set to true, no historical versions will be kept. The server will send back errors for
        /// attempts to read the historical versions. ** Changing this property may recreate the FHIR store (removing
        /// all data) **
        /// </summary>
        [Input("disableResourceVersioning")]
        public Input<bool>? DisableResourceVersioning { get; set; }

        /// <summary>
        /// Whether to allow the bulk import API to accept history bundles and directly insert historical resource
        /// versions into the FHIR store. Importing resource histories creates resource interactions that appear to have
        /// occurred in the past, which clients may not want to allow. If set to false, history bundles within an import
        /// will fail with an error. ** Changing this property may recreate the FHIR store (removing all data) ** **
        /// This property can be changed manually in the Google Cloud Healthcare admin console without recreating the
        /// FHIR store **
        /// </summary>
        [Input("enableHistoryImport")]
        public Input<bool>? EnableHistoryImport { get; set; }

        /// <summary>
        /// Whether this FHIR store has the updateCreate capability. This determines if the client can use an Update
        /// operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through
        /// the Create operation and attempts to Update a non-existent resource will return errors. Please treat the
        /// audit logs with appropriate levels of care if client-specified resource IDs contain sensitive data such as
        /// patient identifiers, those IDs will be part of the FHIR resource path recorded in Cloud audit logs and Cloud
        /// Pub/Sub notifications.
        /// </summary>
        [Input("enableUpdateCreate")]
        public Input<bool>? EnableUpdateCreate { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// User-supplied key-value pairs used to organize FHIR stores. Label keys must be between 1 and 63 characters
        /// long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
        /// [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters
        /// long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
        /// [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object
        /// containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The resource name for the FhirStore. ** Changing this property may recreate the FHIR store (removing all
        /// data) **
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// A nested object resource
        /// </summary>
        [Input("notificationConfig")]
        public Input<Inputs.FhirStoreNotificationConfigArgs>? NotificationConfig { get; set; }

        public FhirStoreArgs()
        {
        }
    }

    public sealed class FhirStoreState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Identifies the dataset addressed by this request. Must be in the format
        /// 'projects/{project}/locations/{location}/datasets/{dataset}'
        /// </summary>
        [Input("dataset")]
        public Input<string>? Dataset { get; set; }

        /// <summary>
        /// Whether to disable referential integrity in this FHIR store. This field is immutable after FHIR store
        /// creation. The default value is false, meaning that the API will enforce referential integrity and fail the
        /// requests that will result in inconsistent state in the FHIR store. When this field is set to true, the API
        /// will skip referential integrity check. Consequently, operations that rely on references, such as
        /// Patient.get$everything, will not return all the results if broken references exist. ** Changing this
        /// property may recreate the FHIR store (removing all data) **
        /// </summary>
        [Input("disableReferentialIntegrity")]
        public Input<bool>? DisableReferentialIntegrity { get; set; }

        /// <summary>
        /// Whether to disable resource versioning for this FHIR store. This field can not be changed after the creation
        /// of FHIR store. If set to false, which is the default behavior, all write operations will cause historical
        /// versions to be recorded automatically. The historical versions can be fetched through the history APIs, but
        /// cannot be updated. If set to true, no historical versions will be kept. The server will send back errors for
        /// attempts to read the historical versions. ** Changing this property may recreate the FHIR store (removing
        /// all data) **
        /// </summary>
        [Input("disableResourceVersioning")]
        public Input<bool>? DisableResourceVersioning { get; set; }

        /// <summary>
        /// Whether to allow the bulk import API to accept history bundles and directly insert historical resource
        /// versions into the FHIR store. Importing resource histories creates resource interactions that appear to have
        /// occurred in the past, which clients may not want to allow. If set to false, history bundles within an import
        /// will fail with an error. ** Changing this property may recreate the FHIR store (removing all data) ** **
        /// This property can be changed manually in the Google Cloud Healthcare admin console without recreating the
        /// FHIR store **
        /// </summary>
        [Input("enableHistoryImport")]
        public Input<bool>? EnableHistoryImport { get; set; }

        /// <summary>
        /// Whether this FHIR store has the updateCreate capability. This determines if the client can use an Update
        /// operation to create a new resource with a client-specified ID. If false, all IDs are server-assigned through
        /// the Create operation and attempts to Update a non-existent resource will return errors. Please treat the
        /// audit logs with appropriate levels of care if client-specified resource IDs contain sensitive data such as
        /// patient identifiers, those IDs will be part of the FHIR resource path recorded in Cloud audit logs and Cloud
        /// Pub/Sub notifications.
        /// </summary>
        [Input("enableUpdateCreate")]
        public Input<bool>? EnableUpdateCreate { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// User-supplied key-value pairs used to organize FHIR stores. Label keys must be between 1 and 63 characters
        /// long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
        /// [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters
        /// long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
        /// [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object
        /// containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The resource name for the FhirStore. ** Changing this property may recreate the FHIR store (removing all
        /// data) **
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// A nested object resource
        /// </summary>
        [Input("notificationConfig")]
        public Input<Inputs.FhirStoreNotificationConfigGetArgs>? NotificationConfig { get; set; }

        /// <summary>
        /// The fully qualified name of this dataset
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        public FhirStoreState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class FhirStoreNotificationConfigArgs : Pulumi.ResourceArgs
    {
        [Input("pubsubTopic", required: true)]
        public Input<string> PubsubTopic { get; set; } = null!;

        public FhirStoreNotificationConfigArgs()
        {
        }
    }

    public sealed class FhirStoreNotificationConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("pubsubTopic", required: true)]
        public Input<string> PubsubTopic { get; set; } = null!;

        public FhirStoreNotificationConfigGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class FhirStoreNotificationConfig
    {
        public readonly string PubsubTopic;

        [OutputConstructor]
        private FhirStoreNotificationConfig(string pubsubTopic)
        {
            PubsubTopic = pubsubTopic;
        }
    }
    }
}