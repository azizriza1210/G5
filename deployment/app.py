import streamlit as st
import eda
import prediction


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Grade Challenge 5')
    st.write('Nama      : M. Aziz Riza')
    st.write('Batch     : MSIB')
    st.write('Tujuan GC    : Membuat model machine learning klasifikasi dengan Logistic Regression, SVM, dan KNN untuk memprediksi default_payment_next_month')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')

    with st.expander("Problem Statement"):
        st.caption('Membuat model machine learning klasifikasi dengan Logistic Regression, SVM, dan KNN untuk memprediksi default_payment_next_month')

    with st.expander("Kesimpulan"):
        st.caption('Model sudah mampu memprediksi dari data yang diberikan, dimana untuk data pertama menghasilkan prediksi 0(no) atau orang tersebut membayar dan untuk data ke dua menghasilkan prediksi 1(yes) atau orang tersebut tidak membayar.')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     prediction .run()