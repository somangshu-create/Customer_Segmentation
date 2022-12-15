import streamlit as st
import app
import Data_Visualization as dataviz
import About as at

#create the side menu 

st.sidebar.title("Menu")
# dataviz.data_analysis()

Page_User = st.sidebar.selectbox("Choices", ["Group Prediction", "Data_Analysis", "About"], index = 2)

#Change the Pages
if Page_User == "Group Prediction":
    app.code()
elif Page_User == "About":
    at.info()
else:
    dataviz.data_analysis()
