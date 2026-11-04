from groq import Groq

import os 
from dotenv import load_dotenv

load_dotenv()



groq_api_key = os.getenv("API_KEY")
client = Groq(api_key=groq_api_key)

#This function is used to get the email of the user
def get_email():
    return "manmohan.singh@grazitti.com"


Tools_list = [{
  "type": "function",
  "function": {
    "name": "get_email",
    "description": "this function is used to get the email of the user",
    "parameters": {
      "properties": {}
    }
  }
}]

Tools_dict = {
    "get_email": get_email,
}



def generate_response(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        max_completion_tokens=2000,
        messages=prompt,
        temperature=0.5,
        reasoning_effort="medium",
        tools=Tools_list,
        top_p=1,
    )
    return completion.choices[0].message

system_prompt = """ You are a email assistant , you have a tool called get_email which you can use to get email"""


while True:
    user_input= input("You: ")

    prompt = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}]
    response = generate_response(prompt)
    print(response.reasoning)
    print("Tools requested : " , response.tool_calls)

    while response.tool_calls:
        tool_call = response.tool_calls[0]
        tool_name = tool_call.function.name
        tool_result = Tools_dict[tool_name]()

        prompt.append(response)
        prompt.append({"role": "tool","tool_call_id": tool_call.id, "name": tool_name, "content": tool_result})
        response = generate_response(prompt)
        print(response.content)
        response.tool_calls = None

    if user_input.lower() == "exit":
        break

