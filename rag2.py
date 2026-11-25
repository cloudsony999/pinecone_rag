'''
What is RAG?

Rag stands for Retrival Augmented Generation.
A college chatbot may need 2 answer from internal admission rules,
attendance policy, fees structure and payment information.

A RAG based application retrieves relevant information and provides to the LLM

1>
RAG Document Ingestion

a>company pdf/text doc
b>document loading
c>Text Splitting / chunking
d>Gemini Embedding Model
e>PineCone Vector Database

2> 
RAG Question-answering 
a>student question
b>Question embedding
c>Pinecone retrieval
d>Relevant context + Question
e>Gemini LLM
f>Final Answer

Interview question related to RAG

WHY document splitting?

A large pdf may contain lots of pages rather than sending the entire doc
for every question , divide it into small meaningful pieces called CHUNKS

WHAT IS CHUNK SIZE AND OVERLAP?

Chunk size is the approximate size of each text chunk.
chenk overlap retails some text from the previous chunk in the next chunk.
chunk_size=500 and chunk_overlap=100
for approx 500-character chunks with 100 characters of overlap

Create sample company documents


1> LOAD PDF DOCUMENTS

Use a dedicated PDF loader integration instead of the deprecated module
langchain-community

use langchain-pymupdf4llm
'''

from langchain_pymupdf4llm import PyMuPDF4LLMLoader as p

loader=p("docs/PROMPTS.pdf")

doc=loader.load()

for _ in doc:
    print(_.page_content)
    print(_.metadata)