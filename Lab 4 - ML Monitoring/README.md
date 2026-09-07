# Parts Demand Forecasting Governance Lab (Watson OpenScale)

> **Interac watsonx Enablement Workshop.** Scenarios, personas, and data in this lab are fictional and for demonstration only.


## Use Case: ML Demand Forecasting Governance

## Introduction

This use case describes how a **machine learning parts demand forecasting model**, developed for a large Canadian enterprise, is deployed into production and governed using **IBM Watson OpenScale**.

The solution demonstrates how IBM technologies enable:
- Scalable and repeatable demand forecasting
- Post-deployment monitoring and governance
- Institutionalization of data science knowledge beyond individual contributors

## Customer Background

The client’s Data Science team was newly formed and faced challenges related to transparency, manual forecasting processes, and reliance on individual expertise.  
Through an IBM Client Engineering (CE) engagement, IBM helped the client modernize parts demand forecasting using machine learning and establish strong data science and governance foundations.

Key outcomes:
- **Significant improvement in forecasting accuracy**
- Forecasting for **all parts simultaneously**
- Reduced manual effort and dependency on senior individuals


For this governance lab, we use the same machine learning parts demand forecasting model developed during the original engagement. The model is a supervised, tree-based regression model (LightGBM) trained on historical parts demand data, seasonality signals, and engineered time-series features.
This model was previously validated with the client’s Data Science team and demonstrated a substantial reduction in forecasting error compared to legacy, manually driven forecasting methods.
In this lab, the model itself is unchanged; the focus is on demonstrating how IBM Watson OpenScale enables post-deployment monitoring, explainability, and governance of a production-ready model.


## Model Background

For this governance lab, we use the **same machine learning parts demand forecasting model** developed during the original engagement.

- **Model type:** Supervised regression  
- **Algorithm:** LightGBM (tree-based)  
- **Features:** Historical demand, seasonality, engineered time-series signals  

## The Objective of this Lab
 
The objective here is to demonstrate **post-deployment monitoring, explainability, and governance** using **IBM Watson OpenScale**.


## Prerequisites

- IBM watsonx / Cloud Pak for Data environment
- Get your API
- Access to:
  - Projects
  - Deployment spaces
  - Watson OpenScale
- Deployment space already created (e.g., `bootcamp_gov`)
- Make sure to consider ⚠️ the extra steps 


## Get you API Key
![IBM Cloud Region](images/API_1.png)
![IBM Cloud Region](images/API_2.png)
![IBM Cloud Region](images/API_3.png)

## Step 1: Create Project

