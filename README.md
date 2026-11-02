# AgenticAI Workshop — JMIT

Workshop labs for Agentic AI.

## Lab 1 — Hello Groq

1. Create a virtual environment and install dependencies:

```bash
cd lab1
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
pip install groq python-dotenv
```

2. Copy `.env.example` to `.env` and set your Groq API key:

```bash
cp .env.example .env
```

3. Run:

```bash
python hellogroq.py
```
