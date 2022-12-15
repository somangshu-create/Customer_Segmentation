#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
from PIL import Image

def data_analysis():
    st.header("Data Analysis and Visualization on the Dataset")
    mall_photo = Image.open("Mall photo.jpg")
    st.image(mall_photo, width=500)
    st.write("###### Note: All findings in this Dataset is subjective, The results can be different for different datasets.")

    st.write('''\n\n\n\n\nThis dataset was taken from kaggle ,given below is a sample . To download it as a csv click-->''')
    csv = open("Mall_Customers.csv")
    st.download_button("Mall_customers_data",csv,file_name="Customer_data.csv")

    df = pd.read_csv("Mall_customers.csv")
    st.dataframe(df.head())

    st.markdown("#### Gender Distribution")
    st.write("Dataset-induced-Bias ::>> As we can clearly see Women come into the mall more often than men.")
    data_viz_1 = Image.open("gender_distribution.png")
    st.image(data_viz_1)

    st.markdown("#### Age_distribution")
    st.write("We can observe here that the majority of the customers are the young working population ")
    data_viz_2 = Image.open("age_group_distribution.png")
    st.image(data_viz_2)

    st.markdown("#### Metrics According to Gender")
    data_viz_3 = Image.open("metrics_according_to_gender.png")
    st.image(data_viz_3)

    st.write('''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')

    st.markdown("#### 1. Segementation based on Annual_Income and Spending_Score")
    st.write('''The black points are the centroids i.e median value in the group , Kmeans is grouping the data points based on the variance from each centroid for their respective groups .
    \n\n
                    1 st group - "Green" --> High spending and low income\n
    2 nd group - " yellow " --> Medium spending and Medium Income\n
    3 rd group - " Red " --> High Income and low spending\n
    4 th group - " blue " --> High Income and High spending \n
    5 th group - " brown " --> Low income and low spending \n
                    
                    
                    ''')
    data_viz_4 = Image.open("segementation_annual_income_spending_score.png")
    st.image(data_viz_4)

    st.markdown("#### 2. Segementation based on Age and Spending_Score")
    st.write('''5 clusters based on Age and spending score.\n
                    1 st group - "Green" --> High spending and Young people\n
    2 nd group - "yellow" --> Medium spending and Young people\n
    3 rd group - "Red" --> Older Adults and low spending\n
    4 th group - "blue" --> Older Adults and High spending \n
                    
                    

    ''')
    data_viz_5 = Image.open("segementation_age_spending_score.png")
    st.image(data_viz_5)


    st.markdown("#### 3. Segmentation based on Age Annual income and Spending score")
    data_viz_6 = Image.open("segementation_age_annual_income_spending_score.png")
    st.image(data_viz_6)
    st.write('''As We can see the KMeans algorithm has divided the data points into 5 clusters based on their age , annual income and spending score .\n
                    1 st group - "Green" --> High spending, young people and low income\n
    2 nd group - "yellow" --> High spending , can be young or old with Medium Income\n
    3 rd group - "Red" --> Medium Income, older adults with Medium spending\n
    4 th group - "blue" --> Young Adults with High Income and High spending \n
    5 th group - "black" --> Older people with  Low income and low spending \n
    ''')


