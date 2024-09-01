from functools import reduce

# Lista de secuencias de ADN
secuencias_adn = ["ATCGATCGA", "GGTACGTA", "CAGTTGCA", "GCGCGCGCGC", "AATTCCGG", "TTAAACCGG", "GGATCGATCG"]

# 1. Calcular el porcentaje del nucleótido 'A' en cada secuencia
porcentajes_a = list(map(lambda secuencia: f"{(secuencia.count('A') / len(secuencia)) * 100:.2f}%", secuencias_adn))

# 2. Filtrar las secuencias que tengan un porcentaje de 'A' mayor al 25%
secuencias_filtradas = list(filter(lambda secuencia: (secuencia.count('A') / len(secuencia)) * 100 > 25, secuencias_adn))

# 3. Concatenar las secuencias filtradas y contar su longitud total
secuencia_concatenada = reduce(lambda x, y: x + y, secuencias_filtradas)
longitud_total = len(secuencia_concatenada)

# Resultados
print("Porcentajes de 'A' en cada secuencia:", porcentajes_a)
print("Secuencias filtradas:", secuencias_filtradas)
print("Secuencia concatenada:", secuencia_concatenada)
print("Longitud total de la secuencia concatenada:", longitud_total)
