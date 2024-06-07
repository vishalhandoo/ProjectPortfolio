import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Python Project Portfolio",
    layout="wide"
)
col1, col2 = st.columns(2)



with col2:
    st.title("Vishal Handoo")
    content = """
    I am a dedicated and proficient Python web developer with a strong specialization in Streamlit, 
    an open-source framework designed for creating and sharing custom web apps for machine learning and data science. 
    With a comprehensive background in both web development and data visualization, I would like to build a career around 
    leveraging Python's robust capabilities to deliver intuitive, interactive, and impactful web applications.
    """
    st.markdown(
        """
        <style>
        .info-text {
            font-size: 20px;
            background-color: #6897bb;
            padding: 10px;
            border-radius: 5px;
            border-left: 6px solid #1f77b4;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f'<div class="info-text">{content}</div>', unsafe_allow_html=True)

content2 = """
        Below you can find Python as well as C++ projects Built by me.
        Feel free to contact me!
"""
st.markdown(
        """
        <style>
        .description {
            font-size: 20px;
        }
        .description2{
            font-size: 20px;
            background-color: #6897bb;
            padding: 10px;
            border-radius: 5px;
            border-left: 6px solid #1f77b4;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown(f'<div class="description">{content2}</div>', unsafe_allow_html=True)


col3, empty_col, col4 = st.columns([1.5,0.5,1.5])


df = pd.read_csv("data.csv", sep=";")

for index, row in df.iterrows():
    image_path = "images/" + row["image"]
    if index < len(df) / 2:
        with col3:
            st.header(row["title"])
            st.markdown(f'<div class="description2">{row["description"]}</div>', unsafe_allow_html=True)
            if os.path.exists(image_path):
                st.image(image_path)
            st.write(f"[Source Code]({row['url']})")
    else:
        with col4:
            st.header(row["title"])
            st.markdown(f'<div class="description2">{row["description"]}</div>', unsafe_allow_html=True)
            if os.path.exists(image_path):
                st.image(image_path)
            st.write(f"[Source Code]({row['url']})")
