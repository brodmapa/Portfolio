import streamlit as st

def show():
    st.title("Contact Page")
    st.write("""
        This is the Contact Page.  
        You can add contact details or a contact form here.
    """)
    st.text_input("Your Name")
    st.text_area("Your Message")
    if st.button("Send"):
        st.success("Message sent successfully!")
