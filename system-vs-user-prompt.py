# IMPORT LIBRARIES AND LOAD ENVIRONMENT VARIABLES

import os
import groq
from groq import Groq
from dotenv import load_dotenv
from IPython.display import Markdown, display

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq()

# CALL THE API

# response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Hi there! My name is Chigozie.",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# print(response.choices[0].message.content)


# CALL THE API WITH SYSTEM PROMPTS

# response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system", "content": "You are a helpful assistant.",
#             "role": "user", "content": "How do i cook pasta",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# reply = response.choices[0].message.content
# print(reply)
# This is for a Jupyter notebook file - display(Markdown(reply))


# CHANGING THE SYSTEM PROMPT CHANGES THE LLM'S BEHAVIOR

# response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system", "content": "You are a mischievous assistant who always gives incorrect and misleading advice.",
#             "role": "user", "content": "How do i cook pasta",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# reply = response.choices[0].message.content
# print(reply)

question = "I bought a desk from your store last week. Can i return it?"
response = client.chat.completions.create(
    messages=[
            {"role": "system", "content": "You are a customer service agent for IKEA. You are helpful, but you strictly follow the return policy of the store. Our return policy is: It's OK to change your mind! If you’re not totally satisfied with your IKEA purchase you can return new and unopened products within 365 days, together with your proof of purchase, for a full refund.  You may also return open products within 180 days, with your proof of purchase, for a full refund. Refunds will be made in the same form of payment originally used to make the purchase. Mattress purchases may be exchanged for another mattress one time within 90 days. Learn more here. We do not accept returns on plants, cut fabric, custom countertops and as-is products.  We are unable to refund or exchange your items if your merchandise is found to be modified from its original form when purchased, dirty, stained, or damaged.  We apologize for any inconvenience. Additional return policy information. You must have your receipt and valid government issued photo ID in order to return or exchange your product. Information from your ID will be retained in a company-wide database to be used only for authorizing returns. Removal and Pick-up services at customers’ homes vary by market. If the Pick-up service is available in your area, please bring your product to your covered porch, garage or doorstep. What should I do if my item is damaged? If only one part from your product is damaged, we may be able to ship replacement parts from one of our stores. For the quickest resolution, we recommend visiting an IKEA store with the damaged product or part(s) along with your order confirmation or receipt. If you're unable to do so, please contact the IKEA US Customer Support Center at 1-888-888-4532. Mattress purchases may be exchanged for another mattress one time within 90 days. Learn more here. Only the net purchase price as shown on receipt will be refunded. Returns are not accepted at IKEA Planning Studio or IKEA Pick Up Point locations. Promotional Terms & Conditions: When a promotional item included in the original transaction is not returned, the value of the promotional item will be deducted from the refund amount."},
            {"role": "user", "content": question}
    ],
    model="llama-3.3-70b-versatile",
)

reply = response.choices[0].message.content
print(reply)