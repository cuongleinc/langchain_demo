import os

from langchain.chains import ConversationChain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug

from prompt_config import MASTER_PROMPT
from rag_util import RAG

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = "sk-abc-xyz"

llm = ChatOpenAI(model="gpt-4o")
set_debug(True)
question_answer_chain = create_stuff_documents_chain(llm, MASTER_PROMPT)
rag_chain = create_retrieval_chain(RAG.get_vector_store_retriever(), question_answer_chain)

def run_chain(user_input: str) -> str:
    """Run the QA chain with a user question."""

    # option 1: ask OPEN_AI and get the answer
    response = llm.invoke(user_input)
    print("Bot:", response.content)
    return response.content

    # option 2: run the chain with user input and print the response applied RAG
    # results = rag_chain.invoke({"input": user_input})
    # print(f"ChatGPT: {results['answer']}")
    # return results['answer']