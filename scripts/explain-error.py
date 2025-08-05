import os
import sys
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Paths
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
error_log_path = os.path.join(base_dir, "logs/error.log")
explanation_path = os.path.join(base_dir, "logs/error-explained.txt")
issue_body_path = os.path.join(base_dir, "logs/gh-issue-body.md")

# Validate error log
if not os.path.exists(error_log_path):
    print(f"❌ Error log not found at: {error_log_path}")
    sys.exit(1)

with open(error_log_path, "r") as f:
    error_text = f.read()

if not error_text.strip():
    print("❌ Error log is empty. Nothing to analyze.")
    sys.exit(1)

print("🔍 Sending error to OpenAI...")

# Call OpenAI for explanation
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": f"Explain the following Terraform error in simple terms:\n\n{error_text}"
        }
    ]
)

ai_explanation = response.choices[0].message.content.strip()

# Save AI explanation
with open(explanation_path, "w") as f:
    f.write(ai_explanation)

# Save GitHub Issue body
with open(issue_body_path, "w") as f:
    f.write("## 🚨 Terraform Apply Failed\n\n")
    f.write("### ❌ Raw Error:\n")
    f.write("```\n")
    f.write(error_text[:1000])  # Truncate to avoid size limits
    f.write("\n```\n\n")
    f.write("### 🤖 AI Explanation:\n")
    f.write(ai_explanation)

print("✅ AI explanation saved to logs/error-explained.txt")
print("✅ GitHub issue body saved to logs/gh-issue-body.md")