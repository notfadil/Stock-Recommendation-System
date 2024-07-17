import json
import os
import urllib.request
from datetime import datetime, timedelta
import time

# Load API keys from the json file
def load_json(file_path, key):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data[key]


apiKeys = load_json("api_keys.json", "api_keys")
keywords = load_json("stocks.json", "stocks")
language = "en"
country = "us"
sortBy = "relevance"  # relevance, published at

# Function to fetch and append data
def fetch_and_append_data(keyword, start_date, end_date, file_path, apiKey):
    url = f"https://gnews.io/api/v4/search?q={keyword}&lang={language}&country={country}&from={start_date}T00:00:00Z&to={end_date}T23:59:59Z&sortby={sortBy}&max=10&apikey={apiKey}"

    try:
        # Fetch the data from the API
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))

        new_articles = data.get('articles', [])

        # Check if the file exists
        if os.path.exists(file_path):
            # Read existing data
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Extract existing URLs to check for duplicates
        existing_urls = {article['url'] for article in existing_data}

        # Filter out duplicates
        filtered_articles = [article for article in new_articles if article['url'] not in existing_urls]

        # Append new filtered data
        existing_data.extend(filtered_articles)

        # Write updated data to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, indent=2)
        
        return len(filtered_articles)
    except Exception as e:
        print(f"Failed to fetch data using API key: {apiKey}. Error: {e}")
        return -1  # Indicate failure to fetch data

# Function to remove Unicode characters and newlines
def remove_unicode_and_newlines_from_file(input_file, output_file):
    # Read the data from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Convert data to JSON string to handle replacements
    content = json.dumps(data, ensure_ascii=False, indent=2)
    
    # Replace Unicode escape sequences and new lines
    cleaned_content = content.replace('\\n', ' ')

    # Write the updated data to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    print(f"Unicode characters and new lines replaced, data written to {output_file}")

# Function to partition date range and fetch news
def partition_and_fetch(keyword, start_date, end_date, step_days, api_keys):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    file_path = f'data/news_{keyword}.json'

    # Ensure the directory exists
    os.makedirs('data', exist_ok=True)

    total_articles = 0
    current_start = start_date
    api_key_index = 0

    while current_start < end_date:
        current_end = current_start + timedelta(days=step_days - 1)
        if current_end > end_date:
            current_end = end_date

        while api_key_index < len(api_keys):
            articles_fetched = fetch_and_append_data(keyword, current_start.strftime("%Y-%m-%d"), current_end.strftime("%Y-%m-%d"), file_path, api_keys[api_key_index])
            if articles_fetched != -1:
                total_articles += articles_fetched
                print(f"Data updated from {current_start.strftime('%Y-%m-%d')} to {current_end.strftime('%Y-%m-%d')} for keyword '{keyword}'")
                break  # Exit the loop and proceed to the next date range
            else:
                api_key_index += 1  # Move to the next API key

        if api_key_index == len(api_keys):
            print("All API keys have reached their limits.")
            break  # Exit the while loop if all API keys have been exhausted

        # Wait for 5 seconds before the next request
        time.sleep(1)

        current_start = current_end + timedelta(days=1)

    print(f"Total number of articles collected for '{keyword}': {total_articles}")

    # Remove Unicode characters and newlines
    remove_unicode_and_newlines_from_file(file_path, file_path)

# Customize start, end and step dates
start_date = "2024-05-14"
end_date = "2024-06-14"
step_days = 2

# Run the partition and fetch function for each keyword
for keyword in keywords:
    partition_and_fetch(keyword, start_date, end_date, step_days, apiKeys)
