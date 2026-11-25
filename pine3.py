'''
connect to pinecone
create a schema based index
generate vectors and upload documents
'''
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from getkey import pinekey,mykey


pc=Pinecone(api_key=pinekey())

print('pinecone ready: ',pc)

index=pc.index('anudip-pinecone-index')

embeds=OpenAIEmbeddings(
    model='text-embedding-3-small',
    api_key=mykey()
)

documents=[
    {
        "id":"DOC101",
        "text":"Employee reveive salary monthly",
        "source":"HR Policy"
    },
    {
            "id":"DOC102",
            "text":"Leave request must be approved by manager",
            "source":"LEAVE Policy"
    },
    {
            "id":"DOC103",
            "text":"Refund require manager approval",
            "source":"Refund Policy"
    },
    {
            "id":"DOC104",
            "text":"Employee reveive mediclaim benifit",
            "source":"LIC Policy"
    }

]


vectors=embeds.embed_documents(
    [_['text'] for _ in documents]
)


records=[]


for item,vector in zip(documents,vectors):
    records.append({
        "_id":item['id'],
        "embedding":vector,
        "text":item['text'],
        "source":item['source']
    })

index.documents.upsert(
    namespace='company',
    documents=records
)



print('....................DOCUMENTS UPLOADED..............')
