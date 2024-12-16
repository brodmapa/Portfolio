import streamlit as st
import logic.utils as utls

# Set the page title
st.set_page_config(page_title="Image Gallery", layout="wide", page_icon="lol", initial_sidebar_state="collapsed")

st.title("My Image Gallery")

col1, col2, col3, col4  = st.columns(4)
with col1:
    st.image(utls.imagerise("./images/Screensaver.png",[1920,1080]), caption="Resized Kitten Image")
with col2:
    st.write("""
    Welcome to the Home Page!  
    This is the main page of the app.
    """)
with col3:
    st.image(utls.imagerise("./images/HBP_edit2.png",[760, 760]), caption="Resized Kitten Image")
with col4:
    st.write("""
    Welcome to the Home Page!  
    This is the main page of the app.
    """)