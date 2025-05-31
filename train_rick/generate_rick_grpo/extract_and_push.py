import re
import json

from datasets import load_dataset

# Define the regex pattern to match valid JSONL entries with "question" and "answer"
pattern = re.compile(r'^\s*{\s*"question"\s*:\s*".+?",\s*"solution"\s*:\s*".+?"\s*}\s*$')

input_file = f"data.txt"
output_file = f"dataset.jsonl"
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line_idx, line in enumerate(infile):
        if line.startswith("{"):  # Check if the line starts with '{'
            try:
                row = json.loads(line)
            except Exception as e:
                print(f"Invalid JSON at line {line_idx + 1}: {line.strip()}")
                continue
            # filter key "question" and "solution"
            row = {key: row[key] for key in row if key in ["question", "solutions"]}
            line = json.dumps(row, ensure_ascii=False) + "\n"
            outfile.write(line)

dataset = load_dataset("json", data_files=output_file)
dataset = dataset["train"].train_test_split(test_size=204)
dataset.push_to_hub("qgallouedec/rick-physics-grpo")
