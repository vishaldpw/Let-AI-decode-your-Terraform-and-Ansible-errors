
# Folder Structure

```plaintext    
├── .github
│   └── workflows
│       └── ai-terraform-check.yml
├── scripts
│   └── explain_error.py
├── terraform
│   └── main.tf
├── ansible
│   └── playbook.yml


## 📌 Explain Terraform & Ansible Errors using AI

This project captures errors from Terraform or Ansible, and uses OpenAI to explain them in simple words.

### 🔧 Structure
- `terraform/main.tf`: Sample infra
- `ansible/play1.yaml`: Sample playbook
- `scripts/explain-error.py`: Sends error to OpenAI
- `.github/workflows/ai-terraform-check.yml`: GitHub Actions CI

### 🧠 To Use:
- Break Terraform or Ansible
- Push code
- Check GitHub Actions log for AI explanation

### 🔐 Required Secret:
- `OPENAI_API_KEY`: Your OpenAI key
