import os
import sys
import argparse

from xai_sdk import Client
from xai_sdk.chat import user
from xai_sdk.tools import code_execution, web_search, x_search

def ask_grok(question):
    client = Client(api_key=os.getenv("XAI_API_KEY"))
    chat = client.chat.create(
        model="grok-4-fast",  # reasoning model
        tools=[
            web_search(),
            x_search(),
            code_execution(),
        ],
    )

    chat.append(user(question))

    response = chat.sample()
    return response.content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact with the Grok AI model.")
    parser.add_argument("question", type=str, help="The question to ask Grok.")
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

    grok_response = ask_grok(full_question)
    print(grok_response)