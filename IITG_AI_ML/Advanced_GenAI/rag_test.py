from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.schema.runnable import RunnableParallel
from operator import itemgetter


pdf_path = os.path.join(os.path.dirname(__file__), "the_nestle_hr_policy_pdf_2012.pdf")
loader = PyPDFLoader(pdf_path)
docs = loader.load()

print(type(docs))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
split_docs = splitter.split_documents(docs)
print(type(split_docs))

# 1. Create embeddings & vector store (Chroma)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectordb = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    persist_directory="./chroma_store"
)
print('>>>>>1')
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# 2. Define LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Create prompt
prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant. Use the following context to answer the question.

    Context:
    {context}

    Question:
    {input}

    Answer:
    """
)

# 4. Create document chain
document_chain = create_stuff_documents_chain(llm, prompt)
print('>>>>>2')
# 5. Create retrieval chain
retrieval_chain = create_retrieval_chain(retriever, document_chain)
print('>>>>>3')
# 6. Wrap with RunnableParallel to also expose source docs
chain_with_sources = RunnableParallel(
    {
        "answer": retrieval_chain,
        "docs": itemgetter("input") | retriever
    }
)

# 7. Run query
response = chain_with_sources.invoke({"input": "tell me about rewards policy"})

print("\n--- Answer ---")
print(response["answer"]["answer"])

print("\n--- Sources ---")
for i, doc in enumerate(response["docs"], start=1):
    print(f"Source {i}: {doc.page_content[:200]} ...")
    print("Metadata:", doc.metadata)

