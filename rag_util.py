from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

class RAG:
    @staticmethod
    def get_vector_store_retriever():
        loader = DirectoryLoader('./knowledge_base', glob="*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        print(f"Loaded {len(docs)} PDF pages")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
        splits = text_splitter.split_documents(docs)
        vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(), persist_directory=None)
        retriever = vectorstore.as_retriever()
        return retriever
