#Percorrendo uma lista inteira com um laço for.

magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(magico)

#Executando mais tarefas em um laço for.

magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(f'\n{magico.title()}, foi um ótimo truque!')

#Podemos adicionar quantas instruções quisermos

magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(f'\n{magico.title()}, foi um ótimo truque!')
    print('Estamos ansiosos pelo seu próximo truque')

#Fazendo algo após um laço for

magicos = ['alice', 'david', 'carolina']
for magico in magicos:
    print(f'\n{magico.title()}, foi um ótimo truque!')
    print('Estamos ansiosos pelo seu próximo truque')

print('\nObrigado a todos. Este foi um grande show de mágica!')
