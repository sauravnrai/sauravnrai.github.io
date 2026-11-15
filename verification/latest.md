# Batch 100 — live verification passed

Verified **2026-11-15 03:29:25 UTC** in the [successful full GitHub Actions run](https://github.com/sauravnrai/sauravnrai.github.io/actions/runs/43672537550), verifier commit `d2348c9a4109b0c464365f281520804a9e59c1d6`.

[Machine-readable evidence](https://sauravnrai.github.io/verification/latest.json) · [All 81 verified URLs](https://sauravnrai.github.io/verification/batch-100-urls.md) · [Full raw reports and browser assertions in job logs](https://github.com/sauravnrai/sauravnrai.github.io/actions/runs/43672537550/job/132685548533)

## Results
- **81 unique owned URLs returned HTTP 200:** 48 Pages resources (20 HTML URLs and 28 assets/supporting resources) plus 33 owned GitHub resources.
- **254 crawl link edges**, all **20 directed main-app cross-links**, **100 page-to-app assertions**, and **117 links in nine source-project NETWORK.md files** passed. These are overlapping measures, not an additive total.
- **46 regression checks passed:** 17 shared ASF data, 11 original Discovery, 15 Batch 100 Discovery, and 3 verifier parser checks.
- **41 browser checks passed**, including native validation, complete recommendations, exact email draft contents/recipient, real TXT/JSON/SVG downloads, native clipboard and fallback selection, stale-report invalidation, clearing, service-worker offline reload, portable local HTML scoring offline, file imports, same-tab handoff, no-match protection, negative bars, missing-record line gaps, scatter exclusions, all three labs, and 390px layout/keyboard entry for all 20 page URLs.
- **Zero failed checks, unexpected external page requests, or uncaught page exceptions.**

## Verified pages
| Page | URL | Result |
|---|---|---|
| Hub | https://sauravnrai.github.io/ | HTTP 200; mobile/keyboard passed |
| Discovery | https://sauravnrai.github.io/discovery/ | HTTP 200; complete flows and offline passed |
| ASF Studio | https://sauravnrai.github.io/ASF/ | HTTP 200; import/handoff passed |
| Analytics | https://sauravnrai.github.io/ASF-analytics/ | HTTP 200; filtering/handoff passed |
| Visualizer | https://sauravnrai.github.io/ASF-visualizer/ | HTTP 200; negative/line/scatter/SVG passed |
| Source catalog | https://sauravnrai.github.io/projects.html | HTTP 200; links passed |
| Studio guide | https://sauravnrai.github.io/ASF/guide.html | HTTP 200 |
| Analytics guide | https://sauravnrai.github.io/ASF-analytics/guide.html | HTTP 200 |
| Visualizer guide | https://sauravnrai.github.io/ASF-visualizer/guide.html | HTTP 200 |
| Batch 100 launchpad | https://sauravnrai.github.io/batch-100.html | HTTP 200 |
| Complete workflow | https://sauravnrai.github.io/workflow.html | HTTP 200 |
| Discovery method/offline guide | https://sauravnrai.github.io/discovery/guide.html | HTTP 200 |
| Worked examples | https://sauravnrai.github.io/discovery/examples.html | HTTP 200 |
| Import lab | https://sauravnrai.github.io/ASF/batch-100.html | HTTP 200 |
| Data-quality lab | https://sauravnrai.github.io/ASF-analytics/batch-100.html | HTTP 200 |
| Chart/caption lab | https://sauravnrai.github.io/ASF-visualizer/batch-100.html | HTTP 200 |
| Explore example | https://sauravnrai.github.io/discovery/?example=explore | HTTP 200; 49 points |
| Quality example | https://sauravnrai.github.io/discovery/?example=quality | HTTP 200; 74 points |
| Presentation example | https://sauravnrai.github.io/discovery/?example=visualize | HTTP 200; 93 points |
| Recovery document | https://sauravnrai.github.io/404.html | HTTP 200 for the explicit document URL |

## Fix and coverage boundary
The first browser run stopped on malformed quoting in its chart selector. The selector was corrected without bypassing the negative-bar assertion; the complete suite was rerun successfully. No app assertions were removed.

No email was sent and no email provider was opened. Drafts address `commercial@ziontechgroup.com`; the visitor must review and click **Send**. No ziontechgroup.com website or external form service was accessed. Verification uses owned repositories and preinstalled Python, Chrome and Node only, with no package installation or third-party Actions.

This is a dated verification snapshot, not a future uptime guarantee, full accessibility audit, cross-browser certification, or email-delivery test. Discovery offline support does not imply offline availability of every app.
