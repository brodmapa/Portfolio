import streamlit as st
import logic.utils as utls

# Set the page title
st.set_page_config(page_title="Image Gallery", layout="wide", page_icon="lol", initial_sidebar_state="collapsed")

st.title("My Image Gallery")

# Create columns for the gallery layout
col1, col2  = st.columns(2)
with col1:
    st.image(utls.imagerise("./images/Screensaver.png",[960,540]), caption="Resized Kitten Image")
with col2:
    st.write("""
    Welcome to the Home Page!  
    This is the main page of the app.
    """)

col4, col5, col6 = st.columns(3)

with col4:
    st.image("https://placekitten.com/400/303", caption="Kitten 4", use_column_width=True)

with col5:
    st.image("https://placekitten.com/400/304", caption="Kitten 5", use_column_width=True)

with col6:
    st.image("https://placekitten.com/400/305", caption="Kitten 6", use_column_width=True)
