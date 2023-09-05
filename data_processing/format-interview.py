import json
import os
import re

output_directory = os.path.join("..", "data", "formatted_interviews")

# PASTE INTERVIEW BELOW THEN RUN SCRIPT
INTERVIEW = """
EZRA KLEIN: So this can be a conversation about finding the states of mind that help you listen, that help you discern, that help you create. And so as we start it, how should we find the right state of mind for this?

RICK RUBIN: Well, we can do maybe five slow deep breaths together to get us rolling. And on the inhale, think about the inhale. And on the exhale — when I say think, maybe that’s not the right word. Maybe say to yourself, cue yourself — inhale. As you’re inhaling, we’re inhaling. And then when you exhale, focus on the exhale. We’re exhaling now. And nothing else.

We’ll do five breaths only being present with our inhale and exhale. Are we ready?

EZRA KLEIN: Let’s do it.

RICK RUBIN: Let’s do it.

[PAUSE]

EZRA KLEIN: So assuming your breaths take about the same amount of time as mine, where are you that you weren’t a minute ago?

RICK RUBIN: We had a little technical issue before we started, which created some energy in my body that was like a rattle. And by the second breath, it felt like that settled. And by the — I don’t know — towards the end, I realized I don’t know how many breaths I’ve done because I’m feeling very relaxed. And that felt really good. That’s what it did for me.

And I also felt like — and I don’t know this — but it tuned us to each other, that now we’re starting at least on a closer wavelength than before that happened.

EZRA KLEIN: I think that’s right. So I normally think it’s cliché to begin by asking anybody about the title of their book, but I do think there’s an interesting interaction for you between the title and subtitle — “The Creative Act” and “A Way of Being.” So tell me about the way of being side of this.

RICK RUBIN: The way of being is really what the book is about. The creative act is what I started out wanting to write. And through the process of looking at what were the decisions made to make things to the best of our ability, it came back to a way of being and that, right now, regardless of what else is going on in my life, the most important thing in the world to me is this conversation that we’re having. This is what we’re doing now. And as long as it takes is as long as it takes. And if it went all day, I would go all day. And that’s the way of being in the world. It’s a combination of paying attention and commitment to doing whatever it takes to do your best, whatever that is.

EZRA KLEIN: You and I have talked a bit about your love of Stephen Mitchell’s translation of the “Tao Te Ching.” This struck me very much as a Daoist book, not just in content but in form. I think when I saw this book coming, I expected to read a lot of recollections of Rick Rubin’s history with various artists and times in the production room and in the studio.

And it reads very Daoistly. It’s very poetic. It’s very spare. There’s not a lot of “I.” It’s very comfortable with paradox and tension and contradiction. So that was intentional?

RICK RUBIN: Absolutely. It would have been much easier to do the book that you described, but it was never interesting to me from the beginning. And when I first set out to work on this, seven or eight years ago, I met with a handful of publishers at that time and told them about what I wanted the book to be.

And all of them had the same reactions, like, well, yeah, but you’re going to tell your stories from the studio and you’re going to tell the stories of all the great people you’ve worked with. I said, no, no, no, that’s not what it is. That makes it a smaller book. This is a timeless book. This is about a way of looking at things.

And I wanted to be very clear in talking about the book, this is not a book about me. There’s not one story about me in the recording studio. There’s not one story about any artist I’ve ever worked with. That’s not what this book is. It’s more of a philosophical work, thinking about how we make beautiful things.


"""

def format_interview(interview_text, interviewer_name):
    lines = interview_text.strip().split("\n")
    conversations = []
    conversation = None

    for line in lines:
        # Remove text within square brackets such as [LAUGHTER] etc.
        line = re.sub(r'\[.*?\]', '', line).strip()

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
