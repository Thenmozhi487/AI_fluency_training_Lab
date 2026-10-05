from openai import OpenAI
from dotenv import load_dotenv
import os

from tools import get_course_fee, calculate_discount

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

model = os.getenv("MODEL", "openai/gpt-oss-20b")


print("========== ReAct AGENT ==========")

# Thought
print("\nTHOUGHT 1:")
print("I need the fees of CS101, AI202 and DS303.")

# Action
print("\nACTION 1:")
print("get_course_fee(CS101)")
cs101 = get_course_fee("CS101")

print("get_course_fee(AI202)")
ai202 = get_course_fee("AI202")

print("get_course_fee(DS303)")
ds303 = get_course_fee("DS303")

# Observation
print("\nOBSERVATION 1:")
print(f"CS101 = ₹{cs101}")
print(f"AI202 = ₹{ai202}")
print(f"DS303 = ₹{ds303}")


# Thought
print("\nTHOUGHT 2:")
print("I will compare the two scholarship options.")


# Action
print("\nACTION 2:")
print("Calculate CS101 + AI202 with 10% scholarship.")

option1_before = cs101 + ai202
option1 = calculate_discount(option1_before, 10)

print("Calculate all three courses with 25% scholarship.")

option2_before = cs101 + ai202 + ds303
option2 = calculate_discount(option2_before, 25)


# Observation
print("\nOBSERVATION 2:")
print(f"Option 1 = ₹{option1:.2f}")
print(f"Option 2 = ₹{option2:.2f}")


# Final Answer
print("\nFINAL ANSWER:")

difference = option2 - option1

if option1 < option2:
    print("CS101 + AI202 with 10% scholarship is cheaper.")
else:
    print("All three courses with 25% scholarship is cheaper.")

print(f"Difference = ₹{difference:.2f}")