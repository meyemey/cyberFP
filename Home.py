from typing import Container
import streamlit as st

st.set_page_config(page_title="Cybersecurity Education",
                   page_icon=":books:", layout="wide")

st.markdown(":house: Home")
st.sidebar.markdown(":house: Home")

with st.container():
    st.title("Cyber Security Awareness")
    st.subheader("Hallo, kami dari kelompok ... :wave:")
    st.write("Sebagaimana judul diatas, dalam rangka menyebarkan edukasi Cyber Security kami mengambil tema mengenai Cyber Security Awareness. Cyber security awareness merupakan sebuah pemahaman akan keamanan penggunaan internet. Cyber security awareness bisa berdampak pada keamanan data. Dengan memiliki kesadaran akan keamanan siber, masyarakat atau instansi menjadi lebih waspada terhadap seluruh aset dan informasi yang diberikan melalui fasilitas teknologi dan jaringan.")
