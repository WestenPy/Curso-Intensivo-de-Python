#4.1 – Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os
#nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
#pizza.

pizzas = ['calabresa', 'portuguesa', 'frango', 'bacon']
for pizza in pizzas:
    print(pizza)

#• Modifique seu laço for para mostrar uma frase usando o nome da pizza em
#vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha
#na saída contendo uma frase simples como Gosto de pizza de pepperoni.

pizzas = ['calabresa', 'portuguesa', 'frango', 'bacon']
for pizza in pizzas:
    print(f'\nEu gosto muito de pizza de {pizza}!')

#• Acrescente uma linha no final de seu programa, fora do laço for, que informe
#quanto você gosta de pizza. A saída deve ser constituída de três ou mais
#linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por
#exemplo, Eu realmente adoro pizza!

pizzas = ['calabresa', 'portuguesa', 'frango', 'bacon']
for pizza in pizzas:
    print(f'\nEu gosto muito de pizza de {pizza}!')
print()
print('Eu realmente sou aficcionado por pizzas!')