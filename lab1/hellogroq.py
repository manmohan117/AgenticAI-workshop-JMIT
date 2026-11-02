from groq import Groq

import os 
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("API_KEY")


client = Groq(api_key=groq_api_key)

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "hi" 
        }
    ]
)
print(completion.choices[0].message.content)