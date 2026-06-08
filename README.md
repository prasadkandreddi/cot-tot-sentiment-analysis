# 🧠 CoT & ToT Reasoning Framework for Sentiment Analysis and Hyperparameter Optimization

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Gemini](https://img.shields.io/badge/LLM-Gemini-orange)
![Scikit-Learn](https://img.shields.io/badge/ML-ScikitLearn-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

This project demonstrates how Large Language Models (LLMs) can be combined with structured reasoning techniques to solve real-world NLP and Machine Learning tasks.

The project contains two reasoning modules:

### 🔹 Task 1 — Chain-of-Thought (CoT) Sentiment Analysis

Customer reviews are analyzed using Gemini LLM and Chain-of-Thought prompting.

The model:

- Identifies positive phrases
- Identifies negative phrases
- Detects mixed sentiment
- Performs reasoning-based classification
- Predicts final sentiment

### 🔹 Task 2 — Tree-of-Thought (ToT) Hyperparameter Analysis

A Random Forest model is trained using GridSearchCV.

The resulting configurations are analyzed using Tree-of-Thought reasoning to:

- Compare candidate models
- Analyze bias-variance tradeoffs
- Detect overfitting
- Evaluate training cost
- Recommend the optimal configuration

---

# 🎯 Objectives

### Task 1

Build an intelligent sentiment analysis system capable of:

- Understanding customer reviews
- Performing step-by-step reasoning
- Producing explainable sentiment predictions

### Task 2

Build an AI-assisted model selection framework capable of:

- Evaluating multiple ML configurations
- Performing reasoning over performance metrics
- Selecting the most suitable model

---

# 🏗️ System Architecture

```text
Customer Review
       │
       ▼
Chain-of-Thought Prompt
       │
       ▼
Gemini LLM
       │
       ▼
Sentiment Classification
```

```text
Dataset
   │
   ▼
Random Forest
   │
   ▼
GridSearchCV
   │
   ▼
Performance Metrics
   │
   ▼
Tree-of-Thought Prompt
   │
   ▼
Gemini LLM
   │
   ▼
Best Hyperparameter Recommendation
```

---

# 🧠 Chain-of-Thought Workflow

The LLM follows a structured reasoning pipeline:

### Step 1
Identify positive phrases.

### Step 2
Identify negative phrases.

### Step 3
Measure sentiment strength.

### Step 4
Check contradictory opinions.

### Step 5
Generate reasoning.

### Step 6
Predict final sentiment.

---

# 🌳 Tree-of-Thought Workflow

The LLM explores multiple reasoning branches.

### Branch 1
Validation Performance Analysis

### Branch 2
Overfitting Detection

### Branch 3
Underfitting Detection

### Branch 4
Training Time Comparison

### Branch 5
Generalization Analysis

### Final Branch
Optimal Hyperparameter Recommendation

---

# 📊 Machine Learning Configuration

### Algorithm

Random Forest Classifier

### Dataset

Breast Cancer Dataset (Scikit-Learn)

### Hyperparameter Space

```python
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [5, 10, None],
    "min_samples_split": [2, 5]
}
```

### Evaluation Metrics

- Cross Validation Accuracy
- Training Accuracy
- Validation Accuracy
- Overfitting Gap
- Training Time

---

# 🚀 Features

### Sentiment Analysis

✅ Positive Classification

✅ Neutral Classification

✅ Negative Classification

✅ Explainable Predictions

✅ Chain-of-Thought Reasoning

### Hyperparameter Analysis

✅ Grid Search CV

✅ Random Forest Optimization

✅ Overfitting Detection

✅ Tree-of-Thought Reasoning

✅ Automated Model Recommendation

### Deployment

✅ Streamlit Web Application

✅ GitHub Version Control

✅ Gemini API Integration

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas |
| Model Selection | GridSearchCV |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
cot-tot-sentiment-analysis/
│
├── app.py
├── prompts.py
├── requirements.txt
├── rf_results.csv
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/prasadkandreddi/cot-tot-sentiment-analysis.git
```

### Move into Project Folder

```bash
cd cot-tot-sentiment-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

# 📈 Sample Output

### Input Review

> This laptop is amazing. Battery life is excellent and performance is very fast.

### Output

```text
Sentiment: Positive

Reason:
The review contains strong positive phrases such as
amazing, excellent, and very fast.
```

---

# 🎓 Learning Outcomes

Through this project:

- Implemented Chain-of-Thought Prompting
- Implemented Tree-of-Thought Prompting
- Integrated Gemini LLM API
- Performed Hyperparameter Optimization
- Built Explainable AI Workflows
- Developed End-to-End Streamlit Application
- Deployed Production-Ready AI Project

---

# 👨‍💻 Author

### Prasad Kandreddi

AI / ML Engineer

**GitHub:**  
https://github.com/prasadkandreddi

**LinkedIn:**  
https://www.linkedin.com/in/kandreddi-prasad-7117952a6

---

## ⭐ If you found this project useful, please give it a star.
