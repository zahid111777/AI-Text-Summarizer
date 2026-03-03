import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from keys/.env (one level up from src/)
env_path = Path(__file__).resolve().parent.parent / "keys" / ".env"
load_dotenv(dotenv_path=env_path)

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

MODEL = "gpt-4o-mini"


def summarize_text(text: str, length: str = "medium", style: str = "paragraph") -> str:
    """
    Summarize the given text using OpenAI gpt-4o-mini.

    Parameters
    ----------
    text   : str  – The input text to summarize.
    length : str  – Desired summary length: "short", "medium", or "long".
    style  : str  – Output format: "paragraph", "bullet points", or "one-liner".

    Returns
    -------
    str – The generated summary.
    """
    length_guide = {
        "short":  "1-2 sentences",
        "medium": "3-5 sentences",
        "long":   "a detailed paragraph",
    }
    length_instruction = length_guide.get(length, "3-5 sentences")

    system_prompt = (
        "You are an expert summarizer. "
        "Provide clear, accurate, and concise summaries without adding information "
        "that is not present in the original text."
    )

    user_prompt = (
        f"Summarize the following text in {length_instruction} "
        f"using the '{style}' format.\n\n"
        f"TEXT:\n{text}"
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content.strip()
