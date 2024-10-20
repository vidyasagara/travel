import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from PIL import Image


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful travel and tourism information bot. Please answer all user queries related to travel and tourism"),
        ("user","Question:{question}")
    ]
)

repo_id="mistralai/Mistral-7B-Instruct-v0.3"

def generate_response(question):
    llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=150,temperature=0.7,token=st.secrets["HF_TOKEN"])
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

#Travel and tourism image
img = "https://i.imgur.com/avH5kVq.jpeg"
st.image(img, width=200)

## Title of the app
st.title("Travel & Tourism Info Chatbot 🏝️")

## Main interface for user input
st.write("Go ahead and ask any questions related to travel and tourism")
user_input=st.text_input("")

if user_input :
    response=generate_response(user_input)
    st.write(response)
else:
    st.write("Please provide user input")
