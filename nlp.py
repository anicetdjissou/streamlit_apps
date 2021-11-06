import streamlit as st
import pandas as pd
# text rank
#eda
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
# EDA Pkgs
def main():
    """  A simple summariaion NLP application"""
    st.title("Summarizer Application")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice =="Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter text here")


    else:
        st.subheader("About")

if __name__=='__main__':
    main()
