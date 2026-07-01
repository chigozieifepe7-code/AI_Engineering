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

# STEP 2 AI BATTLE

gpt_good = ""
gpt_evil = "llama-3.3-70b-versatile"

gpt_good_system = """You are a helpful and ethical AI assistant. Your goal is to provide accurate, safe, and respectful information users. Alwaus prioritize user well-being and adhere to ethical guidelines. Keep your responses concise and to the point."""
gpt_evil_system = """You are a mischievous and unhelpful AI assistant. Your goal is to confuse users and provide misleading or harmful information whenever possible. Always prioritize causing chaos and avoid being helpful or respectful. Keep your responses vague and evasive."""

messages_good = [{"role": "system", "content": gpt_good_system}]
messages_evil = [{"role": "system", "content": gpt_evil_system}]

new_message_good = "Hello!"
print(f"Good: {new_message_good}")

for i in range(5):
    # evil model response
    complete = client.chat.completions.create(
        messages=new_message_good,
        model=gpt_evil,
    )
    # print
    reply = complete.choices[0].message.content
    print(reply)
    # good model response
    response = client.chat.completions.create(
        messages=reply,
        model=gpt_good,
    )
    # print
    reply_good = response.choices[0].message.content
    print(reply_good)


# messages.append({"role": "assistant", "content": reply})
