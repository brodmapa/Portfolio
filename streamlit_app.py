import streamlit as st

# Set the title of the app
st.title("Simple Streamlit Baseline App")

# Add a header and a subheader
st.header("Welcome to My Streamlit App")
st.subheader("This is a baseline example.")

# Add some text
st.write("Streamlit makes it easy to create web apps for data and machine learning projects.")

# Add an interactive widget (e.g., slider)
number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You selected: {number}")

# Add a button
if st.button("Click Me!"):
    st.write("You clicked the button!")

# Add a file uploader
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("Uploaded file name:", uploaded_file.name)

# Add a sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar for navigation or additional options.")
