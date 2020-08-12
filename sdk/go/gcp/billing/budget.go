// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package billing

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Budget configuration for a billing account.
//
// To get more information about Budget, see:
//
// * [API documentation](https://cloud.google.com/billing/docs/reference/budget/rest/v1beta1/billingAccounts.budgets)
// * How-to Guides
//     * [Creating a budget](https://cloud.google.com/billing/docs/how-to/budgets)
//
// ## Example Usage
type Budget struct {
	pulumi.CustomResourceState

	// Defines notifications that are sent on every update to the
	// billing account's spend, regardless of the thresholds defined
	// using threshold rules.
	// Structure is documented below.
	AllUpdatesRule BudgetAllUpdatesRulePtrOutput `pulumi:"allUpdatesRule"`
	// The budgeted amount for each usage period.
	// Structure is documented below.
	Amount BudgetAmountOutput `pulumi:"amount"`
	// ID of the billing account to set a budget on.
	BillingAccount pulumi.StringOutput `pulumi:"billingAccount"`
	// Filters that define which resources are used to compute the actual
	// spend against the budget.
	// Structure is documented below.
	BudgetFilter BudgetBudgetFilterPtrOutput `pulumi:"budgetFilter"`
	// User data for display name in UI. Must be <= 60 chars.
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// Resource name of the budget. The resource name implies the scope of a budget. Values are of the form
	// billingAccounts/{billingAccountId}/budgets/{budgetId}.
	Name pulumi.StringOutput `pulumi:"name"`
	// Rules that trigger alerts (notifications of thresholds being
	// crossed) when spend exceeds the specified percentages of the
	// budget.
	// Structure is documented below.
	ThresholdRules BudgetThresholdRuleArrayOutput `pulumi:"thresholdRules"`
}

// NewBudget registers a new resource with the given unique name, arguments, and options.
func NewBudget(ctx *pulumi.Context,
	name string, args *BudgetArgs, opts ...pulumi.ResourceOption) (*Budget, error) {
	if args == nil || args.Amount == nil {
		return nil, errors.New("missing required argument 'Amount'")
	}
	if args == nil || args.BillingAccount == nil {
		return nil, errors.New("missing required argument 'BillingAccount'")
	}
	if args == nil || args.ThresholdRules == nil {
		return nil, errors.New("missing required argument 'ThresholdRules'")
	}
	if args == nil {
		args = &BudgetArgs{}
	}
	var resource Budget
	err := ctx.RegisterResource("gcp:billing/budget:Budget", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBudget gets an existing Budget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBudget(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BudgetState, opts ...pulumi.ResourceOption) (*Budget, error) {
	var resource Budget
	err := ctx.ReadResource("gcp:billing/budget:Budget", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Budget resources.
type budgetState struct {
	// Defines notifications that are sent on every update to the
	// billing account's spend, regardless of the thresholds defined
	// using threshold rules.
	// Structure is documented below.
	AllUpdatesRule *BudgetAllUpdatesRule `pulumi:"allUpdatesRule"`
	// The budgeted amount for each usage period.
	// Structure is documented below.
	Amount *BudgetAmount `pulumi:"amount"`
	// ID of the billing account to set a budget on.
	BillingAccount *string `pulumi:"billingAccount"`
	// Filters that define which resources are used to compute the actual
	// spend against the budget.
	// Structure is documented below.
	BudgetFilter *BudgetBudgetFilter `pulumi:"budgetFilter"`
	// User data for display name in UI. Must be <= 60 chars.
	DisplayName *string `pulumi:"displayName"`
	// Resource name of the budget. The resource name implies the scope of a budget. Values are of the form
	// billingAccounts/{billingAccountId}/budgets/{budgetId}.
	Name *string `pulumi:"name"`
	// Rules that trigger alerts (notifications of thresholds being
	// crossed) when spend exceeds the specified percentages of the
	// budget.
	// Structure is documented below.
	ThresholdRules []BudgetThresholdRule `pulumi:"thresholdRules"`
}

type BudgetState struct {
	// Defines notifications that are sent on every update to the
	// billing account's spend, regardless of the thresholds defined
	// using threshold rules.
	// Structure is documented below.
	AllUpdatesRule BudgetAllUpdatesRulePtrInput
	// The budgeted amount for each usage period.
	// Structure is documented below.
	Amount BudgetAmountPtrInput
	// ID of the billing account to set a budget on.
	BillingAccount pulumi.StringPtrInput
	// Filters that define which resources are used to compute the actual
	// spend against the budget.
	// Structure is documented below.
	BudgetFilter BudgetBudgetFilterPtrInput
	// User data for display name in UI. Must be <= 60 chars.
	DisplayName pulumi.StringPtrInput
	// Resource name of the budget. The resource name implies the scope of a budget. Values are of the form
	// billingAccounts/{billingAccountId}/budgets/{budgetId}.
	Name pulumi.StringPtrInput
	// Rules that trigger alerts (notifications of thresholds being
	// crossed) when spend exceeds the specified percentages of the
	// budget.
	// Structure is documented below.
	ThresholdRules BudgetThresholdRuleArrayInput
}

func (BudgetState) ElementType() reflect.Type {
	return reflect.TypeOf((*budgetState)(nil)).Elem()
}

type budgetArgs struct {
	// Defines notifications that are sent on every update to the
	// billing account's spend, regardless of the thresholds defined
	// using threshold rules.
	// Structure is documented below.
	AllUpdatesRule *BudgetAllUpdatesRule `pulumi:"allUpdatesRule"`
	// The budgeted amount for each usage period.
	// Structure is documented below.
	Amount BudgetAmount `pulumi:"amount"`
	// ID of the billing account to set a budget on.
	BillingAccount string `pulumi:"billingAccount"`
	// Filters that define which resources are used to compute the actual
	// spend against the budget.
	// Structure is documented below.
	BudgetFilter *BudgetBudgetFilter `pulumi:"budgetFilter"`
	// User data for display name in UI. Must be <= 60 chars.
	DisplayName *string `pulumi:"displayName"`
	// Rules that trigger alerts (notifications of thresholds being
	// crossed) when spend exceeds the specified percentages of the
	// budget.
	// Structure is documented below.
	ThresholdRules []BudgetThresholdRule `pulumi:"thresholdRules"`
}

// The set of arguments for constructing a Budget resource.
type BudgetArgs struct {
	// Defines notifications that are sent on every update to the
	// billing account's spend, regardless of the thresholds defined
	// using threshold rules.
	// Structure is documented below.
	AllUpdatesRule BudgetAllUpdatesRulePtrInput
	// The budgeted amount for each usage period.
	// Structure is documented below.
	Amount BudgetAmountInput
	// ID of the billing account to set a budget on.
	BillingAccount pulumi.StringInput
	// Filters that define which resources are used to compute the actual
	// spend against the budget.
	// Structure is documented below.
	BudgetFilter BudgetBudgetFilterPtrInput
	// User data for display name in UI. Must be <= 60 chars.
	DisplayName pulumi.StringPtrInput
	// Rules that trigger alerts (notifications of thresholds being
	// crossed) when spend exceeds the specified percentages of the
	// budget.
	// Structure is documented below.
	ThresholdRules BudgetThresholdRuleArrayInput
}

func (BudgetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*budgetArgs)(nil)).Elem()
}
