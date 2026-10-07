# Handwritten Digit Classifier

A Random Forest classifier that recognises handwritten digits (0–9) using the UCI Optical Recognition of Handwritten Digits dataset.

## Problem Statement

Recognising handwritten digits is a foundational classification task with real-world applications such as postal code reading and form digitisation. This project trains and evaluates a Random Forest model on pre-processed digit bitmaps, with a focus on deliberate hyperparameter tuning and thorough performance evaluation beyond accuracy alone.

## Dataset

- **Source:** [Optical Recognition of Handwritten Digits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits)
- **Collection:** handwritten digits from 43 individuals — 30 contributing to the training set, 13 to the test set
- **Format:** original 32x32 bitmaps, downscaled to 8x8 matrices (64 features per sample)
- **Target variable:** digit label (0–9)

## Approach

1. **Preprocessing** — None, data was simply loaded into the Jupyter notebook
2. **Model architecture** — RandomForestClassifier
3. **Training** — used training dataset
4. **Hyperparameter tuning** — 'n_estimators', chosen because the number of trees is relied upon heavily in a random forest (more trees leads to more accuracy but can use more resources and take longer).

## Evaluation Metrics

- **Confusion matrix** — to see which digits are most often confused with each other, and identify the class with the highest number of misclassifications
- **Accuracy** — overall proportion of correctly classified digits
- **Precision, Recall, F1-score** — computed with `average="macro"` (via `precision_score`, `recall_score`, `f1_score` from scikit-learn) to weight all ten digit classes equally

## Results

- **Value used:** 50 — chosen because it had the second highest accuracy, could run fast and use less memory than 200
<img width="216" height="182" alt="image" src="https://github.com/user-attachments/assets/63846bd6-d788-4129-9669-3eb0bc566f76" />

- **Class with the most misclassifications:** – 8 and 9
- **Final test accuracy:** 96%
<img width="302" height="125" alt="image" src="https://github.com/user-attachments/assets/d64893c5-476c-473d-a6b4-cbbe874283d1" />


## Key Insights

- We can see the following results in our confusion matrix:
<img width="467" height="332" alt="image" src="https://github.com/user-attachments/assets/0c5c3f1b-f80c-4799-8a6e-e2132caeb721" />

- Both digit 8 and 9 have 12 misclassifications, significantly more than other digits


## Tech Stack

- Python
- scipy, sklearn
- pandas, numpy, matplotlib

## How to Run

Download all files, run Jupyter notebook, important observations and explanations are present in markdown cells or as comments
