# Grok Tool Usage

This document explains how to use `grok_tool.py` to interact with the Grok AI model from your command line.

## Purpose

`grok_tool.py` is a simple Python script that allows you to send a question to the Grok AI model and receive its response directly in your terminal. It's designed for easy integration into command-line workflows or other scripts.

## Prerequisites

Before using `grok_tool.py`, ensure you have:

1.  **xAI SDK installed**: If not, install it using pip:
    ```bash
    pip install xai-sdk
    ```
2.  **XAI API Key**: You need an API key from xAI. Set it as an environment variable named `XAI_API_KEY`.
    ```bash
    export XAI_API_KEY="your_xai_api_key_here"
    ```
    Replace `"your_xai_api_key_here"` with your actual API key.

## Usage

To use `grok_tool.py`, run it from your terminal with your question as a command-line argument. You can also optionally provide one or more files whose content should be included in the question.

```bash
python grok_tool.py "Your question goes here." [--files /path/to/file1.md /path/to/file2.txt]
```

The script will print Grok's response directly to standard output.

## Examples

### Basic Question

```bash
python grok_tool.py "What is the capital of France?"
```

### Getting latest news

```bash
python grok_tool.py "What is the latest news on OpenAI's AI browser?"
```

### Summarizing content from multiple files

To summarize the content of multiple files (e.g., `article1.md` and `article2.md`), use the `--files` argument:

```bash
python grok_tool.py "Please summarize the key points of these documents." --files article1.md article2.md
```

This command will read the content of both files and include them in the prompt sent to Grok.

### Fact-checking a Markdown File

To fact-check the content of a Markdown file (e.g., `your_article.md`), use the `--files` argument:

```bash
python grok_tool.py "Please fact-check this document for accuracy and consistency." --files your_article.md
```

This command will read the content of `your_article.md` and include it in the prompt sent to Grok, making the process robust against special characters within the file.