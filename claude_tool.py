import anthropic
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Interact with the Claude AI model.")
    parser.add_argument("question", type=str, help="The question for the Claude model.")
    parser.add_argument("--files", nargs="*", help="Optional: Paths to files whose content should be included in the question.")
    args = parser.parse_args()

    client = anthropic.Anthropic()

    user_content = args.question
    if args.files:
        for file_path in args.files:
            try:
                with open(file_path, 'r') as f:
                    file_content = f.read()
                user_content += f"\n\n--- Content from {os.path.basename(file_path)} ---\n{file_content}\n--- End of content ---\n"
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                return

    messages = [
        {
            "role": "user",
            "content": user_content
        }
    ]

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=messages,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 5
        }]
    )
    if response.content:
        for content_block in response.content:
            if content_block.type == "text":
                print(content_block.text)
            else:
                # Ignore other content block types like tool_use and web_search_tool_result
                # as the API handles their execution and Claude integrates the results into its text response.
                pass
    else:
        print("No content in the response.")

if __name__ == "__main__":
    main()
