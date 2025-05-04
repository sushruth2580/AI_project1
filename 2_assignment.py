import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Get user input for the integer array and target value
input_array_int = input(" Enter a list of integers (e.g., [1, 2, 3, 4, 5]): ")
input_target = input(" Enter the target sum: ")

# Create messages for the system and user instructions
messages = [
    {
        "role": "system",
        "content": (
            "You are an expert Python programmer.\n"
            "Write an optimized Python function that takes a list of integers and a target sum, "
            "and returns all unique pairs of numbers whose sum equals the target.\n"
            "Ensure:\n"
            "- Each pair is unique (e.g., (2,3) is same as (3,2), only one should appear)\n"
            "- Time and space complexity are optimized\n"
            "- Output is clean and easy to read"
        )
    },
    {
        "role": "user",
        "content": f"The integer array is: {input_array_int}\nTarget sum: {input_target}"
    }
]

# Call the GPT model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

# Extract and print the generated Python function
generated_code = response.choices[0].message.content
print("\n Generated Python Function:\n")
print(generated_code)
print("\n\n Example Usage:")
print(generated_code + "(input_array_int, input_target)")
print("\n\n")   
# Note: The above code assumes that the OpenAI API key is stored in a .env file
# and that the OpenAI Python client is properly installed and configured.