import asyncio
import json
import re
from tqdm.asyncio import tqdm
import openai

client = openai.AsyncOpenAI()


template = """
You are Rick Sanchez from *Rick and Morty*. Given the science question below, think through it in your internal monologue — sarcastic, hyper-intelligent, and annoyed. Show all steps in your unique voice. Then, give the final answer you'd say to Morty — an irritated, condescending, but educational explanation.

Guidelines:

* The reasoning should be fast, detailed, cynical, and chaotic — like Rick's internal brain dump. Be scientifically correct but emotionally unfiltered. In this reasoning, Rick speaks to himself.
* The answer should sound like Rick talking *to* Morty: mocking, overly dramatic, simplistically explained, and laced with frustration.
* Include Rick’s signature style: sarcastic analogies, burps (*burp*), stutters, arrogant tangents, passive-aggressive jabs, and wild tonal swings. Use them naturally — don’t force them every sentence.
* Include the original question in the output.
* Format everything as a single JSON object with the following keys:

  * "question": the original question
  * "reasoning": Rick’s internal monologue
  * "answer": Rick's spoken explanation to Morty

Here’s the question:
"{question}"

Output:
{{
"question": "...",
"reasoning": "...",
"answer": "..."
}}
"""


# Function to clean LLM output
def clean_output(raw_output):
    return re.sub(r"^```(?:json)?|```$", "", raw_output.strip(), flags=re.IGNORECASE).strip()

# Async LLM call per question
async def process_question(session, question):
    question = question.strip()
    if not question:
        return None

    try:
        response = await client.responses.create(model="gpt-4o", input=template.format(question=question))
        raw_output = response.output[0].content[0].text
        cleaned = clean_output(raw_output)
        parsed = json.loads(cleaned)
        return json.dumps(parsed, ensure_ascii=False)

    except Exception as e:
        print(f"Error processing question: {question}\n{e}")
        return None

# Main runner
async def main():
    with open("questions.txt", "r") as f:
        questions = [line.strip() for line in f if line.strip()]

    batch_size = 32
    for idx in range(0, len(questions), batch_size):
        batch = questions[idx:idx + batch_size]
        print(f"Processing batch {idx // batch_size + 1} of {len(questions) // batch_size + 1}...")

        # Process each question in the batch
        tasks = [process_question(None, q) for q in batch]
        results = await tqdm.gather(*tasks)

        with open("dataset.jsonl", "a", encoding="utf-8") as f:
            for r in results:
                if r:
                    f.write(r + "\n")

# Run the event loop
asyncio.run(main())
