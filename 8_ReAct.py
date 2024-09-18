"""
Python code for ReAct Prompting

This script demonstrates the concept of ReAct (Reason + Act) by integrating reasoning tasks with an external calculator tool, as below: 
    1. Reasoning: In the prompt, we explicitly ask the model to reason first about how it will perform the calculation. This step showcases the "reasoning" part of ReAct, where the model must explain its thinking before acting.
    2. Action: After reasoning, the model is instructed to perform the action by completing the calculation (15 + 27). This is the action part of the ReAct process, where the model actually solves the problem based on its reasoning.
    3. External Tool Simulation: While we are simulating the use of an external tool (e.g. a calculator) with a reasoning step before action, in a more complex example, the external tool could be something like querying an API, fetching data from a database, or running code to calculate the result.

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
api_key_file_path = r'<path to the text file including your OpenAI API Key>'

# Read the API key from the file
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
