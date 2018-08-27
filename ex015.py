from random import choice

a1 = str(input('Digite um nome: '))
a2 = str(input('Digite um nome: '))
a3 = str(input('Digite um nome: '))
a4 = str(input('Digite um nome: '))

escolhido = choice([a1,a2,a3,a4])
print('O sorteado foi: {}'.format(escolhido))
