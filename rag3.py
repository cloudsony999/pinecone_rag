'''
Text Splitting using the dedicated package 
langchain-text-splitter  
RecursiveCharacterTextSplitter
This program will split the text file
'''
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

text=Path('docs/company_policy.txt').read_text(encoding='utf8')

document=Document(
    page_content=text,
    metadata={"source":"company_policy.txt"}
)

splitter=RecursiveCharacterTextSplitter(
         chunk_size=200,
         chunk_overlap=40,
         separators=[
             "\n\n",
             "\n",
             ".",
             " ",
             ""
             ]
)

chunks=splitter.split_documents([document])

for i,chunk in enumerate(chunks):
    print("CHUNK: ",i+1)
    print("CHUNK CONTENTS: ",chunk.page_content)
    print("CHUNK METADATA: ",chunk.metadata)
    print("\n\n-------------------------------------------\n\n")
        





