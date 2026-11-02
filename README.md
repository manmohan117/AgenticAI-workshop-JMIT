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
- VS Code (recommended) or any editor
- Terminal open in this project folder  
  - **Windows:** Git Bash or Command Prompt  
  - **Mac:** Terminal app (or the VS Code terminal)

---

## Setup (Windows and Mac)

### Step 0 — Check that Python works

Open a terminal and run:

```bash
python --version
```

If that fails on Mac / some Windows setups, try:

```bash
python3 --version
```

You should see something like `Python 3.10.x` or `Python 3.11.x`.

If you get **“python is not recognized”** / **“command not found”**, jump to [Troubleshooting → Python not found](#1-python-not-found--python-is-not-recognized).

### Step 1 — Go into the lab folder

```bash
cd lab1
```

### Step 2 — Create a virtual environment

A virtual environment keeps this lab’s packages separate from other Python projects.

**Windows:**

```bash
python -m venv .venv
```

**Mac:**

```bash
python3 -m venv .venv
```

### Step 3 — Activate the virtual environment

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

**Windows (Command Prompt):**

```bash
.venv\Scripts\activate
```

**Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run VS Code / PowerShell as Administrator once, or allow scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Mac:**

```bash
source .venv/bin/activate
```

When it is active, you should see `(.venv)` at the start of your terminal line.

### Step 4 — Install the packages

With `(.venv)` active:

```bash
pip install groq python-dotenv
```

On Mac, if `pip` is not found:

```bash
pip3 install groq python-dotenv
```

| Package          | Why you need it                                      |
|------------------|------------------------------------------------------|
| `groq`           | Official library to talk to the Groq API             |
| `python-dotenv`  | Loads secrets from a `.env` file into your program   |

### Step 5 — Add your API key

1. Copy the example env file:

**Windows (Git Bash) / Mac:**

```bash
cp .env.example .env
```

**Windows (Command Prompt):**

```bash
copy .env.example .env
```

2. Open `.env` in your editor and replace the placeholder with your real key:

```env
API_KEY=your_groq_api_key_here
```

**Important:** Never commit `.env` or paste your key into chat / GitHub.  
The `.gitignore` file already keeps `.env` out of git.

### Step 6 — Run the script

**Windows:**

```bash
python hellogroq.py
```

**Mac:**

```bash
python3 hellogroq.py
```

(Or just `python hellogroq.py` if that works after activating `.venv`.)

You should see a short reply from the model in your terminal (a response to `"hi"`).

### Optional — Run from VS Code (Code Runner)

If you prefer the ▶ Run button instead of typing in the terminal:

1. Install the **Code Runner** extension in VS Code  
   (`Extensions` → search **Code Runner** → Install)
2. Open VS Code **Settings** (`Ctrl + ,` on Windows, `Cmd + ,` on Mac)
3. Search for **code runner**
4. Enable:
   - **Code-runner: Run In Terminal** (run in the integrated terminal)
   - **Code-runner: Save File Before Run** (save before running)
5. Open `hellogroq.py` and click Run (or use the Code Runner shortcut)

Also make sure your VS Code terminal has the venv activated (`(.venv)` visible) before you run, so packages like `groq` are found.

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

---

## Troubleshooting

### Quick checklist

| Problem | First thing to try |
|---------|-------------------|
| `python` not found | Install Python / use `python3` / fix PATH (see below) |
| `ModuleNotFoundError` | Activate `.venv`, then `pip install groq python-dotenv` |
| Code does not run in VS Code | Install Code Runner + enable “Run In Terminal” |
| Auth / empty API key | Check `lab1/.env` has `API_KEY=...` |
| Network / API error | Check internet and Groq key |

---

### 1. Python not found / “python is not recognized”

**Check the version first:**

```bash
python --version
```

If that fails:

```bash
python3 --version
```

**Windows — fix it**

1. Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. During install, tick **“Add python.exe to PATH”**
3. Close and reopen the terminal (and VS Code)
4. Check again: `python --version`
5. If VS Code still cannot find Python, try **Run VS Code as Administrator** once, then reopen a normal window

**Mac — fix it**

1. Check if Python 3 is already there: `python3 --version`
2. If missing, install with Homebrew:

```bash
brew install python
```

Or download from [https://www.python.org/downloads/](https://www.python.org/downloads/)

3. Prefer `python3` and `pip3` on Mac for this lab
4. Close and reopen Terminal / VS Code, then check again

---

### 2. Module not found (`ModuleNotFoundError: groq` or `dotenv`)

This almost always means packages were installed outside the venv, or the venv is not active.

**Do these steps in order:**

1. Open a terminal **inside** `lab1`
2. **Create** the environment (if you have not yet):

   - Windows: `python -m venv .venv`
   - Mac: `python3 -m venv .venv`

3. **Activate** it:

   - Windows (Git Bash): `source .venv/Scripts/activate`
   - Windows (CMD): `.venv\Scripts\activate`
   - Mac: `source .venv/bin/activate`

4. Confirm you see `(.venv)` in the prompt
5. **Install** packages again:

```bash
pip install groq python-dotenv
```

6. Run again:

```bash
python hellogroq.py
```

**Extra tips**

- If `pip` fails on Mac, use `pip3 install groq python-dotenv`
- In VS Code, pick the interpreter that points to `lab1/.venv`  
  (`Ctrl/Cmd + Shift + P` → **Python: Select Interpreter** → choose `.venv`)
- On Windows, if activation or install is blocked, try **Run VS Code as Administrator**, create/activate the venv, install packages, then run again

---

### 3. Code not executing / Run button does nothing

1. Install the **Code Runner** extension in VS Code
2. Go to **Settings** → search **code runner**
3. Enable:
   - **Run In Terminal** (Code-runner: Run In Terminal)
   - **Save File Before Run** (Code-runner: Save File Before Run)
4. Make sure `hellogroq.py` is the active file
5. Activate `.venv` in the integrated terminal before running
6. Try running from the terminal manually: `python hellogroq.py` (or `python3 hellogroq.py` on Mac)

---

### 4. Python code not running (general)

Work through this list:

1. **Is Python installed?** → `python --version` or `python3 --version`
2. **Are you in the right folder?** → `cd lab1` then `ls` (Mac/Git Bash) or `dir` (CMD) and confirm you see `hellogroq.py`
3. **Is the venv activated?** → prompt should show `(.venv)`
4. **Are packages installed?** → `pip install groq python-dotenv`
5. **Is `.env` present with a real key?** → `API_KEY=...` inside `lab1/.env`
6. **VS Code Run issues?** → install Code Runner, enable **Run In Terminal** and **Save File Before Run**
7. **Still stuck on Windows permissions?** → Run VS Code as Administrator, recreate/activate venv, reinstall packages
8. **Mac tip:** use `python3` / `pip3` if `python` / `pip` are not found

---

### 5. API key / authentication errors

- Confirm the file is named `.env` (not `.env.txt`) and lives in **`lab1/`**
- Confirm the line looks like: `API_KEY=gsk_...` (no quotes needed)
- Do not leave the placeholder `your_groq_api_key_here`
- Get a fresh key from [https://console.groq.com](https://console.groq.com) if needed

### 6. Network / no reply from Groq

- Check your internet connection
- Confirm the Groq key is valid and not revoked
- Try running the script again after a minute

---

## Lab 2

Coming next in the workshop.
