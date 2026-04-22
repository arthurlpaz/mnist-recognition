# 🧠 MNIST Recognition — End-to-End ML System

Machine Learning including:

* Model training (CNN)
* Experiment versioning (MLflow)
* Inference API (FastAPI)
* Upload of real images (PNG/JPG)
* Batch inference
* Feature Store (abstraction)
* Monitoring (Prometheus-ready)
* Multi-model + A/B testing
* Docker + Deploy

---

# 🚀 Overview

This project simulates a real ML production environment:

```text
Client → API → Model Router → Model Service → Feature Store → Monitoring
```

Supports:

* 🔹 Real-time inference (API)
* 🔹 Batch processing (batch)
* 🔹 Observability (metrics)

---

# 🏗️ Project Structure

```
mnist-recognition/
│
├── configs/
├── data/
├── models/
├── logs/
│
├── src/
│   ├── api/
│   ├── batch/
│   ├── data/
│   ├── evaluation/
│   ├── features/
│   ├── models/
│   ├── monitoring/
│   ├── pipelines/
│   └── utils/
│
├── tests/
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

---

# ⚙️ Environment Setup

## 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Model Training

```bash
python main.py
```

Output:

* Model saved in: `models/model.keras`
* Training logs via MLflow

---

# 🌐 Running the API

```bash
uvicorn src.api.app:app --reload
```

Access:

```
http://localhost:8000/docs
```

---

# 🧠 Technologies Used

* TensorFlow
* FastAPI
* MLflow
* Docker
* NumPy / Scikit-learn

---

# 👨‍💻 Author

Arthur Lincoln da Paz
