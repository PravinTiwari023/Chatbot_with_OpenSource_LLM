"""
LANGCHAIN_API_KEY="ls__167978455811441d9b3ef86b11524f8e"
LANGCHAIN_PROJECT="OPEN_SOURCE_LLM_CHATBOT"
"""

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful ai assistant. Please response to the user queries."),
        ("user","Question:{question}")
    ]
)

# Streamlit framework
st.title("Langchain Open Source LLM")
input_text=st.text_input("Say hii!!")

# Ollama llama2 llm
llm=Ollama(model="llama2")

# Output parser
parser=StrOutputParser()

chain=prompt | llm | parser

if input_text:
    st.markdown(chain.invoke({"question":input_text}))