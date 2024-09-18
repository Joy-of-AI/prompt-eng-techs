"""
Python code for Zero-Shot Prompting

This script uses the OpenAI API to determine the sentiment of a given social media post using zero-shot prompting.

Steps:
1. Reads the OpenAI API key from 'key.txt' for authentication.
2. Sends a zero-shot prompt to the GPT-3.5-turbo model to classify the sentiment of the provided post.
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

# Define the zero-shot prompt
# The prompt asks the model to classify the sentiment of a social media post without any prior examples.
prompt = (
    "Determine the sentiment of the following social media post and categorize it as positive, negative, or neutral: "
    "'Don't miss the electric vehicle revolution! AnyCompany is ditching muscle cars for EVs, creating a huge opportunity for investors.'"
    # The prompt is direct and does not provide examples, relying on the model's inherent understanding.
)

# Get prediction using the chat model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use the chat model suitable for zero-shot tasks
    messages=[  # Define the conversation history
        {"role": "system", "content": "You are a helpful assistant."},  # System message to set context
        {"role": "user", "content": prompt}  # User message with the prompt
    ],
    max_tokens=50,  # Set the maximum number of tokens in the response
    temperature=0  # Set temperature to 0 for more deterministic outputs
)

# Print the response content, stripping any extra whitespace
print(response.choices[0].message['content'].strip())
