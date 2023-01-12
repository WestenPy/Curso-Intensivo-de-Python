#4.3- Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os.
n = []
for valor in range(1, 21):
    n.append(valor)
print(n)
print()
    
#utilizando list comprehensions

numero = [valor for valor in range(1, 21)]
print(numero)
