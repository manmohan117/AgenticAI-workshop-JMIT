from groq import Groq

import os 
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("API_KEY")
client = Groq(api_key=groq_api_key)

conversation_history = [
]

def generate_response(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        max_completion_tokens=2000,
        messages=conversation_history,
        temperature=0.5,
        top_p=1,
        tools=[{"type": "browser_search"}]
    )
    print(completion.choices[0].message.tool_calls)
    return completion.choices[0].message.content

# continue the conversation
while True:
    prompt = input("You: ") 
    conversation_history.append({"role": "user", "content": prompt})
    context = {"role": "user", "content": prompt}
    conversation_history.append({"role": "user", "content": prompt})
    response = generate_response(conversation_history)
    conversation_history.append({"role": "assistant", "content": response})
    print("Groq: ", response)
    if prompt.lower() == "exit":
        break
