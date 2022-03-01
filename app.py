import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPAM HAM CLASIFIER')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('predict'):
  sttitle(op[0])
                                                                                                                                             
