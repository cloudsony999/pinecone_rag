from openai import OpenAI
from getkey import mykey
import tiktoken


text='''
I am amitava
'''

encoding=tiktoken.get_encoding('o200k_base')
tokens=encoding.encode(text)

print('token length: ',len(tokens))

print("token id: ",tokens)