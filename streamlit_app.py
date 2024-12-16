import streamlit as st
from pages.home import show as show_home
from pages.about import show as show_about
from pages.Database import show as show_contact

# Set page configuration
st.set_page_config(page_title="Portfolio Paul Brodmann", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Database"])

# Show the corresponding page
if page == "Home":
    show_home()
elif page == "About":
    show_about()
elif page == "Database":
    show_contact()
