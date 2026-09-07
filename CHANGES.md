# Changes made for the Interac version

This repo is an adapted, cleaned copy of the original `symcor-watsonx-labs` labs. Summary of what was changed and what you still need to do.

## Confidentiality / de-identification
- **Lab 4** fully de-identified: removed all "Honda" / "Honda Canada" references, the `© IBM Confidential – Client Engineering` marking, and the specific client-outcome numbers ("39–50%"). The client is now referred to generically ("a large Canadian enterprise" / "the client"). Project name changed to `interac-ai-gov`.
- Cleared **all notebook outputs** (Lab 3 & Lab 4), which also removed an internal Cloud Object Storage bucket name that had leaked into a Lab 4 cell output.
- Removed all **internal IBM links** participants can't open: `github.ibm.com/skol/...` and `ca-tor.git.cloud.ibm.com/honda/...` (in Lab 3 README, Lab 3 notebook, and Lab 4 README).
- Deleted stale Lab 3 source files that were not linked from the main README and carried internal links + broken image paths: `assets/tasks/`, `assets/hands-on-lab-askhr.md`, `assets/hands_on_lab_askhr_v2.md`, and the duplicate `assets/Agentic RAG Monitoring .ipynb`.
- Lab 2's fictional insurance claims mention car brands (Honda Civic, Ford, Tesla, BMW) as examples — these are not client data and were left as-is.

## Lab 1 — WXO Agent Monitoring
- **Rewrote the test-case CSVs** (`Product-agent-test-cases.csv`, `-part2.csv`): they were Honda car Q&A left over from a template; now they contain credit-card test cases matching the Maple cards, saved as clean UTF-8.
- `instructor/requirements.txt`: added `requests` (the Docker/compose healthcheck imports it — it was previously missing, so the container reported "unhealthy").
- `instructor/docker-compose.yml`: renamed service `honda-quotation-api` → `quotation-api`; removed obsolete `version: '3.8'`.
- `instructor/product_tool.json`: the `servers[0].url` pointed at a watsonx Orchestrate instance URL, not the tool endpoint. Replaced with `https://REPLACE-WITH-YOUR-TOOL-URL` and fixed the misleading description. **You must set this to your deployed tool URL (see below).**
- README: fixed "download from the Lab 5 folder" → "Lab 1 folder"; fixed Conclusion ("Honda Product Agent" → "Credit Card Product Agent"); aligned the knowledge-base name (`Credit-products`) between the setup step and the agent instructions; replaced the "Architecture diagram will be added here" placeholder with a short architecture description.
- Regenerated `instructor.zip` from the fixed files (also dropped the `__MACOSX` junk).

## Lab 2 — LLM Monitoring
- Cleanest lab; no functional changes. Added the Interac workshop banner. CSV columns (`Insurance_Claim`, `Summary`) already match the steps.

## Lab 3 — AI Governance with OpenPages
- Fixed broken image path `hands_on_lab_images/cloud_openpages.png` → `assets/hands_on_lab_images/cloud_openpages.png`.
- `Model76.png` was referenced but missing from the repo; replaced the broken `<img>` with a text caption. If you have that screenshot, drop it in `assets/hands_on_lab_images/` and restore the image tag.
- Removed/neutralized all internal `github.ibm.com` links; deleted stale source files (see above).
- Fixed typo "seperate" → "separate".

## Lab 4 — ML Monitoring
- De-identified (see above). Fixed the broken H1 (it started with a stray "–").
- The "REPORT" link pointed to an internal Honda GitLab repo; repointed it to the report PDF already included in this folder.

## Repo-wide
- Added a **root `README.md`** (there was none) tying the four labs together with prerequisites and an Interac framing, plus a note that all scenarios/data are fictional.
- Added a short Interac workshop banner to each lab README.

---

## ⚠️ Still on you (environment-dependent — I can't do these from here)

1. **Lab 1 tool hosting:** deploy the `instructor/` FastAPI service somewhere reachable (ngrok or a cloud host), then set `servers[0].url` in `etransfer_tool.json` to that URL before importing the tool into watsonx Orchestrate.
2. **Lab 3 environment:** confirm every participant has access to the IBM-provisioned OpenPages governance environment.
3. **Lab 4 notebook:** run `demand_forecasting.ipynb` end-to-end in your target environment (with your API key + space_id) before the session to confirm it deploys cleanly.
4. **Screenshots:** many screenshots still show the original typed names (e.g. an old project name). Text instructions were updated; re-shooting screenshots is optional polish.
5. **Deeper Interac reskin:** use cases still use the original domains (credit cards, insurance claims, demand forecasting). If you want them reworked around Interac's actual domain (payments / e-Transfer / fraud), that needs new data/PDFs/prompts — tell me and I'll do a specific lab.

---

## Lab 1 rebuilt as the Interac e-Transfer Support Agent

Lab 1 was fully re-themed from the generic credit-card advisor to an **Interac e-Transfer Support Agent** (same watsonx Orchestrate teaching flow: RAG + custom tool + monitoring):
- **Knowledge base:** new `Interac_eTransfer_Guide.pdf` (how e-Transfer works, sending/requesting/Autodeposit, sample limits by account tier, fees, delivery times, security best practices, business e-Transfer, FAQ). Removed the old credit-card catalog PDF.
- **Custom tool:** rewrote `instructor/main.py` into an e-Transfer limits/fees/delivery helper and regenerated the OpenAPI spec as `instructor/etransfer_tool.json` (replaces `product_tool.json`). Server URL is a `REPLACE-WITH-YOUR-TOOL-URL` placeholder.
- **Test cases:** new `etransfer-agent-test-cases.csv` (+ `-part2`).
- **Agent instructions & README:** rewritten for e-Transfer support, including a fraud-awareness guardrail. Same 5-part structure (create → knowledge → tool → test → deploy/monitor).
- **Screenshots:** the watsonx Orchestrate UI screenshots are reused; a note at the top of the README says some images still show the earlier scenario's labels, so follow the text. Pruned 37 now-unused images. Re-shooting screenshots against your environment is optional polish.
- All sample limits/fees are labelled as fictional demo values.
