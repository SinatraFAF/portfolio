# Exploratory Data Analysis Report

An in-depth exploratory data analysis (EDA) of the Automobile dataset, aimed at uncovering patterns, relationships, and data quality issues before any modelling work.

## Objective

There is no set question that needs to be answered, but we can indeed observe and find our own. These are the questions I have chosen to answer:

● Which are the 5 most expensive cars?

● Which manufacturer builds the most fuel efficient vehicles? 

● Which vehicles have the largest engine capacity? 

● Which vehicle manufacturer has the most car models in the dataset

## Dataset

- **Source:** [clickable text]Automobile EDA/automobile.txt
- **Size:** 26 columns and 206 rows.
- **Features:** Focus was placed on the following for the purpose of answering the chosen questions:

● Make (Categorical - Nominal)

● Body Style (Categorical - Nominal) 

● Wheel Base (Numerical - Continuous) 

● Curb Weight (Numerical - Continuous) 

● The length, width and height (Numerical - Continuous) 

● Engine Size (Numerical - Continuous) 

● Horsepower (Numerical - Continuous) 

● City and Highway MPG (Numerical - Continuous) 

● Price - (Numerical - Continuous)

## Approach

1. **Data overview** — shape, data types, missing values, duplicates
2. **Univariate analysis** — distributions of individual features (histograms, boxplots, value counts)
3. **Bivariate/multivariate analysis** — relationships between features and the variable(s) of interest (scatter plots, correlation heatmaps, group comparisons)
4. **Outlier detection** — identifying and assessing extreme values
5. **Missing value analysis** — patterns in missingness and how they were handled

## Key Findings

- Lighter hatchbacks tend to be more fuel efficient than larger, heavier sedans
- The most powerful car from the group of the 5 most expensive cars occupies the smallest physical space
- Chevrolet is by far the most fuel efficient car manufacturer (based on this data)
- German cars tend to be larger, heavier and more expensive whereas Japanese cars tend to be small, light and cheap
- The dataset itself does not explicitly tell us what each value is a measure of, so some inference must be made there

## Visualizations

This report includes:
- Bar charts comparing the car manufacturers and fuel efficiency
- Scatter plot to compare engine size and fuel efficiency
- Pie chart comparing the distribution of car manufacturers in the data
- Screenshots from the notebook were also used when appropriate

## Tech Stack

- Python
- pandas, numpy
- matplotlib, seaborn

## How to Run

```bash
git clone [repo-url]
cd eda-report
pip install -r requirements.txt
jupyter notebook eda_report.ipynb
```

## Repo Structure

```
eda-report/
├── data/
├── notebooks/
│   └── eda_report.ipynb
├── requirements.txt
└── README.md
```

## Future Improvements

- [ ] Use findings to inform feature engineering for a downstream model
- [ ] Add statistical tests to confirm significance of observed patterns
- [ ] Build an interactive dashboard version (e.g. with Plotly/Streamlit)
