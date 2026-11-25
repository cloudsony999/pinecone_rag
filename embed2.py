from openai import OpenAI
from getkey import mykey

client=OpenAI(api_key=mykey())

sentences=[
    'python is a popular programming language',
    'java is a popular programming language',
    'Employee reveive monthly salary',
    'Today there is high chance of rain'
]

response=client.embeddings.create(
    model='text-embedding-3-small',
    dimensions=512,
    input=sentences
)

for _ in response.data:
    print("Vector index: ",_.index)
    print("Vector Dimension: ",len(_.embedding))
    print('\n\n----------------\n\n')
        