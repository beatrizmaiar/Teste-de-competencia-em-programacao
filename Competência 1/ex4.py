import pandas as pd
from datetime import datetime
from time import time

#Tempo de execução: 0.2076249122619629 segundos

inicio = time()

#carrega as planilhas
df_com_nomes = pd.read_excel('Input_Teste_Python_Dados Exercício 4 II.xlsx')
df_sem_nomes = pd.read_excel('Input_Teste_Python_Dados Exercicio 4 I.xlsx')

#converte data e hora para um formato comum
def converter_para_datetime(data_str, hora_str, formato_str):
    datetime_str = data_str + ' ' + hora_str
    return datetime.strptime(datetime_str, formato_str)

#converte datas e horas em 'comNomes'
df_com_nomes['Inicio'] = df_com_nomes.apply(lambda linha: converter_para_datetime(linha['Data Inicio'], linha['Hora Inicio'], '%Y-%m-%d %H:%M'), axis=1)
df_com_nomes['Termino'] = df_com_nomes.apply(lambda linha: pd.NaT if pd.isna(linha['Data Termino']) or pd.isna(linha['Hora Termino']) else converter_para_datetime(linha['Data Termino'], linha['Hora Termino'], '%Y-%m-%d %H:%M:%S'), axis=1)

#converte datas e horas em 'semNomes'
df_sem_nomes['Inicio'] = df_sem_nomes.apply(lambda linha: converter_para_datetime(linha['Start Time'].split(' ')[0], linha['Start Time'].split(' ')[1], '%d/%m/%Y %H:%M'), axis=1)
df_sem_nomes['Termino'] = df_sem_nomes.apply(lambda linha: pd.NaT if pd.isna(linha['End Time']) else converter_para_datetime(linha['End Time'].split(' ')[0], linha['End Time'].split(' ')[1], '%Y-%m-%d %H:%M:%S'), axis=1)

#encontra o usuário correspondente
def encontrar_usuario_correspondente(linha, df_com_nomes):
    usuario_correspondente = df_com_nomes[(df_com_nomes['Inicio'] == linha['Inicio']) & (df_com_nomes['Termino'] == linha['Termino'])]['Usuario']
    return usuario_correspondente.iloc[0] if not usuario_correspondente.empty else 'unknown'

#atualiza a coluna de nomes de usuário em 'semNomes'
df_sem_nomes['User Name'] = df_sem_nomes.apply(lambda linha: encontrar_usuario_correspondente(linha, df_com_nomes), axis=1)

#prepara relatórios de nomes encontrados e não encontrados
nomes_encontrados = df_sem_nomes[df_sem_nomes['User Name'] != 'unknown']['User Name'].unique()
nomes_nao_encontrados = df_com_nomes[~df_com_nomes['Usuario'].isin(nomes_encontrados)]['Usuario'].unique()

relatorio_nomes_encontrados = pd.DataFrame(nomes_encontrados, columns=['Nomes Encontrados'])
relatorio_nomes_nao_encontrados = pd.DataFrame(nomes_nao_encontrados, columns=['Nomes Não Encontrados'])

#salvando os dados
df_sem_nomes.to_excel('Final.xlsx', index=False)

with pd.ExcelWriter('Relatorio_Nomes.xlsx') as escritor:
    relatorio_nomes_encontrados.to_excel(escritor, sheet_name='Nomes Encontrados', index=False)
    relatorio_nomes_nao_encontrados.to_excel(escritor, sheet_name='Nomes Não Encontrados', index=False)

fim = time()

print(f'Tempo de execução: {fim - inicio} segundos')