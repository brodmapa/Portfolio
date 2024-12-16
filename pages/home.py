import streamlit as st

def show():
    st.title("Home Page")
    st.write("""
        Welcome to the Home Page!  
        This is the main page of the app.
    """)
    st.image("https://placekitten.com/800/400", caption="Example Image", use_column_width=True)
