from pinecone import Pinecone
from getkey import pinekey


pc=Pinecone(api_key=pinekey())

print('pinecone ready: ',pc)

