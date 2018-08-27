from random import randint

computador = randint(0,10)
cont = 0
print('O computador pensou em um número de 0 a 10 \n \t\t\t Tente advinhar!')
jogador = int(input('Digite sua aposta: '))
while computador != jogador:
    if jogador > computador:
        print('O número certo é menor que {}'.format(jogador))
    else:
        print('O número certo é maior que {}'.format(jogador))
    jogador = int(input('{}Tente novamente{}: '.format('\033[31m','\033[m')))
    cont = cont + 1
if computador == jogador:
    print('{}Parabéns! Você venceu'.format('\033[34m'))
    print('Você precisou de {} tentativa(s) para ganhar'.format(cont+1))

