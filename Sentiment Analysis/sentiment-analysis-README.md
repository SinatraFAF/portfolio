# Sentiment Analysis - Amazon Product Reviews

A sentiment analysis script that classifies Amazon product reviews as positive, negative, or neutral using spaCy and TextBlob polarity scoring.

## Problem Statement

Understanding customer sentiment at scale is valuable for monitoring product feedback and customer satisfaction without manually reading every review. This project builds a rule-based sentiment analysis pipeline using spaCy's NLP tooling and applies it to real Amazon consumer reviews.

## Dataset

- **Source:** [Amazon consumer product reviews collated by Datafiniti (Kaggle)](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products/data?select=Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv)
- **Feature used:** This dataset is a list of over 28,000 consumer reviews for Amazon products like the Kindle, Fire TV Stick, and more from Datafiniti's Product Database updated between February 2019 and April 2019
- **Note:** this is an unsupervised, rule-based approach, so no labelled target variable is used for training

## Approach

1. **Data loading** — loaded the CSV into the Jupyter notebook
2. **Model setup** — loaded the `en_core_web_md` spaCy model and added the `spacytextblob` pipeline component to expose polarity and sentiment scores
3. **Preprocessing**
   - Selected the `reviews.text` column
   - Dropped missing values
   - Cleaned text 
   - Removed stop words
4. **Sentiment function** — defined a function that takes a product review as input, preprocesses it, and returns its sentiment (−1 = very negative, 0 = neutral, +1 = very positive)
5. **Testing** — ran the function on sample reviews to verify predictions
6. **Similarity comparison** — compared pairs of reviews using spaCy's `similarity()` function (1 = more similar, 0 = not similar)

## Evaluation

- Sample reviews tested with predicted polarity/sentiment inspected against the actual review text
- Qualitative assessment of whether predictions match the apparent sentiment of each review

## Results

- **Sample predictions:** Here are 2 sample reviews:
<img width="1005" height="406" alt="image" src="https://github.com/user-attachments/assets/b990a6ff-5642-43ba-a1bd-cb89c1e9008a" />

- **Similarity example:** When these 2 reviews are compared, we get the following similarity score:
<img width="1725" height="82" alt="image" src="https://github.com/user-attachments/assets/c9a052b2-8148-400f-8b2f-9d57b83175d5" />

And when we compare the first review (negative) with a more positive review we get the following result:
<img width="878" height="56" alt="image" src="https://github.com/user-attachments/assets/4bec363f-3a28-4fe0-91a3-8ec50fead4a1" />


## Key Insights

- Words associated with both positive and negative sentiment can lead to misinterpretation
- Concepts like sarcasm, or mixed sentiment cannot be interpreted accurately all the time

## Tech Stack

- Python
- scikit-learn
- NLTK / spaCy
- pandas, matplotlib, seaborn

## How to Run

Download all the files, run the Jupyter notebook. Relevant observations are available either as comments on in markdown cells
