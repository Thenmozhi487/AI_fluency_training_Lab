import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'Day_1')
    )
)

from config import client, MODEL

question = input("Enter your question: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful student assistant."
        },
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)

print("\nChatbot Answer:")
print(response.choices[0].message.content)