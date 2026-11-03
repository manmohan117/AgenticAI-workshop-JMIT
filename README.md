# AgenticAI Workshop — JMIT

Simple labs to build your first AI agent, then put it behind a small web app.

---

## Jump to a section

**Day 1**

- [What you will learn](#what-you-will-learn)
- [Before you start](#before-you-start)
- [Day 1 setup (Windows and Mac)](#day-1-setup-windows-and-mac)
- [Lab 1 — Hello Groq + memory](#lab-1--hello-groq--memory)
- [Lab 2 — Conversation history and built-in tools](#lab-2--conversation-history-and-built-in-tools)

**Day 2**

- [What you will build](#what-you-will-build)
- [How the pieces fit](#how-the-pieces-fit)
- [Day 2 folder map](#day-2-folder-map)
- [Day 2 backend setup](#day-2-backend-setup)
- [Link your agent to the backend](#link-your-agent-to-the-backend)
- [What is CORS and why we need it](#what-is-cors-and-why-we-need-it)
- [Connect the frontend](#connect-the-frontend)
- [Build your own frontend with AI](#build-your-own-frontend-with-ai)
- [Test the full Day 2 app](#test-the-full-day-2-app)

**Help**

- [Troubleshooting](#troubleshooting)

---

# Day 1 — Talk to an AI in the terminal

## What you will learn

On Day 1 you talk to an AI from Python.

You will:

1. Call Groq from a small script
2. Keep **memory** (the model remembers what you just said)
3. Keep **conversation history** (a list of user + assistant messages)
4. Turn on a **built-in tool** (browser search)

**Groq** is a cloud service that runs AI models fast.

```
Your Python script  →  Groq API  →  AI model  →  reply in your terminal
```

---

## Before you start

- Python 3 on your machine
- A free Groq API key from [https://console.groq.com](https://console.groq.com)
- VS Code (recommended)
- A terminal
  - **Windows:** Git Bash or Command Prompt
  - **Mac:** Terminal, or the VS Code terminal

---

## Day 1 setup (Windows and Mac)

### Step 0 — Check Python

```bash
python --version
```

If that fails (common on Mac):

```bash
python3 --version
```

You want something like `Python 3.10` or `Python 3.11`.

If you see **python is not recognized** / **command not found**, go to [Troubleshooting](#1-python-not-found--python-is-not-recognized).

### Step 1 — Go into Day 1

```bash
cd Day1
```

### Step 2 — Create a virtual environment

A virtual environment keeps this lab’s packages in one folder.

**Windows:**

```bash
python -m venv .venv
```

**Mac:**

```bash
python3 -m venv .venv
```

### Step 3 — Activate it

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

If PowerShell blocks this, allow scripts for your user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Mac:**

```bash
source .venv/bin/activate
```

You should see `(.venv)` at the start of the line.

### Step 4 — Install packages

```bash
pip install groq python-dotenv
```

On Mac, if `pip` is missing:

```bash
pip3 install groq python-dotenv
```

| Package         | What it does                         |
|-----------------|--------------------------------------|
| `groq`          | Talks to the Groq API                |
| `python-dotenv` | Reads your secret key from `.env`    |

### Step 5 — Add your API key

**Windows (Git Bash) / Mac:**

```bash
cp .env.example .env
```

**Windows (Command Prompt):**

```bash
copy .env.example .env
```

Open `.env` and put your real key:

```env
API_KEY=your_groq_api_key_here
```

Never put this key in GitHub or in the chat. `.gitignore` already ignores `.env`.

### Optional — Run from VS Code (Code Runner)

1. Install the **Code Runner** extension
2. Open **Settings** (`Ctrl + ,` on Windows, `Cmd + ,` on Mac)
3. Search **code runner**
4. Turn on:
   - **Code-runner: Run In Terminal**
   - **Code-runner: Save File Before Run**
5. Activate `.venv` in the VS Code terminal before you click Run

---

## Lab 1 — Hello Groq + memory

**File:** `Day1/lab1.py`

This script:

- Reads your key from `.env`
- Keeps a list called `conversation_history`
- Uses a **system prompt** (the agent’s job, here: math tutor)
- Loops: you type → AI replies → both are saved in the list

### Run it

From `Day1` with `(.venv)` on:

**Windows:**

```bash
python lab1.py
```

**Mac:**

```bash
python3 lab1.py
```

Type a math question. Type `exit` to stop.

### Simple idea: memory

Without memory, every question is new.

With memory, you send the **old messages + the new one**. Then the model can say things like “as I said above”.

That list of messages is your **conversation history**.

### Try this

1. Ask: `What is 12 times 8?`
2. Then ask: `Now add 10 to that.`
3. The model should use the first answer. That is memory.

Change the `system_prompt` if you want a different helper (for example a grammar tutor).

---

## Lab 2 — Conversation history and built-in tools

**File:** `Day1/lab2.py`

This lab keeps the same chat loop, and adds a **built-in tool**.

### What is a tool?

A tool is something extra the model can use, not only its own memory.

In this lab the tool is:

```python
tools=[{"type": "browser_search"}]
```

That lets the model **search the web** when your question needs fresh facts.

### Run it

```bash
python lab2.py
```

**Mac:** `python3 lab2.py`

Ask something that needs current info, for example:

- `What is the weather idea for today in general news terms?`
- `Search for the latest Python version.`

Type `exit` to stop.

### What to notice

| Idea                  | In the code                                      |
|-----------------------|--------------------------------------------------|
| Conversation history  | `conversation_history` list                      |
| Your message          | `{"role": "user", "content": prompt}`            |
| Model reply           | `{"role": "assistant", "content": response}`     |
| Built-in tool         | `tools=[{"type": "browser_search"}]`             |

You now have a small **agent**: it remembers the chat and can use a tool.

---

# Day 2 — FastAPI backend and chat frontend

## What you will build

On Day 2 you take the Groq agent out of the terminal and put it in a **backend**.

Then any **frontend** (web page) can talk to it.

You will:

1. Set up a clean **FastAPI** backend
2. Link your Groq agent to one API route: `/chat/{user_prompt}`
3. Turn on **CORS** so the browser is allowed to call your API
4. Open the sample chat page, **or** ask AI to build your own page

```
Browser (frontend)  →  FastAPI (backend)  →  Groq agent  →  reply back to the page
```

---

## How the pieces fit

| Piece        | Folder / file                 | Job                                      |
|--------------|-------------------------------|------------------------------------------|
| Agent        | `Day2/backend/services/groq_llm.py` | Sends messages to Groq                   |
| Backend API  | `Day2/backend/main.py`        | Receives HTTP requests, calls the agent  |
| CORS         | inside `main.py`              | Lets the web page call the API           |
| Frontend     | `Day2/index.html` (sample)    | Chat UI. You can replace this file       |

The frontend does **not** hold your API key. Only the backend reads `.env`.

---

## Day 2 folder map

```
Day2/
  index.html                 ← sample chat page (you may replace this)
  backend/
    main.py                  ← FastAPI app + CORS + /chat route
    services/
      groq_llm.py            ← your agent (Groq call + tool)
    .env                     ← create this (API_KEY) — do not commit
```

---

## Day 2 backend setup

Do this from a **new terminal**. Keep Day 1 closed if you want a clean start. You can reuse the same Python.

### Step 1 — Go to the backend folder

This folder is important. Run commands **here**, so Python can find `services.groq_llm`.

```bash
cd Day2/backend
```

### Step 2 — Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

(Command Prompt activate: `.venv\Scripts\activate`)

**Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)`.

### Step 3 — Install backend packages

```bash
pip install fastapi uvicorn groq python-dotenv
```

Mac if needed: `pip3 install fastapi uvicorn groq python-dotenv`

| Package         | Why you need it                          |
|-----------------|------------------------------------------|
| `fastapi`       | Builds the API                           |
| `uvicorn`       | Runs the API server                      |
| `groq`          | Calls the model                          |
| `python-dotenv` | Loads `API_KEY` from `.env`              |

### Step 4 — Add `.env` in the backend folder

Create `Day2/backend/.env` (same key as Day 1):

```env
API_KEY=your_groq_api_key_here
```

Or copy from Day 1:

**Windows (Git Bash) / Mac:**

```bash
cp ../../Day1/.env .env
```

**Windows (Command Prompt):**

```bash
copy ..\..\Day1\.env .env
```

The file must sit next to `main.py` (or in the folder where you start the server).

### Step 5 — Start the backend

Still in `Day2/backend` with `(.venv)` on:

```bash
uvicorn main:app --reload --port 8000
```

Leave this terminal **open**. The server is running.

Open these in your browser to check:

- [http://localhost:8000/home](http://localhost:8000/home) → `{"Hello":"World"}`
- [http://localhost:8000/docs](http://localhost:8000/docs) → FastAPI’s try-it page
- [http://localhost:8000/chat/hello](http://localhost:8000/chat/hello) → `{"response":"..."}` from Groq

If `/home` works, FastAPI is up. If `/chat/hello` works, the **agent is linked**.

To stop the server later: click that terminal and press `Ctrl + C`.

---

## Link your agent to the backend

Two files work together.

### 1. The agent — `Day2/backend/services/groq_llm.py`

This is the Day 1 Groq code, turned into one function:

```python
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
```

- `prompt` is a **list of messages**, same idea as `conversation_history`
- The built-in **browser_search** tool is still on

### 2. The API — `Day2/backend/main.py`

FastAPI imports that function and uses it in a route:

```python
from services.groq_llm import generate_response

@app.get("/chat/{user_prompt}")
def chat(user_prompt: str):
    response = generate_response([{"role": "user", "content": user_prompt}])
    return {"response": response}
```

**In plain words:**

1. The web page calls `/chat/your question`
2. FastAPI reads `your question`
3. FastAPI calls `generate_response(...)`
4. Groq replies
5. FastAPI sends JSON: `{"response": "..."}`

### Change the agent, not the URL

Students: keep the route name `/chat/{user_prompt}` if you can.

Then any frontend that already calls `/chat/...` will still work.

You **may** change:

- The system prompt (add it as a first message in the list)
- The model name
- Tools
- How you store conversation history

Example: add a system prompt (memory of the agent’s job):

```python
@app.get("/chat/{user_prompt}")
def chat(user_prompt: str):
    messages = [
        {"role": "system", "content": "You are a helpful campus guide."},
        {"role": "user", "content": user_prompt},
    ]
    response = generate_response(messages)
    return {"response": response}
```

If you want **full conversation history** like Day 1, keep a list in Python (or send the list from the frontend). Start simple: one user message per request is enough for this lab.

---

## What is CORS and why we need it

The frontend is a file (`index.html`).  
The backend is a server (`http://localhost:8000`).

The browser treats these as **two different places**. By default it **blocks** the page from calling the API.

**CORS** is the backend saying: “This web page is allowed to call me.”

In `main.py` you already have:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

`allow_origins=["*"]` means any local page can call the API. That is fine for a workshop.

**Do not remove CORS** or the frontend will fail with a browser error, even if `/chat/hello` works in the address bar.

---

## Connect the frontend

The sample page is `Day2/index.html`.

It talks to:

```
http://localhost:8000/chat/<your message>
```

and reads:

```json
{ "response": "the model answer" }
```

### Step 1 — Keep the backend running

`uvicorn` must stay on in `Day2/backend`.

### Step 2 — Open the HTML file

Do **not** use FastAPI to serve the page unless you want to. For this lab:

1. In VS Code, right-click `Day2/index.html`
2. Open with a browser  
   or install the **Live Server** extension and click **Go Live**

The page uses:

```javascript
const API_BASE = "http://localhost:8000";
```

If you change the uvicorn port, change this line too.

### Step 3 — Send a message

Type in the box and click **Send**. You should see the Groq reply.

If you see **Could not reach the API**:

- Backend not running
- Wrong port
- CORS missing
- Typo in `API_BASE`

---

## Build your own frontend with AI

The backend is ready. The UI is yours.

**Keep the same API.** Then you can plug any page in.

### API contract (do not change this if you want an easy plug-in)

| Item        | Value                                      |
|-------------|--------------------------------------------|
| Method      | `GET`                                      |
| URL         | `http://localhost:8000/chat/{user_prompt}` |
| Example     | `http://localhost:8000/chat/hello`         |
| Success     | JSON `{ "response": "..." }`               |
| CORS        | Already allowed                            |

Spaces in the question must be encoded (`encodeURIComponent` in JavaScript).

### What you should build

Pick an agent theme, then ask AI for a matching page, for example:

- Math tutor
- Campus FAQ bot
- Travel planner
- Code explainer

Replace `Day2/index.html` (or add `Day2/my-ui.html`). Point it at the same `API_BASE`.

### Copy this prompt into ChatGPT / Cursor / any AI

Paste this, then add your theme at the end:

```
Build a single HTML file chat UI for students.

Rules:
- One file only: HTML + CSS + JS
- No build step, no React, no npm
- Call this API with GET:
  http://localhost:8000/chat/${encodeURIComponent(userMessage)}
- The API returns JSON: { "response": "text" }
- Show user messages and bot messages in a chat list
- Show a loading state while waiting
- Show a clear error if the server is down
- Use const API_BASE = "http://localhost:8000";
- Do not put any API keys in the frontend

My agent theme is: _______________
Make the look and labels match that theme.
```

Then:

1. Save the AI’s HTML over `Day2/index.html` (or a new file)
2. Keep `API_BASE` as `http://localhost:8000`
3. Open the file in the browser
4. Keep uvicorn running

If the new UI calls `/chat/...` and reads `response`, it will work with **no backend change**.

---

## Test the full Day 2 app

1. Backend running: [http://localhost:8000/home](http://localhost:8000/home) shows Hello
2. Agent linked: [http://localhost:8000/chat/hi](http://localhost:8000/chat/hi) shows JSON
3. Docs page: [http://localhost:8000/docs](http://localhost:8000/docs) — try `/chat/{user_prompt}`
4. Frontend open: sample `index.html` or your AI-built page
5. Send two messages and see replies

**Success looks like:** you type in the page → backend terminal shows a request → the page shows the model’s answer.

---

# Troubleshooting

## Quick checklist

| Problem | First thing to try |
|---------|-------------------|
| `python` not found | Install Python / use `python3` / fix PATH |
| `ModuleNotFoundError` | Activate `.venv`, then install packages again |
| Code does not run in VS Code | Code Runner + Run In Terminal + Save Before Run |
| Empty / bad API key | Check `.env` has `API_KEY=...` |
| `uvicorn` not found | `pip install fastapi uvicorn` inside `.venv` |
| `/home` fails | You are not in `Day2/backend`, or server is not running |
| `/chat` fails, `/home` works | `.env` missing, or Groq key / network |
| Frontend cannot reach API | Backend running? CORS on? `API_BASE` = `http://localhost:8000` |
| Network / Groq error | Internet + valid key |

---

## 1. Python not found / “python is not recognized”

Check:

```bash
python --version
```

Then:

```bash
python3 --version
```

**Windows**

1. Install from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Tick **Add python.exe to PATH**
3. Close and reopen the terminal and VS Code
4. Run `python --version` again
5. If VS Code still fails, **Run VS Code as Administrator** once

**Mac**

1. Try `python3 --version`
2. If missing: `brew install python` or install from python.org
3. Use `python3` and `pip3` for this workshop

---

## 2. Module not found (`groq`, `dotenv`, `fastapi`)

1. `cd` into the right folder (`Day1` or `Day2/backend`)
2. Create venv if needed: `python -m venv .venv` (Mac: `python3 -m venv .venv`)
3. Activate it (see Day 1 Step 3)
4. Confirm `(.venv)` is visible
5. Install again:

**Day 1:**

```bash
pip install groq python-dotenv
```

**Day 2:**

```bash
pip install fastapi uvicorn groq python-dotenv
```

6. In VS Code: `Ctrl/Cmd + Shift + P` → **Python: Select Interpreter** → pick `.venv`

On Windows permission errors: run VS Code as Administrator, then activate and install again.

---

## 3. Code not executing / Run button does nothing

1. Install **Code Runner**
2. Settings → search **code runner**
3. Enable **Run In Terminal** and **Save File Before Run**
4. Activate `.venv` in the integrated terminal
5. Or run from the terminal yourself (`python lab1.py` or `uvicorn main:app --reload`)

---

## 4. Python code not running (general)

1. `python --version` or `python3 --version`
2. Are you in the right folder? `Day1` or `Day2/backend`
3. Is `.venv` active?
4. Are packages installed?
5. Does `.env` exist with a real `API_KEY`?
6. VS Code: Code Runner settings above
7. Windows: Run VS Code as Admin if install/activate is blocked
8. Mac: use `python3` / `pip3`

---

## 5. API key / authentication errors

- File name is `.env` (not `.env.txt`)
- Day 1: file is in `Day1/`
- Day 2: file is in `Day2/backend/`
- Line looks like `API_KEY=gsk_...` (no quotes)
- New key: [https://console.groq.com](https://console.groq.com)

---

## 6. FastAPI / uvicorn problems (Day 2)

| What you see | What to do |
|--------------|------------|
| `uvicorn: command not found` | Activate `.venv`, then `pip install uvicorn fastapi` |
| `No module named services` | Start uvicorn from `Day2/backend`, not from the repo root |
| Port already in use | Use `--port 8001` and change `API_BASE` in the HTML |
| Reload errors after you edit | Save the file; uvicorn restarts by itself (`--reload`) |

---

## 7. Frontend cannot talk to the backend

1. Is uvicorn running? Open [http://localhost:8000/home](http://localhost:8000/home)
2. Does CORS still exist in `main.py`?
3. Is `API_BASE` exactly `http://localhost:8000` (no extra slash issues in your fetch URL)?
4. Did you encode the message? Use `encodeURIComponent(msg)`
5. Open the browser **Developer Tools → Console** and read the red error
6. A CORS error means the backend is missing the CORS block
7. `Failed to fetch` often means the server is off

---

## 8. Network / no reply from Groq

- Check internet
- Check the key is still valid
- Wait a minute and try `/chat/hello` again
