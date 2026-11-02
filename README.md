# AgenticAI Workshop — JMIT

Hands-on labs for learning Agentic AI, starting with a simple LLM API call.

---

## Lab 1 — Hello Groq

### What you will learn

In this lab you send a short message to an AI model and print its reply.

You will:

1. Set up a small Python project
2. Store your API key safely in a `.env` file (not in your code)
3. Call Groq’s chat API and see the model’s response in the terminal

### What is Groq?

**Groq** is a cloud service that runs large language models (LLMs) very fast.  
You write a few lines of Python, send a prompt (like `"hi"`), and Groq returns the model’s answer.

Think of it like this:

```
Your Python script  →  Groq API  →  AI model  →  reply printed in your terminal
```

### Before you start

- Python 3 installed on your machine
- A free Groq account and API key from [https://console.groq.com](https://console.groq.com)
- Terminal / Git Bash open in this project folder

---

### Step 1 — Go into the lab folder

```bash
cd lab1
```

### Step 2 — Create and activate a virtual environment

A virtual environment keeps this lab’s packages separate from other Python projects.

```bash
python -m venv .venv
```

**Activate it (Windows Git Bash):**

```bash
source .venv/Scripts/activate
```

**Activate it (Windows Command Prompt):**

```bash
.venv\Scripts\activate
```

When it is active, you should see `(.venv)` at the start of your terminal line.

### Step 3 — Install the packages

```bash
pip install groq python-dotenv
```

| Package          | Why you need it                                      |
|------------------|------------------------------------------------------|
| `groq`           | Official library to talk to the Groq API             |
| `python-dotenv`  | Loads secrets from a `.env` file into your program   |

### Step 4 — Add your API key

1. Copy the example env file:

```bash
cp .env.example .env
```

2. Open `.env` in your editor and replace the placeholder with your real key:

```env
API_KEY=your_groq_api_key_here
```

**Important:** Never commit `.env` or paste your key into chat / GitHub.  
The `.gitignore` file already keeps `.env` out of git.

### Step 5 — Run the script

```bash
python hellogroq.py
```

You should see a short reply from the model in your terminal (a response to `"hi"`).

---

### How the code works (simple walkthrough)

Open `lab1/hellogroq.py`. Here is what each part does:

```python
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()                              # read values from .env
groq_api_key = os.getenv("API_KEY")        # get your API key

client = Groq(api_key=groq_api_key)        # connect to Groq

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",           # which model to use
    messages=[
        {
            "role": "user",
            "content": "hi"                # your prompt / question
        }
    ]
)

print(completion.choices[0].message.content)  # print the model's answer
```

| Piece of code | Plain-English meaning |
|---------------|------------------------|
| `load_dotenv()` | Load `API_KEY` from `.env` |
| `Groq(...)` | Create a client that can call Groq |
| `messages` | The chat history you send (here: one user message `"hi"`) |
| `completion.choices[0].message.content` | The text the model replied with |

### Try this next

After it works, change the `"hi"` string to another question, for example:

- `"Explain agents in one sentence."`
- `"Write a haiku about Python."`

Run the script again and compare the answers.

### Troubleshooting

| Problem | What to check |
|---------|----------------|
| `API_KEY` is `None` / auth error | Is `.env` in `lab1/`? Is the key spelled `API_KEY=` correctly? |
| `ModuleNotFoundError: groq` | Is `.venv` activated? Did you run `pip install groq python-dotenv`? |
| No reply / network error | Check internet connection and that your Groq key is valid |

---

## Lab 2

Coming next in the workshop.
