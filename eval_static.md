# Static Evaluation: Base vs. Fine-Tuned LoRA Model

This document compares the outputs of the base model and the fine-tuned LoRA adapter model on a set of test prompts. Evaluation metrics include BLEU and ROUGE-L scores against the reference answers.

---

## Test Prompts and Results Summary

| # | Question | Base Model Output | LoRA Model Output | BLEU (Base) | ROUGE-L (Base) | BLEU (LoRA) | ROUGE-L (LoRA) |
|-|-|-|-|-|-|-|
| 1 | Create a new Git branch and switch to it. | *No output generated.* | *No output generated.* | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 2 | Compress the folder reports into reports.tar.gz. | *No output generated.* | *No output generated.* | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 3 | List all Python files in the current directory recursively. | *No output generated.* | *No output generated.* | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 4 | Set up a virtual environment and install requests. | 1. Install the virtual environment.<br>2. Install the virtual environment. | 1. Install the virtual environment.<br>2. Install the virtual environment. | 0.0000 | 0.2500 | 0.0000 | 0.2500 |
| 5 | Fetch only the first ten lines of a file named output.log. | *No output generated.* | *No output generated.* | 0.0000 | 0.2222 | 0.0000 | 0.2222 |
| 6 | How to check the size of a directory including all its contents? | *No output generated.* | *No output generated.* | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 7 | How to find and delete all .tmp files in the current directory and its subdirectories? | *No output generated.* | *No output generated.* | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

---

## Reference Answers (Ground Truth)

1. `git branch <branch_name>`  
   `git checkout <branch_name>`

2. `tar -czvf reports.tar.gz reports`

3. `find . -name '*.py'`

4. ```
   python3 -m venv env  
   source env/bin/activate  
   pip install requests
