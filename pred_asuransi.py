import pickle
import streamlit as st

model = pickle.load(open('pred_insurance.sav', 'rb'))

st.title('Prediksi')
st.subheader('Biaya Medis')
st.write('---')

#age,sex,bmi,children,smoker,region
#sex : 0 = female dan 1 = male.
#smoker : tidak merokok (0), merokok (1).
#1 = northwest 
#2 = southeast  
#3 = southwest 

age = st.number_input('Input Age')
bmi = st.number_input('Input BMI')
children = st.number_input('Input Children')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Input Gender')
    sex = st.number_input('female(0) dan male(1)')
with col2:
    st.subheader('Input Smoker')
    smoker = st.number_input('tidak merokok (0), merokok (1)')
region = st.number_input('Input Region')
st.write('1=northwest, 2=southeast, 3=southwest')

predict = ''

if st.button('Predict'):
    predict = model.predict(
        [[age,sex,bmi,children,smoker,region]]
    )
    st.write ('Prediksi Biaya Asuransi : ', predict)