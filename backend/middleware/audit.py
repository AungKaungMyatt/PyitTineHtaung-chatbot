import time, uuid, json
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        req_id = str(uuid.uuid4())

        body_bytes = await request.body()
        try:
            payload = json.loads(body_bytes.decode("utf-8") or "{}")
        except Exception:
            payload = None

        response = await call_next(request)
        duration_ms = int((time.time() - start) * 1000)

        # read lang from response header first, then request header
        lang = response.headers.get("x-lang") or request.headers.get("x-lang")

        print(json.dumps({
            "req_id": req_id,
            "path": request.url.path,
            "method": request.method,
            "status": response.status_code,
            "duration_ms": duration_ms,
            "lang": lang,
            "router_path": response.headers.get("x-router-path"),
            "intent": response.headers.get("x-intent"),
            "intent_score": response.headers.get("x-intent-score"),
            "doc_ids": response.headers.get("x-doc-ids"),
            "payload": payload,
        }))

        return response
