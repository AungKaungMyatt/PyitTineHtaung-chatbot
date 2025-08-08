from fastapi import FastAPI, Request, Response, Query
from handlers.intent_handler import detect_intent
from chatbot import ChatBot
from middleware.audit import AuditMiddleware
from handlers import health
from utils.request_norm import normalize_payload
from utils.audit_utils import set_audit_headers
from utils.sanitizer import detect_language

app = FastAPI()
bot = ChatBot()
app.add_middleware(AuditMiddleware)
app.include_router(health.router)

@app.post("/chat")
async def chat(request: Request, response: Response, verbose: bool = Query(False)):
    payload = await request.json()
    user_input, intent_hint, used_legacy = normalize_payload(payload)

    if not user_input or not user_input.strip():
        return {"response": "Message cannot be empty."}

    lang = request.headers.get("x-lang") or detect_language(user_input) or "en"
    intent, score = (intent_hint, 1.0) if intent_hint else detect_intent(user_input, lang)

    text = bot.get_response(user_input, intent)

    set_audit_headers(response, router_path=intent or "fallback", intent=intent, intent_score=score)
    response.headers["x-lang"] = lang
    if used_legacy:
        response.headers["x-legacy-fields"] = ",".join(f"{k}->{v}" for k, v in used_legacy.items())

    if not verbose:
        return {"response": text}
    return {
        "response": text, "intent": intent, "score": score, "lang": lang,
        "canonical_request": {"user_input": user_input, "intent": intent_hint},
        "used_legacy": used_legacy
    }
