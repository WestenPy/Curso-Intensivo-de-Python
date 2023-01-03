#3.6 Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço
#disponível. Pense em mais três convidados para o jantar.
#-Comece com seu programa do exercício 3.4 ou 3.5. Acrescente uma intrução print
#no final do seu programa informando às pessoas que você encontrou uma mesa
#de jantar maior
#-Utilize insert() para adicionar um novo convidado no inicio da lista.
#-Utilize insert() para adicionar um novo convidado no meio da lista.
#Utilize append() para adicionar um novo convidado no final da lista.
#-Exiba um novo conjunto de mensgens de convite, uma para cada pessoa que está
#em sua lista.

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


