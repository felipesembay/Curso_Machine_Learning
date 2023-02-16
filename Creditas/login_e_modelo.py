import streamlit as st
import pandas as pd
import numpy as np
import joblib
import hashlib
import mysql.connector
from mysql.connector import errorcode
import pymysql

st.sidebar.success('https://www.linkedin.com/in/felipe-sembay/')

# Conectar ao banco de dados
def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="172.17.0.2",
            user="root",
            password="abc123",
            database="creditas_model"
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            st.error("Usuário ou senha inválidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            st.error("Banco de dados não existe")
        else:
            st.error(err)
            
conn = conectar_bd()
cursor = conn.cursor()

model = joblib.load('/home/felipe/Projeto/Portfolio/Creditas/Arquivos_pickle/model_choice1.pkl')

def make_hashes(senha):
	return hashlib.sha256(str.encode(senha)).hexdigest()

def check_hashes(senha,hashed_text):
	if make_hashes(senha) == hashed_text:
		return hashed_text
	return False

#Criando a tabela no banco de dados para salvar os dados dos usuários
def create_usertable():
	cursor.execute("CREATE TABLE IF NOT EXISTS users(usuario TEXT, email VARCHAR(255), senha TEXT, data_criacao TIMESTAMP)")
 
def add_userdata(usuario, email, senha):
	cursor.execute("INSERT INTO users (usuario, email, senha, data_criacao) VALUES (%s, %s, %s, NOW())", (usuario, email, senha))
	conn.commit()
 
def login_user(email,senha):
	cursor.execute("SELECT * FROM users WHERE email = %s AND senha = %s",(email,senha))
	data = cursor.fetchall()
	return data

def view_all_users():
	cursor.execute("SELECT * FROM users")
	data = cursor.fetchall()
	return data

#Criando a tabela para armazenar o nosso modelo de machine learning
#def create_modeltable():
#	cursor.execute("CREATE TABLE IF NOT EXISTS Cliente(nome, sexo, phone_code, cpf_restrition, renda, model_year, autovalue, autodebt, loan_amount, idade, diff_created, previsao)")
 
def add_modeldata(input_name, gender, phone_code, restriction, Renda, Ano_carro, Valor_carro, Debito_carro, Valor_emprestimo, idade, conta, y_pred_proba):
	cursor.execute("INSERT INTO Cliente (clinome, clisexo, cliphone_code, clicpf_restrition, clirenda, climodel_year, cliautovalue, cliautodebt, cliloan_amount, cliidade, clidiff_created, cliprevisao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (input_name, gender, phone_code, restriction, Renda, Ano_carro, Valor_carro, Debito_carro, Valor_emprestimo, idade, conta, y_pred_proba))
	conn.commit()

def view_all_model():
	cursor.execute("SELECT * FROM model")
	data = cursor.fetchall()
	return data

st.image("logo.png")
st.title("PROJETO MACHINE LEARNING END TO END")
st.markdown("**Simulação de Classificação de Crédito**, é um projeto para aprendizado no curso Machine Learning End to End - Youtube. Esses dados fazem parte de um processo para **Analista de Mercado** que ocorreu em 2020 na **Creditas**. Esses dados são totalmente **fictícios**, sendo criado apenas para o teste. Eles não tem a menor relação com a realidade. Acesse o meu [canal](https://www.youtube.com/watch?v=XANG7SKdVu0&t=9s) na aula 1 e aproveite!")
# Página de Modelo de Machine Learning
def model_ml():
    st.title("Modelo de Machine Learning")
    st.write("Conteúdo do seu modelo de machine learning")
    
    
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
    
# Fazer a predição usando os dados do nosso modelo
    prediction_state = st.markdown('calculating...')
    
    input_data = [[gender, phone_code, restriction, Renda, Ano_carro, Valor_carro,Debito_carro, Valor_emprestimo, idade, conta]]

    input_button = st.button("Previsão")
    y_pred = model.predict(input_data)
    y_pred_proba =  model.predict_proba(input_data)[0][1]

    if y_pred[0] == 0:
        msg = '**Empréstimo Negado**'
    else:
        msg = '**Empréstimo Liberado**'
        
    if input_button:
        prediction_state.markdown(msg)
        st.success(y_pred_proba)
        
    if input_button:
        add_modeldata(input_name, gender, phone_code, restriction, Renda, Ano_carro, Valor_carro, Debito_carro, Valor_emprestimo, idade, conta, y_pred_proba)
        st.success('Dados adicionados com sucesso!')
        
        

# Página Principal
def main():
	"""Simple Login App"""

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		email = st.sidebar.text_input("E-mail do usuário")
		senha = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(senha)

			result = login_user(email,check_hashes(senha,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(email))

				task = st.selectbox("Task",["Add Post","Analytics","Model"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
                    
				elif task == "Model":
					st.subheader("")
					model_result = model_ml()
					clean_db = pd.DataFrame(model_result)
					#st.dataframe(clean_db)
			else:
				st.warning("E-mail ou senha incorreto")


	elif choice == "SignUp":
         st.subheader("Criar Nova Conta")
         usuario = st.text_input("Usuário")
         email = st.text_input("E-mail")
         senha = st.text_input("Senha", type='password')
         
         if st.button("Criar Conta"):
            create_usertable()
            add_userdata(usuario, email,make_hashes(senha))
            st.success("Você criou com sucesso uma conta válida")
            st.info("Vá para o menu Login para fazer o login")
            


if __name__ == '__main__':
	main()
        

