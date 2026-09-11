# Deployment Space Setup - New Project
---
## Summary
Before starting the first technical lab, we will be walking through how to create your own project to get familiar with watsonx.ai and ensure you have access to your environment for the bootcamp. 

It is important we create a project in the right environment, or else it will cause issues down the line!

## Table of Contents

  1. [Log into watsonx](#log-in-to-watsonx)
  2. [Check that you are in the right instance](#check-instance)
  3. [Create a new deployment space](#new-deployment-space) 

### 1. Log into watsonx<a name="log-in-to-watsonx"></a>
---
Next, follow this link to log into watsonx: https://dataplatform.cloud.ibm.com/wx/home?context=wx

Please accept the Terms & Conditions!

### 2. Check that you are in the right instance<a name="check-instance"></a>
---
You should now be taken to the watsonx home screen. Check at the top right that you are in the right instance. If it does not show the right name of the instance, you can select it in the drop-down. For the entirety of the bootcamp, you will be working in that same instance!

If you do not know your instance, go to your techzone reservations list https://techzone.ibm.com/my/reservations. Look for your recently created reservation and click on "Open this environment". Scroll down and look for a reservation name that looks similar to this:  ITZ-SAAS-130. 

**Note:** The instance at the top right tends to change to your default personal account every time you switch/go back to a new page. Thus, it's always good to check the top right corner every time you switch to a new page.

![check-right-instance](assets/check-right-instance.png)

### 3. Create a new deployment space<a name="new-deployment-space"></a>
---
Now, we can go ahead and create a new deployment space. 

In the **Deployments** section, click the "+" symbol to create a new project.
 
Or, use the link here to trigger a [New Deployment soace](https://dataplatform.cloud.ibm.com/ml-runtime/spaces/create-space?context=wx) creation.

![create-new-project](assets/create-new-space.png)

Enter a **unique name** for your deployment space, include both your first and last name and any other information you would like.

![unique-name](assets/unique-name-deploy.png)

### Deployment space 

You have to select from 3 deployment stages (Development,Validation,Production). Please consult with your bootcamp lead which space to select.

![select-space](assets/select-space-deploy.png)

### Cloud Object Storage (COS)
It is likely there is also already a Cloud Object Storage instance selected for you, with a name that starts with "itzcos-..." If so, you don't have to do anything! 

Otherwise, you may be prompted to select from multiple instances. Please consult with your bootcamp lead which COS instance to select.

![select-instance](assets/select-instance-deploy.png)

### Click Create
Now, click Create. It may take a few seconds to officially be created.

![click-create](assets/create.png)

###  Deployment Space Ready
---
With the Deployment space created, you should be directed to the deployment space where you can see your created deployment spaces.

![deploy-space](assets/deploy-ready.png)
![deploy-space](assets/deploy-ready1.png)
Time to get started with your assets deployment!
