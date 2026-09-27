"""
Intelligence: The "brain" that processes information and makes decisions using LLMs.
This component handles context understanding, instruction following, and response generation.

More info: https://platform.openai.com/docs/guides/text?api-mode=responses
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def basic_intelligence(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.create(model="gpt-4o", input=prompt)
    return response.output_text


if __name__ == "__main__":
    result = basic_intelligence(prompt="What is artificial intelligence?")
    print("Basic Intelligence Output:")
    print(result)
