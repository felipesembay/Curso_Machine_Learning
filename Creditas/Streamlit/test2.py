import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from pycaret.classification import load_model, predict_model
model = load_model('gbc1_model')


# print title of web app
st.title("Simulação de Classificação de Crédito - Demonstração de um aplicativo para Machine Learning")
st.markdown("Simulação de Classificação de Crédito, é um projeto criado para fins de aprendizado, sem qualquer vinculação com os processos internos para concessão de crédito da empresa.")

def predict(model, input_df):
    predictions_df = predict_model(estimator = model, data = input_df)
    predictions = predictions_df['Score'][0]
    return predictions

def run():
    
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict credit classification')
    st.sidebar.success('https://www.linkedin.com/in/felipe-sembay/')
    
    

    st.title("Credit Loan Prediction App")

    if add_selectbox == 'Online':

        monthly_income = st.number_input('monthly_income', min_value=1, max_value=1000000, value=2000)
        if st.checkbox('cpf_restriction'):
            restriction = 1
        else:
            restriction = 0
        loan_amount = st.number_input('loan_amount', min_value=1, value=5000)
        auto_debt = st.number_input('auto_debt', min_value=0, max_value=1000000, value=0)
        if st.checkbox('declares_income_tax'):
            declares = 1
        else:
            declares = 0
        idade = st.number_input('idade', min_value=18, max_value=120, value=30)
        

        output=""

        input_dict = {'monthly_income' : monthly_income, 'cpf_restriction' : restriction, 'loan_amount': loan_amount, 'auto_debt': auto_debt, 'declares_income_tax': declares, 'idade': idade}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            
          
        st.success('A probabilidade do seu empréstimo ser liberado é de {}'.format(output))
        st.markdown("Valores acima de 0.50 são classificados como liberados; valores inferiores a 0.50 são classificados como negados.")

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()
