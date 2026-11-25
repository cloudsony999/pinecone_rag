from openai import OpenAI
from getkey import mykey

client=OpenAI(api_key=mykey())


response=client.responses.create(
    model='gpt-6.1-sol',
    instructions='''
    You are an experience HR assistant.
    Use Simple English.
    Give 2 practical examples.
    Do not invent employee imformation
    ''',
    input='Explain what is the purpose of employee attendance system'
)

print(response.output_text)