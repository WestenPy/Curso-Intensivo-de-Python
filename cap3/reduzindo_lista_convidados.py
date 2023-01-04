#3.7 Você acaba de descobrir que a sua nova mesa de jantar não chegará a tempo para
#o jantar e tem espaço para somente dois convidados.
#-Comece o seu programa do exercício 3.6. Acrescente uma nova linha que mostre uma
#mensagem informando que pode convidar apenas duas pessoas para o jantar.
#-Utilize pop() para remover os convidados de sua lista. Sempre que remover um nome de sua lista,
#mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito
#por não poder convidá-la para o jantar.
#-Apresente uma mensagem para cada uma das duas pessoas que continuam na lista,
#permitindo que elas saibam que ainda estão convidadas.
#-Utilize del para remover os dois últimos nomes da sua lista, de modo que você
#tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
#uma lista vazia no final de seu programa.

pessoas = ['Lud', 'Vita', 'Jão', 'Bumba']

print(f'{pessoas[0]} gostaria de jantar comigo?\n')
print(f'{pessoas[1]} gostaria de jantar comigo?\n')
print(f'{pessoas[2]} gostaria de jantar comigo?\n')
print(f'{pessoas[3]} gostaria de jantar comigo?\n')

print('Encontrei uma mesa de jantar maior, assim posso convidar mais 3 pessoas')

pessoas.insert(0, 'Brendinha')
pessoas.insert(2, 'Ticia')
pessoas.append('Asmine')

print(f'{pessoas[0]} gostaria de jantar comigo?\n')
print(f'{pessoas[1]} gostaria de jantar comigo?\n')
print(f'{pessoas[2]} gostaria de jantar comigo?\n')
print(f'{pessoas[3]} gostaria de jantar comigo?\n')
print(f'{pessoas[4]} gostaria de jantar comigo?\n')
print(f'{pessoas[5]} gostaria de jantar comigo?\n')
print(f'{pessoas[6]} gostaria de jantar comigo?\n')

print('Infelizmente poderei convidar apenas duas pessoas para o jantar.')

primeiro = pessoas.pop(0)
print(f'\n{primeiro} sinto muito mas vou ter de cancelar o jantar.')
segundo = pessoas.pop(1)
print(f'\n{segundo} sinto muito mas vou ter de cancelar o jantar.')
terceiro = pessoas.pop(2)
print(f'\n{terceiro} sinto muito mas vou ter de cancelar o jantar.')
quarto = pessoas.pop(3)
print(f'\n{quarto} sinto muito mas vou ter de cancelar o jantar.')
quinto = pessoas.pop(0)
print(f'\n{quinto} sinto muito mas vou ter de cancelar o jantar.')

print(f'\n{pessoas[0]} apesar de todos os problemas ainda aguardo sua presença\n')
print(f'{pessoas[1]} apesar de todos os problemas ainda aguardo sua presença\n')

del pessoas[0]
del pessoas[0]
print(pessoas)