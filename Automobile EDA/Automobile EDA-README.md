# EDA Report – Automobile Dataset

An exploratory data analysis of the automobile dataset, cleaning and investigating vehicle characteristics and pricing data, compiled into a standalone PDF report.

## Objective

Clean, sanitise, and explore the dataset to understand its structure, quality, and underlying patterns, and answer a set of guided questions about the data — with all visualisations, investigations, and findings written up as a PDF report. Focus is placed on the following questions:

● Which are the 5 most expensive cars?

● Which manufacturer builds the most fuel efficient vehicles? 

● Which vehicles have the largest engine capacity? 

● Which vehicle manufacturer has the most car models in the dataset

## Dataset

- **Source:** [automobile.txt](automobile.txt)
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

### Data Loading & Cleaning
- Loaded the raw dataset into the notebook
- Removed duplicate rows
- Discarded entries with any missing values
- Converted relevant columns to their correct data types (e.g. numeric fields stored as strings/objects)

### Exploratory Analysis
- Answered the guided questions
- Investigated feature distributions, relationships, and any notable patterns or anomalies in the cleaned dataset

## Key Findings

- Lighter hatchbacks tend to be more fuel efficient than larger, heavier sedans
- The most powerful car from the group of the 5 most expensive cars occupies the smallest physical space
- Chevrolet is by far the most fuel efficient car manufacturer (based on this data)
- German cars tend to be larger, heavier and more expensive whereas Japanese cars tend to be small, light and cheap
- The dataset itself does not explicitly tell us what each value is a measure of, so some inference must be made there

## Visualizations

This report includes:
- Bar charts comparing the car manufacturers and fuel efficiency
  <img width="571" height="502" alt="image" src="https://github.com/user-attachments/assets/1919ec5f-c6bb-4926-b9f3-b2f2e94885e9" />

- Scatter plot to compare engine size and fuel efficiency
  <img width="572" height="448" alt="image" src="https://github.com/user-attachments/assets/26bf0fa6-6071-422c-89f6-8581ff16e281" />

- Pie chart comparing the distribution of car manufacturers in the data
  <img width="407" height="393" alt="image" src="https://github.com/user-attachments/assets/6fa18303-4a81-4a8f-b60e-7de94ef8f656" />

- Screenshots from the notebook were also used when appropriate

## Tech Stack

- Python
- pandas, numpy
- matplotlib, seaborn

## How to Run

Ensure Python and the libraries mentioned above are installed. 
Download all files in this project folder. 
The Jupyter notebook can be opened to see how the data was cleaned and used. 
The report ties things together and provides insights and answers the questions.
