#!/usr/bin/env python3
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_json(path: Path, schema_path: Path):
    schema = load_json(schema_path)
    data = load_json(path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    errors = []
    if isinstance(data, list):
        for i, item in enumerate(data):
            for err in validator.iter_errors(item):
                errors.append(f"{path}:{i}: {err.message}")
    else:
        for err in validator.iter_errors(data):
            errors.append(f"{path}: {err.message}")
    return errors


def validate_jsonl(path: Path, schema_path: Path):
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            for err in validator.iter_errors(obj):
                errors.append(f"{path}:{i}: {err.message}")
    return errors


def main():
    checks = [
        (ROOT / "data/exercises.json", ROOT / "schemas/exercise.schema.json", "json"),
        (ROOT / "data/affirmations.json", ROOT / "schemas/affirmation.schema.json", "json"),
        (ROOT / "data/routines/no_equipment_full_body_hiit.json", ROOT / "schemas/routine.schema.json", "json"),
        (ROOT / "data/routines/single_kettlebell_full_body_hiit.json", ROOT / "schemas/routine.schema.json", "json"),
        (ROOT / "logs/affirmations.example.jsonl", ROOT / "schemas/affirmation_log.schema.json", "jsonl"),
        (ROOT / "logs/workouts.example.jsonl", ROOT / "schemas/workout_log.schema.json", "jsonl"),
    ]

    all_errors = []
    for data_path, schema_path, kind in checks:
        if kind == "jsonl":
            all_errors.extend(validate_jsonl(data_path, schema_path))
        else:
            all_errors.extend(validate_json(data_path, schema_path))

    if all_errors:
        print("VALIDATION FAILED")
        for err in all_errors:
            print("-", err)
        raise SystemExit(1)

    print("VALIDATION PASSED")
    for data_path, _, _ in checks:
        print(f"- {data_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
