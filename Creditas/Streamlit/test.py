import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
model = load_model('gbc_model')


# print title of web app
st.title("Si")
st.markdown("Simulação de Classificação de Crédito, é um projeto para aprendizado")

@st.cache
def predict(model, input_df):
    predictions_df = predict_model(estimator = model, data = input_df)
    predictions = predictions_df['Score'][0]
    return predictions

def run():

    st.sidebar.info('This app is created to predict credit classification')
    st.sidebar.success('https://www.linkedin.com/in/felipe-sembay/')
    

    st.title("Credit Loan Prediction App")


    monthly_income = st.number_input('monthly_income', min_value=1, max_value=1000000, value=2000)
    if st.checkbox('cpf_restriction'):
        restriction = 1
    else:
        restriction = 0
    loan_amount = st.number_input('loan_amount', min_value=1, value=11000)
    

    output=""
    input_dict = {'monthly_income' : monthly_income, 'cpf_restriction' : restriction, 'loan_amount': loan_amount}
    input_df = pd.DataFrame([input_dict])

    if st.button("Predict"):
        output = predict(model=model, input_df=input_df)
        output = str(output)

    st.success('The output is {}'.format(output))

    
if __name__ == '__main__':
    run()