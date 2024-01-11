# IMPORTAÇÃO DA BIBLIOTECA PANDAS
import pandas as pd

# LEITURA DE AMBAS AS ABAS DA PLANILHA
planilha = pd.read_excel(r'Base-Dados-Desafio-D&A-01.xlsx',sheet_name = 'VENDAS')
tabela = pd.read_excel(r'Base-Dados-Desafio-D&A-01.xlsx',sheet_name = 'PRODUTOS')

#1:Qual é o perfil demográfico dos clientes da empresa XYZ?

# BUSCA A SOMA DA QUANTIDADE VENDIDA POR ESTADO
soma_estado = planilha.groupby('ESTADO')['QUANTIDADE_VENDIDA'].sum()
print(soma_estado)


# REPRESENTAÇÃO VISUAL DOS ESTADOS EM QUE HÁ MAIS VENDAS
planilha.plot.bar('ESTADO','QUANTIDADE_VENDIDA')


# BUSCA A SOMA DA QUANTIDADE VENDIDA POR IDADE
soma_idade = planilha.groupby('IDADE')['QUANTIDADE_VENDIDA'].sum()

print(soma_idade)

# REPRESENTAÇÃO VISUAL DAS IDADES EM QUE HÁ MAIS VENDAS
planilha.plot.bar('IDADE','QUANTIDADE_VENDIDA')

# É POSSÍVEL SE VERIFICAR QUE AS IDADES EM QUE OS CLIENTES MAIS ADQUIREM PRODUTOS SÃO COM 43 E 47 ANOS. ALÉM DISSO, HÁ UMA PREDOMINÂNCIA EM RELAÇÃO AOS ESTADOS EM QUE ESTES ESTÃO INSERIDOS SENDO CONCENTRADOS PRINCIPALMENTE EM SANTA CATARINA E NA PARAÍBA.


# 2: Qual a categoria de produto mais vendidas e a menos vendidas?

# TRAZ OS DADOS DE CATEGORIA À TABELA COM OS DADOS DE VENDAS PELO MERGE
temp_tabela = pd.merge(planilha,tabela[['PRODUTO','CATEGORIA']],on = ['PRODUTO'],how='left')

# BUSCA A SOMA DE PRODUTOS VENDIDOS AGRUPADOS POR CATEGORIA
soma_categoria = temp_tabela.groupby('CATEGORIA')['QUANTIDADE_VENDIDA'].sum()

print(soma_categoria.sort_values(ascending = False))

# PELA TABELA GERADA ENTRE AS QUANTIDADES VENDIDAS E AS CATEGORIAS, A CATEGORIA QUE MAIS VENDEU FOI UTILIDADES DOMÉSTICAS E QUE MENOS VENDEU FOI JARDINAGEM

#3: Há alguma relação entre as vendas e a época do ano?

# TRAZ SOMENTE AS DATAS E A QUANTIDADE VENDIDA PARA UMA OUTRA TABELA DE ANÁLISE
tabela_data_quantidade = temp_tabela.loc[:,['DATA','QUANTIDADE_VENDIDA']]

tabela_data_quantidade['mes'] = pd.DatetimeIndex(tabela_data_quantidade['DATA']).month

soma_mes = tabela_data_quantidade.groupby('mes')['QUANTIDADE_VENDIDA'].sum()

soma_mes.plot.bar()

# PELOS DADOS, FOI FEITA UMA ANÁLISE EM CIMA DOS MESES DO ANO E FOI VERIFICADA UMA PREPONDERÂNCIA NOS MESES DE JANEIRO E AGOSTO, ENQUANTO HÁ UMA BAIXA NAS VENDAS ENTRE JUNHO E JULHO. 


#4: Qual é a tendência de vendas por região geográfica?

# CRIAR UMA TABELA AUXILIAR PARA TRAZER APENAS OS DADOS DE ESTADO, QUANTIDADE VENDIDA E DATA
temp_regiao = temp_tabela.loc[:,['ESTADO','QUANTIDADE_VENDIDA','DATA']]

# TRAZER OS MESES PARA AGRUPAR AS VENDAS DE FORMA MENSAL
temp_regiao['mes'] = pd.DatetimeIndex(temp_regiao['DATA']).month

# FAZER UM REPLACE COM OS DADOS DOS ESTADOS PARA TRAZER APENAS AS REGIÕES
temp_regiao2 = temp_regiao.replace({'SANTA CATARINA':'SUL','SÃO PAULO':'SUDESTE','BAHIA':'NORDESTE','PARANÁ':'SUL','RIO GRANDE DO SUL':'SUL','RIO DE JANEIRO':'SUDESTE','PARAÍBA':'NORDESTE'})

# TRAZER A SOMA DA QUANTIDADE VENDIDA POR AGRUPADA POR ESTADO E MES
soma_estado = temp_regiao2.groupby(['ESTADO','mes'])['QUANTIDADE_VENDIDA'].sum()

# PLOTAR OS GRÁFICOS DE BARRA DAS REGIÕES AO LONGO DOS MESES
soma_estado.plot.bar()

# PELO GRÁFICO É POSSÍVEL CONSIDERAR UMA TENDÊNCIA NA REGIÃO NORDESTE, QUE COMPREENDE OS CLIENTES DA BAHIA E DA PARAÍBA, DE QUEDA EM SUAS VENDAS, JÁ NA REGIÃO SUL E SUDESTE HÁ UMA TENDÊNCIA DE CRESCIMENTO DEVIDO, PROVAVELMENTE, AOS MESES SEM VENDAS.


#5: Há alguma correlação entre a idade dos clientes e as categorias de produtos que eles compram?

soma_categoria_idade = temp_tabela.groupby(['IDADE','CATEGORIA'])['QUANTIDADE_VENDIDA'].sum()

print(soma_categoria_idade)

soma_categoria_idade.plot.bar()

# É POSSÍVEL NOTAR EM QUASE TODAS AS CATEGORIAS QUE HÁ UMA QUEDA NO CONSUMO CONFORME O AVANÇO DA IDADE APÓS OS 40 ANOS, FICANDO MAIS EVIDENTE AO COMPARAR AS VENDAS PARA OS CLIENTES DE 20 ANOS COM OS DE 61 E 58. 
