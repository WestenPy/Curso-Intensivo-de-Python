#Ordenando uma lista temporariamente com a função sorted()

carros = ['bmw', 'audi', 'toyota', 'subaru']
print(f'Aqui está a lista original: {carros}')
print(f'Aqui está a lista ordenada: {sorted(carros)}')
print(f'Aqui está a lista original novamente: {carros}')

#Aqui também podemos utilizar o comando 'reverse=True' como segundo argumento,
#para ordenar inversamente a lista.

print(f'\nAqui a lista invertida: {sorted(carros, reverse=True)}')