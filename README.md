# AI Command-Line Tools

This repository contains a collection of Python scripts designed to interact with various AI models directly from your command line. These tools are built for seamless integration with AI-powered CLIs like Gemini CLI, but are also versatile enough for use in shell scripts, automation workflows, or any other command-line based application.

## Purpose

The primary goal of these tools is to provide a simple and consistent interface for querying different large language models (LLMs) without leaving your terminal. You can ask questions, summarize files, and pipe the output to other standard command-line utilities.

## Why This Is Useful

Integrating multiple AI models into a single CLI workflow provides several advantages:

*   **AI-Powered Reflection**: This approach allows for a form of "reflection." If the primary LLM in your CLI is struggling with a task or providing a suboptimal response, you can delegate the task to a different model. This allows you to get a "second opinion" from another AI, leveraging its unique strengths and potentially overcoming the first model's weaknesses.

*   **Access to Specialized Capabilities**: Different models excel at different tasks. For example, one model might have superior real-time web search capabilities for news-related queries, while another might be fine-tuned for high-quality code generation. These tools allow you to direct your request to the best model for the job.

*   **Resilience and Redundancy**: If one model's API is temporarily unavailable, you can easily switch to another to continue your work without interruption.

## Tools Included

### Grok AI Tool (`grok_tool.py`)

-   **Purpose**: Interact with the Grok AI model.
-   **Prerequisites**:
    1.  Python 3.x
    2.  xAI SDK: `pip install xai-sdk`
    3.  API Key: Set the `XAI_API_KEY` environment variable.
        ```bash
        export XAI_API_KEY="your_xai_api_key_here"
        ```

### OpenAI Tool (`openai_tool.py`)

-   **Purpose**: Interact with OpenAI models (e.g., GPT-4). It supports the model's built-in web search capabilities.
-   **Prerequisites**:
    1.  Python 3.x
    2.  OpenAI Library: `pip install openai`
    3.  API Key: Set the `OPENAI_API_KEY` environment variable.
        ```bash
        export OPENAI_API_KEY="your_openai_api_key_here"
        ```

### Claude Tool (`claude_tool.py`)

-   **Purpose**: Interact with the Claude AI model. It supports the model's built-in web search capabilities.
-   **Prerequisites**:
    1.  Python 3.x
    2.  Anthropic Python library: `pip install anthropic`
    3.  API Key: Set the `ANTHROPIC_API_KEY` environment variable.
        ```bash
        export ANTHROPIC_API_KEY="your_anthropic_api_key_here"
        ```

## Usage in an AI-Powered CLI (e.g., Gemini CLI)

These tools are designed to be called by an AI-powered CLI. You would typically instruct your CLI to use a specific tool to accomplish a task. The CLI would then use the corresponding Python script to execute your request.

To enable this, you can first instruct the CLI to learn about the tools by reading their markdown documentation.

**Prompt for an AI CLI:**
> "Learn the tools in this directory by reading `@grok_tool.md`, `@openai_tool.md` and `@claude_tool.md`"

Once the CLI is aware of the tools, you can use them as follows.

### Example 1: Asking a Direct Question

You can instruct your CLI to use one of the tools to answer a question.

**Prompt for an AI CLI:**
> "Use the `grok_tool` to tell me about the latest advancements in AI-powered code generation."

**What happens:** The AI CLI interprets this, finds the `grok_tool.py` script, and executes it with the question as an argument.

### Example 2: Summarizing Files

To have the CLI summarize files, you would reference them in your prompt, delegating the file-reading task to the tool itself.

**Prompt for an AI CLI:**
> "Use the `openai_tool` to summarize the key points of `@article1.md` and `@article2.md`."

**What happens:** The AI CLI identifies the file paths in your prompt and passes them as arguments to the `openai_tool.py` script, which then reads the files directly.

### Example 3: Fact-Checking a Document

You can ask the CLI to perform tasks like fact-checking on a local file.

**Prompt for an AI CLI:**
> "Use `grok_tool` to fact-check the document `@draft.md` for accuracy."

**What happens:** The CLI uses the `grok_tool.py` script, providing the content of `draft.md` as context for the fact-checking request.

## Other Uses

Beyond interactive CLI use, these scripts can be integrated into:
-   Automated reporting scripts.
-   Content generation pipelines.
-   CI/CD workflows for code analysis.
-   Anywhere you need to programmatically access the power of LLMs from a shell environment.
