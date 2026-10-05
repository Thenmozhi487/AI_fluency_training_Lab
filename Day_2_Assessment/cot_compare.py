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

Which is cheaper:
1. CS101 and AI202 with a 10% scholarship
OR
2. All three courses with a 25% scholarship?

Calculate both totals and find the difference.
"""

# Direct Prompting
direct_prompt = f"""
Answer the following question directly.
Do not explain your reasoning step-by-step.

{question}
"""

# Chain-of-Thought style prompt
cot_prompt = f"""
Solve the following problem carefully.

Reason through the calculation step by step internally,
then give the final answer with the important calculation steps.

{question}
"""

print("========== DIRECT PROMPTING ==========")

direct_response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": direct_prompt}
    ],
    temperature=0
)

print(direct_response.choices[0].message.content)

print("\n========== CHAIN-OF-THOUGHT ==========")

cot_response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": cot_prompt}
    ],
    temperature=0
)

print(cot_response.choices[0].message.content)