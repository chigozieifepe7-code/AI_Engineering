# IMPORT LIBRARIES AND API KEYS 


import os
import groq
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq()

if GROQ_API_KEY is None:
    raise Exception("API key is missing.")

# SEARCHING THE WEB

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me the 3 top stories in AI in this past week, according to reliable news media. Do not use simple news aggregators. Each story should be from a separate source and date. Include dates.",
        }
    ],
    max_tokens=500,
    model="groq/compound-mini"
)

search_results = chat_completion.choices[0].message.content
print(search_results)

# SUMMARIZE AND WRITE SOCIAL MEDIA POST

system_message = """
You are a helpful assistant who creates amazing linkedIn posts about AI based on text you are provided with. Make the post engaging and interesting. 
Also make concise and add a thought provoking question at the end to encourage comments.
"""

prompt = f"""
The following text contains top 3 news stories about AI from the past week.
Now please write my linkedIn post based on this information.

{search_results}

"""

completion = client.chat.completions.create(
    
    model="openai/gpt-oss-20b",
    messages=[{"role": "system", "content": system_message},
              {"role": "user", "content": prompt}],
    max_tokens=500, 
    temperature=2
    
)

chat_response = completion.choices[0].message.content
print(chat_response)