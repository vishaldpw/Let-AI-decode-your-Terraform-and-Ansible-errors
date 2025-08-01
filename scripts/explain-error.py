from openai import OpenAI
import os
import sys

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Path from root to error log
error_log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../terraform/error.log"))

with open(error_log_path, "r") as f:
    error_text = f.read()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": f"Explain the following Terraform error in simple terms:\n\n{error_text}"
        }
    ]
)

print(response.choices[0].message.content)
