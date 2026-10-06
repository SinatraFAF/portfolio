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
3. **Modeling**
- Split the data into independent variables (`Gr_Liv_Area`, `Garage_Area`) and the dependent variable (`SalePrice`)
- Split into training and test sets (75% train / 25% test)
- Built a multiple linear regression model on the training set using both predictors
- Printed the model's intercept and coefficients


## Evaluation

- Generated predictions on the test set
- Computed MSE / RMSE on the test set
- Generated an error plot comparing predicted vs. actual `SalePrice` values on the test set

## Results

<img width="298" height="87" alt="image" src="https://github.com/user-attachments/assets/72a1ed7e-5e18-4588-aa02-2642d1a99252" />


Using the model we can predict the sale price for a house and how certain factor can influence this price
<img width="1369" height="354" alt="image" src="https://github.com/user-attachments/assets/20e7d0e9-9b89-4a2c-a340-81876b9419ae" />

The error plot shows results tend to fall close to 0 (and outliers seem to be unique houses/cases):
<img width="613" height="448" alt="image" src="https://github.com/user-attachments/assets/70bf8fa7-ca81-4073-b969-ffff2c961f8b" />



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
