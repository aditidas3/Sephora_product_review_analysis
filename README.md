# Sephora Product Reviews Analysis & Recommendation System

## Overview

This project analyzes Sephora product reviews to understand customer sentiment, uncover key skincare concerns, and predict whether a product is likely to be recommended by users.
Using natural language processing (NLP), topic modeling, and machine learning, the project bridges customer feedback analysis with predictive recommendation modeling.

The goal is not only to extract insights from unstructured review text, but also to demonstrate how these insights can inform data-driven product recommendations.

---

## Problem Statement

Customer ratings alone do not fully capture user satisfaction or dissatisfaction.
This project addresses the following questions:

* What sentiments do customers express in product reviews?
* What recurring skincare concerns emerge from user feedback?
* How do concerns vary across skin types and product categories?
* Can we predict whether a product will be recommended based on review content and product features?

---

## Dataset

* Source: Kaggle – Sephora Product Reviews Dataset
* Data Includes:
  * Product metadata
  * Customer reviews and ratings

---

## Project Structure

```
project-name/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/                        
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_sentiment.ipynb
│   ├── 03_topics.ipynb
│   └── 04_recommendation.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── sentiment.py
└── .gitignore
```

---

## Analysis Workflow

### 01. Exploratory Data Analysis

* Product popularity and review volume trends
* Price distribution and brand positioning
* Offline vs online sales behavior
* Temporal trends in ratings and feedback volume

*Key Insight:*
Skincare products dominate customer engagement, with noticeable growth after 2016 and peak activity around 2020.

---

### 02. Sentiment Analysis

* Text preprocessing (cleaning, tokenization, lemmatization)
* Sentiment labeling using:

  * Rating-based heuristics
  * VADER sentiment scoring
* Visualization of sentiment-specific keywords

*Key Insight:*
Sentiment scores correlate positively with ratings, but textual sentiment provides additional nuance beyond numerical ratings alone.

---

### 03. Topic Modeling (Latent Dirichlet Allocation)

* Applied Latent Dirichlet Allocation (LDA) to negative and neutral reviews
* Identified major concern themes such as:

  * Acne and breakouts
  * Dry and sensitive skin
  * Eye care effectiveness
  * Product dissatisfaction (smell/texture)
* Topic distribution analyzed across:

  * Skin types
  * Product categories
* Ingredient-specific concern analysis using keyword matching

*Key Insight:*
Certain skincare concerns and ingredients appear disproportionately in negative reviews, especially among sensitive and acne-prone skin types.

---

### 04. Recommendation Prediction

* Target variable: `is_recommended`
* Feature set includes:

  * Product attributes
  * Sentiment scores
  * Topic labels
  * Skin type and category information
* Model progression:

  * Baseline logistic regression
  * Tree-based models
  * XGBoost (final model)

Final Model Performance:

* Accuracy: ~75%
* AUC-ROC: ~0.83

*Key Insight:*
Review sentiment and topic-level concerns are among the strongest predictors of product recommendation likelihood.

---

## Key Findings

* Textual reviews provide richer insight than ratings alone
* Topic modeling reveals actionable skincare concerns
* Ingredient mentions align with negative sentiment patterns
* Combining NLP features with structured product data improves recommendation prediction

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK / VADER / TextBlob
* XGBoost
* Matplotlib, Seaborn

---

## How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run notebooks sequentially from `01_eda.ipynb` to `04_recommendation.ipynb`

---

## Future Improvements

* Use transformer-based embeddings for review text
* Incorporate collaborative filtering for hybrid recommendations
* Perform topic coherence optimization
* Deploy model as a lightweight recommendation API

---

## Author

Aditi Das
Data Science | Machine Learning | NLP

---

