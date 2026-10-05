import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'Day_1')
    )
)

from config import client, MODEL


# Tool
def read_private_data():
    with open("private_data.txt", "r") as file:
        return file.read()


question = input("Enter your question: ")

print("\n=== AI Agent ===")

# Loop - Step 1: understand the request
print("Step 1: Agent received the question.")

# Tool use
print("Step 2: Agent decided to use the private-data tool.")
private_data = read_private_data()

print("Step 3: Tool returned the private data.")

# Loop - Step 2: observe tool result and answer
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": """You are a student course assistant.
Use the private college data provided below to answer the question.
Calculate discounts accurately.

Private college data:
""" + private_data
        },
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

print("Step 4: Agent observed the tool result and generated the answer.")

print("\nAI Agent Answer:")
print(response.choices[0].message.content)