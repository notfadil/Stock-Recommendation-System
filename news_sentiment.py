'''
sortBy

relevancy = articles more closely related to q come first.
popularity = articles from popular sources and publishers come first.
publishedAt = newest articles come first.
'''

import json
from newsapi import NewsApiClient

def filter_news_articles(output_path, news_response):
    filtered_response = [
        {
            'title': article['title'],
            'description': article['description'],
            'sourceName' : article['source']['name']
        }
        for article in news_response['articles']
        if '[Removed]' not in article['title']
    ]

    # Print the total number of news articles
    print(f"Total number of news articles: {len(filtered_response)}")

    news_response['articles'] = filtered_response

    # Convert the response to a formatted JSON string
    formatted_response = json.dumps(news_response, indent=2)

    # Write the fetched news articles to a text file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(formatted_response)

    print(f"Filtered news articles have been written to '{output_path}'")


# Load the API key from a json file
with open('api_keys.json', 'r') as file:
    api_keys = json.load(file)
    api_key = api_keys['api_key']

# Define the search parameters
keywords = ['apple', 'tesla', 'microsoft', 'nvidia', 'google']
from_date = '2024-06-13'

# Initialize the NewsApiClient with the API key
newsapi = NewsApiClient(api_key=api_key)

# Fetch news articles
for keyword in keywords:
    response = newsapi.get_everything(q=keyword, from_param=from_date, sort_by='relevancy', language='en')
    filter_news_articles(output_path=f'data/news_articles_{keyword}.txt', news_response=response)



