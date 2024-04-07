import os
import streamlit as st
import pickle
import time
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import FAISS

import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()  

st.title("Edu bot, Article ChatBot")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)


process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"
import os
genai.configure(api_key=os.environ.get("AIzaSyChu5_IibibM5R05b8Uwl-NenXa-lpJnlc"))
main_placeholder = st.empty()

llm = ChatGoogleGenerativeAI(model="gemini-pro")

if process_url_clicked:
    
    # load data
    if len(url) > 0:
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("Data Loading...Started...✅✅✅")
        data = loader.load()
        # split data
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        docs = text_splitter.split_documents(data)
        # create embeddings and save it to FAISS index
        embeddings = GooglePalmEmbeddings()
        try:
            # vectorstore_openai = FAISS.from_documents(docs, embeddings)
            time.sleep(2)
            main_placeholder.text("Embedding Vector Started Building...✅✅✅")
            time.sleep(2)

            # Save the FAISS index to a pickle file
            # with open(file_path, "wb") as f:
                # pickle.dump(vectorstore_openai, f)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            # vectorstore = pickle.load(f)
            # chain = RetrievalQAWithSourcesChain.from_llm(llm=llm)
            # result = chain({"question": query}, return_only_outputs=True)
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            if len(url)>0:
                result = llm.invoke(query)
                st.header("Answer")
                st.write(result.content)
            else:
                st.warning("Please process URLs first to generate the necessary data.")
    else:
        st.warning("Please process URLs first to generate the necessary data.")
