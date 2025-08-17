from fastapi import FastAPI, HTTPException
import openai
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["index.html"],  # Change this to your frontend's URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()

# Set OpenAI API key
openai.api_key = "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 "

def get_data_from_db(query):
    conn = sqlite3.connect("customer_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT response FROM faq WHERE question LIKE ?", ('%' + query + '%',))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "I couldn't find an answer for that."

class ChatRequest(BaseModel):
    message: str


@app.post("/chat/")
async def chat(request: ChatRequest):
    return {"response": f"You said: {request.message}"}

def chat_with_bot(user_input: str):
    db_response = get_data_from_db(user_input)
    
    if db_response != "I couldn't find an answer for that.":
        return {"bot_response": db_response}
    
    # If no DB match, use OpenAI Agent SDK
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful customer support assistant."},
                  {"role": "user", "content": user_input}]
    )
    
    return {"bot_response": response["choices"][0]["message"]["content"]}

