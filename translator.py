import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_and_adapt(text, source_lang="svenska", target_lang="engelska", tone="informell"):
    prompt = f"""
Du är en realtidsöversättare. Översätt följande {source_lang}-text till {target_lang} med en {tone} ton (t.ex. "du"-form eller avslappnat språk). Anpassa språket så att det är lätt att läsa upp med talsyntes.

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
