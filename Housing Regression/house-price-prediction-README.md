# House Price Prediction – Ames Housing (Linear Regression)

A multiple linear regression model that estimates residential sale price from the Ames, Iowa housing dataset, using above-grade living area and garage size as predictors.

## Problem Statement

Accurately pricing a property is difficult given the number of interacting factors. This project builds a simple, interpretable multiple linear regression model to estimate SalePrice from two key size-related features, and evaluates how well those features alone explain price variation.

## Dataset

- **Source:** [Ames, Iowa Assessor’s Office](ames.csv)
- **Size:**  2930 observations and a large number of explanatory variables 
- **Features:** 23 nominal, 23 ordinal, 14 discrete, and 20 continuous
- **Target variable:** `Sale_Price` (continuous)

## Approach

1. **Preprocessing** — Cleaned and prepared the dataset as needed (missing values, data types)
2. **Exploratory Data Analysis** — Visualised the distribution of the dependent variable (SalePrice) and the two independent variables. Explored relationships and trends between Gr_Liv_Area, Garage_Area, and SalePrice via scatter plots
4. **Modeling** — trained and compared:
   - Multiple Linear Regression

## Evaluation Metrics

- **MSE** (Mean Squared Error) — average of the squares of the errors
- **RMSE** (Root Mean Squared Error) — penalises large errors, in same units as price
- **R²** — proportion of variance in price explained by the model

## Results

When we compute the MSE or RMSE, we get the following result: 
<img width="211" height="19" alt="image" src="https://github.com/user-attachments/assets/237be3f1-63b1-4f58-ac53-7b794ef99f8b" />


Using the model we can predict the sale price for a house and how certain factor can influence this price
<img width="1369" height="354" alt="image" src="https://github.com/user-attachments/assets/20e7d0e9-9b89-4a2c-a340-81876b9419ae" />


## Key Insights
The following visualisation shows us correlations between the different factors, and how these relationships can influence the price of a house:
<Figure size 1000x800 with 2 Axes><img width="881" height="786" alt="image" src="https://github.com/user-attachments/assets/8c927279-dfa1-4309-b397-507221d37bed" />


## Tech Stack

- Python
- pandas, numpy
- scikit-learn,
- matplotlib, seaborn

## How to Run

Download all files, run Jupyter Notebook, look at visualisations. Observations are present in comments or markdown cells.
```
