"""
Python code for Few-Shot Prompting

This script uses the OpenAI API to determine the sentiment of provided headlines by using few-shot prompting.

Steps:
1. Reads the OpenAI API key from 'key.txt' for authentication.
2. Sends a few-shot prompt to the GPT-3.5-turbo model to classify the sentiment of the given headlines.
3. Prints the AI's response.

Requirements:
- Install the `openai` package.
- Store your API key in a text file, e.g. 'key.txt', and provide the file path in the code.
"""

import openai

# Define the path to your API key file
api_key_file_path = r'<path to the text file including your OpenAI API Key>'

# Read the API key from the file
with open(api_key_file_path, 'r') as file:
    openai.api_key = file.read().strip()  # Read and strip any extra whitespace/newlines

# Define the prompt with examples
# The prompt includes a few examples to guide the model in classifying sentiment.
prompt = (
    "Determine the sentiment of the following headlines and categorize them as positive, negative, or neutral. Examples:\n"
    "1. 'Research firm fends off allegations of impropriety over new technology.' - Negative\n"
    "2. 'Offshore windfarms continue to thrive as vocal minority in opposition dwindles.' - Positive\n"
    "3. 'New smartphone model has received widespread praise.'"
)

# Get prediction using the chat model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use the chat model for generating responses
    messages=[  # Define the conversation history
        {"role": "system", "content": "You are a helpful assistant."},  # System message to set context
        {"role": "user", "content": prompt}  # User message with the prompt
    ],
    max_tokens=50,  # Set the maximum number of tokens in the response
    temperature=0  # Set temperature to 0 for more deterministic outputs
)

# Print the response content, stripping any extra whitespace
print(response.choices[0].message['content'].strip())
