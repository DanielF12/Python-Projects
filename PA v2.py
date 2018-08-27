inicial = int(input('Digite o valor inicial da PA: '))
razao = int(input('Digite a razão: '))

x = inicial
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(x), end='')
        x = x + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quer ver mais alguns termos? Se sim, quantos? '))
print('Operação finalizada. Foram mostrados {} termos.'.format(total))

