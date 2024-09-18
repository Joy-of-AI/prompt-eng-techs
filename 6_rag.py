"""
Python code for Retrieval-Augmented Generation (RAG)

This script demonstrates the RAG technique by combining the retrieval of relevant data from Wikipedia with the generation of responses using the OpenAI API.

Steps:
1. Retrieves relevant information from Wikipedia based on a query.
2. Combines the retrieved information with a prompt to generate a more informed response using GPT-3.5-turbo.
3. Prints the AI's response.

Requirements:
- Install the `openai` and `requests` packages.
- Store your OpenAI API key in a text file (e.g., 'key.txt') and provide the file path in the code.
"""

import openai
import requests

# Define OpenAI API key
# Define the path to your API key file
api_key_file_path = r'<path to the text file including your OpenAI API Key>'

# Read the API key from the file
with open(api_key_file_path, 'r') as file:
    openai.api_key = file.read().strip()  # Read and strip any extra whitespace/newlines

# Define a function to retrieve relevant information from Wikipedia
def retrieve_information_from_wikipedia(query):
    # Wikipedia API endpoint
    wiki_url = 'https://en.wikipedia.org/w/api.php'
    
    # Parameters for the API request
    params = {
        'action': 'query',
        'format': 'json',
        'titles': query,
        'prop': 'extracts',
        'exintro': True,  # Retrieve only the introduction section
        'explaintext': True  # Get plain text (not HTML)
    }
    
    # Perform the API request
    response = requests.get(wiki_url, params=params)
    data = response.json()
    
    # Extract relevant information from the response
    pages = data.get('query', {}).get('pages', {})
    page = next(iter(pages.values()))
    extract = page.get('extract', 'No relevant information found.')
    
    return extract

# Define the prompt with retrieved information
query = "Electric_vehicle"  # Example query for Wikipedia retrieval
retrieved_info = retrieve_information_from_wikipedia(query)

prompt = (
    f"Based on the following information from Wikipedia, provide an insightful response:\n"
    f"Retrieved information: {retrieved_info}\n\n"
    "What are the current trends and benefits of electric vehicles?"
)

try:
    # Get prediction using chat model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the chat model suitable for conversational tasks
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,  # Increase max_tokens to ensure full response
        temperature=0.7  # Adjust temperature for diverse outputs
    )
    # Print the response content, stripping any extra whitespace
    print(response.choices[0].message['content'].strip())
except Exception as e:
    # Catch and print any errors that occur during the API call
    print(f"An error occurred: {e}")
    # This helps in debugging by providing information about what went wrong.
