# OpenAI GPT-3
import openai

# Load credentials
import os
from dotenv import load_dotenv
load_dotenv()

def query_openai(prompt = ""):
    openai.organization = os.environ['OPENAI_ORG']
    openai.api_key = os.environ['OPENAI_API_KEY']

    # Temperature is a measure of randonmess
    # Max_tokens is the number of tokens to generate
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=80,

    )

    return response.choices[0].text

# Main loop
if __name__ == '__main__': 
    while True:
            print('Enter a query: ')
            query = input()
            speech = query_openai(query)
            print()   
            print("ChatGPT: " + speech)
            # print new line
            print()

            