cont = 0
n = 0
soma = 0
n = int(input('[{}] Digite um valor: '.format(cont)))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('[{}] Digite um valor: '.format(cont)))
print('A soma dos {} números é: {}'.format(cont,soma))
