import os
import openai
from dotenv import load_dotenv

# Load the OpenAI API key from environment
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Prompt user to input a news article
article = input(" Please enter the news article text:\n")

# Define three different summary prompts
prompts = [
    {
        "label": "Prompt 1 - General Summary",
        "system": "Read the paragraph and provide a concise summary.",
    },
    {
        "label": "Prompt 2 - Summary for Students",
        "system": "Summarize the given news article. Highlight the important facts such as events and issues. The audience is students.",
    },
    {
        "label": "Prompt 3 - Detailed & Neutral Summary",
        "system": (
            "Summarize the news in a few sentences. Highlight key events and issues, "
            "avoid speculation or opinions. Tailor the summary for students who want factual clarity."
        ),
    }
]

# Store and display results for comparison
results = []

for prompt in prompts:
    messages = [
        {"role": "system", "content": prompt["system"]},
        {"role": "user", "content": article}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    
    summary = response.choices[0].message.content.strip()
    results.append((prompt["label"], summary))

# Output summaries for comparison
print("\n Summarization Results:\n")
for label, summary in results:
    print(f"🔹 {label}:\n{summary}\n")

# You can optionally expand this with tone/density classification in a second loop
