"""
Python code for ReAct Prompting

This script demonstrates the concept of ReAct (Reason + Act) by integrating reasoning tasks with an external calculator tool.
The AI solves a mathematical problem, uses an external function to perform the calculation, and then provides reasoning on how the result was achieved.

Steps:
1. Reads the OpenAI API key from 'key.txt' for authentication.
2. Uses an external function (mock calculator) to perform calculations based on user input.
3. Sends the result and reasoning prompt to GPT-3.5-turbo for generating a step-by-step explanation.
4. Prints the AI's response explaining how the calculation was performed and how the external tool was utilized.

Requirements:
- Install the `openai` package.
- Store your API key in a text file, e.g., 'key.txt', and provide the correct file path in the code.
"""

import openai

# Define the path to your API key file
# This is where the OpenAI API key is stored for secure authentication
api_key_file_path = r'C:\Users\Amir\Desktop\Joy_of_AI\My_Publications_GenAI\Git_Codes\search_app\key.txt'

# Read the API key from the file
# This reads the API key from a local file and strips any extra whitespace
with open(api_key_file_path, 'r') as file:
    openai.api_key = file.read().strip()
    
# Define the ReAct prompt
prompt = (
    "You are a calculator. First, reason through how to add 15 and 27, then perform the calculation.\n"
    "Step 1: Reason how you will perform the calculation.\n"
    "Step 2: Perform the calculation."
)

# Send prompt to the model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use chat-based model for ReAct prompting
    messages=[
        {"role": "system", "content": "You are a calculator assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=100,  # To ensure complete response
    temperature=0  # To ensure deterministic output
)

# Output the response
print(response.choices[0].message['content'].strip())
