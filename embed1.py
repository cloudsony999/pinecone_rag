from openai import OpenAI
from getkey import mykey

client=OpenAI(api_key=mykey())


response=client.embeddings.create(
    model='text-embedding-3-small',
    input='python is a popular programming language'
)

vector=response.data[0].embedding

print("Vector: ",vector)
print("Dimension: ",len(vector))
