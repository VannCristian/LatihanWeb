import streamlit as st
import pandas as pd
import numpy as np
import time


"""
# My first app
Here's our first attempt at using data to create a table:
"""
st.subheader("1-Magic:")
import streamlit as st
import pandas as pd
st.info('This is a purely informational message', icon="ℹ️")
df = pd.DataFrame({
  'LULUS': [1, 2, 3, 4],
  'TIDAK LULUS': [10, 20, 30, 40]
})
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.snow()
st.balloons()
df

st.subheader("Latihan Data Frame")


st.write("Mencoba Data Frame")
st.info('This is a purely informational message', icon="ℹ️")
st.write(pd.DataFrame({
    'akuh': [1, 2, 3, 4],
    'kamoeh': [10, 20, 30, 40]
}))

st.write("2B: Random dataframe")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

 
st.write("2C: Using Panda Styler")
dataframe = pd.DataFrame(
    np.random.randn(7, 7),
    columns=('col %d' % i for i in range(7)))

st.dataframe(dataframe.style.highlight_max(axis=0))

number = st.number_input('insert number')
st.write ('The current number is ', number)

add_ten=number + 10 

st.write("add 10",add_ten)




title = st.text_input('aku adalah', '')

st.write('aku adalah', title)

st.write('Dia adalah',title)

nama1=st.text_input('nama','')
st.write('nama :',nama1)



