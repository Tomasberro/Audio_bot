# import openai
# import os

# openai.api_key = os.environ.get("OPENAI_API_KEY")

# transcript_text = "Texto transcrito de tu audio"

# response = openai.Completion.create(
#   engine="text-davinci-002",  
#   prompt=transcript_text,
#   temperature=0.7,
#   max_tokens=150
# )

# generated_text = response['choices'][0]['text']
# print(generated_text)
