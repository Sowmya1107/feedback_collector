
# Feedback Collector – Web App

&nbsp;

# Table of Contents
- [1. Feedback Collector – Web App](#1-feedback-collector--web-app)
  - [Project Description](#project-description)
  - [How to Run the App](#how-to-run-the-app)
    - [1. Local Deployment](#1-local-deployment)
    - [2. Azure Deployment](#2-azure-deployment)
  - [REST API](#rest-api)
  - [Bonus Features](#bonus-features)
  - [Screenshot](#screenshot)
  - [Results](#results)

&nbsp;  

# 1. Feedback Collector – Web App

## Project Description
This project is a minimal internal feedback tool for team members to **anonymously submit feedback** about meetings. Users can submit text-based feedback and a 1–5 star rating. All feedbacks are shown with timestamps.

The application is built with a **Flask backend** and a simple **HTML + JavaScript frontend**, with in-memory storage. It is structured for easy migration to a full database in the future.

## How to Run the App

### 1. Local Deployment

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/feedback-collector.git
   cd feedback-collector
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask server:
   ```bash
   python app.py
   ```

4. Open the browser at:  
   `http://localhost:5000`

---

### 2. Azure Deployment

The application is deployed on Azure Web App (Linux, Python 3.11).

🔗 **Azure URL**: [https://feedbackcollector-webapp.azurewebsites.net](https://feedbackcollector-webapp.azurewebsites.net)

📄 Deployment screenshot with timestamp is provided in the screenshot section below.

---

## Screenshot

![Azure Deployment Screenshot](./deployment_screenshot.png)

> Timestamp: 16 July 2025, 19:45 CEST

---

## Results

The Feedback Collector MVP fulfills all required functionalities:

- ✅ Frontend for feedback entry and listing
- ✅ REST API for feedback submission and retrieval
- ✅ In-memory backend structure with extensibility
- ✅ Azure deployment completed and accessible

> The app is ready for internal use and can be scaled further with DB integration and authentication if needed.
