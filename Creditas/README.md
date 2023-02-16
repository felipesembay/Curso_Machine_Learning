![logo Creditas](logo.png)

# Curso_Machine_Learnig

Nesse repositório serão adicionados os arquivos referente ao Curso de Machine Learning. 

Na pasta do repositório estão os seguintes arquivos:

- **Arquivos Jupyter** -  Todos os arquivos que foram utilizados para a Analise Exploratória dos Dados (EDA), construção do Modelo de Machine Learning e persistência do disco (teste dos arquivos pickle referente aos modelos)
- **Arquivos Modelos** - Pickle. Nessa pasta encontra todos os arquivos salvos das nossas análises. Temos vários modelos salvos para testar. 
- **Dados e suas transformações** - Nessa pasta encontra-se o arquivo csv que utilizamos para criar os nossos dados em **SQL**. Também encontram-se derivações dos nossos dados, nas quais utilizamos na Análise Exploratória e também na transformação dos dados. 
- **SQL - Database**- Nessa pasta encontra-se o arquivo em formato **SQL** que utilizamos para subir nosso arquivo no **MYSQL** que se encontra no nosso **Docker**. 
- **STREAMLIT**- Nessa pasta encontra-se os nossos arquivos que utilizaremos para construir o nosso protótipo no **Streamlit**. 

## Aula 1 - INTRODUÇÃO
Aula 1 pode ser acessada clicando [aqui](https://www.youtube.com/watch?v=XANG7SKdVu0&t=4s), foi criado o nosso ambiente docker (mysql), e subimos os nossos dados em formato SQL. Para mais informações, acessar na **descrição** do vídeo. 

## Aula 2.1 - ANALISE EXPLORATÓRIA DOS DADOS
Nessa aula que pode ser acessada cliando [aqui](https://www.youtube.com/watch?v=nF-BHtiSfy0&t=16s), foram feitas algumas consultas básicas utilizando a **query** do **MySQL**. Em seguida, conectamos com cada uma das tabelas no banco de dados e por fizemos um **merge** com essas tabelas. Após realizarmos o merge, verificamos se a coluna **id** possuía algum dado duplicado. E em seguida, foram criadas duas **features novas** com base na data de nascimento do cliente, e na data de criação da conta do cliente. Criamos as colunas idade do cliente e também, criação da conta do cliente (em semanas). 

### Aula 2.2 - ANALISE EXPLORATÓRIA DOS DADOS (média, moda, mediana, assimetria e curtose)
Na aula 2.2 que pode ser acessada clicando [aqui](https://www.youtube.com/watch?v=io0-P4wEcsg&t=30s), foi ensinado a utilizar a moda, média e mediana, para imputar os valores nulos, dentro do seu conjunto de dados. 
Além do mais, foi explicado o que é **Assimetria e curtose**, e como utilizar ela para auxiliar na detecção de outliers em nossos dados. 

### Aula 2.3 - ANALISE EXPLORATÓRIA DOS DADOS (gráficos e insights)
Na aula 2.3 que pode ser acessada clicando [aqui](https://www.youtube.com/watch?v=SuebV-O1tr4&t=5s), fizemos vários gráficos para entender e buscar insights nos nossos dados. 

### Aula 2.4 - ANALISE EXPLORATÓRIA DOS DADOS (gráficos e insights)
Na aula 2.4 que pode ser acessada clicando [aqui](https://www.youtube.com/watch?v=r9QPEx_2p6g&t=29s), é a continuação da aula 2.3, aonde buscamos gerar novos gráficos para continuar buscando insights dos nossos dados. Nessa aula, foram tratados os outliers com a técnica do primeiro e terceiro quartile, dessa forma criando nossos limites superiores e limites inferiores. E por último, para aquelas **features** que estão fora do range de **assimetria e curtose**, foram tratadas utilizando o **logaritmo na base X**, para corrigir e normalizar os dados. É uma forma de transformação muito conhecida na **Econometria**. 


## Aula 3.1 - MACHINE LEARNING NA PRÁTRICA
Na aula 3.1 que pode ser acessada cliando [aqui](https://www.youtube.com/watch?v=5J3BVf-QSqg).....continua