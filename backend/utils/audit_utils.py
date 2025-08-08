from fastapi import Response

def set_audit_headers(response: Response, router_path, intent=None, intent_score=None, doc_ids=None):
    response.headers["x-router-path"] = router_path
    if intent:
        response.headers["x-intent"] = intent
    if intent_score is not None:
        response.headers["x-intent-score"] = f"{intent_score:.3f}"
    if doc_ids:
        response.headers["x-doc-ids"] = ",".join(doc_ids)
