import openai
import json
import os
import random

# Constants
INPUT_DIR = os.path.join("..", "data", "formatted_interviews")
OUTPUT_DIR = os.path.join("..", "data", "refined_interviews")

# Initialize OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

def is_short_content(content):
    return len(content.split()) <= 3

# Generates 2 questions and 2 answers that lead up to the provided question and answer for added context
def generate_contextual_conversation(question, answer):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Generate a 3-question, 3-answer conversation that leads up to and ends with the exact same Question and Answer as the one provided. Ensure the tone for all of the answers you generate matches the original answer. Start each question with 'Question:' and each answer with 'Answer:'. Make sure there is a newline between each question and answer and make sure the conversation makes sense."},
            {"role": "user", "content": f"Question: {question}, Answer: {answer}"}
        ]
    )
    return completion.choices[0].message['content']

# Parses the generated contextual conversation into a list of messages
def parse_contextual_conversation(conversation_text):
    lines = conversation_text.split("\n")
    messages = []
    for i in range(4):  # We only want the first 2 Q&As
        line = lines[i]
        role = "user" if "Question:" in line else "assistant"
        content = line.split(":")[1].strip()
        messages.append({"role": role, "content": content})
    return messages

def augment_prompt(question, answer):
    augmented_prompts = []
    
    for _ in range(3):  # Generate 3 different wordings
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You will be provided a Question and an Answer. Rework the question to make it standalone and contextually appropriate for the given answer while still maintaining some of the contextual details from the original question. Return only the reworked question."},
                {"role": "user", "content": f"Question: {question}, Answer: {answer}"}
            ]
        )
        reworked_question = completion.choices[0].message['content']
        augmented_prompts.append(reworked_question)
    
    return augmented_prompts


def refine_dataset(filename):
    with open(os.path.join(INPUT_DIR, filename + ".json"), 'r') as f:
        data = json.load(f)

    refined_data = []
    for conversation in data:
        user_content = conversation['messages'][0]['content']
        assistant_content = conversation['messages'][1]['content']

        if is_short_content(user_content) or is_short_content(assistant_content):
            continue

        # Randomly decide if a Q&A pair should get a contextual conversation
        if random.choice([True, False]):
            contextual_conversation_text = generate_contextual_conversation(user_content, assistant_content)
            contextual_messages = parse_contextual_conversation(contextual_conversation_text)
            contextual_messages.append({"role": "user", "content": user_content})
            contextual_messages.append({"role": "assistant", "content": assistant_content})
            refined_data.append({"messages": contextual_messages})
        else:
            augmented_prompts = augment_prompt(user_content, assistant_content)
            for prompt in augmented_prompts:
                refined_data.append({
                    "messages": [
                        {"role": "user", "content": prompt},
                        {"role": "assistant", "content": assistant_content}
                    ]
                })

    with open(os.path.join(OUTPUT_DIR, filename + ".json"), 'w') as f:
        json.dump(refined_data, f, indent=4)

if __name__ == "__main__":
    filename = input("Enter the name of the file (without .json extension): ")
    refine_dataset(filename)
    print(f"Refined dataset saved to {os.path.join(OUTPUT_DIR, filename + '.json')}")
