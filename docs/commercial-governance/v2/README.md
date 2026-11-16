# Commercial governance v2 — public review edition

Source checkpoint: `commercial-framework-2026-11-16-v2`.

Original checkpoint SHA-256: `af69eb927fbe330ad7d7aa13389ff318096843da754037f63568f4186fd1f518` (119,876 UTF-8 bytes).

Public publication was explicitly approved by the owner. This feature branch is for review; no merge or live-system deployment is authorized by these files.

## Published documentation

- [Pipeline governance playbook](pipeline_governance_playbook.md): roles, weekly cadence, evidence gates and stale-deal handling.
- [Compliance audit playbook](compliance_audit_playbook.md): purpose-specific permission, expiry and central suppression controls.
- [All 38 audit checks](audit_checklists.csv): 18 pipeline checks and 20 compliance checks, with accountable roles and evidence requirements.
- [Typed reporting schema](management_reporting_schema.json): all 15 reporting entities, keys, fields, types, optionality and relevant enums.
- [Reporting blueprint and metric contracts](management_reporting_blueprint.md): reproducible populations, formulas, null rules and reconciliation.

These are review-friendly rendered/compact exports of the verified v2 framework, not a byte-identical copy of every original source artifact. The original checkpoint remains unchanged. The complete original 15-file recovery package, including original playbooks, schema, baseline, reference code, tests and hash manifest, is available as a [source package](https://backend.composio.dev/api/v3/sl/-80AnGY3T_). Its source files and synthetic validation must not be confused with production operating evidence.

## Boundaries

This is a logical operating design, not legal certification, a deployed CRM, a scheduled calendar, a forecast model or a physically air-gapped infrastructure attestation. Configure OPS_TZ, an approved internal business calendar, role holders and jurisdiction-specific policies before operation. No real customer KPI values are claimed. The original 50 reference tests are synthetic only.

HubSpot integration is omitted because workflow inspection lacked the `automation` scope. No HubSpot pipelines, properties, contacts or deals were changed by this synchronization. No access-control bypass was attempted. Gmail routing markers are internal, non-delivery draft notes; they must not become recipient addresses or authorization to send.
