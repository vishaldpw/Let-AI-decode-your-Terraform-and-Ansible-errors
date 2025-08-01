import os
import sys
import openai

def load_error_log(file_path):
    """Load and filter Terraform error lines from the log."""
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        # Filter lines with 'Error:' or terraform trace blocks
        filtered_lines = [line.strip() for line in lines if "Error:" in line or "│" in line]
        return "\n".join(filtered_lines).strip()
    except FileNotFoundError:
        return None

def explain_error_with_ai(error_text):
    """Send error to OpenAI for explanation."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set.")
        sys.exit(1)

    if not error_text:
        print("No errors found in the log.")
        return

    print("Sending error to OpenAI for explanation...\n")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert in Terraform. Analyze the following error message from a Terraform run. "
                    "Provide a clear explanation and recommend how to fix it. Avoid generic responses and hallucinations."
                ),
            },
            {
                "role": "user",
                "content": error_text,
            },
        ],
        temperature=0.3,
    )

    explanation = response.choices[0].message["content"]
    print("🔍 AI Explanation:\n")
    print(explanation)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python explain-error.py <path-to-error.log>")
        sys.exit(1)

    error_log_path = sys.argv[1]
    error_text = load_error_log(error_log_path)
    explain_error_with_ai(error_text)
