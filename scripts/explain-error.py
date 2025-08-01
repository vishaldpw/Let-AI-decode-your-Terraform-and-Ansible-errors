import openai
import sys
import os

# Check if error log file was passed
if len(sys.argv) < 2:
    print("Usage: python explain-error.py <error_log_file>")
    sys.exit(1)

# Load OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

openai.api_key = api_key

# Read the error log
with open(sys.argv[1], "r") as f:
    error_text = f.read()

# Trim very long errors (optional safeguard)
max_chars = 3000
if len(error_text) > max_chars:
    error_text = error_text[-max_chars:]  # keep last part of log

# Call OpenAI GPT
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful DevOps engineer."},
            {"role": "user", "content": f"Explain this Terraform or Ansible error in simple terms and how to fix it:\n\n{error_text}"}
        ]
    )
    print("\n🤖 AI Explanation:\n")
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"Error while calling OpenAI API: {e}")
