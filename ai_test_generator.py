import os
from dotenv import load_dotenv
from groq import Groq

from prompts import QA_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_test_cases(user_story):

    prompt = QA_PROMPT.format(
        user_story=user_story
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content