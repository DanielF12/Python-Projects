from random import randint

print("Pedra - 0\n Papel - 1\n Tesoura - 2")
jogador = int(input('Escolha pedra, papel ou tesoura: '))

opcoes = ('Pedra','Papel', 'Tesoura')
computador = randint(0,2)

print('Sua jogada: {}'.format(opcoes[jogador]))
print('Jogada do computador: {}'.format(opcoes[computador]))

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('{}COMPUTADOR VENCEU'.format('\033[31m'))
    elif jogador == 2:
        print('{}COMPUTADOR VENCEU'.format('\033[31m'))
    else:
        print('Opção inválida. Tente novamente')
elif computador == 1:
    if jogador == 0:
        print('{}VOCÊ VENCEU!'.format('\033[34m'))
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('{}VOCÊ VENCEU!'.format('\033[34m'))
    else:
        print('Opção inválida. Tente novamente')
else:
    if jogador == 0:
        print('{}VOCÊ VENCEU!'.format('\033[34m'))
    elif jogador == 1:
        print('{}COMPUTADOR VENCEU'.format('\033[31m'))
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção inválida. Tente novamente')