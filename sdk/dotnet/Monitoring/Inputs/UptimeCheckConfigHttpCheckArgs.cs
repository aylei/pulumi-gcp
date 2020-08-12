// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Inputs
{

    public sealed class UptimeCheckConfigHttpCheckArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The authentication information. Optional when creating an HTTP check; defaults to empty.
        /// Structure is documented below.
        /// </summary>
        [Input("authInfo")]
        public Input<Inputs.UptimeCheckConfigHttpCheckAuthInfoArgs>? AuthInfo { get; set; }

        /// <summary>
        /// The request body associated with the HTTP POST request. If contentType is URL_ENCODED, the body passed in must be URL-encoded. Users can provide a Content-Length header via the headers field or the API will do so. If the requestMethod is GET and body is not empty, the API will return an error. The maximum byte size is 1 megabyte. Note - As with all bytes fields JSON representations are base64 encoded. e.g. "foo=bar" in URL-encoded form is "foo%3Dbar" and in base64 encoding is "Zm9vJTI1M0RiYXI=".
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        /// <summary>
        /// The content type to use for the check.
        /// Possible values are `TYPE_UNSPECIFIED` and `URL_ENCODED`.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        [Input("headers")]
        private InputMap<string>? _headers;

        /// <summary>
        /// The list of headers to send as part of the uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at https://www.w3.org/Protocols/rfc2616/rfc2616.txt (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.
        /// </summary>
        public InputMap<string> Headers
        {
            get => _headers ?? (_headers = new InputMap<string>());
            set => _headers = value;
        }

        /// <summary>
        /// Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with ******.
        /// </summary>
        [Input("maskHeaders")]
        public Input<bool>? MaskHeaders { get; set; }

        /// <summary>
        /// The path to the page to run the check against. Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. Optional (defaults to "/").
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The HTTP request method to use for the check. If set to METHOD_UNSPECIFIED then requestMethod defaults to GET.
        /// Default value is `GET`.
        /// Possible values are `METHOD_UNSPECIFIED`, `GET`, and `POST`.
        /// </summary>
        [Input("requestMethod")]
        public Input<string>? RequestMethod { get; set; }

        /// <summary>
        /// If true, use HTTPS instead of HTTP to run the check.
        /// </summary>
        [Input("useSsl")]
        public Input<bool>? UseSsl { get; set; }

        /// <summary>
        /// Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect.
        /// </summary>
        [Input("validateSsl")]
        public Input<bool>? ValidateSsl { get; set; }

        public UptimeCheckConfigHttpCheckArgs()
        {
        }
    }
}
