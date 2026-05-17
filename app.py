import streamlit as st

st.title("Hello Streamlit Cloud 👋")
st.write("这是一个最简单的 Streamlit 应用，用来测试部署。")

name = st.text_input("你的名字：")
if name:
    st.success(f"你好，{name}！欢迎使用 Streamlit Cloud。")