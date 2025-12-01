#import streamlit as st

#st.title("Result Analyzer")
#st.write("Welcome to the app 👋")


import streamlit as st
import pandas as pd

st.title("📊 Result Analyzer")
st.write("Upload your marks Excel file and analyze student performance")

uploaded_file = st.file_uploader("Upload Excel or CSV file", type=["xlsx", "csv"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df)

    # Basic stats
    st.subheader("📈 Basic Statistics")
    st.write(df.describe())

    # Subject toppers
    st.subheader("🏆 Highest Marks in Each Subject")
    st.write(df.max())

    # Lowest marks
    st.subheader("🔻 Lowest Marks in Each Subject")
    st.write(df.min())

    # Pass/Fail calculation (assume 40 passing)
    st.subheader("🟢 Pass/Fail Summary")
    pass_mark = 40

    passed = (df.iloc[:, 1:] >= pass_mark).all(axis=1).sum()
    failed = len(df) - passed

    st.write(f"✔️ Passed Students: **{passed}**")
    st.write(f"❌ Failed Students: **{failed}**")
else:
    st.info("Upload a student marks file to continue.")
