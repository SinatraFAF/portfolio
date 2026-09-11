# Handwritten Digit Classifier

An image classification model that recognises handwritten digits (0-9), trained on the MNIST dataset — a classic computer vision benchmark.

## Problem Statement

Recognising handwritten digits is a foundational computer vision task with real-world applications in postal code reading, bank cheque processing, and form digitisation. This project builds and evaluates a neural network to classify digit images accurately.

## Dataset

- **Source:** MNIST [Training set](Image Recognition/optdigits.tra) and [Test set](Image Recognition/optdigits.tes)
- **Size:** 60,000 training images, 10,000 test images
- **Format:** 28x28 grayscale images
- **Target variable:** digit label (0-9)

## Approach

1. **Preprocessing** — none
2. **Model architecture** — RandomForestClassifier
3. **Training** — used training data
4. **Parameter to change** — n_estimators

## Evaluation Metrics

- **Accuracy** — overall proportion of correctly classified digits
- **Confusion matrix** — to see which digits get confused with each other

## Results

- **Final test accuracy:** 96%
<img width="302" height="125" alt="image" src="https://github.com/user-attachments/assets/d64893c5-476c-473d-a6b4-cbbe874283d1" />


## Key Insights

- We can see the following results in our confusion matrix:
  <img width="467" height="332" alt="image" src="https://github.com/user-attachments/assets/0c5c3f1b-f80c-4799-8a6e-e2132caeb721" />
- n_estimators was chosen because the number of trees is relied upon heavily in a random forest (more trees leads to more accuracy but can use more resources and take longer).  


## Tech Stack

- Python
- scipy, sklearn
- pandas, numpy, matplotlib

## How to Run

Download all files, run Jupyter notebook, important observations and explanations are present in markdown cells or as comments

## Future Improvements

- [ ] Experiment with deeper CNN architectures
- [ ] Data augmentation to improve generalisation
- [ ] Test on custom handwritten input (e.g. drawn digits via a simple UI)
