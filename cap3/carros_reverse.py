#Exibindo uma lista em ordem inversa permanente com o método reverse()

carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros)
carros.reverse()
print(carros)

#Note que ele não muda a ordem alfabética e sim a ordem que foi passada na lista 
# original

#para voltar a lista ao normal aplicamos novamente o método reverse()

carros.reverse()
print(f'Retornando a lista ao normal: {carros}')