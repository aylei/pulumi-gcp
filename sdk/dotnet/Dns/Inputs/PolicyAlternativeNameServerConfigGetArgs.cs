// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Dns.Inputs
{

    public sealed class PolicyAlternativeNameServerConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("targetNameServers", required: true)]
        private InputList<Inputs.PolicyAlternativeNameServerConfigTargetNameServerGetArgs>? _targetNameServers;

        /// <summary>
        /// Sets an alternative name server for the associated networks. When specified,
        /// all DNS queries are forwarded to a name server that you choose. Names such as .internal
        /// are not available when an alternative name server is specified.  Structure is documented below.
        /// </summary>
        public InputList<Inputs.PolicyAlternativeNameServerConfigTargetNameServerGetArgs> TargetNameServers
        {
            get => _targetNameServers ?? (_targetNameServers = new InputList<Inputs.PolicyAlternativeNameServerConfigTargetNameServerGetArgs>());
            set => _targetNameServers = value;
        }

        public PolicyAlternativeNameServerConfigGetArgs()
        {
        }
    }
}