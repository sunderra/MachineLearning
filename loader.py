import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    filename = uploaded_file.name
    if filename.endswith(".xlsx") :
        st.write("Excel file : " + uploaded_file.name)
        data = pd.read_excel(uploaded_file, header=None)
        st.write(data)
    elif filename.endswith(".csv"):
        st.write("CSV file: " + uploaded_file.name)
        data = pd.read_csv(uploaded_file, header=None)
        st.write(data)
    else:    
        st.write("Unknown file type")
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
