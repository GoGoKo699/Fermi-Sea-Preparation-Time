# Verify hosted mathematics

The collector opens a fresh anonymous browser on the exact public commit-pinned GitHub pages. It inventories the committed Markdown, compiles reference MathML locally, then compares that reference with GitHub's actual accessible mathematics at wide and narrow viewports. It retains source identities, screenshots, page receipts and a structural report. The source and hosted expression counts must agree.

The local compiler is the reference side of the comparison; it does not establish hosted rendering. A structural pass also does not establish pixel quality or scientific truth. Inspect the captured screenshots and the mathematical source separately.

The same-repository pull-request workflow uses read-only contents access, no persisted checkout credentials, no secrets and pinned actions. It first probes the README and a table-containing verification page, then captures every committed Markdown page. The exact PR-head commit is checked; a moving branch is not an evidence identity.

For a compatible local public-browser environment:

```bash
npm install --prefix /tmp/fermi-math-runtime playwright@1.56.1 mathjax-full@3.2.1
node /tmp/fermi-math-runtime/node_modules/playwright/cli.js install chromium
NODE_PATH=/tmp/fermi-math-runtime/node_modules node verification/hosted_math/capture_hosted_math.cjs --root . --repository GoGoKo699/Fermi-Sea-Preparation-Time --revision FULL_COMMIT_SHA --output /tmp/fermi-hosted-evidence
```

Use a new empty output directory for each attempt. Replace FULL_COMMIT_SHA with the actual inspected commit. A representative diagnostic is available through probe_hosted_math.cjs with exactly one --page argument; it cannot establish final repository readiness. The complete collector supports exact-source --resume-from for eligible interrupted transport captures, preserving observation times and prior failures.

[source_pins.json](source_pins.json) identifies the exact helper bytes. Raw hosted captures are reproducible diagnostic artifacts; workflow retention is not permanent research preservation.
