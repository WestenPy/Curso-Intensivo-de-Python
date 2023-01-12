#O exemplo a seguir cria uma lista de quadrados perfeitos que vimos antes, porém
#utiliza uma list comprehensions:

quadrados = [valor ** 2 for valor in range(1, 11)]
print(quadrados)
