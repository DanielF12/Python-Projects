dist = float(input('Digite a distância: '))

if(dist <= 200):
    preço = 0.50 * dist
    print('Sua viagem custará R${:.2f} reais'.format(preço))
else:
    preço = 0.45 * dist
    print('Sua viagem custará R${:.2f} reais'.format(preço))