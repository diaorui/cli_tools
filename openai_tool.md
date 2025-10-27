# OpenAI Tool Usage

This document explains how to use `openai_tool.py` to interact with the OpenAI models from your command line, including built-in web search capabilities.

## Purpose

`openai_tool.py` is a simple Python script that allows you to send a question to an OpenAI model and receive its response directly in your terminal. It's designed for easy integration into command-line workflows or other scripts, and leverages the model's built-in web search tool when needed.

## Prerequisites

Before using `openai_tool.py`, ensure you have:

1.  **OpenAI Python library installed**: If not, install it using pip:
    ```bash
    pip install openai
    ```
2.  **OpenAI API Key**: You need an API key from OpenAI. Set it as an environment variable named `OPENAI_API_KEY`.
    ```bash
    export OPENAI_API_KEY="your_openai_api_key_here"
    ```
    Replace `"your_openai_api_key_here"` with your actual API key.

## Usage

To use `openai_tool.py`, run it from your terminal with your question as a command-line argument. You can also optionally provide one or more files whose content should be included in the question.

```bash
python openai_tool.py "Your question goes here." [--files /path/to/file1.md /path/to/file2.txt]
```

The script will print the OpenAI model's response directly to standard output.

## Built-in Web Search

`openai_tool.py` is configured to allow the OpenAI model to use its built-in web search tool if it deems necessary to answer your question. The model will automatically perform a web search and incorporate the results into its response.

## Examples

### Basic Question

```bash
python openai_tool.py "What is the capital of France?"
```

### Getting latest news

```bash
python openai_tool.py "What is the current weather in London?"
```

### Summarizing content from multiple files

To summarize the content of multiple files (e.g., `article1.md` and `article2.md`), use the `--files` argument:

```bash
python openai_tool.py "Please summarize the key points of these documents." --files article1.md article2.md
```

This command will read the content of both `article1.md` and `article2.md` and include them in the prompt sent to the OpenAI model.

### Fact-checking a Markdown File

To fact-check the content of a Markdown file (e.g., `your_article.md`), use the `--files` argument:

```bash
python openai_tool.py "Please fact-check this document for accuracy and consistency." --files your_article.md
```

This command will read the content of `your_article.md` and include it in the prompt sent to the OpenAI model, making the process robust against special characters within the file.