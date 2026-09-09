# Lab 4: Interac Transaction-Volume Forecasting Governance with Watson OpenScale (~50 min)

> **Interac watsonx Enablement Workshop.** Scenarios, personas, and data in this lab are fictional and for demonstration only.

## What you'll do

Interac processes very high e-Transfer volumes nationwide, so accurate **transaction-volume forecasts** drive capacity planning, settlement readiness, and healthy fraud/monitoring baselines. A data-science team built a **LightGBM regression model** that forecasts e-Transfer transaction volume over time.

**This lab is not about building the model — it's about governing it in production with IBM Watson OpenScale:** monitoring forecast **quality**, detecting **drift**, **explaining** predictions, and keeping an **audit trail (AI Factsheets)** — the model-risk-management story a regulated financial institution needs.

**Format (Lite):**
- **Part A — Deploy the model (hands-on, ~20 min):** create the project, run the provided notebook, get the model Online.
- **Part B — Govern it with OpenScale (instructor-led demo, ~20 min):** configure Quality / Drift / Explainability monitors.
- **Part C — Review results (~10 min):** run one evaluation and read the risk report.

---

## ⚠️ Environment prerequisite (read first)

Watson OpenScale evaluations (Part B/C) store results in an **evaluation database (datamart)** attached to the account's **watsonx.governance / OpenScale** service instance. Configuring it needs **administrator rights**.

To avoid the most common failure ("Database required" / "Associate a service instance"), **do the entire lab in ONE account and region where:**
1. you have **admin** on the watsonx.governance instance, and
2. the **OpenScale datamart is already configured** (Watson OpenScale → System setup → Database shows a database), and
3. the project, deployment space, and governance instance are all in **that same account + region**.

Confirm this in the workshop environment **before** the session. If it isn't set up, Part B/C are run as an **instructor demo from screenshots / the included report**, and participants still do Part A hands-on.

---

## Prerequisites

- A watsonx / Cloud Pak for Data environment with access to **Projects**, **Deployment spaces**, and **Watson OpenScale**.
- An IBM Cloud **API key** (Get your API key: Manage → Access (IAM) → API keys → Create).
- Files from this repo: `demand_forecasting.ipynb`, `training_data_v2.csv`, `test_data.csv`.

---

## Part A — Deploy the model (hands-on)

### Step 1: Create project + deployment space

1. Go to [watsonx.ai](https://dataplatform.cloud.ibm.com/wx/home?context=wx); confirm you're in the **correct account and region**.
2. **☰ Menu → Projects → New project**, name it `interac-ai-gov`.
3. In the project → **Manage → Services & Integrations → Associate service** → select **watsonx.ai Runtime** → **Associate**.
4. ⚠️ Create an access token: **Manage → Access control → Access tokens → New access token**, name `ml_gov`, role **Editor** → **Create**. *(Needed to run the notebook.)*
5. **☰ Menu → Deployment spaces → New deployment space**, name `bootcamp_gov`, stage **Development**, pick the environment's **Runtime** and **Storage**.
6. ⚠️ Capture the **Space GUID**: in the space → **Manage → General → Space GUID**. *(Needed by the notebook.)*

### Step 2: Import the notebook

In `interac-ai-gov` → **New asset → Work with data and models in Python or R notebooks → Local file → Browse** → upload `demand_forecasting.ipynb` → **Create**.

### Step 3: Run the notebook to deploy the model

The notebook is pre-built and validated — **no code changes needed**.

1. Open the notebook → **Edit**.
2. Drag-and-drop `training_data_v2.csv` into the notebook to upload it.
3. Insert your **project access token** and the **Space GUID** from Step 1.
4. **Run → Run All Cells.** This trains and deploys the LightGBM model (`demand_forecasting_lgbm`) to `bootcamp_gov`.
   - 📌 Note the **RMSE** the notebook prints — you'll use it as a Quality threshold in Part B.

### Step 4: Verify the deployment

**Deployment spaces → `bootcamp_gov`** → confirm `demand_forecasting_lgbm` exists and is **Online**.

✅ *Everyone should reach this point. The model is now deployed and ready to be governed.*

---

## Part B — Govern the model with Watson OpenScale (instructor-led)

> Presenter drives; participants follow along if their environment has the datamart configured, otherwise watch. This is where the governance value shows.

On the deployed `demand_forecasting_lgbm` → **Evaluation → Configure OpenScale evaluation settings**.

1. **Model details:** Data type **Numeric / categorical**, Algorithm type **Regression** → **View summary → Save and continue**.
2. **Manual setup → Next.** Upload `training_data_v2.csv` as the training reference (delimiter **Comma**). Confirm the time-series features, set **`target`** as the label and select the **prediction** column → **Finish**.
3. Enable the three monitors that apply to a regression forecast (skip **Fairness** — N/A for time-series regression):

   **✅ Quality** — forecast accuracy over time:
   - **Pearson** 0.8 (do peaks/drops line up over time)
   - **Spearman** 0.6 (is the relative volume ranking preserved)
   - **RMSE** ← use the value from the notebook (sample: ~2454)
   - Sample size: min **300**, max **1000**

   **✅ Drift v2** — early warning before accuracy drops:
   - Compute **in Watson OpenScale**
   - Upper thresholds: Output drift **0.2**, Feature drift **0.2**
   - Important feature: **`TXN_VOLUME`** → Next → Save

   **✅ Explainability** — why the model predicts what it does:
   - Enable **Global explanation**, method **LIME (enhanced)** (global + local)
   - Parameters: sample size **5000**, stability threshold **0.85**, use training-data global explanation → Save

4. Close the setup when the monitors finish initializing.

---

## Part C — Run and review evaluations

1. **Evaluation → Actions → Evaluate Now → Import from CSV** → upload `test_data.csv` → **Upload and Evaluate** (takes a couple of minutes).
2. Review the dashboard: **Quality** (Pearson/Spearman/RMSE), **Drift**, **Explainability**.
3. Download the report — see the included example: [risk-evaluation-report](risk-evaluation-report-1769635817795.pdf).

**Reading the result:** green = healthy. A **red drift** flag means the model is seeing input (e.g. the `TXN_VOLUME` feature) that differs from what it was trained on, so its predictions may shift — even while other health metrics look fine. That early warning is exactly the point of production monitoring.

---

## What this demonstrates

With Watson OpenScale, Interac could monitor **model performance drift** and **data drift**, **explain** forecasts with feature attribution, keep **AI Factsheets** for audit, and keep a production model governed even as team members change — the core of responsible **model risk management** for a regulated financial institution.

## Summary

Lab 4 shows how **IBM Watson OpenScale** governs a production **transaction-volume forecasting** model — monitoring, explainability, and audit at scale. The focus is not building a model, but **governing production AI responsibly.**
