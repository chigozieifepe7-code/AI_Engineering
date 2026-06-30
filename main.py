# IMPORT LIBRARIES AND LOAD ENVIRONMENT VARIABLES

import os
import groq
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq()

if GROQ_API_KEY is None:
    raise Exception("API key is missing.")
else:
    print(GROQ_API_KEY[:8])

# CALL THE API

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is an okapi",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)