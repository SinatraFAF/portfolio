# House Price Prediction

A regression model that estimates residential property sale prices based on property characteristics, built to support pricing decisions for buyers, sellers, or agents.

## Problem Statement

Accurately pricing a property is difficult given the number of interacting factors (location, size, number of floors, amenities). This project builds a model to predict sale price from structured property data, helping remove some of the guesswork from pricing.

## Dataset

- **Source:** [Ames, Iowa Assessor’s Office](ames.csv)
- **Size:**  2930 observations and a large number of explanatory variables 
- **Features:** 23 nominal, 23 ordinal, 14 discrete, and 20 continuous
- **Target variable:** `Sale_Price` (continuous)

## Approach

1. **Exploratory Data Analysis** — examined price distribution, correlations between features and price, and identified outliers
2. **Preprocessing** — handled missing values, removed duplicates, encoded categorical features, scaled numeric features, engineered new features where useful (e.g. house age, total square footage)
3. **Modeling** — trained and compared:
   - Multiple Linear Regression

## Evaluation Metrics

- **MSE** (Mean Squared Error) — average of the squares of the errors
- **RMSE** (Root Mean Squared Error) — penalises large errors, in same units as price
- **R²** — proportion of variance in price explained by the model

## Results

| Model |  MSE | RMSE | R² |
--Placeholder--
|---|---|---|---|
| Multiple Linear Regression | – | – | – |

[Add actual vs. predicted price scatter plot here]

## Key Insights
--Placeholders--
- [Most influential features on price, e.g. square footage, overall quality]
- [Any nonlinear relationships or interactions discovered]

## Tech Stack

- Python
- pandas, numpy
- scikit-learn,
- matplotlib, seaborn

## How to Run

Download all files, run Jupyter Notebook, look at visualisations. Observations are present in comments or markdown cells.
```

## Future Improvements

- [ ] Feature engineering pass (interaction terms, polynomial features)
- [ ] Try stacking/ensemble of top models
- [ ] Deploy as a simple web app for interactive price estimates
