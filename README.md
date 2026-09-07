# Interac watsonx Enablement Labs

A hands-on workshop for exploring **IBM watsonx** agent building, evaluation, monitoring, and AI governance. The labs walk through the full lifecycle — from building an AI agent, to evaluating prompts and LLMs, to governing and monitoring models in production.

> **Note on scenarios and data:** All company names, personas, products (e.g. the "Maple" credit cards), and datasets in these labs are **fictional and illustrative**, used only to demonstrate watsonx capabilities. They do not represent real customers or real data.

## Prerequisites

- Access to an IBM watsonx environment (watsonx.ai / watsonx Orchestrate / watsonx.governance), as provided for the workshop.
- An IBM Cloud account and API key (each lab explains where this is needed).
- Familiarity with basic AI/ML and REST/OpenAPI concepts is helpful but not required.
- **Lab 3 requires a separate, IBM-provisioned OpenPages governance environment** — confirm access before the session.

## Labs

| # | Lab | What you'll do | Environment |
|---|-----|----------------|-------------|
| 1 | [WXO Agent Monitoring](Lab%201%20-%20WXO%20Agent%20Monitoring/README.md) | Build an Interac e-Transfer Support Agent with RAG + a custom limits/fees tool, then evaluate and monitor it | watsonx Orchestrate + watsonx.governance |
| 2 | [LLM Monitoring](Lab%202%20-%20LLM%20Monitoring/README.md) | Import a project, deploy a prompt, and run prompt evaluations (ROUGE, BLEU) with AI Factsheets | watsonx.ai + watsonx.governance |
| 3 | [AI Governance with OpenPages](Lab%203%20-%20AI%20Governance%20with%20OpenPages/README.md) | Run a multi-persona AI governance workflow (model owner, validator, RCO, developer) | watsonx.governance + OpenPages |
| 4 | [ML Monitoring](Lab%204%20-%20ML%20Monitoring/README.md) | Deploy an ML demand-forecasting model and configure Watson OpenScale evaluations (quality, drift, explainability) | watsonx.ai + Watson OpenScale |

Each lab folder contains its own step-by-step `README.md` and any data or instructor assets it needs.

## Getting started

Open the folder for the lab you're running and follow its `README.md`. Labs are self-contained and can be run independently, though the ordering above reflects a natural build-up from agent creation to production governance.
