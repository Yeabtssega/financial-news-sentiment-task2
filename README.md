# Financial News Sentiment Analysis

This project analyzes financial news articles and headlines to determine their sentiment (positive, neutral, or negative) using natural language processing (NLP).
## Objective

# 📰📈 Financial News Sentiment Analysis with Stock Prices

This project analyzes the sentiment of financial news headlines and examines how it correlates with daily stock price movements for companies like Apple (AAPL), Amazon (AMZN), and others.

## 🧠 Project Objective

To explore whether sentiment from financial news headlines can help explain or predict stock market movements. This is part of Task 2 of a larger financial analytics project.


## 🔧 Features

- Cleans and preprocesses financial news headlines using `NLTK`
- Applies sentiment analysis using **VADER**
- Calculates **technical indicators** (SMA, RSI, MACD) using `TA-Lib`
- Calculates **financial metrics** (daily returns, volatility) using `PyNance`
- Combines **sentiment scores** with **stock price data**
- Visualizes sentiment vs stock price trends using `matplotlib`

---

## 📁 Project Structure

```bash
 Stock Analysis/
├── AAPL.csv                         # Historical stock data from Yahoo Finance
├── news_with_sentiment.csv         # Headlines with sentiment scores
├── AAPL_sentiment_combined.csv     # Merged stock + sentiment data
├── sentiment_analysis.py           # Script to clean headlines + analyze sentiment
├── task2_analysis.py               # Script to calculate indicators for all stocks
├── combine_sentiment_price.py      # Merges sentiment and stock prices
├── plot_sentiment_vs_price.py      # Visualizes sentiment vs stock
├── aapl_sentiment_plot.png         # Saved plot image


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




