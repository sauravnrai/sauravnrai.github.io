# App Network Hub

[Open the hub](https://sauravnrai.github.io/) · [Discovery](https://sauravnrai.github.io/discovery/) · [ASF Studio](https://sauravnrai.github.io/ASF/) · [Analytics](https://sauravnrai.github.io/ASF-analytics/) · [Visualizer](https://sauravnrai.github.io/ASF-visualizer/)

A static, self-contained directory of four browser tools with bidirectional navigation. Published from `main` → `/` on GitHub Pages. No build packages or runtime APIs, fonts, CDNs, tracking or paid services. The optional directory filter runs in the browser; links and content remain usable without JavaScript.

## Fresh content

- [Local-data quickstart](https://sauravnrai.github.io/ASF/guide.html)
- [Completeness and statistics](https://sauravnrai.github.io/ASF-analytics/guide.html)
- [Choosing a chart](https://sauravnrai.github.io/ASF-visualizer/guide.html)
- [Source-only project catalog](https://sauravnrai.github.io/projects.html): nine repositories clearly separated from browser-hosted tools.

`network.json` is a downloadable, versioned catalog, not a dynamic API dependency.

## Discovery and sharing

Discovery scores readiness locally, shows full results immediately, and supports copy/TXT/JSON downloads. Gmail and mail-app buttons only open drafts; the visitor must review the report and click Send. No email is sent automatically and delivery is not claimed by the application.

## Privacy

See the homepage privacy section. ASF's same-tab session storage is shared by the Pages origin; it is not a security boundary. Do not use sensitive data. Discovery keeps answers in memory only. Explicitly opening an email draft passes the report to the selected provider/application. Source-only backend projects have their own setup requirements and are not part of the dependency-free browser runtime.

## Verification

The package-free GitHub Actions workflow `verify.yml` performs real HTTP, assets/anchors, cross-navigation, browser scoring, downloads and ASF handoff checks without sending email. It runs only on manual dispatch, uses the runner's standard Python/Node/Chrome, and writes timestamped evidence to `verification/latest.json` and `verification/latest.md`. Its repository-scoped GitHub token is only used inside Actions to read committed test tools and publish evidence. No credentials exist in the browser app.

Until the report status is `passed`, build or source checks alone must not be described as live verification.
