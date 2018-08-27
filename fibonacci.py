n = int(input('Digite um número: '))

cont = 0
anterior = 1
atual = 0

while cont != n:
    print('{} -> '.format(atual), end='')
    atual = atual + anterior
    anterior = atual - anterior
    cont = cont + 1



