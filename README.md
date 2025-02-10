# Stock Recommendation System

This project presents an advanced **Stock Recommendation System** that integrates **Sentiment Analysis** of financial news with **Technical Indicators** to provide short-term stock recommendations. Additionally, it utilizes **Long Short-Term Memory (LSTM)** networks to forecast long-term stock price movements.

---

## 📌 Project Overview

Investors often struggle with making informed decisions due to the overwhelming volume of financial data and market sentiment. This project aims to enhance stock prediction by combining:

- **📈 Technical Indicators:** Analyzing historical stock data trends and momentum indicators.
- **📰 Sentiment Analysis:** Assessing market sentiment from financial news using Natural Language Processing (NLP).
- **📊 Price Prediction Model:** Using LSTM networks to forecast future stock prices based on historical data.

### 🔍 Key Features:
✔ **Multi-Model Approach:** Combines Sentiment Analysis, Technical Indicators, and LSTM models.  
✔ **Short-Term & Long-Term Analysis:** Provides both immediate trading signals and future price predictions.  
✔ **Real-Time Data Integration:** Fetches stock market data using **YFinance API** and news sentiment from **GNews API**.  
✔ **Machine Learning-Powered Analysis:** Utilizes **SVM, Random Forest, and Multinomial Naïve Bayes** for sentiment classification.  

---

## 🏗️ Project Architecture

![Flowchart](<images/flowchart.png>)

The system consists of **three primary models**:

1. **📉 Long-Term Price Prediction Model (LSTM)**  
   - Forecasts future stock prices using historical stock data.  
   - Uses **Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R²** for evaluation.  

2. **📊 Short-Term Recommendation Model**  
   - Integrates **Technical Indicators** and **News Sentiment Model** to provide **Buy, Sell, or Hold** recommendations.  

3. **📡 Data Sources:**  
   - **Stock Data:** Extracted using **YFinance API**.  
   - **News Data:** Fetched via **GNews API**.  
   - **Sentiment Dataset:** FinancialPhraseBank dataset for training Sentiment Analysis model.  

---

## 📊 Data Collection & Processing

| **Data Source** | **Details** |
|----------------|------------|
| **YFinance API** | Fetches **5 years** of historical stock data (Open, Close, Volume, etc.) |
| **GNews API** | Retrieves financial news articles for sentiment analysis |
| **Financial PhraseBank** | Labeled financial statements for training Sentiment Analysis model |

### 📌 Data Preprocessing:
✔ Removing duplicates and irrelevant columns.  
✔ Normalizing stock price data using **MinMaxScaler**.  
✔ Tokenizing & vectorizing text for sentiment analysis.  

---

## 📈 Methodology

### **1️⃣ Long-Term Stock Price Prediction (LSTM)**
- Uses **four LSTM layers** followed by Dropout layers to prevent overfitting.  
- **Optimizer:** Adam, **Loss Function:** MSE, **Epochs:** 50, **Batch Size:** 32.  
- Trained on **70%** of the dataset, tested on **30%**.  
- Performance evaluation using **MSE, RMSE, MAE, and R² metrics**.  

![Price Prediction Example](<images/pricepredictionexample.png>)
![](<images/pricepredictionexample2.png>)

### **2️⃣ Short-Term Recommendation Model**

#### **(a) News Sentiment Analysis Model**
- Classifies financial news articles into **Positive, Negative, or Neutral** using:  
  ✔ **Multinomial Naïve Bayes (MNB)**  
  ✔ **Support Vector Machine (SVM) - Best Model**  
  ✔ **Random Forest (RF)**  
- **Best performing model:** **SVM with 79.75% accuracy**.  

![Flowchart](<images/newssentimentflowchart.png>)

#### **(b) Technical Indicators Model**
- Uses four key indicators:  
  ✔ **Moving Average (MA)**: Identifies trends.  
  ✔ **Relative Strength Index (RSI)**: Detects overbought/oversold conditions.  
  ✔ **Average Directional Index (ADX)**: Measures trend strength.  
  ✔ **On-Balance Volume (OBV)**: Analyzes volume flow.  

✔ **Buy Signal:** If RSI < 30, Price > 50-day MA.  
✔ **Sell Signal:** If RSI > 70, Price < 50-day MA.  

### **3️⃣ Model Integration**
- **Final Recommendation Score = 40% Sentiment Analysis + 60% Technical Indicators**  
- Weighted combination determines **Buy, Sell, or Hold** signal.  

![Results](<images/integratedresult.png>)

---

## 🏆 Results & Accuracy

| Model | Accuracy |
|---------|-----------|
| **LSTM Stock Price Prediction** | RMSE: 4.2 |
| **Technical Indicators Model (TIM)** | 67.07% |
| **News Sentiment Model (SVM)** | 79.75% |
| **Final Weighted Model (TIM + Sentiment)** | **71.95%** |

🔹 The final **Short-Term Model** improved accuracy by **5%** over the Technical Indicators alone.  
🔹 The **Hold signal** accuracy significantly improved after integrating sentiment analysis.  

---
