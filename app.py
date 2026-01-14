import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceEndpoint
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

# Specific LLaMA model from HuggingFace
REPO_ID = "meta-llama/Meta-Llama-3-70B-Instruct"

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    # Using local embeddings (free, runs on CPU)
    # model_name="all-MiniLM-L6-v2" is a small, fast, and good quality model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore, api_key):
    # Using Hugging Face Inference API for LLaMA 3
    llm = HuggingFaceEndpoint(
        repo_id=REPO_ID, 
        max_length=512, 
        temperature=0.5, 
        huggingfacehub_api_token=api_key
    )

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("Please upload and process documents first!")
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs (LLaMA 3)", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with PDF :books: (powered by LLaMA 3)")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        # Check API Key for Hugging Face
        api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        if not api_key:
            try:
                api_key = st.secrets.get("HUGGINGFACEHUB_API_TOKEN")
            except Exception:
                pass
        
        if api_key:
            os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_key
            
        if not os.getenv("HUGGINGFACEHUB_API_TOKEN") and "HUGGINGFACEHUB_API_TOKEN" not in st.session_state:
             api_key_input = st.text_input("HuggingFace Access Token", type="password")
             if api_key_input:
                 os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_key_input
                 st.session_state["HUGGINGFACEHUB_API_TOKEN"] = api_key_input
                 st.rerun()

        if st.button("Process"):
            # Check for API key (only needed for LLaMA, but good to enforce before starting)
            if not os.environ.get("HUGGINGFACEHUB_API_TOKEN") and not api_key:
                 st.error("Please provide a HuggingFace Access Token to proceed.")
            elif not pdf_docs:
                st.error("Please upload at least one PDF.")
            else:
                with st.spinner("Processing (Using LLaMA 3 & Local Embeddings)..."):
                    
                    # 1. Get PDF Text
                    raw_text = get_pdf_text(pdf_docs)

                    # 2. Get Text Chunks
                    text_chunks = get_text_chunks(raw_text)

                    # 3. Create Vector Store (Local Embeddings - No API Key needed here)
                    vectorstore = get_vectorstore(text_chunks)

                    # 4. Create Conversation Chain (LLaMA 3 - Needs API Key)
                    # We fetch the key again to be safe
                    hf_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
                    st.session_state.conversation = get_conversation_chain(vectorstore, hf_token)
                    
                    st.success("Done! You can now ask questions.")

if __name__ == '__main__':
    main()
