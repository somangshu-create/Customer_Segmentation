import streamlit as st 
from PIL import Image

def info():
    st.title("Project Expo  - 2022")
    college_image = Image.open("college_logo.jpg")
    st.image(college_image,width=300)
   
    st.markdown("#### Softwares Used: ")
    

    jupyter_image = Image.open("jupyter_notebook_icon.png")
    firefox_image = Image.open("firefox_logo.jpg")
    images_1 =[jupyter_image,firefox_image]
    st.image(images_1, width = 100, caption =['Jupyter Notebook', 'Firefox'])
   
    st.markdown("#### Group Members:-->")
    st.write('''
    ###### Somangshu Chakraborty - coding and web app\n
    ###### Mayur Jagdish Patil - Research and Suggestions\n
    
    ''')
    st.markdown("#### Introduction")
    st.write('''
    
    What's the best way to reach the right customers at the correct time with the information they need? Customer segmentation.
    
    Customer segmentation is the process of tagging and grouping customers based on shared characteristics.
    This process also makes it easy to tailor and personalize your marketing, service,\n and sales efforts to the needs of specific groups.
    The result is a potential boost to customer loyalty and conversions.
    ''')
   
    
    st.markdown("###### Real Life examples of Customer Segmentation software-:")
    experian = Image.open("experian_image.jpg")
    sprout_social = Image.open("sprout_social_image.jpg")
    qualtrics = Image.open("qualtrics_image.jpg")
    images_2 = [experian,sprout_social,qualtrics]
    st.image(images_2, width=650, caption=['Experian','Sprout Social' , 'Qualtrics'])

    
    st.markdown("##### Benifits -->")
    st.write('''
    Improving your customer service and customer support efforts.\n

    Helping internal teams prepare for challenges different groups are likely to experience.\n

    Communicating with segments of customers through preferred channels or platforms.\n

    Finding new opportunities for products, support, and service efficiently.\n
    ''')

    st.success("Thanks for Reading and using our project!!", icon="✅")
    