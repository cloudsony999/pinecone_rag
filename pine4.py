'''
connect to pinecone
create a schema based index
generate vectors and upload documents
Search PineCone
'''
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone,DenseVectorQuery
from getkey import pinekey,mykey


pc=Pinecone(api_key=pinekey())

print('pinecone ready: ',pc)

index=pc.index('anudip-pinecone-index')

embeds=OpenAIEmbeddings(
    model='text-embedding-3-small',
    api_key=mykey()
)


question='when do employees receive payment?'
query_vector=embeds.embed_query(question)

results=index.documents.search(
    namespace='company',
    top_k=3,
    score_by=[
        DenseVectorQuery(
            fields=['embedding'],
            values=query_vector
    
        )
    ],
    include_fields=['text','source']
)



for match in results.matches:

    print("Document object:", match)

    print("Dictionary:", match.to_dict())

    print("ID:", match.id)
    print("Score:", match.score)

    print("-----------------------")


    