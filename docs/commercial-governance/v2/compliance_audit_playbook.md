# Communication approval and suppression playbook — v2

Source checkpoint: `af69eb927fbe330ad7d7aa13389ff318096843da754037f63568f4186fd1f518`. Objective: zero unauthorized releases through fail-closed controls. A checklist or synthetic test is not a legal opinion, a production audit or a zero-gap guarantee.

## Permission validity

Record contact, purpose, channel, jurisdiction, approved basis, evidence reference, approver/time, valid_from, review_due_at and policy version. EXPLICIT_EXPIRY requires expires_at. NO_FIXED_EXPIRY_REVIEW_REQUIRED requires an explicit privacy-approved rationale and review_due_at. No universal statutory consent duration is asserted.

At proposed release time t require valid_from <= t, t < review_due_at and t < expires_at where explicit. Equality at expiry or review due fails closed. Unknown required dates/mode/scope/control state blocks release. Revocation, suppression or another stop event overrides otherwise unexpired approval. Review overdue is an operational hold, not invented legal expiry.

Generate internal reminders 14, 7 and 1 days before configured expiry/review. They do not renew consent, authorize contact or justify automatic date extension. Preserve approval history and obtain fresh evidence for renewal or scope changes.

## Concrete send review

Source and purpose/channel/jurisdiction must be approved. Current scope, confidentiality, conflict, capacity and claims reviews apply. Use approved firm identity/address and required privacy/opt-out mechanism. One external recipient; necessary allowlisted internal CC only. Bind explicit human approval to final To/CC, subject/body hash and template version. Template approval or a high score is never concrete send authorization. Re-read authoritative permission, suppression and stop status immediately before release; a weekly snapshot or stale export is not authority. Use duplicate-step prevention and a serialized/manual final check.

Recipient-free drafts have empty To, Cc and Bcc. An internal review marker naming commercial@ziontechgroup.com is not a recipient, forwarding rule or proof review occurred. Keep DRAFT / DO NOT SEND status; remove internal notes only after separate final-message approval. This repository sends no messages or notifications.

## Central suppression ledger

Required: suppression ID, verified contact identity, normalized email, purpose/channel scope, reason, effective/recorded times, evidence, recorder, status and release approval/history. Preserve original addresses; do not strip plus-tags or silently merge aliases.

1. Ingest revocations, opt-outs, complaints and applicable legal blocks immediately when known; block affected pending commercial releases and reconcile sequences/queues/exports before continuation.
2. Match identity and normalized email at import, enrollment and release; do not bypass through duplicate records, alternate addresses or restored backups.
3. Apply the request and approved policy across relevant commercial purposes/channels. Unknown scope is held for privacy review. Hard bounce blocks the affected address. Necessary service communication has a separate purpose-specific basis and is not a marketing workaround.
4. Release only for documented appropriate new grounds or verified correction, with independent privacy approval. Sales, score and deletion cannot release suppression.
5. Reapply the current register after import, restore or stale-file reuse. Retain minimal evidence under approved retention and least privilege; keep private legal narratives restricted.

## Complete audit and incidents

Use all 20 CA controls in audit_checklists.csv. Weekly populations: 100% of actual outbound attempts/releases; all current active approvals for active opportunities; approvals expiring/review-due within 14 days; and suppression additions/releases plus relevant imports/restores. Record population/checked counts, outcome, evidence, reviewer, exception/severity, owner/due date and independent closure proof. Zero population is NOT_OPERATED/null coverage, not 100% compliance. Incomplete testing is NOT_TESTED, not PASS.

P0 suspected unauthorized release/suppression breach: immediately freeze affected workflow, preserve logs, compliance-led scope/cause assessment and counsel-directed notification assessment. P1 invalid control/material integrity issue: block affected release/advancement/commit and review the same business day. P2 commercial staleness: owner review within 2 business days. Retest independently before closing sensitive exceptions. Statuses: PASS, FAIL, BLOCKED, NOT_OPERATED, NOT_TESTED.

HubSpot is OMITTED_ACCESS_CONSTRAINTS because the connected workflow inspection lacked automation permission. This synchronization executed zero HubSpot CRM writes; no pipeline/property/contact/deal migration or access bypass is implied by these rules.
