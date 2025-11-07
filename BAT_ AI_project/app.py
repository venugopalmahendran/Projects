from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from flask import Flask,render_template,request,jsonify
import re
import os

app = Flask(__name__)

os.environ['GROQ_API_KEY']="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"

loader=PyMuPDFLoader(r"C:\Users\Admin\Desktop\BAT_ AI_project\VENUGOPAL MAHENDRAN RESUME.pdf")
docs=loader.load()

spliter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)
chunk=spliter.split_documents(docs)
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector_store=Chroma.from_documents(
    documents=chunk,
    embedding=embedding,
    persist_directory="/db/chroma"
)
retriever=vector_store.as_retriever(search_kwargs={"k":3})

memory=ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=1
            )
model=ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bat_ai",methods=["POST"])
def ai():
    userinput=request.json["message"]
    response=model.invoke(userinput)
    clean_text=re.sub(r'[#\*]+','',response.get('answer'))
    return jsonify({"response":clean_text})

if __name__ == "__main__":
    app.run(debug=True)


