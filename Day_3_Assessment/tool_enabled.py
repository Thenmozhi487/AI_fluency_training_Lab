from openai import OpenAI
from dotenv import load_dotenv
import os

from tools import get_course_fee

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
    print("\nQuestion:", question)

    if "CS101" in question:
        print("Tool Call: get_course_fee('CS101')")
        result = get_course_fee("CS101")
        print("Tool Result:", result)

    elif "DS303" in question:
        print("Tool Call: get_course_fee('DS303')")
        result = get_course_fee("DS303")
        print("Tool Result:", result)

    else:
        result = None

    prompt = f"""
Answer the user's question using the tool result when one is provided.

User question: {question}

Tool result: {result}
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    print("Final Answer:", response.choices[0].message.content)