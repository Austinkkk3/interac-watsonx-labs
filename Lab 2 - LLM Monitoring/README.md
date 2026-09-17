# Lab 2: Interac e-Transfer Dispute Summarization with watsonx.governance (~45 min)

> **Interac watsonx Enablement Workshop.** Scenarios, personas, and data in this lab are fictional and for demonstration only.

## Use Case: Interac e-Transfer Dispute Summarization

Interac support teams receive large volumes of customer dispute and complaint narratives about e-Transfer (wrong recipient, suspected fraud, declined transfers, duplicate sends, and so on). In this lab you govern and evaluate a **text-summarization prompt** that condenses these dispute narratives into short, consistent summaries — the kind of GenAI assist a support team would put into production.

The lab uses IBM's **"Getting started with watsonx governance"** sample project as the starting point. It ships a summarization prompt (named *Insurance claim summarization* in the sample). You will **adapt that prompt to Interac's dispute-summarization use case** and evaluate it against Interac e-Transfer dispute data. The governance workflow — deploy, evaluate (ROUGE, BLEU), model health, and AI Factsheets — is identical regardless of the domain.

> **Note on names:** because we import IBM's sample project unchanged (so it imports cleanly), some assets and screenshots still show their original sample names (e.g. *Insurance claim summarization*). Follow the steps — you will customize the prompt content for Interac.


## Table of Contents

