import openai
import os
import sys

openai.api_key = os.environ["OPENAI_API_KEY"]

# Fix the correct log path
error_log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs/error.log"))

if not os.path.exists(error_log_path):
    print("❌ Error log not found:", error_log_path)
    sys.exit(1)

with open(error_log_path, "r") as f:
    error_text = f.read()

if not error_text.strip():
    print("❌ Error log is empty. Nothing to analyze.")
    sys.exit(1)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": f"Explain the following Terraform error in simple terms:\n\n{error_text}"
        }
    ]
)

print(response["choices"][0]["message"]["content"])
