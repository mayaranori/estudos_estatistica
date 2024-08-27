# -*- coding: utf-8 -*-
# Estudando Pandas-EBA.py

# Certifique-se de que o pandas está instalado.
# No terminal do VS Code, execute: pip install pandas

import pandas as pd

# Carregando os datasets
df = pd.read_csv("C:\\Users\\USER\\Desktop\\drive_eba\\top10s.csv", encoding="ISO-8859-1")
dfs = pd.read_csv("C:\\Users\\USER\\Desktop\\drive_eba\\SpotifyTopSongsByCountry - May 2020.csv", encoding="ISO-8859-1")

# Exibindo as 5 primeiras linhas de cada dataframe
print(df.head())
print(dfs.head())

# Exibir informações sobre o dataframe
print(df.info())
print(df.describe())

# Exibir colunas únicas, contagem e valores distintos
print(df['artist'].unique())
print(df['artist'].nunique())
print(df['title'].nunique())

# Operações básicas no dataframe
print(df.shape)
print(df.size)
print(df.columns)
print(df.memory_usage())

# Encontrando valores específicos
print(df.query("artist == 'Ariana Grande' "))
print(df.query("artist == 'Katy Perry' "))
print(df.query('dur > 200'))

# Groupby
df_grouped = df.groupby('artist')['title'].count()
print(df_grouped)

# Merge datasets
merged_df = df.merge(dfs, left_on='artist', right_on='Artists', how='left')
print(merged_df.fillna(0))

# Extras: Correlação
# Selecionar apenas as colunas numéricas antes de calcular a correlação
df_numerico = df.select_dtypes(include=['float64', 'int64'])
print(df_numerico.corr())
