CLI Instruction Generation with LoRA Fine-Tuned Model

Project Overview:
This project fine-tunes an open-weight causal language model (≤ 2B parameters) using LoRA on 150+ command-line Q&A pairs (Git, Bash, grep, tar, venv, etc.). It provides a CLI agent that generates detailed step-by-step instructions and dry-runs shell commands from natural language input.

Requirements:
- Python 3.8 or higher
- GPU recommended for fine-tuning (Google Colab T4 or local GPU)
- Internet connection for downloading models

Installation:
1. Clone the repository:
   git clone <your-repo-url>
   cd <repo-folder>

2. (Optional) Create and activate a virtual environment:
   python -m venv venv
   For Linux/macOS: source venv/bin/activate
   For Windows: venv\Scripts\activate

3. Install required packages:
   pip install -r requirements.txt

Data:
- data/qa_pairs.json contains 150+ validated command-line question and answer pairs used for fine-tuning.

Fine-Tuning the Model:
Using the training script:
   python train_lora.py --data_path data/qa_pairs.json --output_dir lora-gptneo --epochs 1

Or use the Colab notebook:
Open train_lora.ipynb in Google Colab to fine-tune on a free T4 GPU.

Running the CLI Agent:
Generate step-by-step instructions from the command line:
   python agent.py "Create a new Git branch and switch to it"

- The agent outputs numbered steps.
- If the first step looks like a shell command, it is dry-run echoed (echo <cmd>).
- All interactions are logged to logs/trace.jsonl.

Evaluation:
- Static evaluation (base vs. fine-tuned outputs + BLEU/ROUGE) in eval_static.md.
- Dynamic evaluation (agent runs + manual scoring) in eval_dynamic.md.
- Project summary and insights in report.md.

Project Structure:
agent.py
data/
  qa_pairs.json
lora-gptneo/
  (LoRA adapter files ≤ 500MB)
evaluate_script.py
train_lora.py / train_lora.ipynb
logs/
  trace.jsonl
eval_static.md
eval_dynamic.md
report.md
requirements.txt
README.md

Notes:
- The LoRA adapter must be downloaded or fine-tuned before running agent.py.
- Python 3.8+ recommended.
- Internet is required initially for model downloads.

