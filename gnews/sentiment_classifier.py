import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import glob

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']

def get_stock_name(file_path):
    return os.path.basename(file_path).split('_')[-1].split('.')[0]

def process_news_data(input_file, output_file):
    # Read the JSON data from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    total_sentiment = 0
    total_articles = len(data)
    
    # Process each article and append the sentiment score
    for article in data:
        content = article.get('content', '')
        sentiment_score = analyze_sentiment(content)
        article['sentiment_score'] = sentiment_score
        total_sentiment += sentiment_score
    
    # Calculate the average sentiment score
    average_sentiment = total_sentiment / total_articles if total_articles > 0 else 0
    
    # Write the updated data back to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)
    
    print(f"Average Sentiment Score for {get_stock_name(output_file)}: {average_sentiment}({total_articles})")
    return average_sentiment, total_articles

if __name__ == "__main__":
    input_files = glob.glob('data/news_*.json')
    
    avg_sentiments = {}
    
    for input_file in input_files:
        stock_name = get_stock_name(input_file)
        output_file = f'data/news_{stock_name}.json'
        
        avg_sentiment, total_articles = process_news_data(input_file, output_file)
        avg_sentiments[stock_name] = [avg_sentiment, total_articles]
    
    # Write the average sentiments and total articles to a JSON file
    with open('data/avg_sentiments.json', 'w', encoding='utf-8') as file:
        json.dump(avg_sentiments, file, indent=2)
    
    print("Average sentiment scores and total articles stored in data/avg_sentiments.json")
