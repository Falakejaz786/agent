import json
import os
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

def is_shell_command(line):
    shell_cmd_starts = (
        "cd ", "ls", "git ", "mkdir", "rm", "echo", "touch",
        "python", "./", "sudo", "cat ", "cp ", "mv ", "pwd"
    )
    return line.strip().startswith(shell_cmd_starts)

def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python agent.py \"<your instruction>\"")
        return

    instruction = sys.argv[1]

    base_model_name = "EleutherAI/gpt-neo-125M"
    print("⏳ Loading tokenizer and base model...")
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    base_model = AutoModelForCausalLM.from_pretrained(base_model_name)

    print("✅ Loading fine-tuned LoRA adapter...")
    model = PeftModel.from_pretrained(base_model, "./lora-gptneo")
    model.eval()

    # Few-shot style prompt with example to guide output format
    prompt = f"""
Instruction: Initialize a new Git repo and push code to GitHub
Steps:
1. git init
2. git add .
3. git commit -m "Initial commit"
4. git branch -M main
5. git remote add origin <repo_url>
6. git push -u origin main

Instruction: {instruction}
Steps:
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            top_p=0.9,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            early_stopping=True,
        )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract the steps after last "Steps:" occurrence
    steps_text = generated_text.split("Steps:")[-1].strip()
    # Filter and clean lines that look like numbered steps
    steps = []
    for line in steps_text.split("\n"):
        line = line.strip()
        # Accept lines that start with a number and dot like "1. git init"
        if line and (line[0].isdigit() and line[1] == "."):
            steps.append(line)

    if not steps:
        print("⚠️ No steps were generated.")
        return

    os.makedirs("logs", exist_ok=True)
    log_path = "logs/trace.jsonl"
    log_entries = []

    print("\n📋 Generated Steps:")
    for idx, step in enumerate(steps, start=1):
        dry_run = False
        # If first step looks like a shell command, echo it as dry-run
        # Remove numbering for checking shell command
        step_text = step.partition(" ")[2].strip() if " " in step else step
        if idx == 1 and is_shell_command(step_text):
            dry_run = True
            print(f"(Dry-run) {step_text}")
        else:
            print(f"Step {idx}: {step_text}")

        log_entries.append({
            "step": idx,
            "text": step_text,
            "dry_run": dry_run
        })

    with open(log_path, "a") as f:
        for entry in log_entries:
            f.write(json.dumps(entry) + "\n")

if __name__ == "__main__":
    main()
