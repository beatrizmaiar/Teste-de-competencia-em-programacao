import pandas as pd
from datetime import timedelta
from time import time

#Tempo de execução: 0.5490894317626953 seg

inicio = time()

def converter_colunas_tempo(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'], format="%d/%m/%Y %H:%M")
    df['End Time'] = pd.to_datetime(df['End Time'], format="%Y-%m-%d %H:%M:%S")
    return df

#mesclar intervalos sobrepostos
def mesclar_intervalos_sobrepostos(intervalos):
    intervalos_ordenados = sorted(intervalos, key=lambda x: x[0])
    intervalos_mesclados = []

    for atual in intervalos_ordenados:
        if not intervalos_mesclados or atual[0] > intervalos_mesclados[-1][1]:
            intervalos_mesclados.append(atual)
        else:
            intervalos_mesclados[-1] = (
                intervalos_mesclados[-1][0],
                max(intervalos_mesclados[-1][1], atual[1])
            )

    return intervalos_mesclados

#calcula a duração do uso e lidar com sobreposições
def calcular_duracao_uso(df):
    df['Data'] = df['Start Time'].dt.date
    colunas_unicas = df.drop(columns=['Start Time', 'End Time']).drop_duplicates()
    resultados = []

    for indice, linha in colunas_unicas.iterrows():
        nome_usuario = linha['User Name']
        data = linha['Data']
        intervalos_usuario = df[(df['User Name'] == nome_usuario) & (df['Data'] == data)][['Start Time', 'End Time']]
        intervalos = intervalos_usuario.values
        intervalos_mesclados = mesclar_intervalos_sobrepostos(list(map(tuple, intervalos)))
        duracao_total = sum((fim - inicio for inicio, fim in intervalos_mesclados), pd.Timedelta(0))
        linha['Duração Total'] = duracao_total
        resultados.append(linha)

    return pd.DataFrame(resultados)

#formata a coluna de duração total do uso
def formatar_duracao_total_uso(df):
    df['Duração Total'] = df['Duração Total'].apply(lambda td: str(td).replace('0 days ', '').replace('days', 'd'))
    return df

#salva o resultado em um novo arquivo
def salvar_resultados(df, caminho_saida):
    df.to_excel(caminho_saida, index=False)


#executa as funções
df = pd.read_excel('Input_Teste_Python_exercicio 3.xlsx')
df = converter_colunas_tempo(df)
resultados = calcular_duracao_uso(df)
resultados = formatar_duracao_total_uso(resultados)
salvar_resultados(resultados, 'DuracaoTotal.xlsx')

fim = time()

print(f'Tempo de execução: {fim - inicio} seg')

