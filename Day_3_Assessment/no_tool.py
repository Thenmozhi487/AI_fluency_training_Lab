from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

model = os.getenv("MODEL", "openai/gpt-oss-20b")

questions = [
    "What is the current fee of CS101?",
    "Which is cheaper: ₹12,000 or ₹18,000?",
    "What is the fee of DS303?"
]

for question in questions:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    print("\nQuestion:", question)
    print("LLM Answer:", response.choices[0].message.content)