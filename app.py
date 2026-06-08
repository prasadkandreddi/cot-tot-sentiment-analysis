import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from prompts import cot_prompt, tot_prompt

# -----------------------------
# Load API Key
# -----------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="CoT & ToT Project",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Chain-of-Thought & Tree-of-Thought Project")

tab1, tab2 = st.tabs(
    [
        "Task 1 - Sentiment Analysis",
        "Task 2 - Hyperparameter Tuning"
    ]
)

# ====================================================
# TASK 1
# ====================================================

with tab1:

    st.header("Customer Review Sentiment Analysis")

    review = st.text_area(
        "Enter Customer Review",
        height=150
    )

    if st.button("Analyze Sentiment"):

        if review.strip():

            prompt = cot_prompt.format(
                review=review
            )

            with st.spinner("Analyzing..."):

                response = model.generate_content(
                    prompt
                )

            st.subheader("Chain-of-Thought Analysis")
            st.write(response.text)

        else:
            st.warning("Please enter a review.")

# ====================================================
# TASK 2
# ====================================================

with tab2:

    st.header("Tree-of-Thought Hyperparameter Tuning")

    if st.button("Run Hyperparameter Search"):

        with st.spinner("Training models..."):

            data = load_breast_cancer()

            X = data.data
            y = data.target

            param_grid = {
                "n_estimators": [50, 100, 200],
                "max_depth": [5, 10, None],
                "min_samples_split": [2, 5]
            }

            rf = RandomForestClassifier(
                random_state=42
            )

            grid = GridSearchCV(
                rf,
                param_grid,
                cv=5,
                scoring="accuracy",
                return_train_score=True,
                n_jobs=-1
            )

            grid.fit(X, y)

            results = pd.DataFrame(
                grid.cv_results_
            )

            results["overfit_gap"] = (
                results["mean_train_score"]
                - results["mean_test_score"]
            )

            display_df = results[
                [
                    "param_n_estimators",
                    "param_max_depth",
                    "param_min_samples_split",
                    "mean_train_score",
                    "mean_test_score",
                    "mean_fit_time",
                    "overfit_gap"
                ]
            ]

            st.subheader("Grid Search Results")
            st.dataframe(display_df)

            top10 = display_df.sort_values(
                by="mean_test_score",
                ascending=False
            ).head(10)

            prompt = tot_prompt.format(
                results=top10.to_string(index=False)
            )

            response = model.generate_content(
                prompt
            )

            st.subheader("Tree-of-Thought Analysis")
            st.write(response.text)

            st.success(
                f"Best Accuracy: {grid.best_score_:.4f}"
            )

            st.info(
                f"Best Parameters: {grid.best_params_}"
            )