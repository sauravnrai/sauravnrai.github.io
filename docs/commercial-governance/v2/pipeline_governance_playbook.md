# Pipeline governance playbook — v2

Normative source checkpoint SHA-256: `af69eb927fbe330ad7d7aa13389ff318096843da754037f63568f4186fd1f518`. Proposed internal operating rules; no live pipeline migration or meeting scheduling is implied.

## Taxonomy and qualification

Retain seven stored statuses: INTAKE, QUALIFIED, DISCOVERY, PROPOSAL, DECISION, WON, LOST. There are five open stages and two terminal outcomes. The success path ends in WON (Closed-Won); LOST (Closed-Lost) is a branch from any open stage. HOLD/NURTURE/DISQUALIFIED are dispositions, not additional funnel stages.

Qualification requires total >=60/100, current evidence coverage >=80%, mandate=20, sponsor>=5, funding>=5, delivery eligibility=10 and applicable gates APPROVED. Fit/intent maxima remain 60/40. Unknown values are null, not invented facts; unknowns contribute zero only to a provisional total and do not count as assessed coverage. Known evidenced zeros count toward coverage. Revalidate intent evidence older than 30 days. Neither a score nor a stage authorizes communication.

## Accountability and operating calendar

All clock times are proposed OPS_TZ; approve the actual time zone and internally maintained business-day/holiday calendar before scheduling.

| When | Accountable role | Required output |
|---|---|---|
| Daily 09:00 | RevOps and compliance | Suppression/revocation/expiry/stop-event and overdue-action queue; affected releases stay blocked. |
| Friday 16:00 | Deal owners; delivery/finance as relevant | Current evidence packet, buyer/procurement map, score, mutual actions, decision dates, currency/economics and unresolved gaps. |
| Monday 08:30, cutoff 08:00 | RevOps | Immutable as-of snapshot, source-count reconciliation, policy/calendar/metric versions and late-arrival classification. |
| Monday 09:00, 15 minutes | Compliance and RevOps | Control exceptions, upcoming expiries, suppression changes/releases and suspected unauthorized activity. |
| Monday 09:30, 60 minutes | Commercial lead and owners | 5 minutes quality/control; 10 dashboard; 25 stage gates/stale deals; 10 enterprise buying blockers; 10 decisions/owners/dates. |
| Monday 12:00 | Lead and RevOps | Evidence-backed decision ledger and internal next-action tasks; publication requires separate authorization where applicable. |
| Wednesday 15:00, 20 minutes | Owners and lead | Exception closure, missed milestones and unsupported commit/forecast review. |
| Monthly after finance close; quarterly calibration | Finance, lead and RevOps | Reconciled delivered margins and controlled policy/metric change log. |

Owners supply evidence and next actions. Commercial leadership approves commercial decisions and forecast exceptions but cannot waive privacy/suppression. RevOps maintains append-only events and reproducible reporting. Compliance owns communication basis, expiry and suppression releases. Finance owns economics/cost completeness. Delivery owns capacity, acceptance and handoff. Control-sensitive exceptions require independent review.

## Stage gates

| Status | Required evidence / advancement | Internal follow-up |
|---|---|---|
| INTAKE | Unique mandate, account, owner, authorized original source and timestamp; advance only after the complete qualification gate. | Triage within 1 business day. |
| QUALIFIED | Versioned score and evidence, authority/funding paths, approved controls and dated owner task; obtain prospect-agreed discovery participants, purpose and date before DISCOVERY. | Scheduling review within 2 business days. |
| DISCOVERY | Prospect-validated decision, measurable outcome, scope, budget route, buyer committee, procurement/legal/security/vendor applicability, information access, capacity and mutual proposal action. | Draft recap/task within 1 business day after meeting. |
| PROPOSAL | Approved proposal actually delivered with final version and separate send approval; amount/currency, scope, pricing/margin and capacity approved; buyer decision route/date and mutual next step. | Internal review after 2 business days, then 5 additional business days if appropriate; prospect-agreed timetable prevails. |
| DECISION | Active evaluation confirmed, named signature authority, mutual action/date, procurement/legal/security/credit/start-condition status and explicit risks. | Agreed timetable and weekly review; missed decision date escalates immediately. |
| WON | Binding executed agreement, approved fee/scope/success measures, required funding/credit/start conditions and delivery owner. | Handoff within 2 business days; bookings are not earned revenue. |
| LOST | Evidenced rejection, competitor decision or lead-approved no-decision close with standardized reason. | Record within 1 business day; age/silence alone never creates loss or re-enrollment. |

Append each transition's cycle ID, old/new stage, effective and recorded times, actor, approver, evidence, reason and policy version. Preserve regressions/repeated spells. A business reopening creates a linked new cycle; real data errors use linked corrections. A documented exception may supply skipped-stage evidence, never waive privacy/suppression or contract requirements. A draft is not proposal delivery; verbal enthusiasm is not WON. Intake attrition is distinct from qualified-opportunity loss.

## Stale and exception policy

- Missing owner/source/stage evidence/dated internal task: immediate hygiene exception; block advancement and correct within 1 business day.
- Overdue task: immediate flag; escalate after 2 unresolved business days. Never silently roll dates forward.
- STALE_ACTIVITY: >=14 calendar days without substantive two-way exchange, held meeting or documented prospect decision. Fall back to first qualification/cycle opening if none. Internal notes, opens, unanswered sends and ownership edits do not reset the clock. Owner reviews within 2 business days.
- MUTUAL_STEP_GAP: no valid prospect-agreed dated action for >=30 calendar days, measured from mutual_step_absent_since_at. Record retain/regress/hold/nurture/closure-review decision; never automatically close.
- Initial stage-age review alerts: more than 3/10/20/15/20 business days in INTAKE/QUALIFIED/DISCOVERY/PROPOSAL/DECISION. These are hypotheses, not external benchmarks or loss dates. Show current spell, total all-spell and calendar age.
- Missed decision date, expired material evidence or non-approved control: immediate block of relevant advancement/communications; remove unsupported commit and expose the blocked amount.
- HOLD: internal review within 2 business days. NURTURE: internal review in 60-90 days; no automatic recontact. Keep both visible outside eligible active forecast.

Reconcile gross inventory to blocked/hold/nurture inventory and eligible active forecast by currency. Preserve calendar age; net-active time requires complete disposition intervals. Review the 18 PG controls in audit_checklists.csv. Every remediation needs one owner, due date and closure evidence.

## Optimization

Select one internally evidenced bottleneck at a time. Record hypothesis, eligible cohort, intervention, baseline, cost/margin effects and guardrails. Compare mature like-for-like cohorts rather than raw weekly stage counts. Version changes; do not invent probabilities, causal lift or industry benchmarks, and never lower legal/evidence gates to improve apparent conversion.
