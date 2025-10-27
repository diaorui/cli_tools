import os
import sys
import argparse
import json
import openai

# Initialize the OpenAI client
# It's recommended to load the API key from an environment variable
# export OPENAI_API_KEY="your_openai_api_key_here"
client = openai.OpenAI()

def ask_openai(question: str):
    response = client.responses.create(
        model="gpt-5-mini",
        tools=[{"type": "web_search"}],
        input=question
    )

    return response.output_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact with the OpenAI model.")
    parser.add_argument("question", type=str, help="The question to ask OpenAI.")
    parser.add_argument("--files", nargs='+', type=str, help="Paths to files whose content should be included in the question.")

    args = parser.parse_args()

    full_question = args.question
    
    if args.files:
        all_file_content = []
        for file_path in args.files:
            try:
                with open(file_path, 'r') as f:
                    file_content = f.read()
                all_file_content.append(f"--- FILE: {file_path} ---\n{file_content}")
            except FileNotFoundError:
                print(f"Error: File not found at {file_path}", file=sys.stderr)
                sys.exit(1)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}", file=sys.stderr)
                sys.exit(1)
        
        full_question = f"--- FILE CONTENT START ---\n{'\n\n'.join(all_file_content)}\n--- FILE CONTENT END ---\n\n{args.question}"

    openai_response = ask_openai(full_question)
    print(openai_response)
