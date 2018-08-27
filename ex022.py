import random

x = random.randint(1,5)

numero = int(input('Digite um número: '))

if(numero == x):
    print('{}Parabéns! Você venceu! Ele tinha pensando em {} mesmo!'.format('\033[34m',x))
else:
    print('{}O computador venceu,ele pensou em {}, tente novamente!'.format('\033[31m',x))
