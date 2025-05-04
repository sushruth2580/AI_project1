import os
import openai
from dotenv import load_dotenv  # For loading environment variables securely

# Load the OpenAI API key from .env file
load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Prompt user for the paragraph to translate
input_paragraph = input("\nPlease Enter the English paragraph about renewable energy systems:\n")

# Prepare the system and user messages
messages = [
    {
        "role": "system",
        "content": (
            "You are a professional technical translator. "
            "Translate the following English paragraph into Spanish. "
            "Ensure the translation uses accurate renewable energy terminology, "
            "technical vocabulary, and conveys the original concept precisely."
        )
    },
    {
        "role": "user",
        "content": input_paragraph
    }
]

# Make the API call using GPT-4o
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

# Extract and print the translated paragraph
translated_text = response.choices[0].message.content
print("\n🌍 Translated Paragraph (Spanish):\n")
print(translated_text)
# Save the translated paragraph to a file
output_filename = "translated_paragraph.txt"
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(translated_text)