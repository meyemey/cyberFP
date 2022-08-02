import streamlit as st
import time

st.set_page_config(page_title="Cybersecurity Education",
                   page_icon=":books:", layout="wide")

st.markdown(":video_camera: Video")
# st.title("Article")
st.sidebar.markdown(":video_camera: Video")

with st.spinner('Tunggu Sesaat...'):
    time.sleep(3)
pass

with st.container():
    st.write('---')
    st.title("Apa Itu Cyber Security?")
    st.video('https://www.youtube.com/watch?v=h6f8T2LhNdU')

with st.container():
    st.write('---')
    st.title("Waspada Kejahatan Siber, Mari Kita Cegah")
    st.video('https://www.youtube.com/watch?v=y_AvxuWdcfY')

with st.container():
    st.write('---')
    st.title("Manajemen Password")
    st.video('https://www.youtube.com/watch?v=eTfL-7cNnfs')

with st.container():
    st.write('---')
    st.title("Perbedaan Hacker dan Cracker")
    st.video('https://www.youtube.com/watch?v=i11P3ugFO2w')

with st.container():
    st.write('---')
    st.title("Cara Menjaga Privasi dan Keamanan dalam Dunia Digital")
    st.video('https://www.youtube.com/watch?v=gxIU4g-Qd6I')

with st.container():
    st.write('---')
    st.title("Tips Aman Berinternet Dari Serangan Siber")
    st.video('https://www.youtube.com/watch?v=tph6R-xZAl8')
