import streamlit as st
import pandas as pd
import numpy as np



st.write("Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.snow()

st.subheader("Widgets:")

st.write("Slider")
x = st.slider('x')  #  this is a widget
st.write(x, 'squared is', x * x)

st.write("Text input")
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# .streamlit/secrets.toml

public_gsheets_url = "https://docs.google.com/spreadsheets/d/1mwIlHi4Zdrh4ZlIZ6SqU2M59wchLmzbGvxhJvp1qZC4/edit#gid=0"
