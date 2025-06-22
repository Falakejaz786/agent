# 🖥️ Command-Line Q&A Model Fine-Tuning

This repository contains an end-to-end demo of fine-tuning a small language model (≤ 2B parameters) on command-line Q&A pairs using LoRA, and wrapping it into a CLI assistant.

---

## 🚀 Project Overview

✅ **Data:**  
Collected over 150 public Q&A pairs covering common command-line topics: Git, Bash, tar/gzip, grep, venv, and more.

✅ **Model:**  
Fine-tuned `TinyLlama-1.1B` / `Phi-2` / `GPT-Neo-125M` (open weights, ≤ 2B parameters) using LoRA for 1 epoch on a free Colab T4 GPU.

✅ **CLI Agent:**  
- Accepts a natural-language instruction.
- Generates a step-by-step plan using the fine-tuned model.
- Dry-runs shell commands (via `echo <command>`).
- Logs each step to `logs/trace.jsonl`.

✅ **Evaluation:**  
- Compared base vs fine-tuned outputs on 7 prompts (5 predefined + 2 custom edge cases).
- BLEU / ROUGE-L scores + plan quality (0-2 scale).

---

## ⚙ How to Use

### 🔹 Clone the repo
```bash
git clone https://github.com/Falakejaz786/agent.git
cd your-repo-name
````
### 🔹 Run the CLI agent

```bash
python agent.py
```

Type a natural-language task like:

```
create a new git branch called feature-login
```

The agent generates a plan, dry-runs commands (`echo <command>`), and logs to `logs/trace.jsonl`.

---

## 📊 Evaluation

* **Metrics:** BLEU / ROUGE-L
* **Plan Quality (0-2):**

  * 0 → Poor/wrong plan
  * 1 → Partial/incomplete plan
  * 2 → Clear and correct plan

---

## 💡 Future Improvements

* Extend dataset with harder multi-step command-line tasks.
* Add safe real command execution (sandboxed) instead of echo.

