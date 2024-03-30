import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from Spearman.report import plot_correlation_matrix
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Exploration Data Analysis')
    
#Memanggil data csv 
    st.title('Dataset')
    df= pd.read_csv(r'P1G5_Set_1_mohammad_aziz.csv')

#menampilakn 5 data teratas
    st.table(df.head(5))


#menampilakn Spearman matrix
    st.title('Spearman Correlation Matrix')
    image = Image.open('Eda_Correlation.png')
    st.image(image, caption='figure 1')

# #menampilkan penjelasan 
#     with st.expander('Explanation'):
#         st.caption('lorem ipsum')




