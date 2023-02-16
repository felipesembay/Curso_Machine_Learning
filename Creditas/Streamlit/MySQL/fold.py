import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime as dt
from datetime import date
import datetime
import mysql.connector
   
# Conectar ao banco de dados
cnx = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    password="abc123",
    database="creditas_model"
)

# Criar cursor para interagir com o banco de dados
cursor = cnx.cursor()

# Criar tabela no banco de dados, se ela não existir
#tabela = "CREATE TABLE IF NOT EXISTS dados (nome VARCHAR(255), idade INT(3))"
#cursor.execute(tabela)

# Página inicial do Streamlit
# Carregar modelo
model = joblib.load('/home/felipe/Projeto/Portfolio/Creditas/Arquivos_pickle/model_choice1.pkl')

st.title("PROJETO MACHINE LEARNING END TO END")
st.markdown("Simulação de Classificação de Crédito, é um projeto para aprendizado no curso Machine Learning End to End - Youtube")

#Receber dados para o modelo processar
with st.form(key="Include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
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
    
    Valor_carro = st.number_input('Valor do carro?', value=21000.0)
    
    Debito_carro = st.number_input('Debito do carro', value=0.0)
    
    Valor_emprestimo = st.number_input('Valor desejado de empréstimo?', min_value=1.0, value=11000.0)
    
    idade = st.slider('idade', min_value=18, max_value=100, value=40)
    
    conta = st.slider('Há quantas semanas essa conta foi criada?', max_value=500, value=20)
    
# this is how to dynamically change text
    prediction_state = st.markdown('calculating...')
    
    input_data = [[gender, phone_code, restriction, Renda, Ano_carro, Valor_carro,Debito_carro, Valor_emprestimo, idade, conta]]

    input_button_submit = st.form_submit_button("Previsão")
    y_pred = model.predict(input_data)
    y_pred_proba =  model.predict_proba(input_data)[0][1]

    if y_pred[0] == 0:
        msg = '**Empréstimo Negado**'
    else:
        msg = '**Empréstimo Liberado**'
        
if input_button_submit:
    prediction_state.markdown(msg)
    st.success(y_pred_proba) 


# Salvar dados no banco de dados quando o botão é clicado
if input_button_submit:
    query = """INSERT INTO Cliente (clinome, clisexo, cliphone_code, clicpf_restrition, clirenda,
    climodel_year, cliautovalue, cliautodebt, cliloan_amount, cliidade, clidiff_created, cliprevisao) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (input_name, gender, phone_code, restriction, Renda, Ano_carro, Valor_carro, Debito_carro, Valor_emprestimo, idade, conta, y_pred_proba))
    cnx.commit()
    st.success("Dados salvos com sucesso!")

# Fechar conexão com o banco de dados
cnx.close()
    