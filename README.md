# 🌐 LangChain Demo with Streamlit UI

This project is a simple demo of **LangChain + OpenAI** with a **Streamlit web interface**.  
You can ask questions, and the app will respond using your knowledge base.

---

## ⚙️ Prerequisites
- Python 3.9+  
- An [OpenAI API Key](https://platform.openai.com/account/api-keys)  

---

## 🚀 How to Run the Application

### 1. Configure Environment Key
Set your OpenAI API key as an environment variable:

**Linux / macOS (bash/zsh):**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Windows (PowerShell):**
```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

---

### 2. Install Dependencies
Install required packages:
```bash
pip install -r requirements.txt
```

*(Make sure `streamlit`, `langchain`, `openai`, and any loaders like `pypdf` are included in your `requirements.txt`.)*

---

### 3. Start the Application
Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 🖥️ Usage
- Open the link shown in your terminal (usually [http://localhost:8501](http://localhost:8501))  
- Type your question in the input box  
- Get instant answers powered by **LangChain** and **OpenAI**  

---

## 📂 Project Structure
```
├── app.py               # Streamlit UI
├── main.py              # Core logic + run_chain function
├── prompt_config.py     # Prompt template setup
├── rag_util.py          # Retriever / RAG utilities
├── requirements.txt     # Dependencies
└── README.md            # This file
```

---

## ✨ Example
```text
You: What is LangChain?
AI: LangChain is a framework for developing applications powered by language models...
```

---

## 🛑 Stop the App
Press `CTRL+C` in your terminal to stop the Streamlit server.

---
