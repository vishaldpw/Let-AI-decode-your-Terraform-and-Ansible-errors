import openai
import sys
import os

with open(sys.argv[1], "r") as f:
    error_text = f.read()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a DevOps expert."},
        {"role": "user", "content": f"Explain this Terraform error:\n\n{error_text}"}
    ]
)

print(response.choices[0].message.content)
