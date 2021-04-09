# from summa import summarizer
import streamlit as st
import numpy as np
import pandas as pd

# Add title on the page
st.title("Holo Trader")

# Ask user for input text
input_sent = st.text_area("Input Text", "", height=200)

ratio = st.slider(
    "Summarization fraction", min_value=0.0, max_value=1.0, value=0.2, step=0.01
)

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
