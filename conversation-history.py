# IMPORT LIBRARIES AND LOAD ENVIRONMENT VARIABLES

import os
import groq
from groq import Groq
from dotenv import load_dotenv
from IPython.display import Markdown, display
from pprint import pprint

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq()

# CALL THE API
messages = [{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Next week I'm traveling to Spain.",}
            ]
response = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
    )

reply = response.choices[0].message.content
messages.append({"role": "assistant", "content": reply})

pprint(messages)


