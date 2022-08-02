import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Cybersecurity Education",
                   page_icon=":books:", layout="wide")

st.markdown(":skull: Data Cybercrime")
st.sidebar.markdown(":skull: Data Cybercrime")

st.title('Data Pelaporan Kasus Kejahatan Siber di Kepolisian')
df = pd.read_excel(
    io='data.xlsx',
    engine='openpyxl',
    sheet_name='data',
    skiprows=1,
    usecols='B:R',
    nrows=1000,
)
# st.write(df)
st.dataframe(df)
st.markdown("""---""")
