import streamlit as st
import panda as pd

st.title('Machine Learning')

st.write('This application is to demonstrate Machine Learning by predicting the future price of gold!')

with st.expander('Data'):
                 st.write('Raw Data')
df = pd.read_csv()
df


