// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.CloudAsset
{
    /// <summary>
    /// Describes a Cloud Asset Inventory feed used to to listen to asset updates.
    /// 
    /// To get more information about FolderFeed, see:
    /// 
    /// * [API documentation](https://cloud.google.com/asset-inventory/docs/reference/rest/)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/asset-inventory/docs)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class FolderFeed : Pulumi.CustomResource
    {
        /// <summary>
        /// A list of the full names of the assets to receive updates. You must specify either or both of
        /// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
        /// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
        /// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
        /// </summary>
        [Output("assetNames")]
        public Output<ImmutableArray<string>> AssetNames { get; private set; } = null!;

        /// <summary>
        /// A list of types of the assets to receive updates. You must specify either or both of assetNames
        /// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
        /// the feed. For example: "compute.googleapis.com/Disk"
        /// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
        /// supported asset types.
        /// </summary>
        [Output("assetTypes")]
        public Output<ImmutableArray<string>> AssetTypes { get; private set; } = null!;

        /// <summary>
        /// The project whose identity will be used when sending messages to the
        /// destination pubsub topic. It also specifies the project for API
        /// enablement check, quota, and billing.
        /// </summary>
        [Output("billingProject")]
        public Output<string> BillingProject { get; private set; } = null!;

        /// <summary>
        /// Asset content type. If not specified, no content but the asset name and type will be returned.
        /// Possible values are `CONTENT_TYPE_UNSPECIFIED`, `RESOURCE`, `IAM_POLICY`, `ORG_POLICY`, and `ACCESS_POLICY`.
        /// </summary>
        [Output("contentType")]
        public Output<string?> ContentType { get; private set; } = null!;

        /// <summary>
        /// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
        /// </summary>
        [Output("feedId")]
        public Output<string> FeedId { get; private set; } = null!;

        /// <summary>
        /// Output configuration for asset feed destination.
        /// Structure is documented below.
        /// </summary>
        [Output("feedOutputConfig")]
        public Output<Outputs.FolderFeedFeedOutputConfig> FeedOutputConfig { get; private set; } = null!;

        /// <summary>
        /// The folder this feed should be created in.
        /// </summary>
        [Output("folder")]
        public Output<string> Folder { get; private set; } = null!;

        /// <summary>
        /// The ID of the folder where this feed has been created. Both [FOLDER_NUMBER] and folders/[FOLDER_NUMBER] are accepted.
        /// </summary>
        [Output("folderId")]
        public Output<string> FolderId { get; private set; } = null!;

        /// <summary>
        /// The format will be folders/{folder_number}/feeds/{client-assigned_feed_identifier}.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a FolderFeed resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FolderFeed(string name, FolderFeedArgs args, CustomResourceOptions? options = null)
            : base("gcp:cloudasset/folderFeed:FolderFeed", name, args ?? new FolderFeedArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FolderFeed(string name, Input<string> id, FolderFeedState? state = null, CustomResourceOptions? options = null)
            : base("gcp:cloudasset/folderFeed:FolderFeed", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing FolderFeed resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FolderFeed Get(string name, Input<string> id, FolderFeedState? state = null, CustomResourceOptions? options = null)
        {
            return new FolderFeed(name, id, state, options);
        }
    }

    public sealed class FolderFeedArgs : Pulumi.ResourceArgs
    {
        [Input("assetNames")]
        private InputList<string>? _assetNames;

        /// <summary>
        /// A list of the full names of the assets to receive updates. You must specify either or both of
        /// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
        /// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
        /// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
        /// </summary>
        public InputList<string> AssetNames
        {
            get => _assetNames ?? (_assetNames = new InputList<string>());
            set => _assetNames = value;
        }

        [Input("assetTypes")]
        private InputList<string>? _assetTypes;

        /// <summary>
        /// A list of types of the assets to receive updates. You must specify either or both of assetNames
        /// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
        /// the feed. For example: "compute.googleapis.com/Disk"
        /// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
        /// supported asset types.
        /// </summary>
        public InputList<string> AssetTypes
        {
            get => _assetTypes ?? (_assetTypes = new InputList<string>());
            set => _assetTypes = value;
        }

        /// <summary>
        /// The project whose identity will be used when sending messages to the
        /// destination pubsub topic. It also specifies the project for API
        /// enablement check, quota, and billing.
        /// </summary>
        [Input("billingProject", required: true)]
        public Input<string> BillingProject { get; set; } = null!;

        /// <summary>
        /// Asset content type. If not specified, no content but the asset name and type will be returned.
        /// Possible values are `CONTENT_TYPE_UNSPECIFIED`, `RESOURCE`, `IAM_POLICY`, `ORG_POLICY`, and `ACCESS_POLICY`.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
        /// </summary>
        [Input("feedId", required: true)]
        public Input<string> FeedId { get; set; } = null!;

        /// <summary>
        /// Output configuration for asset feed destination.
        /// Structure is documented below.
        /// </summary>
        [Input("feedOutputConfig", required: true)]
        public Input<Inputs.FolderFeedFeedOutputConfigArgs> FeedOutputConfig { get; set; } = null!;

        /// <summary>
        /// The folder this feed should be created in.
        /// </summary>
        [Input("folder", required: true)]
        public Input<string> Folder { get; set; } = null!;

        public FolderFeedArgs()
        {
        }
    }

    public sealed class FolderFeedState : Pulumi.ResourceArgs
    {
        [Input("assetNames")]
        private InputList<string>? _assetNames;

        /// <summary>
        /// A list of the full names of the assets to receive updates. You must specify either or both of
        /// assetNames and assetTypes. Only asset updates matching specified assetNames and assetTypes are
        /// exported to the feed. For example: //compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1.
        /// See https://cloud.google.com/apis/design/resourceNames#fullResourceName for more info.
        /// </summary>
        public InputList<string> AssetNames
        {
            get => _assetNames ?? (_assetNames = new InputList<string>());
            set => _assetNames = value;
        }

        [Input("assetTypes")]
        private InputList<string>? _assetTypes;

        /// <summary>
        /// A list of types of the assets to receive updates. You must specify either or both of assetNames
        /// and assetTypes. Only asset updates matching specified assetNames and assetTypes are exported to
        /// the feed. For example: "compute.googleapis.com/Disk"
        /// See https://cloud.google.com/asset-inventory/docs/supported-asset-types for a list of all
        /// supported asset types.
        /// </summary>
        public InputList<string> AssetTypes
        {
            get => _assetTypes ?? (_assetTypes = new InputList<string>());
            set => _assetTypes = value;
        }

        /// <summary>
        /// The project whose identity will be used when sending messages to the
        /// destination pubsub topic. It also specifies the project for API
        /// enablement check, quota, and billing.
        /// </summary>
        [Input("billingProject")]
        public Input<string>? BillingProject { get; set; }

        /// <summary>
        /// Asset content type. If not specified, no content but the asset name and type will be returned.
        /// Possible values are `CONTENT_TYPE_UNSPECIFIED`, `RESOURCE`, `IAM_POLICY`, `ORG_POLICY`, and `ACCESS_POLICY`.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// This is the client-assigned asset feed identifier and it needs to be unique under a specific parent.
        /// </summary>
        [Input("feedId")]
        public Input<string>? FeedId { get; set; }

        /// <summary>
        /// Output configuration for asset feed destination.
        /// Structure is documented below.
        /// </summary>
        [Input("feedOutputConfig")]
        public Input<Inputs.FolderFeedFeedOutputConfigGetArgs>? FeedOutputConfig { get; set; }

        /// <summary>
        /// The folder this feed should be created in.
        /// </summary>
        [Input("folder")]
        public Input<string>? Folder { get; set; }

        /// <summary>
        /// The ID of the folder where this feed has been created. Both [FOLDER_NUMBER] and folders/[FOLDER_NUMBER] are accepted.
        /// </summary>
        [Input("folderId")]
        public Input<string>? FolderId { get; set; }

        /// <summary>
        /// The format will be folders/{folder_number}/feeds/{client-assigned_feed_identifier}.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public FolderFeedState()
        {
        }
    }
}
