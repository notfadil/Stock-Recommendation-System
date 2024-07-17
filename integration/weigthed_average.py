import json

def weighted_average(predictions, weights):
    combined_prediction = sum(pred * weight for pred, weight in zip(predictions, weights))
    total_weight = sum(weights)
    return combined_prediction / total_weight

def get_news_score(stock, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data.get(stock, [0])[0]  # Return 0 if stock not found

stock = 'apple'
sentiment_file_path = 'data/avg_sentiments.json'

# Example predictions from three models
news_sentiment_prediction = get_news_score(stock, sentiment_file_path)  # Get sentiment from file
print("news_sentiment_prediction",news_sentiment_prediction)
price_prediction = 0.4  # Hold
technical_indicator_prediction = 0.3  # Sell

# Weights for each model (sum should be 1 for simplicity, but can be any positive values)
weights = [0.5, 0.3, 0.2]

# Combine the predictions
combined_prediction = weighted_average(
    [news_sentiment_prediction, price_prediction, technical_indicator_prediction], weights)

print(f"Combined Prediction: {combined_prediction}")

# Interpretation of combined prediction
if combined_prediction >= 0.5:
    print("Buy")
elif combined_prediction <= -0.5:
    print("Sell")
else:
    print("Hold")
