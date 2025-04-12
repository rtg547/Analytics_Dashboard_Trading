import streamlit as st
import pandas as pd

st.title("Trading Dashboard")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
                                 
if uploaded_file is not None:
    # Read the uploaded file into Pandas DataFrame
    data = pd.read_csv(uploaded_file)
        
    # Display the DataFrame in the Streamlit app
    st.write(data)