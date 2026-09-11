# Project Setup - New Project
---
## Summary
Before starting the first technical lab, we will be walking through how to create your own project to get familiar with watsonx.ai and ensure you have access to your environment for the bootcamp. 

It is important we create a project in the right environment, or else it will cause issues down the line!

## Table of Contents

- [Project Setup - New Project](#project-setup---new-project)
  - [Summary](#summary)
  - [Table of Contents](#table-of-contents)
    - [1. Log into watsonx](#1-log-into-watsonx)
    - [2. Check that you are in the right instance](#2-check-that-you-are-in-the-right-instance)
    - [3. Create a new project](#3-create-a-new-project)
    - [Cloud Object Storage (COS)](#cloud-object-storage-cos)
    - [Click Create](#click-create)
    - [4. Associate the correct runtime instance](#4-associate-the-correct-runtime-instance)

### 1. Log into watsonx<a name="log-in-to-watsonx"></a>
---
Next, follow this link to log into watsonx: https://dataplatform.cloud.ibm.com/wx/home?context=wx

Please accept the Terms & Conditions!

### 2. Check that you are in the right instance<a name="check-instance"></a>
---
You should now be taken to the watsonx home screen. Check at the top right that you are in the right instance. If it does not show the right name of the instance, you can select it in the drop-down (this value should match the cloud account field in the email invite you received to join this environment). For the entirety of the bootcamp, you will be working in that same instance! 

**Note:** The instance at the top right tends to change to your default personal account every time you switch/go back to a new page. Thus, it's always good to check the top right corner every time you switch to a new page.

![check-right-instance](assets/check-right-instance.png)

### 3. Create a new project<a name="new-project"></a>
---
Now, we can go ahead and create a new project. 

In the **Projects** section, click the "+" symbol to create a new project.
 
Or, use the link here to trigger a [New Project](https://dataplatform.cloud.ibm.com/projects/new-project?context=wx) creation.

![create-new-project](assets/create-new-project.png)

Enter a **unique name** for your project, include both your first and last name and any other information you would like.

![unique-name](assets/unique-name.png)

### Cloud Object Storage (COS)
It is likely there is also already a Cloud Object Storage instance selected for you, with a name that starts with "itzcos-..." If so, you don't have to do anything! 

Otherwise, you may be prompted to select from multiple instances. Please consult with your bootcamp lead which COS instance to select.

![select-instance](assets/select-instance.png)

### Click Create
Now, click Create. It may take a few seconds to officially be created.

### 4. Associate the correct runtime instance<a name="runtime-instance"></a>
---
With the project created, you should be directed to the project home page. Select the "Manage" tab.

Click on "Services and Integrations" in the left sidebar. Then, click on "Associate service."

![manage-tab](assets/manage-tab.png)

Select the service listed with "Type" = "watsonx.ai Runtime" and click **Associate**. 

![select-runtime-service](assets/select-runtime-service.png)

**Note:** If you can't find the service, remove all filters from the "Locations" dropdown. If you see 2+ Watson Machine Learning services, select the one where "Group" = the same *environment* name of the instance. The *environment* name can be found in the email you received to join the environment in the cloud account field.

![techzone](assets/techzone.png)


Time to get started with your first use case!
