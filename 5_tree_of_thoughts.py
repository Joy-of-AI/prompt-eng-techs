"""
Python code for Tree of Thoughts (ToT)

This script uses the OpenAI API to solve a problem using the ToT technique, where the model explores various reasoning paths in a branching fashion to find a solution.

Steps:
1. Reads the OpenAI API key from 'key.txt' for authentication.
2. Sends a ToT prompt to the GPT-3.5-turbo model, asking the model to systematically explore possible combinations to solve a problem.
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

# Define the Tree of Thoughts (ToT) prompt
# The prompt asks the model to explore different combinations and strategies to solve the Game of 24.
prompt = (
    "In the Game of 24, you have four numbers and need to use basic operations (+, -, *, /) to reach the number 24. "
    "Systematically explore possible combinations and operations to find a solution. Please provide all potential solutions and strategies."
    # The prompt encourages the model to explore various reasoning paths to solve the problem.
)

# Initialize a list to store responses
responses = []

# Number of reasoning paths to explore
num_paths = 3

# Get predictions using the chat model for multiple reasoning paths
for i in range(num_paths):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the chat model suitable for ToT tasks
            messages=[  # Define the conversation history
                {"role": "system", "content": "You are a strategic problem solver."},  # System message to set context
                {"role": "user", "content": prompt}  # User message with the prompt
            ],
            max_tokens=500,  # Set the maximum number of tokens in the response to handle complex solutions
            temperature=0  # Set temperature to 0 for more deterministic outputs
        )
        responses.append(response.choices[0].message['content'].strip())
    except Exception as e:
        print(f"An error occurred: {e}")

# Print all collected responses
print("Responses from multiple reasoning paths:")
for idx, response in enumerate(responses):
    print(f"Path {idx + 1}: {response}")

# Note: For Tree of Thoughts (ToT), you would typically aggregate results from multiple responses
# to determine the most comprehensive solution. This example prints out each response for manual review.
