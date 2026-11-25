from dotenv import find_dotenv,load_dotenv

import os

def mykey()->str:
    load_dotenv(find_dotenv(),override=True)    
    try:
        key=os.getenv('OPENAI_API_KEY')
        print('Obtained key....')
    except ValueError as e:
        print('OPENAI KEY IS NOT SET...')
    else:
        return key

def pinekey()->str:
    load_dotenv(find_dotenv(),override=True)    
    try:
        key=os.getenv('PINECONE_API_KEY')
        print('Obtained pinecone key....')
    except ValueError as e:
        print('pinecone KEY IS NOT SET...')
    else:
        return key

print(mykey())


