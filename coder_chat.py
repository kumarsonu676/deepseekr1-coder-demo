import streamlit as st
from langchain_ollama import OllamaLLM  # Correct import
# from langchain.chains import LLMChain
from langchain.schema.runnable import RunnableSequence
from langchain.prompts import PromptTemplate

# Initialize Ollama with DeepSeek-Coder
llm = OllamaLLM(
        model="deepseek-coder-v2:latest", 
        base_url="http://localhost:11434",
        streaming=True
    )

# Define a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are an expert coder. Answer the following question:\n\n{question}",    
)

# Create an LLM chain
# llm_chain = LLMChain(llm=llm, prompt=prompt)
llm_chain = RunnableSequence(prompt | llm)

# Streamlit UI
st.set_page_config(page_title="DeepSeek Coder Chat", 
                   # layout="wide", 
                   initial_sidebar_state="expanded"
                )
st.title("💬 DeepSeek Coder Chat with LangChain")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask something about coding...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)  # Display user input immediately

    # Stream response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()  # Placeholder for streaming
        full_response = ""  # Store the full response

        for chunk in llm_chain.stream({"question": user_input}):
            full_response += chunk
            response_placeholder.markdown(full_response)  # Update UI dynamically

    # Save assistant response in chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
