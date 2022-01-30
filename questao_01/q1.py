import pandas as pd

# Criando o dataframe a partir do nome do arquivo.txt
df = pd.read_csv("../dataset/pib_municipio_2010_a_2018.txt", sep=";")

# Renomeando as colunas
rename_df = df.rename(columns={ 'Sigla da Unidade da Federação': 'UF', 
                                'Nome da Unidade da Federação': 'Estado', 
                                'Nome do Município': 'Município',
                                'Valor adicionado bruto da Agropecuária a preços correntes (R$ 1.000)': 'VABAGRO_PC',
                                'Valor adicionado bruto da Indústria a preços correntes (R$ 1.000)': 'VABI_PC',                                 
                                'Valor adicionado bruto dos Serviços a preços correntes (R$ 1.000)': 'VABS_PC',    
                                'Valor adicionado bruto da Administração a preços correntes (R$ 1.000)': 'VABA_PC', 
                                'Impostos, líquidos de subsídios, sobre produtos a preços correntes (R$ 1.000)': 'ILS_PPC', 
                                'Produto Interno Bruto per capita a preços correntes (R$ 1,00)': 'PIB_PERC_PC'
                            }
                    )
# Fazer seleção de colunas para diminuir o dataframe e agilizar o processamento
colunasSelecionadas = ['Ano', 'UF', 'Município', 'PIB_PERC_PC']

# Novo dataframe com as colunas selecionadas
df_filter = rename_df.filter(items=colunasSelecionadas)

# Apagar valores NaN
df_filter = df_filter.dropna()

# Substituir valores
df_filter['PIB_PERC_PC'] = df_filter['PIB_PERC_PC'].str.replace('(','')
df_filter['PIB_PERC_PC'] = df_filter['PIB_PERC_PC'].str.replace(')','')

# Converter a coluna PIB_PERC_PC de object para float
df_filter['PIB_PERC_PC'] = df_filter['PIB_PERC_PC'].astype(float, errors = 'raise')

# Filtrar o ano de 2018
df_2018 = df_filter[df_filter.Ano == '2018']

# Agrupar por Estados
df_uf = df_2018.groupby('UF')

# 1. Qual a cidade de cada estado que possui o maior PIB per capita, no ano de 2018? 
df_saida = df_uf.max()

# Salvando resultado em txt
df_saida.to_csv("saida_q1.txt")


