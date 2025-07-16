
# Feedback Collector – Web App

&nbsp;

# Table of Contents
- [1. Feedback Collector – Web App](#1-feedback-collector--web-app)
  - [Project Description](#project-description)
- [2. Results](#2-results)
    - [Azure Deployment](azure-deployment)
    - [Screenshot](#screenshot)
    
&nbsp;  

# 1. Feedback Collector – Web App

## Project Description
This project is a minimal internal feedback tool for team members to **anonymously submit feedback** about meetings. Users can submit text-based feedback and a 1–5 star rating. All feedbacks are shown with timestamps.

The application is built with a **Flask backend** and a simple **HTML + JavaScript frontend**, with in-memory storage. It is structured for easy migration to a full database in the future.

# 2. Results

The Feedback Collector MVP fulfills all required functionalities:

- ✅ Frontend for feedback entry and listing
- ✅ REST API for feedback submission and retrieval
- ✅ In-memory backend structure with extensibility
- ✅ Azure deployment completed and accessible

The application is deployed on Azure Web App (Linux, Python 3.11).

### 2. Azure Deployment
🔗 **Azure URL**: [https://feedbackcollector-webapp.azurewebsites.net](https://feedbackcollector-webapp.azurewebsites.net)

📄 Deployment screenshot with timestamp is provided in the screenshot section below.

---

## Screenshot

![Azure Deployment Screenshot](./deployment_screenshot.png)
