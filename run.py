# This python scripts calls together.ai api

import os, asyncio
from together import AsyncTogether, Together
from typing import Union, List, Dict

async_client = AsyncTogether(api_key=os.environ.get("TOGETHER_API_KEY"))
messages = [
    "What are the top things to do in San Francisco?",
    "What country is Paris in?",
]

def chat_completion(message, 
                    model: str = "meta-llama/Llama-3-8b-chat-hf", 
                    temperature = 0.6,
                    max_tokens = 512,
                    stop=["</s>"]):
    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
    if isinstance(message, str):
        message = [{"role": "user", "content": message}]
    elif isinstance(message, list):
        pass
    else:
        raise ValueError("message must be a string or a list of dictionaries", type(message))
    response = client.chat.completions.create(
        model=model,
        messages=message,
        temperature=temperature,
        max_tokens=max_tokens,
        # stop=stop,
    )
    return response.choices[0].message.content
async def async_chat_completion(messages):
    async_client = AsyncTogether(api_key=os.environ.get("TOGETHER_API_KEY"))
    tasks = [
        async_client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[{"role": "user", "content": message}],
        )
        for message in messages
    ]
    responses = await asyncio.gather(*tasks)
    return_responses = []
    for response in responses:
        return_responses.append(response.choices[0].message.content)
    return return_responses


if __name__ == "__main__":
    responses = asyncio.run(async_chat_completion(messages))
    for response in responses:
        print(response)