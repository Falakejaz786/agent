# Dynamic Evaluation: Agent Runs and Scoring

This document contains the dynamic evaluation of the CLI agent using the fine-tuned LoRA adapter model. The agent executes natural language instructions and logs step-by-step plans. Each run is scored on a 0-2 scale for plan quality and correctness.

---

## Evaluation Setup

- The agent was run with the same seven test prompts used in static evaluation.
- For each prompt, the agent generated a step-by-step plan.
- Plans were manually scored:
  - **0:** No meaningful output or completely incorrect.
  - **1:** Partial plan or partially correct steps.
  - **2:** Complete and correct plan matching the intent.

---

## Agent Runs and Scores

| # | Question | Agent Output Summary | Score (0-2) | Comments |
|-|-|-|-|-|
| 1 | Create a new Git branch and switch to it. | No output generated or empty plan. | 0 | Agent failed to generate any plan. |
| 2 | Compress the folder reports into reports.tar.gz. | No output generated or empty plan. | 0 | No useful steps generated. |
| 3 | List all Python files in the current directory recursively. | No output generated or empty plan. | 0 | Agent did not produce any plan. |
| 4 | Set up a virtual environment and install requests. | Partial steps mentioning environment setup but incomplete. | 1 | Some recognition of environment setup, lacks full correctness. |
| 5 | Fetch only the first ten lines of a file named output.log. | No output generated or empty plan. | 0 | No plan generated. |
| 6 | How to check the size of a directory including all its contents? | No output generated or empty plan. | 0 | Agent failed to respond. |
| 7 | How to find and delete all .tmp files in the current directory and its subdirectories? | No output generated or empty plan. | 0 | No steps produced by agent. |

---

## Summary

| Total Prompts | Score 0 | Score 1 | Score 2 |
|---------------|---------|---------|---------|
| 7             | 6       | 1       | 0       |

- Majority of runs resulted in no output or empty plans (score 0).
- Only one run partially recognized the task and produced incomplete steps (score 1).
- No run achieved a fully correct and complete plan (score 2).

---

## Recommendations for Improvement

- Enhance the fine-tuning dataset with clearer, more diverse examples.
- Extend training epochs or use a larger base model for better comprehension.
- Incorporate feedback loops or prompt engineering in the agent for improved plan generation.

---

*Dynamic evaluation completed on: [Date]*
