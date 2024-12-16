import streamlit as st
from home import show as show_home
from about import show as show_about
from contact import show as show_contact

# Set page configuration
st.set_page_config(page_title="Portfolio Paul Brodmann", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Show the corresponding page
if page == "Home":
    show_home()
elif page == "About":
    show_about()
elif page == "Contact":
    show_contact()
