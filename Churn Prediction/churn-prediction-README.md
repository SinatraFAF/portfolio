# Customer Churn Prediction

Predicting which customers are likely to churn (cancel or stop using a service) using historical customer data, so that retention efforts can be targeted before it's too late.

## Problem Statement

Customer churn is costly — acquiring a new customer typically costs more than retaining an existing one. This project builds a classification model that flags customers at high risk of churning, giving the business a chance to intervene (offers, outreach, support) before losing them.

## Dataset

- **Source:** [Telco Customer Churn](Telco-Customer-Churn.csv)
- **Size:** 21 columns, 7043 rows
- **Features:** customer account details (tenure, contract type, payment method), billing info (MonthlyCharges, TotalCharges), and service subscriptions (phone, internet, streaming, security add-ons)
- **Target variable:** `Churn_1` (binary — Yes/No)

## Approach

**Data Inspection** — Reviewed the first 10 rows, column names, and data types to understand the raw structure
### Preprocessing:
   - Converted TotalCharges to numeric (was stored as object/string)
   - Dropped rows with missing values
   - Removed the non-predictive customerID column
   - Encoded 'Churn_1' as binary (Yes → 1, No → 0)
   - One-hot encoded categorical variables into a dummy-variable DataFrame (telecom_cust_dummies), dropping one category per feature to avoid the dummy variable trap and reduce multicollinearity
### Data Visualisation
- Correlation plot of all features against `Churn`
- Histogram of `tenure` distribution
- Scatter plot of `MonthlyCharges` vs. `TotalCharges`
- Box plot comparing `tenure` between churned and non-churned customers

### Preparing for ML
- Scaled all features to a 0–1 range using min-max scaling
- Split into training/test sets (75% train / 25% test)

## Models

### Logistic Regression
- Baseline linear classifier trained on the scaled, encoded feature set

### Random Forest
Tuned hyperparameters:
- `n_estimators` = 2000
- `oob_score` = True (out-of-bag error estimation)
- `max_features` = "sqrt"
- `max_leaf_nodes` = 50
- `bootstrap` = True

## Evaluation Metrics

Both models are evaluated beyond plain accuracy, since churn prediction has an inherent cost asymmetry between false positives and false negatives:
- **Accuracy** — overall proportion correctly classified
- **OOB error estimate** (Random Forest) — generalisation estimate computed as `1 - oob_score_`, without needing a separate validation set
- **Confusion matrix** — breakdown of true/false positives and negatives for each model
- **Precision** — of predicted churners, how many actually churned
- **Recall** — of actual churners, how many were correctly identified

## Results

| Model | Accuracy | Precision | Recall |
|---|---|---|---|
| Logistic Regression | – | – | – |
| Random Forest | – | – | – |

## Placeholder for confusion matrix

## Key Insights

- 
- 

## Tech Stack

- Python
- pandas, numpy
- scikit-learn
- matplotlib, seaborn

## How to Run
Download the files, run the Jupyter notebook. Noteworthy observations are available as markdown cells or comments.

## Future Improvements

- [ ] Try additional models (e.g. LightGBM, neural network)
- [ ] Deploy as an API for real-time churn scoring
- [ ] Add SHAP values for model explainability

## Contact

[Your name] | [LinkedIn] | [GitHub]
