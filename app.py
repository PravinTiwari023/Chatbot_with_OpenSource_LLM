"""
LANGCHAIN_API_KEY="ls__167978455811441d9b3ef86b11524f8e"
LANGCHAIN_PROJECT="OPEN_SOURCE_LLM_CHATBOT"
"""

from langchain_core.prompt import ChatPromptTemplate
from langchain_core.ouput_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv