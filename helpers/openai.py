# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatGPT(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "You work for an organization called One Center."},
            {"role": "system", "content": "You provide assistant to callers."},
            {"role": "system", "content": "If a caller asks you for a question you have no prior discussion of with them, you can just assume the prior discussion and continue from there."},
            {"role": "user", "content": "Hello?"},
            {"role": "assistant", "content": "How can I help you today?"},
            {"role": "user", "content": message},
        ]
        )
    return completion.choices[0].message
