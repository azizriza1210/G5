import streamlit as st
import pandas as pd
import pickle

def run():
# Load All Files

    with open('model.pkl', 'rb') as file:
       full_process = pickle.load(file)
       
       education_level = st.selectbox(label='choose your education level here',options=['Graduate School', 'University', 'High School', 
                                                                                        'Others', 'Unknown'])
       # Buat input slider untuk memilih status pembayaran
       pay_0 = st.select_slider(
          label='Repayment status in Pay 0',
          options=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          format_func=lambda x: 'pay duly' if x == -1 else f'delay for {x} months'
          )
       pay_2 = st.select_slider(
          label='Repayment status in Pay 2',
          options=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          format_func=lambda x: 'pay duly' if x == -1 else f'delay for {x} months'
          )
       pay_3 = st.select_slider(
          label='Repayment status in Pay 3',
          options=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          format_func=lambda x: 'pay duly' if x == -1 else f'delay for {x} months'
          )
       pay_4 = st.select_slider(
          label='Repayment status in Pay 4',
          options=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          format_func=lambda x: 'pay duly' if x == -1 else f'delay for {x} months'
          )
       pay_5 = st.select_slider(
          label='Repayment status in Pay 5',
          options=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          format_func=lambda x: 'pay duly' if x == -1 else f'delay for {x} months'
          )
       pay_6 = st.select_slider(
          label='Repayment status in Pay 6',
          options=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          format_func=lambda x: 'pay duly' if x == -1 else f'delay for {x} months'
          )
       limit_balance	= st.number_input(label='input your limit balance here',min_value=0.0)
       pay_amt_1 = st.number_input(label='input your pay amount 1 here')
       pay_amt_2 = st.number_input(label='input your pay amount 2 here')
       pay_amt_3 = st.number_input(label='input your pay amount 3 here')
       pay_amt_4 = st.number_input(label='input your pay amount 4 here')
       pay_amt_5 = st.number_input(label='input your pay amount 5 here')
       pay_amt_6 = st.number_input(label='input your pay amount 6 here')
       
       st.write('In the following is the result of the data you have input : ')
       
       education_mapping = {'Graduate School': 1, 'University': 2, 'High School': 3, 'Others': 4, 'Unknown': 5}
       
       # Mendapatkan nilai angka dari dictionary sesuai dengan pilihan pengguna
       education_level_numeric = education_mapping[education_level]
       
       data_inf = pd.DataFrame({
          'education_level' : education_level_numeric,
          'pay_0' : pay_0,
          'pay_2' : pay_2,
          'pay_3' : pay_3,
          'pay_4' : pay_4,
          'pay_5' : pay_5,
          'pay_6' : pay_6,
          'limit_balance' : limit_balance ,
          'pay_amt_1' : pay_amt_1,
          'pay_amt_2' : pay_amt_2,
          'pay_amt_3' : pay_amt_3,
          'pay_amt_4' : pay_amt_4,
          'pay_amt_5' : pay_amt_5,
          'pay_amt_6' : pay_amt_6,
          }, index=[0])
       st.table(data_inf)
       
       if st.button(label='predict'):
          
          # Melakukan prediksi data dummy
          y_pred_inf = full_process.predict(data_inf)
          
          st.metric(label="Here is a prediction of the default payment next month : ", value = y_pred_inf[0])
          
          #  If your data is a classification, you can follow the example below 
          if y_pred_inf[0] == 0:
             st.write('No')
          else:
             st.write('Yes')
