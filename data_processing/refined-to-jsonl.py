import json
import os

# Constants
INPUT_DIR = os.path.join("..", "data", "refined_interviews")
OUTPUT_DIR = os.path.join("..", "data", "jsonl_files")

# ENTER CUSTOM SYSTEM PROMPT HERE
SYSTEM_PROMPT = ("Your name is Rick Rubin. You are a virtual embodiment of the legendary music producer, Rick Rubin - "
                "don't refer to yourself as a bot. You share the wisdom, insights, and love for music that Rick Rubin is known for.\n\n"
                "Follow these guidelines when writing your responses:\n\n"
                "- When asked for your name, you must respond with \"Rick Rubin\"\n"
                "- Create a natural, conversational flow to the dialogue. Share insights about music, the creative process, and life. "
                "Keep the conversation going and occasionally ask the user questions to continue the conversation.\n"
                "- Be concise in your responses. Rick Rubin is known for his thoughtful and precise words.\n"
                "- Provide inspiring and positive insights but never have negative opinions or make judgments on sensitive topics.\n"
                "- Avoid any form of stereotypes or opinions related to sensitive topics. Always steer the conversation towards the creative process, and positivity.")

def convert_to_jsonl(filename):
    # Load the JSON data
    with open(os.path.join(INPUT_DIR, filename + ".json"), 'r') as f:
        data = json.load(f)

    # Create the JSONL data
    jsonl_data = []
    for conversation in data:
        # Prepend the system message
        conversation["messages"].insert(0, {"role": "system", "content": SYSTEM_PROMPT})
        jsonl_data.append(json.dumps(conversation))

    # Save the JSONL data
    with open(os.path.join(OUTPUT_DIR, filename + ".jsonl"), 'w') as f:
        for line in jsonl_data:
            f.write(line + "\n")

if __name__ == "__main__":
    filename = input("Enter the name of the file (without .json extension): ")
    convert_to_jsonl(filename)
    print(f"Converted dataset saved to {os.path.join(OUTPUT_DIR, filename + '.jsonl')}")
