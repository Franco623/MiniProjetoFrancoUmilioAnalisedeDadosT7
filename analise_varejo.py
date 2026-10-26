# importando biblioteca pandas
import pandas as pd

# Carregando base de dados.csv
df_varejo = pd.read_csv("Base_Varejo.csv", sep = ";")

#  Mostra a quantidade de registros e colunas 
print("\n--- DIMENSÕES DA BASE ---") 
print(f"Quantidade de registros: {df_varejo.shape[0]}")
print(f"Quantidade de colunas: {df_varejo.shape[1]}")

# Mostra os nomes das colunas 
print("\n--- Nomes das colunas ---")																																																																																																																																																																																																																																																																																										
print(df_varejo.columns.tolist())

# Mostra os tipos de dados 
print("\n--- TIPOS DE DADOS ---") 
print(df_varejo.dtypes)

# Mostra as primeiras linhas 
print ("\n--- PRIMEIRAS LINHAS DA BASE ---") 
print(df_varejo.head())