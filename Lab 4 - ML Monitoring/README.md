# Lab 4: Interac Transaction-Volume Forecasting Governance with Watson OpenScale (~50 min)

> **Interac watsonx Enablement Workshop.** Scenarios, personas, and data in this lab are fictional and for demonstration only.

## What you'll do

Interac processes very high e-Transfer volumes nationwide, so accurate **transaction-volume forecasts** drive capacity planning, settlement readiness, and healthy fraud/monitoring baselines. A data-science team built a **LightGBM regression model** that forecasts e-Transfer transaction volume over time.

**This lab is not about building the model — it's about governing it in production with IBM Watson OpenScale:** monitoring forecast **quality**, detecting **drift**, **explaining** predictions, and keeping an **audit trail (AI Factsheets)** — the model-risk-management story a regulated financial institution needs.

**Format — hands-on and self-paced.** You do every step yourself. Approximate timing is ~50 minutes; **if you don't finish during the session you can continue on your own afterward** — every step is self-contained.
- **Part A — Deploy the model (~20 min):** create the project, run the provided notebook, get the model Online.
- **Part B — Configure OpenScale monitors (~20 min):** set up Quality / Drift / Explainability.
- **Part C — Run & review (~10 min):** run one evaluation and read the risk report.

---

## ⚠️ Environment prerequisite (read first)

Watson OpenScale evaluations (Part B/C) store results in an **evaluation database (datamart)** attached to the account's **watsonx.governance / OpenScale** service instance. Configuring it needs **administrator rights**.

To avoid the most common failure ("Database required" / "Associate a service instance"), **do the entire lab in ONE account and region where:**
1. you have **admin** on the watsonx.governance instance, and
2. the **OpenScale datamart is already configured** (Watson OpenScale → System setup → Database shows a database), and
3. the project, deployment space, and governance instance are all in **that same account + region**.

Confirm this in the workshop environment **before** the session. If you hit **"Database required"** (or "Associate a service instance") in Part B, your governance instance has no datamart associated — flag it to the environment administrator; Parts B–C can't run until it's set up. (Part A does not need the datamart.)

---

## Prerequisites

- A watsonx / Cloud Pak for Data environment with access to **Projects**, **Deployment spaces**, and **Watson OpenScale**.
- Files from this repo: `demand_forecasting.ipynb`, `training_data_v2.csv`, `test_data.csv`.
- An IBM Cloud **API key** (Manage → Access (IAM) → API keys → Create):

  ![Get API key](images/API_1.png)
  ![Get API key](images/API_2.png)
  ![Get API key](images/API_3.png)

---

## Part A — Deploy the model (hands-on)

### Step 1: Create project + deployment space

