# Vetor fictício de faturamento diário de 365 dias
faturamento_diario = [0, 1200, 2500, 0, 0, 3000, 3400, 0, 500, 800, 1000, 0, 2000, 1500, 0]  # Exemplo pequeno para fins de teste

# a) Encontrar o menor e o maior valor de faturamento, desconsiderando os dias sem faturamento (0)
faturamento_valido = [f for f in faturamento_diario if f > 0]  # Ignorando dias sem faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# b) Calcular a média anual de faturamento, ignorando os dias sem faturamento
media_anual = sum(faturamento_valido) / len(faturamento_valido)

# c) Número de dias com faturamento acima da média anual
dias_acima_da_media = sum(1 for f in faturamento_valido if f > media_anual)

# Exibir resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento}")
print(f"Maior valor de faturamento: R$ {maior_faturamento}")
print(f"Número de dias com faturamento acima da média anual: {dias_acima_da_media}")

# ----------------------
# Complexidade e Explicação:
#
# O algoritmo realiza três etapas principais:
#
# 1. Filtrar os dias com faturamento > 0:
#    Esta etapa cria uma nova lista com os dias válidos (desconsiderando faturamento zero). A complexidade dessa operação é O(n),
#    onde 'n' é o número total de elementos no vetor (n = 365 dias, no caso mais comum).
#
# 2. Encontrar o menor e o maior valor no vetor filtrado:
#    As funções min() e max() percorrem a lista uma vez cada, ambas com complexidade O(m), onde 'm' é o número de dias válidos
#    (aqueles com faturamento > 0). No pior caso, 'm' pode ser igual a 'n', mas no geral, 'm' <= 'n'.
#
# 3. Calcular a média e contar os dias com faturamento acima da média:
#    A função sum() para calcular a média percorre a lista uma vez (O(m)), e depois usamos outra iteração para contar os dias
#    com faturamento acima da média, o que também é O(m).
#
# Como todas as operações principais envolvem percorrer o vetor no máximo três vezes, a complexidade total do algoritmo é O(n),
# sendo 'n' o tamanho total do vetor (365 dias). Este é o algoritmo mais eficiente possível, já que precisamos analisar todos os elementos 
# do vetor pelo menos uma vez para determinar o menor, maior e dias acima da média.
