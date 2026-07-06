import streamlit as st

faq = {
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is Python?": "Python is a programming language.",
    "What is Machine Learning?": "Machine Learning is a branch of AI.",
    "Who developed Python?": "Python was created by Guido van Rossum.",
    "What is ChatGPT?": "ChatGPT is an AI chatbot developed by OpenAI."
}

st.title("🤖 FAQ Chatbot")

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question in faq:
        st.success(faq[question])
    else:
        st.warning("Sorry! I don't know the answer to this question.")