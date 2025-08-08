import sys, json, time, csv
from pathlib import Path

# Ensure imports work when running this file directly
THIS = Path(__file__).resolve()
BACKEND = THIS.parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from chatbot import ChatBot
from handlers.intent_handler import detect_intent
from utils.sanitizer import detect_language

DATA_DIR = BACKEND / "tests" / "data"
OUT_DIR = BACKEND / "tests" / "out"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def load_jsonl(p: Path):
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)

def run_file(path: Path, bot: ChatBot):
    rows = []
    for item in load_jsonl(path):
        text = item["text"]
        expected = item.get("expected_intent")

        lang = detect_language(text)
        t0 = time.time()

        intent, score = detect_intent(text, lang)
        resp = bot.get_response(text, intent)

        latency_ms = int((time.time() - t0) * 1000)
        rows.append({
            "file": path.name,
            "lang": lang,
            "text": text,
            "expected_intent": expected,
            "pred_intent": intent,
            "intent_score": round(float(score), 3) if score is not None else None,
            "latency_ms": latency_ms,
            "response_preview": (resp or "")[:120].replace("\n", " ")
        })
    return rows

def summarize(rows):
    total = len(rows)
    fallthrough = sum(1 for r in rows if r["pred_intent"] == "ai")
    labeled = [r for r in rows if r["expected_intent"] is not None and r["expected_intent"] != "ai"]
    correct = sum(1 for r in labeled if r["pred_intent"] == r["expected_intent"])
    p95 = sorted(r["latency_ms"] for r in rows)[max(0, int(0.95 * total) - 1)] if total else 0
    return {
        "total": total,
        "fallthrough_count": fallthrough,
        "fallthrough_rate": round(fallthrough / total, 3) if total else 0.0,
        "labeled_known": len(labeled),
        "rule_precision_on_known": round(correct / len(labeled), 3) if labeled else None,
        "latency_p95_ms": p95
    }

def main():
    bot = ChatBot()
    all_rows = []

    for fname in ["queries.en.jsonl", "queries.my.jsonl"]:
        fpath = DATA_DIR / fname
        if not fpath.exists():
            print(f"[WARN] Missing {fpath}")
            continue
        rows = run_file(fpath, bot)
        all_rows.extend(rows)
        out_csv = OUT_DIR / f"{fname.replace('.jsonl','')}.results.csv"
        with out_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"[OK] {out_csv}  rows={len(rows)}")

    if all_rows:
        summary = summarize(all_rows)
        print("\n==== Evaluation Summary ====")
        for k, v in summary.items():
            print(f"{k}: {v}")
    else:
        print("[ERROR] No evaluation data found.")

if __name__ == "__main__":
    main()
