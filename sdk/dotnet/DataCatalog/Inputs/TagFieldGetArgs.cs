// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.DataCatalog.Inputs
{

    public sealed class TagFieldGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Holds the value for a tag field with boolean type.
        /// </summary>
        [Input("boolValue")]
        public Input<bool>? BoolValue { get; set; }

        /// <summary>
        /// -
        /// The display name of this field
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Holds the value for a tag field with double type.
        /// </summary>
        [Input("doubleValue")]
        public Input<double>? DoubleValue { get; set; }

        /// <summary>
        /// Holds the value for a tag field with enum type. This value must be one of the allowed values in the definition of this enum.
        /// Structure is documented below.
        /// </summary>
        [Input("enumValue")]
        public Input<string>? EnumValue { get; set; }

        /// <summary>
        /// The identifier for this object. Format specified above.
        /// </summary>
        [Input("fieldName", required: true)]
        public Input<string> FieldName { get; set; } = null!;

        /// <summary>
        /// -
        /// The order of this field with respect to other fields in this tag. For example, a higher value can indicate
        /// a more important field. The value can be negative. Multiple fields can have the same order, and field orders
        /// within a tag do not have to be sequential.
        /// </summary>
        [Input("order")]
        public Input<int>? Order { get; set; }

        /// <summary>
        /// Holds the value for a tag field with string type.
        /// </summary>
        [Input("stringValue")]
        public Input<string>? StringValue { get; set; }

        /// <summary>
        /// Holds the value for a tag field with timestamp type.
        /// </summary>
        [Input("timestampValue")]
        public Input<string>? TimestampValue { get; set; }

        public TagFieldGetArgs()
        {
        }
    }
}
