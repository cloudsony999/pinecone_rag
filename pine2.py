'''
connect to pinecone
create a schema based index
generate vectors and upload documents
'''

from pinecone import Pinecone
from getkey import pinekey


pc=Pinecone(api_key=pinekey())

print('pinecone ready: ',pc)

index_name='anudip-pinecone-index'

existing_names=[_.name for _ in pc.indexes.list()]


if index_name not in existing_names:
    pc.indexes.create(
        name=index_name,
        schema={
            "fields":{
                "embedding":{
                    "type":"dense_vector",
                    "dimension":1536,
                    "metric":"cosine"
                }
            }
        },
        deployment={
            "deployment_type":"managed",
            'cloud':"aws",
            'region':'us-east-1'
        }
    )

index=pc.index(index_name)

print('....................INDEX IS READY..............')
