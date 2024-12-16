import streamlit as st

# Set page configuration
st.set_page_config(page_title="Streamlit Multi-Page App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# Home Page
if page == "Home":
    st.title("Home Page")
    st.write("""
        Welcome to the Home Page!  
        This is a simple baseline app with multiple pages.
    """)
    st.image("https://placekitten.com/800/400", caption="Example Image", use_column_width=True)

# About Page
elif page == "About":
    st.title("About Page")
    st.write("""
        This is the About Page.  
        Here you can provide information about yourself or your app.
    """)
    st.info("Streamlit makes it easy to build web apps for data and machine learning.")

