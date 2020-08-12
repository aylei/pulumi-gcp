// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Monitoring.Outputs
{

    [OutputType]
    public sealed class UptimeCheckConfigHttpCheck
    {
        /// <summary>
        /// The authentication information. Optional when creating an HTTP check; defaults to empty.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.UptimeCheckConfigHttpCheckAuthInfo? AuthInfo;
        /// <summary>
        /// The request body associated with the HTTP POST request. If contentType is URL_ENCODED, the body passed in must be URL-encoded. Users can provide a Content-Length header via the headers field or the API will do so. If the requestMethod is GET and body is not empty, the API will return an error. The maximum byte size is 1 megabyte. Note - As with all bytes fields JSON representations are base64 encoded. e.g. "foo=bar" in URL-encoded form is "foo%3Dbar" and in base64 encoding is "Zm9vJTI1M0RiYXI=".
        /// </summary>
        public readonly string? Body;
        /// <summary>
        /// The content type to use for the check.
        /// Possible values are `TYPE_UNSPECIFIED` and `URL_ENCODED`.
        /// </summary>
        public readonly string? ContentType;
        /// <summary>
        /// The list of headers to send as part of the uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at https://www.w3.org/Protocols/rfc2616/rfc2616.txt (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Headers;
        /// <summary>
        /// Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to True then the headers will be obscured with ******.
        /// </summary>
        public readonly bool? MaskHeaders;
        /// <summary>
        /// The path to the page to run the check against. Will be combined with the host (specified within the MonitoredResource) and port to construct the full URL. Optional (defaults to "/").
        /// </summary>
        public readonly string? Path;
        /// <summary>
        /// The port to the page to run the check against. Will be combined with host (specified within the MonitoredResource) to construct the full URL.
        /// </summary>
        public readonly int? Port;
        /// <summary>
        /// The HTTP request method to use for the check. If set to METHOD_UNSPECIFIED then requestMethod defaults to GET.
        /// Default value is `GET`.
        /// Possible values are `METHOD_UNSPECIFIED`, `GET`, and `POST`.
        /// </summary>
        public readonly string? RequestMethod;
        /// <summary>
        /// If true, use HTTPS instead of HTTP to run the check.
        /// </summary>
        public readonly bool? UseSsl;
        /// <summary>
        /// Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitoredResource is set to uptime_url. If useSsl is false, setting validateSsl to true has no effect.
        /// </summary>
        public readonly bool? ValidateSsl;

        [OutputConstructor]
        private UptimeCheckConfigHttpCheck(
            Outputs.UptimeCheckConfigHttpCheckAuthInfo? authInfo,

            string? body,

            string? contentType,

            ImmutableDictionary<string, string>? headers,

            bool? maskHeaders,

            string? path,

            int? port,

            string? requestMethod,

            bool? useSsl,

            bool? validateSsl)
        {
            AuthInfo = authInfo;
            Body = body;
            ContentType = contentType;
            Headers = headers;
            MaskHeaders = maskHeaders;
            Path = path;
            Port = port;
            RequestMethod = requestMethod;
            UseSsl = useSsl;
            ValidateSsl = validateSsl;
        }
    }
}
