from langchain_openai import ChatOpenAI
from getkey import mykey


llm=ChatOpenAI(
    api_key=mykey,
    model='gpt-6.1-sol',
    max_retries=2,
    timeout=60,
    max_completion_tokens=100
    
)

response=llm.invoke('hi')

print(response.content)

