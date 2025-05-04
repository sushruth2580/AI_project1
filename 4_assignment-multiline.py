import os
import openai
from dotenv import load_dotenv

# Load OpenAI API key from environment
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

def get_news_article():
    """Prompt user to enter a news article. Accepts multiple lines until 'END' is entered."""
    print("📰 Please paste your news article below. Type 'END' on a new line when you're done:\n")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        lines.append(line)
    return "\n".join(lines)

# Capture user input
article_text = get_news_article()
print("\n✅ News article received.\n")

# Prepare messages for OpenAI model
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant that summarizes news articles clearly and objectively. "
            "Summarize the key events and issues in a few sentences. Avoid speculation, personal opinions, or excessive detail. "
            "Tailor the summary for students who want to understand current events quickly."
        )
    },
    {
        "role": "user",
        "content": article_text
    }
]

# Call GPT-4o model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0  # Use 0 for deterministic and fact-based summary
)

# Extract and display the summary
summary = response.choices[0].message.content.strip()
print("📝 News Summary:\n")
print(summary)
