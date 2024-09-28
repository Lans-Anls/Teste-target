import json;

with open('C:\\Users\\AnLNS\\OneDrive\\Área de Trabalho\\Todas as pastas da area de trabalho\\Teste Tecnico estagio Target\\Teste-target\\ATV3\\dados.json', 'r') as f:
    dados = json.load(f)
print(f"\n")
print(f"Valores JSON:{dados}\n")


# Filtrar os dias que possuem faturamento maior que 0
valores_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

Todos_os_dias = [dia['dia'] for dia in dados if dia['valor'] >= 0]

print(f"Dias faturados: {len(valores_faturamento)}\n")
print(f"Dias Totais: {len(Todos_os_dias)}\n")

# Cálculo do menor e maior valor de faturamento
menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)

# Cálculo da média de faturamento
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Criando Lista com os dias que possuem faturamento acima da média
dias_acima_da_media = [dia['dia'] for dia in dados if dia['valor'] > media_mensal]

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_valor}\n")
print(f"Maior valor de faturamento: {maior_valor}\n")
print(f"Dias com faturamento superior à média: {dias_acima_da_media}\n")
print(f"Total de dias com faturamento superior à média: {len(dias_acima_da_media)}\n")
print(f"Média de faturamento: {media_mensal}\n")
