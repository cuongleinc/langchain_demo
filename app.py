import streamlit as st
from main import run_chain

st.set_page_config(page_title="LangChain Demo", layout="wide")

st.title("LangChain Demo UI")
st.write("Ask me anything from the knowledge base!")

# Input
user_input = st.text_input("Your question:")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            answer = run_chain(user_input)
            st.success("Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
