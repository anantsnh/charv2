# charv2
character.ai but good

# to use:
- go to the data_processing directory
- paste an interview into format_interview this will format the interview
- go to the formatted_interviews directory in the data directory
- go through the interview and remove any questions/answers that you do not think are suitable for training
- run the refine-interview.py script, this will augment the questions for each interview Q&A to make it make sense in solo context
- paste a system prompt into refined-to-jsonl.py and run
- run finetune.py
- profit
