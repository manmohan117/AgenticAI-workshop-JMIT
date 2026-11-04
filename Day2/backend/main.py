from fastapi import FastAPI
from services.groq_llm import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/home")
def read_root():
    return {"Hello": "JMIT"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/chat/{user_prompt}")
def chat(user_prompt: str):
    response = generate_response([{"role": "user", "content": user_prompt}])
    return {"response": response}
