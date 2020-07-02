// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Diagflow
{
    /// <summary>
    /// Represents an entity type. Entity types serve as a tool for extracting parameter values from natural language queries.
    /// 
    /// To get more information about EntityType, see:
    /// 
    /// * [API documentation](https://cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.entityTypes)
    /// * How-to Guides
    ///     * [Official Documentation](https://cloud.google.com/dialogflow/docs/)
    /// 
    /// ## Example Usage
    /// </summary>
    public partial class EntityType : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of this entity type to be displayed on the console.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Enables fuzzy entity extraction during classification.
        /// </summary>
        [Output("enableFuzzyExtraction")]
        public Output<bool?> EnableFuzzyExtraction { get; private set; } = null!;

        /// <summary>
        /// The collection of entity entries associated with the entity type.  Structure is documented below.
        /// </summary>
        [Output("entities")]
        public Output<ImmutableArray<Outputs.EntityTypeEntity>> Entities { get; private set; } = null!;

        /// <summary>
        /// Indicates the kind of entity type.
        /// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
        /// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
        /// types can contain references to other entity types (with or without aliases).
        /// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
        /// </summary>
        [Output("kind")]
        public Output<string> Kind { get; private set; } = null!;

        /// <summary>
        /// The unique identifier of the entity type. Format: projects/&lt;Project ID&gt;/agent/entityTypes/&lt;Entity type ID&gt;.
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
        /// Create a EntityType resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EntityType(string name, EntityTypeArgs args, CustomResourceOptions? options = null)
            : base("gcp:diagflow/entityType:EntityType", name, args ?? new EntityTypeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EntityType(string name, Input<string> id, EntityTypeState? state = null, CustomResourceOptions? options = null)
            : base("gcp:diagflow/entityType:EntityType", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing EntityType resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EntityType Get(string name, Input<string> id, EntityTypeState? state = null, CustomResourceOptions? options = null)
        {
            return new EntityType(name, id, state, options);
        }
    }

    public sealed class EntityTypeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of this entity type to be displayed on the console.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// Enables fuzzy entity extraction during classification.
        /// </summary>
        [Input("enableFuzzyExtraction")]
        public Input<bool>? EnableFuzzyExtraction { get; set; }

        [Input("entities")]
        private InputList<Inputs.EntityTypeEntityArgs>? _entities;

        /// <summary>
        /// The collection of entity entries associated with the entity type.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.EntityTypeEntityArgs> Entities
        {
            get => _entities ?? (_entities = new InputList<Inputs.EntityTypeEntityArgs>());
            set => _entities = value;
        }

        /// <summary>
        /// Indicates the kind of entity type.
        /// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
        /// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
        /// types can contain references to other entity types (with or without aliases).
        /// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
        /// </summary>
        [Input("kind", required: true)]
        public Input<string> Kind { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public EntityTypeArgs()
        {
        }
    }

    public sealed class EntityTypeState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of this entity type to be displayed on the console.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Enables fuzzy entity extraction during classification.
        /// </summary>
        [Input("enableFuzzyExtraction")]
        public Input<bool>? EnableFuzzyExtraction { get; set; }

        [Input("entities")]
        private InputList<Inputs.EntityTypeEntityGetArgs>? _entities;

        /// <summary>
        /// The collection of entity entries associated with the entity type.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.EntityTypeEntityGetArgs> Entities
        {
            get => _entities ?? (_entities = new InputList<Inputs.EntityTypeEntityGetArgs>());
            set => _entities = value;
        }

        /// <summary>
        /// Indicates the kind of entity type.
        /// * KIND_MAP: Map entity types allow mapping of a group of synonyms to a reference value.
        /// * KIND_LIST: List entity types contain a set of entries that do not map to reference values. However, list entity
        /// types can contain references to other entity types (with or without aliases).
        /// * KIND_REGEXP: Regexp entity types allow to specify regular expressions in entries values.
        /// </summary>
        [Input("kind")]
        public Input<string>? Kind { get; set; }

        /// <summary>
        /// The unique identifier of the entity type. Format: projects/&lt;Project ID&gt;/agent/entityTypes/&lt;Entity type ID&gt;.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public EntityTypeState()
        {
        }
    }
}
