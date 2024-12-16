import streamlit as st

def show():
    st.title("About Page")
    st.write("""
        This is the About Page.  
        Here you can provide information about yourself or your app.
    """)
    st.info("Streamlit makes it easy to build web apps for data and machine learning.")
