from groq import Groq

import os 
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("API_KEY")

client = Groq(api_key=groq_api_key)


conversation_history = [
    {"role": "system" , "content": "You are a math tutor Assistant. You will only answer math related queries"}
]

def generate_response(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        max_completion_tokens=200,
        messages=conversation_history
    )
    return completion.choices[0].message.content

# continue the conversation
while True:
    prompt = input("You: ") # hi 
    conversation_history.append({"role": "user", "content": prompt})
    context = {"role": "user", "content": prompt}
    conversation_history.append(context)
    response = generate_response(conversation_history)
    conversation_history.append({"role": "assistant", "content": response})
    print("Groq: ", response)
    if prompt.lower() == "exit":
        break
