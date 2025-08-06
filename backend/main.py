from fastapi import FastAPI, Request
from handlers.intent_handler import detect_intent
from chatbot import ChatBot

app = FastAPI()
bot = ChatBot()

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        message = data.get("message", "").strip()
        if not message:
            return {"response": "Message cannot be empty."}
        
        intent = detect_intent(message)
        response = bot.get_response(message, intent)
        return {"response": response}

    except Exception as e:
        return {"response": f"An error occurred: {str(e)}"}
    
'''from fastapi import FastAPI, Request
from handlers.intent_handler import detect_intent
from chatbot import ChatBot

app = FastAPI()
bot = ChatBot()

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        message = data.get("message", "").strip()
        if not message:
            return {"response": "Message cannot be empty."}
        intent = detect_intent(message)
        response = bot.get_response(message)
        return {"response": response}
    except Exception as e:
        return {"response": f"An error occurred: {str(e)}"}'''