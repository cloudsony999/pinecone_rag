from langchain_openai import ChatOpenAI
from getkey import mykey
from langchain_core.prompts import ChatPromptTemplate



prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a python trainer."),
        ("human","Explain {topic} with {number} of examples.")
    ]
)

llm=ChatOpenAI(
    api_key=mykey,
    model='gpt-6.1-sol'  
)

chain=prompt | llm

value=input('what topic U want?')
ex=int(input('How many examples U want?'))

args={"topic":value,"number":ex}

response=chain.invoke(args)

print(response.content)

