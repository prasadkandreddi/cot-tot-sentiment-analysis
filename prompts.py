cot_prompt = """
You are an expert sentiment analyst.

Analyze the customer review step by step.

Step 1: Identify all positive sentiment phrases.
Step 2: Identify all negative sentiment phrases.
Step 3: Determine sentiment strength.
Step 4: Check for mixed or contradictory opinions.
Step 5: Explain the reasoning.
Step 6: Decide the final sentiment.

Output Format:

Positive Evidence:
- ...

Negative Evidence:
- ...

Sentiment Strength:
- ...

Mixed Sentiment Check:
- ...

Reasoning:
...

Final Sentiment:
Positive / Neutral / Negative

Review:
{review}
"""


tot_prompt = """
You are a Machine Learning expert.

Analyze the following Random Forest hyperparameter tuning results using Tree-of-Thought reasoning.

Results:

{results}

Branch 1: Validation Performance
- Identify configurations with highest validation accuracy.

Branch 2: Overfitting Analysis
- Compare train score and validation score.
- Identify models that overfit.

Branch 3: Underfitting Analysis
- Identify models that underfit.

Branch 4: Computational Cost
- Compare training times.

Branch 5: Generalization
- Find configurations with best balance of performance and robustness.

Final Decision:
- Recommend the best configuration.
- Explain why it is preferred.

Output Format:

Tree-of-Thought Analysis

Branch 1:
...

Branch 2:
...

Branch 3:
...

Branch 4:
...

Branch 5:
...

Recommended Configuration:
...

Reason:
...
"""