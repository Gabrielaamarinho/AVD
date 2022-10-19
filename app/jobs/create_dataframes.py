import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
# import psycopg
# import io
  
#LECOM
fornecedores = pd.DataFrame(pd.read_csv('app/data/fornecedores.csv', delimiter=','))
avaliacoes = pd.DataFrame(pd.read_csv('app/data/avaliacoes.csv', delimiter=','))
fornecedores_avaliacoes = fornecedores.merge(avaliacoes,how='left',left_on='Fornecedor', right_on='Fornecedor')

# PIRAMIDE
recife = pd.DataFrame(pd.read_csv('app/data/fornecedores.csv', delimiter=','))
norte = pd.DataFrame(pd.read_csv('app/data/fornecedores.csv', delimiter=','))
sorocaba = pd.DataFrame(pd.read_csv('app/data/fornecedores.csv', delimiter=','))
curitiba = pd.DataFrame(pd.read_csv('app/data/fornecedores.csv', delimiter=','))
relatorios = pd.concat([recife,norte,sorocaba,curitiba])

# GRAFICO SETORES
frequencia_categorias = pd.DataFrame(fornecedores["Produto / Serviço"].value_counts().reset_index().values, columns=["Categoria", "Frequencia"])
frequencia_categoriasindex = frequencia_categorias.sort_index(axis = 0, ascending=True)
frequencia_categoriasindex = frequencia_categoriasindex.loc[(frequencia_categoriasindex.Frequencia > 4)]


def lecom_data():
  return fornecedores_avaliacoes

def piramide_data():
  return fornecedores_avaliacoes

def freq_categorias():
  return frequencia_categoriasindex