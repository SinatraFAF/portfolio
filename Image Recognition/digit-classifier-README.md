# Handwritten Digit Classifier

An image classification model that recognises handwritten digits (0-9), trained on the MNIST dataset — a classic computer vision benchmark.

## Problem Statement

Recognising handwritten digits is a foundational computer vision task with real-world applications in postal code reading, bank cheque processing, and form digitisation. This project builds and evaluates a neural network to classify digit images accurately.

## Dataset

- **Source:** MNIST (via `keras.datasets` / `torchvision.datasets`)
- **Size:** 60,000 training images, 10,000 test images
- **Format:** 28x28 grayscale images
- **Target variable:** digit label (0-9)

## Approach

1. **Preprocessing** — normalised pixel values (0-1), reshaped images for model input, one-hot encoded labels (if applicable)
2. **Model architecture** — [MLP / CNN — describe layers, e.g. Conv2D → MaxPooling → Dense layers]
3. **Training** — loss function (categorical cross-entropy), optimizer (Adam), number of epochs, batch size
4. **Validation** — held-out validation split to monitor overfitting

## Evaluation Metrics

- **Accuracy** — overall proportion of correctly classified digits
- **Confusion matrix** — to see which digits get confused with each other

## Results

- **Final test accuracy:** [X]%
- [Add training/validation accuracy and loss curves]
- [Add confusion matrix image]
- [Add grid of sample correct vs. incorrect predictions]

## Key Insights

- [Which digits are most commonly confused, e.g. 4 vs 9, 3 vs 5]
- [Effect of architecture choices on performance]

## Tech Stack

- Python
- TensorFlow/Keras (or PyTorch)
- numpy, matplotlib

## How to Run

```bash
git clone [repo-url]
cd digit-classifier
pip install -r requirements.txt
jupyter notebook digit_classifier.ipynb
```

## Repo Structure

```
digit-classifier/
├── notebooks/
│   └── digit_classifier.ipynb
├── requirements.txt
└── README.md
```

## Future Improvements

- [ ] Experiment with deeper CNN architectures
- [ ] Data augmentation to improve generalisation
- [ ] Test on custom handwritten input (e.g. drawn digits via a simple UI)

## Contact

[Your name] | [LinkedIn] | [GitHub]
