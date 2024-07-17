import json

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

if __name__ == "__main__":
    input_file = 'data/news_data.json'
    output_file = 'data/news_data_cleaned.json'
    remove_unicode_and_newlines_from_file(input_file, output_file)
    print(f"Unicode characters and new lines replaced, data written to {output_file}")
