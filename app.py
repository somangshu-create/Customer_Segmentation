#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def header():
    
    # getting the model 
    
    file = "Customer_Segmentation_model"
    loaded_model = joblib.load(file)
    
    # Web App Title
    st.write("""
    ## Prediction for Customer Segmentation app
    
    
    
    
    This is a web application built and hosted on Streamlit, whose purpose is to segment customers according to the given metrics. In this project we deal with a **clustering** problem.
    
    """)
    
    
    return loaded_model

def Predict_Points(input_data,loaded_model):
    
    #predict
    prediction = loaded_model.predict(input_data)

    
    #show the result
    
    
    if(prediction == 0):
        st.markdown(''' #### You are part of group 1:
                    ''')
        st.write("""If you are in this group :
        
        1.You have low to a bit less than average annual income.
        2.You are in the age group of 18-35 which means you are either a student or a salary man.
        3.Your projected  spending is high .
        
        Select from the following to see your offers now!!
        """)
       
    elif(prediction == 1):
        
        st.markdown(''' #### You are part of Group 2:
                    ''')
        st.write("""
                 If you are in this group:

                 1. Your age can be from young adult to even senior people .

                 2. You have generally High spending tendencies.

                 3. Your income is a bit higher than average.

                 
                 """)

        

    elif(prediction == 2):
        st.markdown(''' #### You are part of group 3:
                    ''')
        st.write("""
                 If you are in this group;

                 1.You are low to medium spending tendencies.

                 2. Your income can vary between average to a bit higher average.

                 3. You are in a wide age group of 38 - senior people . You can be below 30 also but that's very unlikely.
                
                 """)
        
    elif (prediction==3):
        st.markdown(''' #### You are part of group 4:
                    ''')
        st.write("""
                 If you are in this group:

                 1.You have a very high Income 
                 
                 2. Your spending history is also high so you being a businessman in very likely or you can be a salaryman buying a one time pricy thing.
                 
                 3. You are in the age category of 20 - 40.
                
                 """)
        
    else:
        st.markdown(''' #### You are part of group 5:
                    ''')
        st.write("""
                 If you are in this group :
                 
                 1. You have low spending history along with low income .
                 2. You can either be a student ,  a salaryman or a retired person.
                 
                
                 """)
        

def code():
    #load model
    loaded_model = header()
    
    #customer input
    form = st.form(key='som')
    
    AGE = form.number_input('Whats the customer age?' ,key='1', value=20,max_value=90,step=1)
    ANNUAL_INCOME = form.number_input('what is the approximate annual income (in 1000 rupees) of the customer ?',value=500,max_value=10000,key='2')
    SPENDING_SCORE = form.number_input("What type of spender the customer is at the moment ?",value=50,key='3',max_value=100)
    
    form.form_submit_button('Add')
    st.write("\n\n")
    #dataset creation
    data = [[AGE,ANNUAL_INCOME/80,SPENDING_SCORE]]
    columns = ['Age','Annual Income (k$)','Spending Score (1-100)']
    
    #insert
    df = pd.DataFrame(data=data, columns=columns)
    
    #creating a button for prediction
    st.write("##### User Guide:-->\n")
    st.write("Tell the customer's approx income , You dont need to give the exact details.")
    st.write('''Enter value in 1-100 based on how you rate the customer spending at the mall in the history, Click the Results button to see which group the customer belongs to.''')
    if st.button('Result'):
        st.write('''Your selected values''')
        st.dataframe(df)
        Predict_Points(data,loaded_model)
        
    
if __name__ == '__main__':
    code()






