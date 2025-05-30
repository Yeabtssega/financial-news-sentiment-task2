# Financial News Sentiment Analysis

This project analyzes financial news articles and headlines to determine their sentiment (positive, neutral, or negative) using natural language processing (NLP).
## Objective

To help investors and analysts understand how news impacts stock prices by automating sentiment analysis using machine learning and NLP techniques.
## Data

The dataset used includes financial news headlines scraped from [source]. It was cleaned and preprocessed for sentiment classification.
## Tools & Libraries

- Python 3.11
- pandas, numpy
- matplotlib, seaborn
- nltk, scikit-learn
- FinBERT / PyTorch (for sentiment analysis)
## Methodology

1. Load and clean the news data.
2. Preprocess text (tokenization, stopword removal, etc.).
3. Apply FinBERT model for sentiment classification.
4. Analyze and visualize sentiment trends.
## Results

- Accuracy: 83%
- Most news headlines are neutral, followed by negative, then positive.
## How to Run

1. Clone the repo.
2. Install the requirements: `pip install -r requirements.txt`
3. Run: `python sentiment_analysis.py`
## Future Work

- Compare different sentiment models (FinBERT vs. others)
- Include live stock price data
- Create a dashboard for real-time insights




