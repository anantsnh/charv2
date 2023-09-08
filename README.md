# **charv2**
*character.ai but better*

## **Processing Interview Data**

1. Navigate to the `data_processing` directory:
   - All necessary scripts are located here.
2. Format the interview:
   - Paste an interview into `format_interview.py` and execute the script.
3. Review the formatted interview:
   - Head to the `formatted_interviews` sub-directory inside the `data` directory.
   - Examine the content, removing any Q&A pairs unsuitable for training.
4. Refine the interview:
   - Execute the `refine-interview.py` script.
     - This augments the questions for each Q&A, ensuring they make sense in a standalone context.
5. Review the refined interview:
   - Navigate to the `refined_interviews` sub-directory in the `data` directory.
   - Again, remove any Q&A pairs you deem inappropriate for training.

## **Processing General Information (from Blogs, Books, Lectures)**

1. Refine the content:
   - Paste the information into `refine-quotes.py` and run it.
     - This creates user prompts for each "quote" and saves them as JSON.

## **Additional Dataset Refinement**

1. Enhance the dialogue flow:
   - Run `add-questions-to-refined.py`.
     - This adds follow-up questions to approximately 35% of the assistant's responses, ensuring a natural conversation flow.

## **Converting Refined Data to JSONL**

1. Convert the dataset:
   - Insert a system prompt into `convert-refined-to-jsonl.py` and execute.
   - The JSONL version of the refined dataset will be saved in the `jsonl_files` sub-directory inside the `data` directory.

## **Fine-tuning the Model**

1. Execute the `finetune.py` script.
2. Profit!
