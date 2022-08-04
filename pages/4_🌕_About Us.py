import streamlit as st

st.set_page_config(page_title="Cybersecurity Education",
                   page_icon=":books:", layout="wide")

st.markdown(":full_moon: About Us")
# st.title("Article")
st.sidebar.markdown(":full_moon: About Us")
st.title("Tentang Anggota Kelompok Kami")

with st.container():
    st.write('---')
    st.subheader("Programmer")
    # silakan isi sesuai dengan keinginan ini contoh aja
    st.write(
        "Perkenalkan saya adalah [Mei Purweni](https://twitter.com/), saat ini saya berdomisili di Jogjakarta dan saya mengajar di Universitas Duta Bangsa Surakarta")

with st.container():
    st.write('---')
    st.subheader("Programmer")
    # silakan isi
    st.write(
        "Perkenalkan saya adalah [Ihda Mawaddah](https://twitter.com/ihdakaito), saat ini saya bekerja di Rumah Sakit Umum Daerah (RSUD) di salah satu Kabupaten dari Provinsi Kalimantan Selatan pada bagian IT.")

with st.container():
    st.write('---')
    st.subheader("Content Writer")
    # silakan isi sesuai dengan keinginan ini contoh aja
    st.write(
        "Perkenalkan saya adalah [Ahzka Nabillah Tuzzahrah](https://twitter.com/), ")
