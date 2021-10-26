import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

st.title("Salary Prediction Tool")
html_temp = """
  <div style="background-color:blue;opacity: 0.3;;padding:10px">
  <h2 style="text-align:center;">Sid's Tool </h2>
  </div>

"""
st.markdown(html_temp,unsafe_allow_html=True)

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()