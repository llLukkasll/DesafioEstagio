# Valores de faturamento por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Cálculo do valor total mensal de faturamento
valor_total_mensal = sum(faturamento_por_estado.values())

# Cálculo do percentual de representação de cada estado
percentuais_por_estado = {}
for estado, faturamento in faturamento_por_estado.items():
    percentual = (faturamento / valor_total_mensal) * 100
    percentuais_por_estado[estado] = percentual

# Exibição dos resultados
for estado, percentual in percentuais_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
