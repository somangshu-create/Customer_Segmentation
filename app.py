#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import joblib
import pandas as pd


# In[8]:


def header():
    
    # getting the model 
    
    file = "Customer_Segmentation"
    loaded_model = joblib.load(file)
    
    # Web App Title
    st.write("""
    ## Prediction for Customer Segmentation app
    
    #### Developed by: Somangshu Chakraborty
    
    This is a web application built and hosted on Streamlit, whose purpose is to segment customers. In this project we deal with a **clustering** problem.
    
    """)
    
    
    return loaded_model


# In[9]:


def Predict_Points(input_data,loaded_model):
    
    #predict
    prediction = loaded_model.predict(input_data)

    
    #show the result
    if(prediction == 0):
        st.markdown(''' #### You are part of group 1:
                    ''')
        st.write("""In this group the quantity of goods ordered is about 27.5, the price of each good purchased is approximately 100 dollars.
                 In addition, total purchases are approximately 3000 dollars, the largest purchases occur in December and the most consumed 
                 product line is classic cars, and the agreements with these individuals are medium to small.""")
    else:
        if(prediction == 1):
            st.markdown(''' #### You are part of group 2:
                        ''')
            st.write("""
                     In this group, the quantity of goods ordered is about 45, purchases more products in the range of 100 dollars, 
                     as well as having total purchases of about 4000 dollars. Their purchases occur more frequently in December and the most consumed product line is classic cars.
                     The agreements with this group are medium-sized""")
        elif(prediction == 2):
            st.markdown(''' #### You are part of group 3:
                        ''')
            st.write("""
                     In this group, the quantity of goods ordered is about 45, purchases more products in the range of 100 dollars, 
                     as well as having total purchases of about 4000 dollars. Their purchases occur more frequently in December and the most consumed product line is classic cars.
                     The agreements with this group are medium-sized""")
        elif (prediction==3):
            st.markdown(''' #### You are part of group 4:
                        ''')
            st.write("""
                     In this group, the quantity of goods ordered is about 45, purchases more products in the range of 100 dollars, 
                     as well as having total purchases of about 4000 dollars. Their purchases occur more frequently in December and the most consumed product line is classic cars.
                     The agreements with this group are medium-sized""")
        else:
            st.markdown(''' #### You are part of group 5:
                        ''')
            st.write("""
                     In this group, the amount of merchandise ordered is about 30, buys more products in the range of 65 dollars, 
                     as well as having total purchases of about 1600 dollars. This group buys more in December and the most purchased 
                     product line is vintage cars. Agreements with this group are small.
                     """)
    


# In[14]:


def code():
    #load model
    loaded_model = header()
    
    #customer input
    form = st.form(key='som')
    AGE = form.number_input('Whats the customer age?' ,key='1', min_value=10,value=75,step=1)
    ANNUAL_INCOME = form.number_input('what is the approximate annual income in K$ of the customer ?',value=100,key='2')
    SPENDING_SCORE = form.number_input("What type of spender the customer is at the moment ?",key='3')
    
    form.form_submit_button('Add')
    
    #dataset creation
    data = [[AGE,ANNUAL_INCOME,SPENDING_SCORE]]
    columns = ['Age','Annual Income (k$)','Spending Score (1-100)']
    
    #insert
    df = pd.DataFrame(data=data, columns=columns)
    
    #creating a button for prediction
    if st.button('Result'):
        Predict_Points(data,loaded_model)
        
    


# In[15]:


if __name__ == '__main__':
    code()


# In[ ]:




