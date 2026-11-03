from groq import Groq

import os 
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("API_KEY")
client = Groq(api_key=groq_api_key)


def generate_response(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        max_completion_tokens=2000,
        messages=prompt,
        temperature=0.5,
        top_p=1,
        tools=[{"type": "browser_search"}]
    )
    return completion.choices[0].message.content
