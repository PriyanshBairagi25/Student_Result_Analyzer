# This is the ready-to-upload GitHub folder structure for your Student Result Analyzer

# Folder: Student_Result_Analyzer/
# ├── app.py        # Streamlit application code
# ├── requirements.txt  # All dependencies
# └── sample.xlsx   # Sample Excel file with student data

# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Student Result Analyzer")
st.write("Welcome! Upload your Excel/CSV file to analyze results.")

uploaded_file = st.file_uploader("Upload Excel/CSV file")

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    
    st.subheader("Student Data")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(df.describe())

    st.subheader("Topper")
    st.write(df.loc[df['Marks'].idxmax()])

    st.subheader("Marks Distribution")
    fig, ax = plt.subplots()
    df['Marks'].hist(ax=ax)
    st.pyplot(fig)

# requirements.txt
"""
streamlit
pandas
matplotlib
openpyxl
"""

# sample.xlsx
# Create a simple Excel file with columns: Name, Marks
# Example rows:
# Name, Marks
# Alice, 85
# Bob, 78
# Carol, 92