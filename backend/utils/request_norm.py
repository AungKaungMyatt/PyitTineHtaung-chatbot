from typing import Optional, Tuple, Dict

LEGACY_FIELD_MAP = {
    "message": "user_input",
    "text": "user_input",
    "user_message": "user_input",
    "user_text": "user_input",
    "user_intent": "intent",
}

def normalize_payload(payload: Dict) -> Tuple[str, Optional[str], Dict[str, str]]:
    """
    Returns (user_input, intent, used_legacy) where used_legacy is a map of legacy->canonical.
    Accepts legacy keys and maps them to canonical:
      - user_input
      - intent
    """
    used_legacy = {}

    # Copy to avoid mutating original
    data = dict(payload or {})

    # Fold legacy keys into canonical
    for legacy, canonical in LEGACY_FIELD_MAP.items():
        if legacy in data and canonical not in data:
            data[canonical] = data[legacy]
            used_legacy[legacy] = canonical

    user_input = data.get("user_input") or ""
    intent_hint = data.get("intent")

    return user_input, intent_hint, used_legacy
