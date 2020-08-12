// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Outputs
{

    [OutputType]
    public sealed class URLMapPathMatcherRouteRule
    {
        /// <summary>
        /// Specifies changes to request and response headers that need to take effect for
        /// the selected backendService.
        /// headerAction specified here take effect before headerAction in the enclosing
        /// HttpRouteRule, PathMatcher and UrlMap.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.URLMapPathMatcherRouteRuleHeaderAction? HeaderAction;
        /// <summary>
        /// The rules for determining a match.
        /// Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.URLMapPathMatcherRouteRuleMatchRule> MatchRules;
        /// <summary>
        /// For routeRules within a given pathMatcher, priority determines the order
        /// in which load balancer will interpret routeRules. RouteRules are evaluated
        /// in order of priority, from the lowest to highest number. The priority of
        /// a rule decreases as its number increases (1, 2, 3, N+1). The first rule
        /// that matches the request is applied.
        /// You cannot configure two or more routeRules with the same priority.
        /// Priority for each rule must be set to a number between 0 and
        /// 2147483647 inclusive.
        /// Priority numbers can have gaps, which enable you to add or remove rules
        /// in the future without affecting the rest of the rules. For example,
        /// 1, 2, 3, 4, 5, 9, 12, 16 is a valid series of priority numbers to which
        /// you could add rules numbered from 6 to 8, 10 to 11, and 13 to 15 in the
        /// future without any impact on existing rules.
        /// </summary>
        public readonly int Priority;
        /// <summary>
        /// In response to a matching matchRule, the load balancer performs advanced routing
        /// actions like URL rewrites, header transformations, etc. prior to forwarding the
        /// request to the selected backend. If  routeAction specifies any
        /// weightedBackendServices, service must not be set. Conversely if service is set,
        /// routeAction cannot contain any  weightedBackendServices. Only one of routeAction
        /// or urlRedirect must be set.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.URLMapPathMatcherRouteRuleRouteAction? RouteAction;
        /// <summary>
        /// The backend service or backend bucket link that should be matched by this test.
        /// </summary>
        public readonly string? Service;
        /// <summary>
        /// When this rule is matched, the request is redirected to a URL specified by
        /// urlRedirect. If urlRedirect is specified, service or routeAction must not be
        /// set.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.URLMapPathMatcherRouteRuleUrlRedirect? UrlRedirect;

        [OutputConstructor]
        private URLMapPathMatcherRouteRule(
            Outputs.URLMapPathMatcherRouteRuleHeaderAction? headerAction,

            ImmutableArray<Outputs.URLMapPathMatcherRouteRuleMatchRule> matchRules,

            int priority,

            Outputs.URLMapPathMatcherRouteRuleRouteAction? routeAction,

            string? service,

            Outputs.URLMapPathMatcherRouteRuleUrlRedirect? urlRedirect)
        {
            HeaderAction = headerAction;
            MatchRules = matchRules;
            Priority = priority;
            RouteAction = routeAction;
            Service = service;
            UrlRedirect = urlRedirect;
        }
    }
}
