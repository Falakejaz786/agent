# Project Report: Command-Line Instruction Fine-Tuning with LoRA

## Objective  
This project aimed to build an end-to-end demo that fine-tunes a small language model to understand and generate step-by-step plans for command-line instructions. The demo includes data collection, model fine-tuning using LoRA, CLI agent development, evaluation, and reporting.

## Data Collection  
- Collected over 150 validated question-answer pairs related to command-line topics (Git, Bash, tar/gzip, grep, venv, etc.)  
- Source: Stack Overflow API, filtered by tags and top voted answers  
- Data saved in `data/commandline_qa.json`

## Model Fine-Tuning  
- Base model: TinyLlama-1.1B (open weights, ≤ 2B parameters)  
- Fine-tuning method: LoRA (Low-Rank Adaptation) using QLoRA technique  
- Training done on free Google Colab T4 GPU for one epoch  
- Adapter size ≤ 500 MB  
- Training time: ~2 hours  
- Hyperparameters: learning rate 1e-4, batch size 8, max sequence length 512

## CLI Agent  
- `agent.py` script accepts natural language instructions from terminal input  
- Generates step-by-step command plans using the fine-tuned model  
- Executes shell commands in dry-run mode (echo) if applicable  
- Logs all steps and execution traces to `logs/trace.jsonl`

## Evaluation  

### Static Evaluation  
- Compared base model vs. fine-tuned model outputs on 7 test prompts  
- Metrics: BLEU and ROUGE-L scores calculated against reference commands  
- Results: Both models returned mostly empty outputs; low BLEU/ROUGE scores (0.0–0.25)  
- Indicates room for improvement in fine-tuning and dataset quality

### Dynamic Evaluation  
- Agent run on same prompts, manual scoring on 0-2 scale for plan quality  
- Scores: Mostly 0 (no output), one partial plan with score 1, zero full plans  
- Suggests limited current practical usability

## Challenges and Limitations  
- Rate limiting issues with Stack Overflow API slowed data collection  
- Model struggled to generate meaningful outputs, possibly due to limited data and one epoch training  
- Small model size constrained language understanding capabilities

## Improvement Ideas  
1. Increase dataset size and diversify with synthetic/generated data  
2. Train for more epochs and experiment with larger base models  
3. Implement prompt engineering and reinforcement learning to boost agent response quality

---

*Project developed and evaluated in June 2025.*

