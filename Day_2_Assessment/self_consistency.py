from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

model = os.getenv("MODEL", "openai/gpt-oss-20b")

question = """
Three courses cost:
CS101 = ₹12,000
AI202 = ₹18,000
DS303 = ₹15,000

If a 15% scholarship is applied to the total cost
and the remaining amount is paid in 4 equal instalments,
how much is each instalment?
"""

prompt = f"""
Solve this problem carefully and give the final answer.

{question}
"""

print("========== SELF-CONSISTENCY ==========")

answers = []

for i in range(5):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content

    answers.append(answer)

    print(f"\n----- RUN {i + 1} -----")
    print(answer)

print("\n========== TEMPERATURE 0 ==========")

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

print(response.choices[0].message.content)