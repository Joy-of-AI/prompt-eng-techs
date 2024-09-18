"""
Python code for Self-Consistency

This script uses the OpenAI API to solve an arithmetic problem using the self-consistency technique, where multiple reasoning paths are explored to enhance accuracy.

Steps:
1. Reads the OpenAI API key from 'key.txt' for authentication.
2. Sends a self-consistency prompt to the GPT-3.5-turbo model, asking the model to reason through the problem from multiple perspectives.
3. Aggregates the responses to determine the final answer.
4. Prints the AI's final answer.

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

# Define the self-consistency prompt
# The prompt asks the model to reason through a problem from multiple perspectives to find the correct answer.
prompt = (
    "Q: Terry had 12 apples, gave half to Jane, and John gave him three more apples. How many apples does Terry have now?\n"
    "Please reason through the problem step by step and provide multiple answers to ensure accuracy."
    # The prompt encourages the model to explore multiple reasoning paths for more accurate results.
)

# Initialize a list to store responses
responses = []

# Number of reasoning paths to explore
num_paths = 3

# Get predictions using the chat model for multiple reasoning paths
for i in range(num_paths):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the chat model suitable for self-consistency tasks
            messages=[  # Define the conversation history
                {"role": "system", "content": "You are a helpful assistant."},  # System message to set context
                {"role": "user", "content": prompt}  # User message with the prompt
            ],
            max_tokens=200,  # Set the maximum number of tokens in the response
            temperature=0  # Set temperature to 0 for more deterministic outputs
        )
        responses.append(response.choices[0].message['content'].strip())
    except Exception as e:
        print(f"An error occurred: {e}")

# Print all collected responses
print("Responses from multiple reasoning paths:")
for idx, response in enumerate(responses):
    print(f"Path {idx + 1}: {response}")

# Note: For self-consistency, you would typically aggregate results from multiple responses
# to determine the most likely correct answer. This example prints out each response for manual review.
