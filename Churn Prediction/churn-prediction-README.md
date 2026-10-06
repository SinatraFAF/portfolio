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
| Logistic Regression | 0.791 | 0.618 | 0.517 |
| Random Forest | 0.793 | 0.647 | 0.454 |

<img width="882" height="56" alt="image" src="https://github.com/user-attachments/assets/8c9e75bf-0e79-4fcd-a41c-da9a4948f665" />

The confusion matrices for both models:

<img width="291" height="122" alt="image" src="https://github.com/user-attachments/assets/8b207859-ac23-4daa-a780-64e75e2f2a75" />



## Key Insights

- Logistic Regression is better at identifying churn (lower recall)
- Churn tends to take place earlier in customer tenure:
<img width="737" height="536" alt="image" src="https://github.com/user-attachments/assets/052b3022-02ef-459c-8043-851390d5163b" />

- This portion of the correlation plot shows the top features correlated with churn:
  <img width="1087" height="527" alt="image" src="https://github.com/user-attachments/assets/ec8f8b9b-735b-466e-b227-25745a5c792f" />


## Tech Stack

- Python
- pandas, numpy
- scikit-learn
- matplotlib, seaborn

## How to Run
Download the files, run the Jupyter notebook. Noteworthy observations are available as markdown cells or comments.
