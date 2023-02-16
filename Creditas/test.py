import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pycaret.classification import load_model, predict_model
import datetime as dt
import datetime
from datetime import date 

#Carregando o arquivo pickle usando joblib
model = joblib.load('/home/felipe/Projeto/Portfolio/Creditas/Arquivos_pickle/model_choice.pkl')


# print title of web app
st.title("PROJETO MACHINE LEARNING END TO END")
st.markdown("Simulação de Classificação de Crédito, é um projeto para aprendizado")

@st.cache
def main():
    st.write("Importando o arquivo pickle com Joblib")
    st.markdown("Modelo de aprendizado de máquina:")

def run():

    st.sidebar.info('This app is created to predict credit classification')
    st.sidebar.success('https://www.linkedin.com/in/felipe-sembay/')


    if st.checkbox('É homem?'):
        gender = 1
    else:
        gender = 0
    
    phone_code = st.slider('Código do DDD', min_value = 1, max_value =100, value=11)
    
    if st.checkbox('CPF com restrição?'):
        restriction = 1
    else:
        restriction = 0
    
    Renda = st.number_input('Renda Mensal', min_value=1, max_value=100000, value=3000)
    
    Ano_carro = st.slider('Ano do modelo do carro', min_value=1960, max_value=2022, value=2012)
    
    Valor_carro = st.number_input('Valor do modelo do carro', value=21000.0)
    
    Debito_carro = st.number_input('Debito do carro', value=0.0)
    
    Valor_emprestimo = st.number_input('Valor desejado de empréstimo?', min_value=1.0, value=11000.0)
    
    idade = st.slider('idade', min_value=18, max_value=100, value=40)
    
    st.write("Calculando a quantas semanas atrás foi aberto a conta:")
    date1 = st.date_input("Data 1:", datetime.datetime.now())
    date2 = st.date_input("Dia Atual:", datetime.datetime.now())
    difference = ((date2 - date1)/7).days
    st.write("A diferença em semanas entre as datas é:", difference)
    

    output=""
    input_dict = {'gender': gender,
                  'phone_code': phone_code,
                  'cpf_restriction': restriction,
                  'monthly_income': Renda,
                  'model_year': Ano_carro,
                  'auto_value': Valor_carro,
                  'auto_debt': Debito_carro,
                  'loan_amount': Valor_emprestimo,
                  'idade': idade,
                  'diff_created': difference}
    input_df = pd.DataFrame([input_dict])

    if st.button("Predict"):
        output = model.predict(input_df)
        #output = str(output)
        prob = model.predict_proba(input_df)
        
    if(output ==0):
        st.title('Empréstimo Negado')
        st.success(f'A sua pontuação é de {prob[0][0]}')
    if(output ==1):
        st.title('Empréstimo Aprovado')
        st.success(f'A sua pontuação é de {prob[0][1]}')

    
if __name__ == '__main__':
    run()