from groq import Groq

import os 
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("API_KEY")


client = Groq(api_key=groq_api_key)

def generate_response(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        max_completion_tokens=200,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content

# continue the conversation
while True:
    prompt = input("You: ")
    response = generate_response(prompt)
    print("Groq: ", response)
    if prompt.lower() == "exit":
        break
