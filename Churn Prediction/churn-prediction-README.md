# Customer Churn Prediction

Predicting which customers are likely to churn (cancel or stop using a service) using historical customer data, so that retention efforts can be targeted before it's too late.

## Problem Statement

Customer churn is costly — acquiring a new customer typically costs more than retaining an existing one. This project builds a classification model that flags customers at high risk of churning, giving the business a chance to intervene (offers, outreach, support) before losing them.

## Dataset

- **Source:** [add dataset source/link]
- **Size:** [X rows, Y features]
- **Features:** mix of demographic, account, and usage data (e.g. tenure, contract type, monthly charges, service usage)
- **Target variable:** `Churn` (binary — Yes/No)

## Approach

1. **Exploratory Data Analysis** — checked class balance, distributions, and relationships between features and churn
2. **Preprocessing** — handled missing values, encoded categorical variables, scaled numeric features, addressed class imbalance (e.g. SMOTE / class weighting)
3. **Modeling** — trained and compared multiple classifiers:
   - Logistic Regression (baseline)
   - Random Forest
   - XGBoost
4. **Hyperparameter tuning** — [GridSearchCV / RandomizedSearchCV, if used]

## Evaluation Metrics

Since churn datasets are typically imbalanced, accuracy alone is misleading. This project prioritises:
- **Precision** — of predicted churners, how many actually churned
- **Recall** — of actual churners, how many were caught
- **F1-score** — balance of precision and recall
- **ROC-AUC** — overall model discrimination ability

## Results

| Model | Precision | Recall | F1-score | ROC-AUC |
|---|---|---|---|---|
| Logistic Regression | – | – | – | – |
| Random Forest | – | – | – | – |
| XGBoost | – | – | – | – |

[Add confusion matrix / ROC curve image here]

## Key Insights

- [Top features driving churn, e.g. contract type, tenure, monthly charges]
- [Any surprising patterns found during analysis]

## Tech Stack

- Python
- pandas, numpy
- scikit-learn, XGBoost
- matplotlib, seaborn

## How to Run

```bash
git clone [repo-url]
cd churn-prediction
pip install -r requirements.txt
jupyter notebook churn_prediction.ipynb
```

## Repo Structure

```
churn-prediction/
├── data/
├── notebooks/
│   └── churn_prediction.ipynb
├── requirements.txt
└── README.md
```

## Future Improvements

- [ ] Try additional models (e.g. LightGBM, neural network)
- [ ] Deploy as an API for real-time churn scoring
- [ ] Add SHAP values for model explainability

## Contact

[Your name] | [LinkedIn] | [GitHub]