1. [What is Watsonx.governance](#what-is-watsonxgovernance)
2. [Terminologies](#terminologies)
3. [Getting Started](#getting-started)
4. [Create Project](#create-project)
5. [Create Deployment Space](#create-deployment-space)
6. [Track Assets](#track-assets)
7. [Adapt the Prompt for Interac](#adapt-the-prompt-for-interac)
8. [Deploy Prompt](#deploy-prompt)
9. [Prompt Evaluations](#prompt-evaluations)
10. [Model Health and AI Factsheets](#model-health-and-ai-factsheets)

---

## What is Watsonx.governance

Watsonx.governance allows for organizations to implement formal governance procedures around their model/prompt lifecycles. It can help in risk reduction, real-time monitoring, both traditional and GenAI models. Watsonx.governance allows for third party AI monitoring as well.

![Watsonx.governance Overview](images/image1.png)

---

## Terminologies

### 1. Project
A space to experiment with models or foundation models. It can include assets, data connections, etc.

### 2. Deployment
A space where candidate models or prompts can be deployed for testing and exposing it to the outside world. It can include assets required for the deployment.

### 3. AI Factsheets
Keeps all the information and updates regarding a model/prompt in one place for easy explainability and transparency. With increasing scrutiny around AI, laws are put in place to provide explainability for model's outputs. AI factsheets provide a way to easily get all the information without always reaching out to Data Scientists to AI developers. Easy PDF, doc report generation, able to customise the layout for enterprise needs.

### 4. Evaluations
Evaluations metrics for prompts or models, e.g. Rouge, BLEU.

---

## Getting Started

1. Navigate to Watsonx.ai using IBM Cloud. Use [link](https://dataplatform.cloud.ibm.com/wx/home?context=wx). Make sure that you are in correct account and check that US(Dallas) is selected as the location. Your environment will be named something like "watsonx-events2".

   ![IBM Cloud Login](images/image2.png)
   ![IBM Cloud Region](images/image3.png)

---

## Create Project

1. Select **View all projects** from Projects

   ![View All Projects](images/image4.png)

2. Click **New Project**

   ![New Project](images/image5.png)

3. Select **Local file** and click **Browse** and upload `Auto-claim-summary.zip` file

   ![Upload File](images/image6.png)

4. Give Name, select the choice for the Cloud objext Storage Instance, and click **Create**. If you see an option to **Create Key**, click on that.

   ![Name Project](images/image7.png)
   ![Name Project](images/image46.png)

5. Click **View new project**

   ![View New Project](images/image8.png)

6. This will bring the project. Click **View import summary**

   ![Import Summary](images/image9.png)

7. There should not be any errors in importing the project. **Failed** value should be zero. Otherwise, please reimport the project again. 

   After you verify the import, click **Close**

   ![Verify Import](images/image10.png)

8. Associate a watsonx.ai runtime service instance. Click the **Manage** tab, click **Services & Integration** and then click **Associate service**

   ![Services & Integration](images/image11.png)

9. Select the instance and click **Associate**. Create a new service (watsonx.ai Runtime) if no option available to select. 

   ![Associate Service](images/image12.png)

---

## Create Deployment Space

1. Select **View all deployment spaces** from Deployment Spaces from Hamburger menu

   ![Deployment Spaces Menu](images/image13.png)

2. Click on **New deployment space**

   ![New Deployment Space](images/image14.png)

3. Provide Name, Description select Deployment stage (**Testing** for our lab)

   ![Configure Space](images/image15.png)

4. Select watsonx.ai Runtime and click **create**

   ![Select ML Instance](images/image16.png)

---

## Track Assets

1. Go back to the project created earlier by using Hamburger menu at top. Click **View all projects** and select the project your created earlier

  <img width="1472" height="826" alt="Screenshot 2026-09-17 at 7 17 33 PM" src="https://github.com/user-attachments/assets/bc6fbaed-5d56-44ea-8552-a7d0f91141b5" />


2. Click on **Assets** tab

   ![Assets Tab](images/image17.png)

3. Click on **Insurance claim summarization prompt**. If you get option to select between Go to project, Preview or Edit, click **Preview**. 

   ![Select Prompt](images/image18.png)

4. If the default model is not llama-3-3, go back, click **Edit**
   <img width="1326" height="750" alt="16" src="https://github.com/user-attachments/assets/5364c486-1f66-4a1d-a887-f4d8af8e4d24" />


6. Go back and click on the three dots on the right of **Insurance claim summarization prompt** and click **Go to AI factsheets**

   ![Go to AI Factsheets](images/image19.png)

7. Scroll and see what all there in AI Factsheets, e.g. prompts, parameters

   ![Review Factsheets 1](images/image20.png)
   ![Review Factsheets 1](images/image21.png)

---

## Adapt the Prompt for Interac

Before deploying, customize the summarization prompt for Interac's dispute-summarization use case.

1. In the project **Assets** tab, open the summarization prompt (shown as *Insurance claim summarization*) and click **Edit**.

2. Replace the **instruction** with the Interac version:
   ```
   You are an Interac customer support analyst. Summarize the following Interac e-Transfer customer dispute. Focus on what happened, the amount involved, and the customer's requested resolution. Make the summary at least 3 sentences long.
   ```

3. Optionally paste one of the dispute cases from `etransfer_dispute_validation.csv` as the input to test the prompt, then click **Save**.

---

## Deploy Prompt

1. Go back to **Auto Claim Summary** project. Click three dots next to summarization prompt and click **Promote to space**

   ![Promote to Space](images/image22.png)

2. Select the deployment space created earlier. Select **Go to the prompt template in the space after promoting it**

   ![Select Space](images/image23.png)

 3. Click on **New deployment**

   ![New Deployment](images/image24.png)
   
4. Associate with Runtime Service if you didn't do it in the previous step

<img width="1414" height="750" alt="15" src="https://github.com/user-attachments/assets/623ca0f6-e9ec-4928-89c0-606c9889d955" />

   <img width="1414" height="793" alt="14" src="https://github.com/user-attachments/assets/58b2a8d6-f61e-4aaa-99fa-536ff59fd580" />



5. Give it a Name and click **Create**

   ![Name Deployment](images/image25.png)

6. Click on the deployment created

   ![View Deployment](images/image26.png)

7. You can see endpoints that can be used to call the deployed prompt or model

   ![View Endpoints](images/image27.png)

8. You can test the prompt here as well

   ![Test Prompt](images/image28.png)

---

## Prompt Evaluations

1. Let's evaluate the prompt. Click on **Evaluations** and click **Evaluate**. If there is a pop-up, click **Associate a service instance**

   ![Start Evaluation](images/image29.png)

2. Select **Next**

   ![Continue](images/image30.png)

3. Click **Browse** and select the `etransfer_dispute_validation.csv` file provided

    ![Upload File](images/image31.png)

4. For Input select **Dispute_Case** and for Reference output select **Summary**

    ![Configure I/O](images/image32.png)

5. Check the **Task credentials** checkbox. After that, click **Evaluate**. 

    ![Run Evaluation](images/image33.png)

6. Now evaluations should show up (Evaluations can take 5-10 mins)

    ![Wait for Results](images/image34.png)

7. You should be able to see evaluations like Rouge, BLEU, etc. (Different metrics for different use cases)

    ![Evaluation Metrics](images/image35.png)

8. You can click on **settings** button to configure the thresholds for different metrics. We won't be configuring this in lab and will keep the values default

    ![Configure Thresholds 1](images/image36.png)
    ![Configure Thresholds 2](images/image37.png)

9. Click **View metrics** to see the metrics in detail

    ![View Metrics](images/image38.png)

10. Scroll down and click **Rouge** and **BLEU**, to see Rouge values in detail

    ![Rouge Metrics](images/image39.png)

    ![BLEU Metrics](images/image40.png)

---

## Model Health and AI Factsheets

1. *(Optional)* Go to the **Model health** tab and open **Throughput and Latency (API)** to see quality-of-service metrics for the deployed prompt.

    ![Model Health Tab](images/image41.png)

2. Now click on the **AI Factsheet** tab. You should be able to see all the updates like deployed endpoints and evaluations in the factsheet — this is the governance payoff: everything that happened to the prompt (deployment, evaluations) is captured in one place for explainability and audit.

    ![AI Factsheet Tab](images/image43.png)

    ![Factsheet Details](images/image44.png)

    ![Factsheet Updates](images/image45.png)

---
