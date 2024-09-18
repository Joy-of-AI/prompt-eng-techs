"""
Python code for Automatic Reasoning and Tool-Use (ART)

This script demonstrates the concept of ART by integrating reasoning tasks with an external tool (in this case, a mock calculator function).
The AI solves a multi-step problem (splitting a bill and adding a tip), uses an external function to calculate the result, and then provides
a step-by-step explanation of how the calculation was done.

Steps:
1. Reads the OpenAI API key from 'key.txt' for authentication.
2. Uses an external function to perform calculations for splitting a bill with a tip.
3. Sends the result and reasoning prompt to GPT-3.5-turbo for generating a detailed explanation.
4. Prints the AI's response explaining how the calculation was performed.

Requirements:
- Install the `openai` package.
- Store your API key in a text file, e.g., 'key.txt', and provide the correct file path in the code.
"""

import openai
import requests  # Used if external APIs like a calculator are needed

# Define the path to your API key file
api_key_file_path = r'<path to the text file including your OpenAI API Key>'

# Read the API key from the file
with open(api_key_file_path, 'r') as file:
    openai.api_key = file.read().strip()

# Function to calculate the total bill including tip using an external tool (mock calculator function)
# This function simulates the use of an external tool (e.g., a calculator API) for performing the calculation
def calculate_bill_with_tip(bill_amount, tip_percentage, people_count):
    total_with_tip = bill_amount * (1 + tip_percentage / 100)  # Adds the tip to the bill
    amount_per_person = total_with_tip / people_count  # Splits the bill among the people
    return round(amount_per_person, 2)  # Rounds the result to 2 decimal places for clarity

# Define the bill details
# These variables represent the total bill, the tip percentage, and the number of people splitting the bill
bill_amount = 125.45
tip_percentage = 15
people_count = 3

# Perform the bill calculation (using the external tool simulation)
# This calls the above function to calculate the amount each person needs to pay, including the tip
calculated_amount = calculate_bill_with_tip(bill_amount, tip_percentage, people_count)

# Define the prompt for GPT-3 including reasoning and external calculation result
# This prompt explains the problem and includes the result from the external tool (calculated amount per person)
prompt = (
    f"John needs to split a bill of ${bill_amount} among {people_count} people, including a {tip_percentage}% tip.\n"
    f"The external calculator API determined that each person should pay ${calculated_amount}.\n"
    "Provide a step-by-step explanation of how this amount was calculated."
)

try:
    # Get prediction using GPT-3.5-turbo model
    # The OpenAI API is called to generate a response. The model processes the prompt and generates reasoning based on the result
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The chat model used for conversational tasks, capable of reasoning
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # System message to set the assistant's role
            {"role": "user", "content": prompt}  # User message that includes the reasoning task and result
        ],
        max_tokens=300,  # Max tokens to control the length of the AI's response
        temperature=0.5  # Temperature set to balance creativity and reasoning (higher values increase randomness)
    )
    
    # Print the AI's reasoning and response
    # The model generates a step-by-step explanation of the calculation, which is printed out
    print(response.choices[0].message['content'].strip())

except Exception as e:
    # Catch and print any errors that occur during the API call
    # If any error occurs (e.g., network issues, API limit), it is caught and printed
    print(f"An error occurred: {e}")
