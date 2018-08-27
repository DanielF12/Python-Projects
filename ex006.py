numero = int(input('Digite o numero para saber sua tabuada: '))
print('Numero: {}\n'.format(numero))

for i in range(1,11):
    r = i * numero;
    print('{} * {} = {}'.format(numero,i,r));
