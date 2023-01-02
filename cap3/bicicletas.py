bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)
print()
#extrair a primeira bicicleta da lista
print(bicicletas[0])
print()
#formatando o elemento com o método title
print(bicicletas[0].title())
print()
#mostrando as bicicletas no índice 1 e 3
print(bicicletas[1])
print(bicicletas[3])
print()
#outra forma de acessar o último item da lista
print(bicicletas[-1])
print()
#Obter a primeira bicicleta da lista e compor uma mensagem usando esse valor
print('Minha primeira bicicleta foi uma ' + bicicletas[0].title() + '.')