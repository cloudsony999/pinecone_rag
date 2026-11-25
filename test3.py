from openai import OpenAI
from getkey import mykey

client=OpenAI(api_key=mykey())


response=client.responses.create(
    model='gpt-6.1-sol',
    input='Explain RAG step by step',
    stream=True
)

for _ in response:
    if _.type=='response.output_text.delta':
        print(_.delta,end=' ',flush=True)