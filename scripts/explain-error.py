import openai
import os
import sys

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open(sys.argv[1], "r") as f:
    error_log = f.read()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Terraform expert. Explain the following error:"},
        {"role": "user", "content": error_log}
    ],
    temperature=0.3,
)

print(response.choices[0].message.content)
