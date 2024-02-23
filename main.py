import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")

client = OpenAI(api_key=api_key, organization=org_id)

with open("system_message.txt", "r") as file:
    system_message = file.read().strip()

with open("user_message.txt", "r") as file:
    user_message = file.read().strip()

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)
