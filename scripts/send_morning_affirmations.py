#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Send rotating morning affirmations")
    parser.add_argument("--affirmations", default=str(Path(__file__).resolve().parents[1] / "data" / "affirmations.json"))
    parser.add_argument("--state", default=str(Path(__file__).resolve().parents[1] / "logs" / ".affirmation-rotation-state.json"))
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--channel", default="telegram")
    parser.add_argument("--target", default="-1003555895168")
    parser.add_argument("--thread-id", default="6228")
    parser.add_argument("--account", default="default")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    affirmations = load_json(Path(args.affirmations))
    if not isinstance(affirmations, list) or not affirmations:
        raise SystemExit("No affirmations found")

    state_path = Path(args.state)
    state = {"next_index": 0}
    if state_path.exists():
        try:
            state = load_json(state_path)
        except Exception:
            state = {"next_index": 0}

    start = int(state.get("next_index", 0)) % len(affirmations)
    selected = [affirmations[(start + i) % len(affirmations)] for i in range(args.count)]

    lines = ["Good morning. Read these out loud now:", ""]
    for i, item in enumerate(selected, start=1):
        text = item.get("text", "").strip()
        lines.append(f"{i}) {text}")

    lines.extend([
        "",
        "Reply DONE after reading.",
        "Extra credit: send a mirror voice message repeating all 5 (DONE + VOICE)."
    ])
    msg = "\n".join(lines)

    cmd = [
        "openclaw", "message", "send",
        "--channel", args.channel,
        "--target", args.target,
        "--thread-id", args.thread_id,
        "--account", args.account,
        "--message", msg,
    ]

    if args.dry_run:
        print("[DRY RUN]", " ".join(cmd))
        print(msg)
        return

    subprocess.run(cmd, check=True)
    state["next_index"] = (start + args.count) % len(affirmations)
    save_json(state_path, state)


if __name__ == "__main__":
    main()
