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
colunasSelecionadas = ['Ano', 'UF', 'Município', 'VABAGRO_PC', 'VABI_PC', 'VABS_PC', 'VABA_PC', 'ILS_PPC']


# Novo dataframe com as colunas selecionadas
df_filter = rename_df.filter(items=colunasSelecionadas)

# Apagar valores NaN
df_filter = df_filter.dropna()

# Filtrar pela cidade de Manaus
df_manaus = df_filter[df_filter.Município == 'Manaus']

# Converter a colunas VABAGRO_PC e ILS_PPC de object para float
df_manaus['VABAGRO_PC'] = df_manaus['VABAGRO_PC'].astype(float, errors = 'raise')
df_manaus['ILS_PPC'] = df_manaus['ILS_PPC'].astype(float, errors = 'raise')

# Criar uma nova coluna PIB e somar os valores da Agropecuária, Indústria, Serviços, Administração e Impostos
df_manaus['PIB'] = df_manaus['VABAGRO_PC'] + df_manaus['VABI_PC'] + df_manaus['VABS_PC'] + df_manaus['VABA_PC'] + df_manaus['ILS_PPC']

# 2. Qual o valor médio do Produto Interno Bruto da cidade de Manaus no período que abrange o dataset? 
df_saida = df_manaus.head()

# Salvar resultado em txt
df_saida.to_csv("saida_q2.txt")