1. Go to [watsonx.ai](https://dataplatform.cloud.ibm.com/wx/home?context=wx); confirm the **correct account and region**.

   ![IBM Cloud login](images/image2.png)
   ![IBM Cloud region](images/image3.png)

2. **☰ Menu → Projects → New project**, name it `interac-ai-gov`.

   ![Projects](images/project_1.png)
   ![New project](images/project_2.png)
   ![Name project](images/3.png)

3. In the project → **Manage → Services & Integrations → Associate service** → select **watsonx.ai Runtime** → **Associate**.

   ![Associate service](images/4.1.png)
   ![Select runtime](images/4.2.png)

4. ⚠️ Create an access token: **Manage → Access control → Access tokens → New access token**, name `ml_gov`, role **Editor** → **Create**. *(Needed to run the notebook.)*

   ![Access tokens](images/4.3.png)
   ![New access token](images/4.4.png)

5. **☰ Menu → Deployment spaces → New deployment space**, name `bootcamp_gov`, stage **Development**, pick the environment's **Runtime** and **Storage**.

   ![Deployment spaces](images/4.5.png)
   ![New deployment space](images/4.6.png)
   ![Configure space](images/4.7.png)

6. ⚠️ Capture the **Space GUID**: in the space → **Manage → General → Space GUID**. *(Needed by the notebook.)*

   ![Space GUID](images/4.8.png)

### Step 2: Import the notebook

In `interac-ai-gov` → **New asset → Work with data and models in Python or R notebooks → Local file → Browse** → upload `demand_forecasting.ipynb` → **Create**.

   ![New asset](images/5.png)
   ![Notebook editor](images/5.1.png)
   ![Browse local file](images/6.png)
   ![Upload notebook](images/6.1.png)
   ![Create](images/7.png)

### Step 3: Run the notebook to deploy the model

The notebook is pre-built and validated — **no code changes needed**.

1. Open the notebook → **Edit**.

   ![Open notebook](images/7.0.1.png)
   ![Edit notebook](images/7.1.png)

2. Drag-and-drop `training_data_v2.csv` into the notebook to upload it.

   ![Upload data](images/7.1.1.png)

3. Insert your **project access token** and the **Space GUID** from Step 1.

   ![Insert token and space id](images/7.2.png)

4. **Run → Run All Cells.** This trains and deploys the LightGBM model (`demand_forecasting_lgbm`) to `bootcamp_gov`.
   - 📌 Note the **RMSE** the notebook prints — you'll use it as a Quality threshold in Part B.

   ![Run all cells](images/8.png)

### Step 4: Verify the deployment

**Deployment spaces → `bootcamp_gov`** → confirm `demand_forecasting_lgbm` exists and is **Online**, then open it → **Evaluation → Configure OpenScale evaluation settings**.

   ![Deployment spaces](images/9.png)
   ![Select space](images/10.png)
   ![Deployment online](images/11.png)
   ![Configure OpenScale](images/12.png)

✅ *Everyone should reach this point. The model is now deployed and ready to be governed.*

---

## Part B — Configure OpenScale monitors (hands-on)

> This is where the governance value shows — you configure all three monitors on the model you just deployed.

1. **Model details:** Data type **Numeric / categorical**, Algorithm type **Regression** → **View summary → Save and continue → Next (manual setup)**.

   ![Model details](images/13.png)
   ![Save and continue](images/14.png)
   ![Manual setup](images/15.png)

2. Upload `training_data_v2.csv` as the training reference (delimiter **Comma**). Confirm the time-series features, set **`target`** as the label and select the **prediction** column → **Finish**.

   ![Upload training data](images/16.png)
   ![Delimiter](images/17.png)
   ![Features](images/18.png)
   ![Features continued](images/19.png)
   ![Model output](images/20.png)
   ![Prediction column](images/21.png)
   ![Review](images/22.png)
   ![Complete setup](images/23.png)

3. Enable the three monitors that apply to a regression forecast (skip **Fairness** — N/A for time-series regression):

   ![Monitors](images/24.png)

   **✅ Quality** — forecast accuracy over time. Click **Quality → Edit**:
   - **Pearson** 0.8 (do peaks/drops line up over time)
   - **Spearman** 0.6 (is the relative volume ranking preserved)
   - **RMSE** ← use the value from the notebook (sample: ~2454)
   - Sample size: min **300**, max **1000**

   ![Quality edit](images/25.png)
   ![Quality thresholds](images/26.png)
   ![Sample size](images/27.png)

   **✅ Drift v2** — early warning before accuracy drops. Click **Drift v2 → Edit**:
   - Compute **in Watson OpenScale**
   - Upper thresholds: Output drift **0.2**, Feature drift **0.2**
   - Important feature: **`TXN_VOLUME`** → Next → Save

   ![Drift edit](images/28.1.png)
   ![Compute option](images/28.2.png)
   ![Drift thresholds](images/28.3.png)
   ![Important features](images/28.4.png)
   ![Select feature](images/28.5.png)
   ![Save drift](images/28.6.png)
   ![Drift initializing](images/28.7.png)

   **✅ Explainability** — why the model predicts what it does. Click **Explainability → Parameters → Edit**:
   - Enable **Global explanation**, method **LIME (enhanced)** (global + local)
   - Parameters: sample size **5000**, stability threshold **0.85**, use training-data global explanation → Save

   ![Explainability](images/29.png)
   ![LIME method](images/30.png)
   ![Explainability parameters](images/31.png)

4. Wait for the monitors to finish initializing, then close the setup.

   ![Initializing](images/32.png)
   ![Close](images/33.png)

---

## Part C — Run and review evaluations

1. **Evaluation → Actions → Evaluate Now → Import from CSV** → upload `test_data.csv` → **Upload and Evaluate** (takes a couple of minutes).

   ![Evaluate now](images/35.png)
   ![Import from CSV](images/36.png)
   ![Select test data](images/36.1.png)
   ![Upload and evaluate](images/37.png)

2. Review the dashboard: **Quality** (Pearson/Spearman/RMSE), **Drift**, **Explainability**.

   ![Evaluation complete](images/38.png)

3. Download the report — see the included example: [risk-evaluation-report](risk-evaluation-report-1769635817795.pdf).

   ![Report](images/39.png)

**Reading the result:** green = healthy. A **red drift** flag means the model is seeing input (e.g. the `TXN_VOLUME` feature) that differs from what it was trained on, so its predictions may shift — even while other health metrics look fine. That early warning is exactly the point of production monitoring.

---

## What this demonstrates

With Watson OpenScale, Interac could monitor **model performance drift** and **data drift**, **explain** forecasts with feature attribution, keep **AI Factsheets** for audit, and keep a production model governed even as team members change — the core of responsible **model risk management** for a regulated financial institution.

## Summary

Lab 4 shows how **IBM Watson OpenScale** governs a production **transaction-volume forecasting** model — monitoring, explainability, and audit at scale. The focus is not building a model, but **governing production AI responsibly.**
