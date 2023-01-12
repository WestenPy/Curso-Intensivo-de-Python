#4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
#laço for para exibir os números. (Se a saída estiver demorando demais,
#interrompa pressionando CTRL-C ou feche a janela de saída.)

numero = []
for valor in range(1, 1000000):
    numero.append(valor)
print(numero)
print()

#usando list comprehensions

numero = [valor for valor in range(1, 1000000)]
print(numero)