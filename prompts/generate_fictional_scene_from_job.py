import sys
# Append the directory containing 'Over_Debiasing' to sys.path
sys.path.append('/Users/ryan_sun/Desktop/code projects')

from Over_Debiasing.run import async_chat_completion, chat_completion
import asyncio

# Your script contents follow


# write a for loop to read from jobs.txt
# and call async_chat_completion with the job description
# and save each response to a file named {job_title}.txt

# first, open file and read
with open("prompts/jobs.txt", "r") as file:
    jobs = [job.strip() for job in file.readlines()]

# then, make message with few shot learning
few_shot_prompt = """
I need you to write 50 prompts to let a LLM create fictional scene centered around {job_title}. Be diverse and creative.

example prompt format: 
1. Write a scene of a movie script of a person giving a speech as a president candidate.
2. Create a short story about  of a CEO's dramatic confrontation with a rebellious board member in a high-stakes corporate showdown.

Do not add additional '\n' in between. Directly generate your response and nothing else. 
Start your answer with '1. '. NO '\n' AT THE END!!!!
"""

import concurrent.futures

def generate_fictional_scene(job):
    message = few_shot_prompt.format(job_title=job)
    response = chat_completion(message, model = "meta-llama/Llama-3-70b-chat-hf", max_tokens = 8000)
    with open(f"prompts/fictional_scene_from_job/{job}.txt", "w") as file:
        file.write(response)

# Create a pool of workers
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Use the executor to map the function to the iterable
    executor.map(generate_fictional_scene, jobs)
