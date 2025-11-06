import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def generate_meme_caption(topic: str) -> str:
    """
    Generates a funny meme caption using Groq + LLaMA.
    """
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = f"Generate a short, funny meme caption about '{topic}'. Keep it witty and under 15 words."

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # updated model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=50,
    )

    # Use dot notation instead of dictionary access
    caption = completion.choices[0].message.content.strip()
    return caption

