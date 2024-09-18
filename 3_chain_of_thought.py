"""
Python code for Chain of thoughts (CoT)

This script uses the OpenAI API to compare the down payments for two vehicles.

Steps:
1. Reads the OpenAI API key from 'key.txt' for authentication.
2. Sends a CoT prompt to the GPT-3.5-turbo model to calculate and compare down payments.
3. Prints the AI's response.

Requirements:
- Install the `openai` package.
- Store your API key in text file, e.g. 'key.txt' and provide the file path in below code.
"""

import openai

# Define the path to your API key file
api_key_file_path = r'<path to the text file including your OpenAI API Key>'

# Read the API key from the file
with open(api_key_file_path, 'r') as file:
    openai.api_key = file.read().strip()  # Read and strip any extra whitespace/newlines

# Define the CoT prompt
# The prompt is designed to ask the model to calculate the down payment for two vehicles and compare them.
prompt = ( 
    "Which vehicle requires a larger down payment based on the following information?\n"
    "Vehicle A: $40,000 with 30% down payment\n"
    "Vehicle B: $50,000 with 20% down payment\n"
    "(Think step by step and provide complete calculations)"
    # Including "(Think step by step and provide complete calculations)" helps guide the model to show detailed reasoning.
)

try:
    # Get prediction using chat model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the chat model suitable for conversational tasks
        messages=[ # Define the conversation history
            {"role": "system", "content": "You are a helpful assistant."}, # System message to set the context
            {"role": "user", "content": prompt} # User message with the prompt
        ],
        max_tokens=200,  # Increase max_tokens to ensure full response
        temperature=0  # Set temperature to 0 for more deterministic outputs, reducing randomness in the response
    )
    # Print the response content, stripping any extra whitespace
    print(response.choices[0].message['content'].strip())
except Exception as e:
    # Catch and print any errors that occur during the API call
    print(f"An error occurred: {e}")
    # This helps in debugging by providing information about what went wrong.
