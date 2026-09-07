# Watsonx.governance Lab Guide

> **Interac watsonx Enablement Workshop.** Scenarios, personas, and data in this lab are fictional and for demonstration only.


## Table of Contents

1. [What is Watsonx.governance](#what-is-watsonxgovernance)
2. [Model lifecycle management with Watsonx.governance (overview)](#model-lifecycle-management-with-watsonxgovernance-overview)
3. [Terminologies related to Watsonx.governance](#terminologies-related-to-watsonxgovernance)
4. [Project creation](#project-creation)
5. [Deployment space creation](#deployment-space-creation)
6. [Prompt evaluations](#prompt-evaluations)
7. [Prompt updates in AI factsheets](#prompt-updates-in-ai-factsheets)

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

1. Navigate to Watsonx.ai using IBM Cloud. Use [link](https://dataplatform.cloud.ibm.com/wx/home?context=wx). Make sure that you are in correct account and check that US(Dallas) is selected as the location. Your environment will be named something like "itz-watsonx-11".

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

9. Select the instance and click **Associate**

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

   ![Navigate to Project](images/image4.png)

2. Click on **Assets** tab

   ![Assets Tab](images/image17.png)

3. Click on **Insurance claim summarization prompt**. If you get option to select between Go to project, Preview or Edit, click **Preview**. 

   ![Select Prompt](images/image18.png)

4. Go back and click on the three dots on the right of **Insurance claim summarization prompt** and click **Go to AI factsheets**

   ![Go to AI Factsheets](images/image19.png)

5. Scroll and see what all there in AI Factsheets, e.g. prompts, parameters

   ![Review Factsheets 1](images/image20.png)
   ![Review Factsheets 1](images/image21.png)

---

## Deploy Prompt

1. Go back to **Auto Claim Summary** project. Click three dots next to summarization prompt and click **Promote to space**

   ![Promote to Space](images/image22.png)

2. Select the deployment space created earlier. Select **Go to the prompt template in the space after promoting it**

   ![Select Space](images/image23.png)

3. Click on **New deployment**

   ![New Deployment](images/image24.png)

4. Give it a Name and click **Create**

   ![Name Deployment](images/image25.png)

5. Click on the deployment created

   ![View Deployment](images/image26.png)

6. You can see endpoints that can be used to call the deployed prompt or model

   ![View Endpoints](images/image27.png)

7. You can test the prompt here as well

   ![Test Prompt](images/image28.png)

---

## Prompt Evaluations

1. Lets evaluate the prompt. Click on **Evaluations** and click **Evaluate**

   ![Start Evaluation](images/image29.png)

2. Select **Next**

   ![Continue](images/image30.png)

3. Click **Browse** and select `claim_summarization_validation.csv` file provided

    ![Upload File](images/image31.png)

4. For Input select **Insurance_Claim** and for Reference output select **Summary**

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

1. Now scroll back up and go to **Model health** tab and scroll down and click on **Throughput and Latency (API)**. This shows the quality of service

    ![Model Health Tab](images/image41.png)

    ![Throughput and Latency](images/image42.png)

2. Now click on the **AI Factsheet** tab. You should be able to see all the updates like deployed endpoints and evaluations in the factsheet;.

    ![AI Factsheet Tab](images/image43.png)

    ![Factsheet Details](images/image44.png)

    ![Factsheet Updates](images/image45.png)

---