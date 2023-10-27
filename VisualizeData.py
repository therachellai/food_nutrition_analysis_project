import streamlit as st

"""
Below is an example from chatGPT on how to use streamlit
"""
# Create a title for your app
st.title("My First Streamlit App")

# Add text to the app
st.write("Welcome to my Streamlit app!")

# Create a button that triggers an action
if st.button("Click me"):
    st.write("You clicked the button!")

# Display a chart (example)
st.line_chart({"data": [1, 2, 3, 4, 5]})

# Show text input and display the entered value
user_input = st.text_input("Enter something:")
st.write("You entered:", user_input)