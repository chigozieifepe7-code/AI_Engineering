import json
from litellm import completion

messages = [{"role": "user", "content": "Where is Surfers Paradise?"}]

response = completion(
    model="openai/gpt-5-nano",
    messages=messages
)

reply = response.choice[0].message.content
print(reply)

print(json.dumps[response.model_dump(), indent= 2])


print(f"prompt tokens: {response.usage.prompt_tokens}")
print(f"completion tokens: {response.usage.completion_tokens}")
print(f"total tokens: {response.usage.total_tokens}")

print(json.dumps[response._hidden_params, indent = 2])