1. Navigate to Watsonx.ai using IBM Cloud. Use [link](https://dataplatform.cloud.ibm.com/wx/home?context=wx). Make sure that you are in correct account and check that US(Dallas) is selected as the location. Your environment will be named something like "itz-watsonx-11".

   ![IBM Cloud Login](images/image2.png)
   ![IBM Cloud Region](images/image3.png)

From **☰** Menu,  Navigate to **Projects** 

![Project list](images/project_1.png)

Create **New Project** 

![Project list](images/project_2.png)

Define the Project's **Name** `interac-ai-gov`

![Define project details](images/3.png)

In `interac-ai-gov` project, Got to **Manage**, Select **Services & Integrations**, Click on **Associate Service**

![Step 4a](images/4.1.png)

Select **watsonx.ai Runtime** and Click on **Associate**

![Step 4b](images/4.2.png)

⚠️You need to get an **acess token** to run the notebook and deploy the ML model. 

In `interac-ai-gov` project, Got to **Manage**, Select **Access control**, Click on **Access tokens** and then Click on **New access token**

![Step 4b](images/4.3.png)

Give the access token **Name** `ml_gov`, **Acess role** `Editor` then Click on **Create**

![Step 4b](images/4.4.png)

From **☰** Menu, Navigate to **Deployment spaces**

![Step 4b](images/4.5.png)

Go to **Spaces** and Click on **New deployment space**

![Step 4b](images/4.6.png)

Give the Development space **Name** `bootcamp_gov`, **Stage:** select `Development`, **Runtime:** `wml-itz-wxo-xxxxxxxxxxxxx` and  **Storage:** `cos-itz-wxo-xxxxxxxxxxxx`

![Step 6a](images/4.7.png)

⚠️You need to get the **space_id** to run the notebook and deploy the ML model. 

In Deployment spaces, Capture the Deployment Space QuUID. Go to **Manage**, select **General** and **Space GUID:** `xxxxxxx-xxxx-xxx-xxx-xxxxxxxxxxxx` for the notebook

![Step 6b](images/4.8.png)


## Step 2: Import Demand Forecasting Notebook

 From **☰** Menu, Navigate to back **Projects** , Select **View all projects** and Click on **interac-ai-gov** and **New asset**

![Step 5](images/5.png)

Look for **Work with data and models in Python or R notebooks** and Select it. 

![Step 7](images/5.1.png)

Go to **Local file** and Click on **Browse**

![Upload notebook](images/6.png)  

Upload `demand_forecasting.ipynb` the file you downloaded from this repo. 

![Upload notebook](images/6.1.png)

Click on **Create**

![Notebook details](images/7.png)

## Step 3: Run the Notebook to depoly the ML

The notebook is **pre-built and validated**.

> ⚠️ No code changes are required.

Simply:

-Open the notebook that you just uploaded it in the project 

![Notebook details](images/7.0.1.png)

-Click on Edit the **notebook**

![Notebook details](images/7.1.png)

- Upload the data 'training_data_v2.csv' that you downloaded from this repo. Just Drag-and-drop the file. 

![Notebook details](images/7.1.1.png)

- Insert the **project access token** and the **Space_id**, both obtained in the previous steps 

![Notebook details](images/7.2.png)

Then, go to **Run > Run all Cells**. That will deploy the ML model to monitor

![Run notebook](images/8.png)


## Step 4: Verify Deployment Space

Navigate to **Deployment spaces**

![Deployment spaces](images/9.png)  

Click on `bootcamp_gov`

![Select space](images/10.png)

Confirm that the model deployment exists and is **Online**.

![Deployment list](images/11.png) 

Click on `demand_forecasting_lgbm`, Go to **Evaluation**, click on **Configure OpenScale evaluation settings**

![Deployed model](images/12.png)

---

## Step 5: Configure Watson OpenScale Evaluations

From the drop-down menu, select **Data type:** Numeric / categorical, **Algorithm type:** Regression and Click on **View summary**
 
![Evaluations tab](images/13.png)

Review and Click on **Save and continue**

![Model information](images/14.png)

In the page, **use manual setup** is the only option, go **Next**.

![Review setup](images/15.png)

Select **Upload file**

![Upload training data](images/16.png)

Browse to the training dataset `training_data_v2.csv` used to train the ML model

![Select CSV delimiter](images/17.png)

Choose **Comma (,) ** as the delimiter to match the training dataset format.

![Select features and label](images/18.png)

Confirm all engineered time-series features and set **target** as the label column.

![Select features continued](images/19.png)

![Select model output](images/20.png)

Select the **prediction** column generated by the deployed model.

![Configure quality metrics](images/21.png)

Review the step-up and Confirm:

- Algorithm type: Regression  
- Input type: Numeric / categorical  
- Training data reference  
- Feature list and prediction column

Click on **Finish**

![Review model details](images/22.png)

Complete OpenScale Setup

![Complete setup uploading](images/23.png)

In this step, you configure governance evaluations for a deployed time-series demand forecasting model. You see there are four types of Evaluations:

⚠️ Just Select the ones with ✅: 

⛔ Fairness (not applicable to regression time-series forecasting)

✅ **Quality**:

Monitors forecast accuracy over time using regression metrics (Pearson, Spearman, RMSE):

  **Pearson**: Captures the model trend by measuring whether peaks align with peaks and drops align with drops over time.

  **Spearman** : Captures the relative demand pattern (not exact values) by measuring whether higher-demand periods are ranked above lower-demand periods over time.

  **RMSE**: The root of the average magnitude of prediction error


✅ **Drift v2**:

For ML model in production, it detects changes in time-series input distributions and Provides early warning signals before forecast accuracy declines.

✅ **Explainability**:

Uses SHAP or LIME to explain how input features contribute to demand forecasts

![Complete setup summary](images/24.png)

Click on Quality and then Click on **Edit**

![Setup finished](images/25.png)

Set **Quality thresholds**:

**Pearson**: 0.8

**Spearman**: 0.6

**Root of mean squared error (RMSE)**: 2454 ( I got RMSE from the Notebook )

![Setup finished](images/26.png)

Set **Sample Size**: 

**Minimum samples sizes**: 300

**Maximum samples sizes**: 1000

![Step 27](images/27.png)

Click on Drift v2 and then Click on **Edit**

![Step 27](images/28.1.png)

In **Compute option**, Select Compute on **Compute in Watson OpenScale**

![Step 27](images/28.2.png)

Set **Upper thersholds**, **Output drift**: 0.2 and **Feature Drift**: 0.2 

![Step 27](images/28.3.png)

In **Importaant features**, select **PART_DEMAND** feature (you can select up to 10 features all togather) and Click on **Next**.

![Step 27](images/28.4.png)

Select **PART_DEMAND**, Click on **Next**

![Step 27](images/28.5.png)

Keep the **Minimum sample size** and Click **Save**.

![Step 27](images/28.6.png)

Wait for some time. 

![Step 27](images/28.7.png)

Click on Explainability, Parametes, and then Click on **Edit**

![Step 30](images/29.png)

- Enable **Global explanation**
- Choose **LIME (enhanced)** for:
  - Global explanation method
  - Local explanation method

![Step 30](images/30.png)

- Click **Edit** under *Parameters*
- Set **Sample size (number of transactions)** to `5000`
- Set **Global explanation stability threshold** to `0.85`
- Select **Use training data global explanation**
- Click **Save**

![Step 31](images/31.png)

Wait for some time ( couple of minutes). 

![Step 32](images/32.png)

Click on Close **X**

![Step 32](images/33.png)

## Step 6: Run and Review Evaluations

Go to **Evalulation**, Click on **Actions** and Select **Evaluate Now**

![Step 32](images/35.png)

Select from **Import** `from CSV file` and Click on browse.

![Step 32](images/36.png)

Select 'test_data.csv' that you downloaded from this repo.

![Step 32](images/36.1.png)

Click on **Upload and Evaluate** and wait for couple of minutes to complete the evaluation 

![Step 32](images/37.png)

The Evaluations in completed 

![Step 32](images/38.png)

You can also download the report

Click on this to see the report ==> [REPORT](risk-evaluation-report-1769635817795.pdf) 

![Step 32](images/39.png)

Things looks normal (green). 

The red drift indicator means the model is receiving input `Features` (in our case `PART_DEMAND` feature) that might differ from what it was trained on, causing its `Output` predictions to shift, even though all other model health metrics remain normal.



## What This Demonstrates

Using Watson OpenScale, your organization can now:
- Monitor **model performance drift**
- Track **data drift**
- Explain predictions using feature attribution
- Maintain **AI Factsheets** for compliance and audit
- Ensure continuity even when team members leave


## Summary

This lab revisits a **previously successful ML model** and demonstrates how **IBM Watson OpenScale** enables trustworthy AI through governance, monitoring, and transparency.

The focus is not on building a new model, but on showing how **production-ready AI systems are governed responsibly at scale**.

---


