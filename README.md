🚀 MLOps End-to-End Project – Production Grade ML Pipeline
A complete, cloud-ready MLOps system built with modular pipelines, CI/CD, Docker, AWS, MongoDB, and automated deployment.
<p align="center"> <img src="https://img.shields.io/badge/MLOps-Production%20Ready-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/CI--CD-GitHub%20Actions-green?style=for-the-badge" /> </p>
🌟 Project Overview

This repository showcases a fully operational MLOps pipeline built from scratch—covering everything from data ingestion → data validation → data transformation → model training → model evaluation → model deployment → CI/CD → cloud hosting.

It demonstrates industry-grade skills in:

🔹 Pipeline Orchestration

🔹 Cloud Services (AWS EC2, S3, ECR, IAM)

🔹 Containerization (Docker)

🔹 CI/CD Automation (GitHub Actions + Self-Hosted Runner)

🔹 MongoDB Atlas Integration

🔹 Clean, modular, and scalable code architecture

This is the kind of end-to-end ML project setup used in real production systems.

📁 Project Structure
.
├── src/
│   ├── components/
│   ├── configuration/
│   ├── data_access/
│   ├── entity/
│   ├── pipelines/
│   ├── aws_storage/
│   ├── utils/
│   ├── app.py
│
├── notebook/
├── templates/
├── static/
├── Dockerfile
├── .github/workflows/aws.yaml
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md

🔧 Tech Stack & Tools Used
👨‍💻 Core Technologies

Python (Modular OOP Architecture)

FastAPI / Flask Web Application

Jupyter Notebooks

🗄️ Database & Storage

MongoDB Atlas (Cloud NoSQL)

AWS S3 (Model Registry)

☁️ Cloud & DevOps

AWS EC2 (Deployment Server)

AWS ECR (Docker Image Registry)

AWS IAM (User & Key Management)

GitHub Actions (CI/CD Pipeline)

Docker (Containerization)

📦 Packaging

setup.py

pyproject.toml

Local package imports

🟩 1. Project Initialization
✔ Create project template
python template.py

✔ Setup local package imports

setup.py

pyproject.toml

✔ Create and activate a virtual environment
conda create -n proj1 python=3.18.3 -y
conda activate proj1
pip install -r requirements.txt

🟦 2. MongoDB Atlas Setup
Steps performed:

✔ Create project & cluster (M0)

✔ Create DB user & password

✔ Enable IP access: 0.0.0.0/0

✔ Copy connection string (Python driver)

✔ Upload dataset to MongoDB using Jupyter Notebook

✔ Validate uploaded collections in key-value format

🟧 3. Logging, Exception Handling & Notebooks

Centralized logging module

Custom exception class

EDA & feature engineering notebooks

Clean logging & exception design ensures better debugging and monitoring.

🟪 4. Data Ingestion Pipeline
Includes:

MongoDB connection utilities

Fetching and converting data to DataFrame

config_entity.py & artifact_entity.py setup

Component-wise ingestion workflow

Training pipeline integration

Environment variable setup for MongoDB URL

🟨 5. Data Validation, Transformation & Model Training
✔ Written modularly:

utils.main_utils.py

config.schema.yaml

Validation rules (missing, dtype, drift, schema)

Transformation pipeline

estimator.py class for model handling

Model Trainer setup

This ensures reproducibility & automation.

🟫 6. AWS Setup (Model Registry + Deployment)
IAM User

Created user

Downloaded access keys

Set environment variables for:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION

S3 Bucket

Region: us-east-1

Bucket name: my-model-mlopsproj

Allows model push/pull via code

AWS Code Components:

aws_connection.py

aws_storage/ (S3 handling)

s3_estimator.py (model registry interface)

🟥 7. Model Evaluation & Model Pusher

Evaluate model improvement using threshold

Compare with S3 model

Push new model to S3 if improved

Prepare production-ready artifacts

Connect to Model Registry

🟦 8. Prediction Pipeline + App UI

Designed the serving pipeline

Built app.py for UI/API

Added:

templates/

static/

🟩 9. Docker Setup
Includes:

Dockerfile

.dockerignore

Containerizing the full ML app

🟧 10. CI/CD Pipeline (GitHub Actions + EC2 Runner)
CI/CD Workflow:

GitHub → Build Docker image

Push image → AWS ECR

Trigger EC2 self-hosted runner

EC2 pulls updated image

EC2 runs container on port 5080

Application becomes live

🟫 11. EC2 Deployment Setup

Created Ubuntu EC2 instance

Installed Docker

Connected EC2 ↔ GitHub using Self-Hosted Runner

Opened inbound rule:

Port 5080 for app

Final deployment accessible via:

http://<EC2-public-ip>:5080

🎉 Final Output

✔ Fully automated ML training pipeline

✔ Cloud-hosted prediction API

✔ CI/CD powered continuous updates

✔ Dockerized & scalable application

✔ Model registry with version control

✔ Production-grade architecture

🙌 If You Like This Project

⭐ Star the repository & connect with me on LinkedIn!
This project is built to showcase clean, industry-level MLOps skills for production ML systems.
