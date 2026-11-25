from openai import OpenAI
from getkey import mykey

client=OpenAI(api_key=mykey())


response=client.responses.create(
    model='gpt-6.1-sol',
    input='hi'
)

print(response.output_text)