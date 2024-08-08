#!/usr/bin/env python3
import json
import sys

def process_json(data):
    if isinstance(data, list):
        for item in data:
            process_json(item)
    elif isinstance(data, dict):
        #if "t" in data and data["t"] == "Div" and "r-stack" in data.get("c", []):
        if "t" in data and data["t"] == "Div" and isinstance(data.get("c", []), list) and len(data["c"]) > 1 and "r-stack" in data["c"][0][1]:
            if data["c"][1][0]["t"] == "Para":
                data["c"][1][0]["t"] = "Plain"
        else:
            for key, value in data.items():
                process_json(value)

if __name__ == "__main__":
    # Read JSON data from stdin as text
    input_json_text = sys.stdin.read()

    try:
        input_json = json.loads(input_json_text)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e, file=sys.stderr)
        sys.exit(1)

    process_json(input_json)

    # Print the modified JSON to stdout
    json.dump(input_json, sys.stdout, indent=2)
