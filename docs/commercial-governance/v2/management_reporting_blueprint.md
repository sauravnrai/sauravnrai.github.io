# Management reporting contracts — v2

Source SHA-256: `af69eb927fbe330ad7d7aa13389ff318096843da754037f63568f4186fd1f518`. Logical design only; no real customer metrics or deployed BI is claimed.

## Grain and time

One deal_cycle_id is one business pursuit. A genuine reopening creates a linked new cycle; real errors use linked correction/supersession events. Preserve first qualification and original-source/owner/ICP snapshots. Keep initial/reopened cycles and new business/expansion/renewal segments separate.

Store UTC effective/event time and recorded time. Select events effective by as_of and known by recorded_cutoff. Local cohort-month boundaries use approved OPS_TZ and a versioned internal business calendar. Calendar elapsed days and business-day operating SLAs are different. Late arrivals create labeled new vintages, never silent changes to old snapshots. Aggregate each fact to its grain before joins; avoid stage/activity/finance fan-out.

## Seven metric families

### STAGE_VELOCITY

For each completed stage spell, duration=exit_at-entry_at. Publish median and P75 by stage and exit type (advanced/lost/regressed), spell count and distinct-cycle count. Reentry creates another spell; also report total all-spell time per cycle. Show open-spell age separately, not in completed medians. Net-active duration subtracts the union of explicit clipped HOLD/NURTURE intervals; incomplete pause history means null. Use continuous linear interpolation at rank p*(n-1): n=0 null; n=1 the observed value. Terminal-stage residence is not selling velocity.

### QUALIFIED_TO_PROPOSAL_H

Initial H=60 elapsed calendar days; changing H creates a metric version. Group by first-qualified local month. Denominator: eligible cycles in that cohort with first_qualified_at+H <= as_of. Numerator: those cycles with an actual first proposal issued between first qualification and first qualification+H inclusive. Each cycle counts once; early losses and unresolved-at-H cycles remain in the denominator. Drafts/current-stage counts are not issuance events. Show immature cohorts separately as provisional; publish numerator, denominator, horizon, exclusions and maturity. Never reset cohort dates to improve conversion.

### CLOSED_COHORT_WIN_RATE

For qualified eligible cycles terminally closed in the reporting period: win rate=W/(W+L), loss rate=L/(W+L), win/loss ratio=W/L. Exclude open/hold/nurture and unqualified intake attrition. No closed outcomes means null rates. L=0 means null ratio with NO_LOSSES, not infinity. Count once per cycle; report reopened cohorts separately and preserve prior closure history.

### DELIVERED_ENGAGEMENT_MARGIN

Use delivered/accepted engagements with finance-final complete costs. R=net earned advisory fees, excluding taxes and policy-excluded true pass-throughs; C=fully burdened delivery labor+subcontractors+direct engagement expenses+approved signed adjustments. Fee credits reduce R; cost adjustments retain their approved sign. Margin amount=R-C; margin rate=(R-C)/R. R<=0 gives null percentage and a finance-review flag, while amount remains visible. Blended rate=sum(R-C)/sum(R), never mean of individual percentages. Missing costs are not zero. FINAL costs support final results; accrued/provisional results are separate. Bookings, invoices and cash are not earned fees. Keep currencies separate unless a complete internally approved FX basis exists. This is direct engagement margin, not corporate operating profit.

### STALE_ACTIVE_RATE

Distinct eligible open ACTIVE cycles with inactivity, mutual-step-gap or stage-age flags divided by all eligible open ACTIVE cycles at the same snapshot. Publish reason counts and amounts by currency. Keep blocked/hold/nurture gross inventory visible. Empty denominator is null.

### NEXT_STEP_COMPLETENESS

Active open cycles with accountable owner and open dated internal next action divided by all active open cycles. Publish prospect-agreed mutual-action coverage separately; an internal reminder is not agreement.

### COMMUNICATION_CONTROL_COVERAGE

For each defined audit population report checked_count/population_count plus FAIL/BLOCKED/NOT_TESTED and confirmed unauthorized releases separately. Zero population is NOT_OPERATED/null, not 100% compliance. Blocked attempts are not completed unauthorized sends. No zero-gap claim without real operating evidence.

## Dashboard and reconciliations

Panels: executive gross/eligible pipeline and outcomes; funnel/velocity/mature conversion; governance/control exceptions; final delivery economics and completeness. Always show cutoff/vintage, versions, numerator/denominator, sample_n, exclusions and null/quality reasons. SMALL_SAMPLE at n<10 is an internal caution, not a significance test. Do not invent probabilities, causal lift or external benchmarks.

Reconcile one snapshot row per cycle to gross inventory; nonnegative non-overlapping effective stage intervals; proposal issuance chronology; one primary terminal outcome per cycle; money by currency; delivery/finance lines and completeness; and every audit denominator. Missing dates, cost, FX or controls remain flagged/null rather than imputed as success. Typed keys/fields/required flags for all 15 entities are in management_reporting_schema.json. The original 15-table operational CRM remains a separate model and is not automatically instantiated as 15 HubSpot custom objects.
