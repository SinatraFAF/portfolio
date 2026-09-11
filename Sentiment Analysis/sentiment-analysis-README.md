# Sentiment Analysis

A text classification model that predicts sentiment (positive/negative, or positive/neutral/negative) from written text such as product reviews.

## Problem Statement

Understanding customer sentiment at scale is valuable for monitoring brand perception, product feedback, and customer satisfaction without manually reading every review. This project builds a model to automatically classify text sentiment.

## Dataset

- **Source:** [Kaggle](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products/data?select=Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv)
- **Size:** This dataset is a list of over 28,000 consumer reviews for Amazon products like the Kindle, Fire TV Stick, and more from Datafiniti's Product Database updated between February 2019 and April 2019
- **Class balance:** Roughly balanced
- **Labels:** Positive/Neutral/Negative

## Approach

1. **Text preprocessing** — removed rows with missing review text, lowercasing, removing leading and trailing spaces, tokenization
2. **Feature extraction** — [TF-IDF / Bag-of-Words / word embeddings]
3. **Modeling** — trained and compared:
   - Logistic Regression (baseline)
   - Naive Bayes
   - [Neural network / transformer-based model, if used]
4. **Hyperparameter tuning** — [if applicable]

## Evaluation Metrics

- **Accuracy** — overall correctness
- **Precision / Recall / F1-score** — per-class performance, especially important if classes are imbalanced
- **Confusion matrix** — to see which sentiment classes get confused

## Results

| Model | Accuracy | Precision | Recall | F1-score |
|---|---|---|---|---|
| Logistic Regression | – | – | – | – |
| Naive Bayes | – | – | – | – |

[Add confusion matrix image]
[Add example predictions — correct and incorrect]

## Key Insights

- [Common words/phrases associated with positive vs. negative sentiment]
- [Types of text the model struggles with, e.g. sarcasm, mixed sentiment]

## Tech Stack

- Python
- scikit-learn
- NLTK / spaCy
- pandas, matplotlib, seaborn

## How to Run

```bash
git clone [repo-url]
cd sentiment-analysis
pip install -r requirements.txt
jupyter notebook sentiment_analysis.ipynb
```

## Repo Structure

```
sentiment-analysis/
├── data/
├── notebooks/
│   └── sentiment_analysis.ipynb
├── requirements.txt
└── README.md
```

## Future Improvements

- [ ] Try transformer-based embeddings (e.g. BERT)
- [ ] Handle sarcasm/negation more explicitly
- [ ] Extend to multi-class or aspect-based sentiment analysis

## Contact

[Your name] | [LinkedIn] | [GitHub]
