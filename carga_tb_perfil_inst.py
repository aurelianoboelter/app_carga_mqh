import pandas as pd

# Dados em forma de dicionário
dados = {
    "Coluna1": ["Hosp_01", "Hosp_02", "Hosp_03"],
    "Coluna2": [25000, 320, 2910],
    "Coluna3": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)
