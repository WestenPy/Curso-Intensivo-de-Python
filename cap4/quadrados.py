#modo como podemos colocar os dez primeiros quadrados perfeitos em uma lista: 
quadrados = []
for valor in range(1, 11):
    quadrado = valor**2
    quadrados.append(quadrado)
print(quadrados)
print()

#Para escrever esse código de modo mais conciso, omita a variável
#temporária square e concatene cada novo valor diretamente na lista:
quadrados = []
for valor in range(1, 11):
    quadrados.append(valor**2)
print(quadrados)
