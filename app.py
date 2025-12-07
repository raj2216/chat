import os
import dotenv
import streamlit as st
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

cm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

if "coversation" not in st.session_state:
    st.session_state["conversation"]=[]
    st.session_state["memory"]=[]
    st.session_state["memory"].append(("system","You are a helpful assistant."))
user_data=st.chat_input("user message")
if user_data:
    
    st.session_state["memory"].append(("user",user_data))

    output=cm.invoke(st.session_state["memory"])

    st.session_state["memory"].append(("assistant",output.content))

    st.session_state["conversation"].append({"role":"user","data":user_data})
    st.session_state["conversation"].append({"role":"ai","data":output.content})
    if user_data=="bye":
        st.session_state["conversation"]=[]
        st.session_state["memory"]=[]
for chat in st.session_state["conversation"]:
    with st.chat_message(chat["role"]):
        st.write(chat["data"])




