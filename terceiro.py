import json

# Leitura do arquivo JSON com os dados de faturamento
with open('faturamento_mensal.json', 'r') as arquivo:
    dados = json.load(arquivo)

faturamento_diario = dados['faturamento_diario']

# Cálculo do menor e maior valor de faturamento diário
menor = faturamento_diario[0]
maior = faturamento_diario[0]
for valor in faturamento_diario:
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor

# Cálculo da média mensal de faturamento
dias_com_faturamento = 0
total_faturamento = 0
for valor in faturamento_diario:
    if valor != 0:
        dias_com_faturamento += 1
        total_faturamento += valor

media = total_faturamento / dias_com_faturamento

# Cálculo do número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = 0
for valor in faturamento_diario:
    if valor > media:
        dias_acima_da_media += 1

# Exibição dos resultados
print(f"Menor valor de faturamento diário: R${menor:.2f}")
print(f"Maior valor de faturamento diário: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
