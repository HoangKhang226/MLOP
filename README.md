# 📡 Telco Customer Churn Prediction: A Production-Grade MLOps Ecosystem

[![MLOps CI/CD](https://github.com/HoangKhang226/MLOps/actions/workflows/main.yml/badge.svg)](https://github.com/HoangKhang226/MLOps/actions/workflows/main.yml)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/hoangkhang226/mlop-churn)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

## 🌟 Project Vision

Customer churn is one of the most critical challenges in the telecom industry. This project goes beyond training a simple model; it builds a **scalable, reproducible, and production-ready MLOps ecosystem**.

By transforming raw data into actionable insights through a standardized 6-stage modular pipeline, we provide a blueprint for turning machine learning research into a living, breathing software product.

---

## 🚀 Key Features (Production-Ready)

- **🏗️ 6-Stage Modular Pipeline**: Clean separation of concerns following the MLOps industry standard: Ingestion, Validation, Transformation, Training, Evaluation, and Deployment.
- **🔄 End-to-End CI/CD Automation**:
  - **CI (Continuous Integration)**: Automated code linting (Flake8), formatting (Black), strict data validation, and unit testing on every push.
  - **CD (Continuous Delivery)**: Automatic Docker image building and pushing to **Docker Hub** upon successful CI completion.
- **🧬 Robust Data Ingestion**: A resilient ingestion system capable of handling multiple data formats (Zip or raw CSV) ensuring the pipeline never breaks due to source format changes.
- **⚡ Dual-Service Architecture**:
  - **Back-end (FastAPI)**: Optimized for high-performance and low-latency real-time inference.
  - **Front-end (Streamlit)**: A premium interactive dashboard for business users to run "What-if" churn simulations.

---

## 🛠️ Tech Stack & Architecture

| Category                | Tools                                           |
| :---------------------- | :---------------------------------------------- |
| **Language**            | Python 3.12                                     |
| **Automation (CI/CD)**  | GitHub Actions                                  |
| **Tracking & Registry** | MLflow                                          |
| **Containerization**    | Docker, Docker Hub                              |
| **Web Frameworks**      | FastAPI, Streamlit                              |
| **Machine Learning**    | Scikit-Learn, XGBoost, Imbalanced-Learn (SMOTE) |

---

## 🏗️ The 6-Stage Lifecycle

Each stage is a self-contained module located in `src/mlProject/pipeline`:

1.  **Data Ingestion**: Automated retrieval and extraction of the Telco Churn dataset.
2.  **Data Validation**: Strict schema enforcement to prevent "Training-Serving Skew".
3.  **Data Transformation**: Orchestration of one-hot encoding, feature scaling, and SMOTE-based class balancing.
4.  **Model Trainer**: Automated hyperparameter optimization using GridSearchCV.
5.  **Model Evaluation**: Deep dive into Accuracy, Recall, and ROC-AUC metrics; logs artifacts to MLflow.
6.  **Prediction Service**: The UI & API bridge that serves the production model to the world.

---

## ⚡ Quick Start

### 🔌 Local Development

```bash
# 1. Clone & Enter
git clone https://github.com/HoangKhang226/MLOps.git && cd MLOps

# 2. Setup Environment
python -m venv venv
source venv/Scripts/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .

# 3. Run the ML Pipeline
python main.py

# 4. Launch Services (FastAPI & Streamlit)
bash start.sh
```

### 🐳 Docker (Instant Deployment)

Run the entire production stack with one command:

```bash
docker run -p 8000:8000 -p 8501:8501 hoangkhang226/mlop-churn:latest
```

---

## 📂 Project Navigation

```text
.
├── .github/workflows/    # CI/CD Heart (GitHub Actions)
├── app.py                # FastAPI Backend Service
├── streamlit_app.py      # Streamlit Frontend Dashboard
├── main.py               # Central Pipeline Orchestrator
├── artifacts/            # Intermediate Data & Model Storage
├── tests/                # Automated Unit Tests
└── src/mlProject/
    ├── components/       # Technical Logic for Stages
    ├── pipeline/         # Workflow Definition
    └── config/           # Centralized Configuration
```

---

## 🤝 Contributing & Security

This project is maintained by **[HoangKhang226](https://github.com/HoangKhang226)**.
To contribute or fork, ensure you configure `DOCKER_USERNAME` and `DOCKER_PASSWORD` in your repository's GitHub Secrets to enable the automated CI/CD pipeline.

---

_Built with passion for modern MLOps standards._
