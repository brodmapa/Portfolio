import streamlit as st
import logic.utils as utls

st.set_page_config(page_title="Home", layout="wide")
st.sidebar.image(utls.imagerise("images/pb.png", [100, 100]), caption="My App")

st.title("Welcome to the Home Page!")
st.write("This is the content of the Home page.")