# IMPORT LIBRARIES AND LOAD ENVIRONMENT VARIABLES

import gradio as gr
import os
import groq
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq()

if GROQ_API_KEY is None:
    raise Exception("API key is missing.")

# STEP 2: BASIC UI INTERFACE


# def respond_basic(message, history):
#     return f"I'm crazy about AI! ***m: {message}, ***h: {history}"


# gr.ChatInterface(fn=respond_basic).launch()


# def respond_basic(message, history):
#     return f"I'm crazy about AI! And I'm chatting with you in the browser."


# gr.ChatInterface(fn=respond_basic).launch(inbrowser=True) # (share=True)

def respond_ai(message, history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}
                ] + history + [{"role": "user", "content": message}]
    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    reply = response.choices[0].message.content
    return reply


gr.ChatInterface(fn=respond_ai).launch()
