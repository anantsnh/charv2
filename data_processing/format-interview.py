import json
import os
import re

output_directory = os.path.join("..", "data", "formatted_interviews")

# PASTE INTERVIEW BELOW THEN RUN SCRIPT
INTERVIEW = """

"""

def format_interview(interview_text, interviewer_name):
    lines = interview_text.strip().split("\n")
    conversations = []
    conversation = None

    for line in lines:
        # Remove text within square brackets such as [LAUGHTER] etc.
        line = re.sub(r'\[.*?\]', '', line).strip()

        if not line:
            continue

        colon_index = line.find(":")
        if colon_index == -1:
            continue

        role = "user" if interviewer_name in line[:colon_index] else "assistant"
        content = line[colon_index + 1:].strip()

        if role == "user":
            if conversation:
                conversations.append(conversation)
            conversation = {
                "messages": []
            }

        conversation["messages"].append({
            "role": role,
            "content": content
        })

    if conversation:
        conversations.append(conversation)

    return conversations

if __name__ == "__main__":
    interviewer_name = input("Enter the interviewer's name (e.g., EZRA KLEIN): ")
    formatted_data = format_interview(INTERVIEW, interviewer_name)
    output_filename = input("Enter the output filename (without .json extension): ") + ".json"
    output_path = os.path.join(output_directory, output_filename)

    with open(output_path, 'w') as outfile:
        json.dump(formatted_data, outfile, indent=4)

    print(f"Formatted interview saved to {output_path}")
