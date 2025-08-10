# llm_analysis.py
import os
from openai import OpenAI

# Initialize OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=openai_api_key)

def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of the given text using OpenAI GPT model.
    Returns a string: 'Positive', 'Negative', or 'Neutral'.
    """
    prompt = f"""
    Analyze the sentiment of the following text and respond with exactly one word:
    Positive, Negative, or Neutral.

    Text: {text}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can change to gpt-4 if you have access
        messages=[
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    sentiment = response.choices[0].message.content.strip()
    return sentiment
