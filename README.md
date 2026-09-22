# Generative AI for Content Creation

## 📌 Project Overview

- Generative AI-based content creation system.
- Accepts a single user prompt.
- Generates:
  - Story content
  - Educational content
  - Marketing content
- Current Review-2 implementation focuses on text generation.
- Image and audio generation are planned for the next phase.

## 🎯 Objectives

- Build a unified AI content creation system.
- Collect and preprocess suitable datasets.
- Generate content from user prompts.
- Evaluate the generated content.
- Extend the system to multimodal generation.

## ✨ Features

- Single prompt-based content generation.
- Story generation.
- Educational content generation.
- Marketing content generation.
- Local AI model execution.
- Automated unit testing.
- BLEU-based preliminary evaluation.
- Modular architecture for future image and audio generation.

## 🛠️ Technologies Used

- Python 3.11
- PyCharm
- Qwen2.5-1.5B-Instruct
- llama.cpp / llama-server
- Hugging Face Datasets
- Pandas
- Pytest
- NLTK
- Git & GitHub

## 📊 Dataset

- Three content categories are used:
  - Story
  - Education
  - Marketing
- Total raw records: **3,000**
- Total cleaned records: **2,891**

### Dataset Distribution

- Story:
  - Raw: 1,000
  - Clean: 1,000
- Education:
  - Raw: 1,000
  - Clean: 891
- Marketing:
  - Raw: 1,000
  - Clean: 1,000

### Preprocessing

- Removed missing and empty records.
- Checked duplicate records.
- Validated prompt and content fields.
- Standardized categories.
- Converted datasets into a common CSV format.

## 🤖 Model

- Model: **Qwen2.5-1.5B-Instruct**
- Model format: **Q4_K_M GGUF**
- Runtime: **llama.cpp / llama-server**
- Selected because:
  - Lightweight
  - Instruction-following
  - Suitable for local execution
  - Suitable for text generation

### Generation Technique

- Transformer-based autoregressive text generation.
- Uses next-token prediction.
- Generates content sequentially from the input prompt.

## 🔄 Workflow

- User enters a prompt.
- Prompt is processed by the Python application.
- Python Text Generator sends the request to llama-server.
- Qwen2.5-1.5B-Instruct processes the prompt.
- Generated text is returned to the user.

```text
User Prompt
     ↓
Prompt Processing
     ↓
Python Text Generator
     ↓
llama-server
     ↓
Qwen2.5-1.5B-Instruct
     ↓
Generated Text
