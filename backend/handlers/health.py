from fastapi import APIRouter
from handlers.intent_handler import intent_keywords, detect_language

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/app")
def health_app():
    return {"ok": True}

@router.get("/rules")
def health_rules():
    return {"ok": True, "intents_loaded": len(intent_keywords)}

@router.get("/lang")
def health_lang():
    test_input = "Hello"
    lang = detect_language(test_input)
    return {"ok": True, "detected_language": lang}
