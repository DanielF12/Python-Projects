vel = float(input('Digite a velocidade: '))

if(vel > 80):
    print('{}Acima da velocidade! Você será multado'.format('\033[31m'))
    multa = 7 * (vel - 80)
    print('Você foi multado no valor de: R${:.1f} reais'.format(multa))
else:
    print('{}Tudo certo, você NÃO será multado'.format('\033[34m'))