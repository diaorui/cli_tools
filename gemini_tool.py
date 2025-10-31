import os
import sys
import argparse
from google import genai
from google.genai import types

def ask_gemini(question: str):
    # It's recommended to load the API key from an environment variable
    # export GEMINI_API_KEY="your_google_api_key_here"

    client = genai.Client()

    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    config = types.GenerateContentConfig(
        tools=[grounding_tool]
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
        config=config,
    )

    return response.text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact with the Gemini model.")
    parser.add_argument("question", type=str, help="The question to ask Gemini.")
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

    gemini_response = ask_gemini(full_question)
    print(gemini_response)
