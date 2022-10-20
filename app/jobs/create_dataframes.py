import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px

#LECOM
fornecedores = pd.DataFrame(pd.read_csv('./data/fornecedores.csv', delimiter=','))
new_header = fornecedores.iloc[0]
fornecedores = fornecedores[1:]
fornecedores.columns = new_header
fornecedores = fornecedores[fornecedores['Fornecedor'].notna()]

avaliacoes = pd.DataFrame(pd.read_csv('./data/avaliacoes.csv', delimiter=','))
new_header = avaliacoes.iloc[0]
avaliacoes = avaliacoes[1:]
avaliacoes.columns = new_header
avaliacoes = avaliacoes[avaliacoes['Fornecedor'].notna()]

fornecedores_avaliacoes = fornecedores.merge(avaliacoes,how='left',left_on='Fornecedor', right_on='Fornecedor')


# PIRAMIDE
recife = pd.DataFrame(pd.read_csv('./data/fornecedores.csv', delimiter=','))
norte = pd.DataFrame(pd.read_csv('./data/fornecedores.csv', delimiter=','))
sorocaba = pd.DataFrame(pd.read_csv('./data/fornecedores.csv', delimiter=','))
curitiba = pd.DataFrame(pd.read_csv('./data/fornecedores.csv', delimiter=','))
relatorios = pd.concat([recife,norte,sorocaba,curitiba])

# DF SETORES
frequencia_categorias = pd.DataFrame(fornecedores["Produto / Serviço"].value_counts().reset_index().values, columns=["Categoria", "Frequencia"])
frequencia_categoriasindex = frequencia_categorias.sort_index(axis = 0, ascending=True)
frequencia_categoriasindex = frequencia_categoriasindex.loc[(frequencia_categoriasindex.Frequencia > 4)]


def lecom_data():
  return fornecedores_avaliacoes

def piramide_data():
  return fornecedores_avaliacoes

def freq_categorias():
  return frequencia_categoriasindex