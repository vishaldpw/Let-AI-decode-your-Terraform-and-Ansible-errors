import os
import sys
from openai import OpenAI

# Ensure you imported sys — already fixed
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read error log passed as argument
with open(sys.argv[1], "r") as f:
    error_log = f.read()

# Call OpenAI API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a Terraform and Ansible expert. Explain the following error and suggest how to fix it.",
        },
        {"role": "user", "content": error_log},
    ],
    temperature=0.3,
)

# Print the explanation
print(response.choices[0].message.content)
