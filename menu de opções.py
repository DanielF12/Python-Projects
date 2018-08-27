n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

maior = 0
menor = 0
op = 0

while op != 5:
    print(' [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa \n')
    op = int(input('Digite uma opção: '))
    if op == 1:
        soma = n1 + n2
        print('Soma entre {} e {} = {}'.format(n1,n2,soma))
    elif op == 2:
        multiplicacao = n1 * n2
        print('Multiplicação entre {} e {} = {}'.format(n1,n2,multiplicacao))
    elif op == 3:
        if n1 == n2:
            print('Não tem maior! São iguais')
        elif n1 > n2:
            maior = n1
            print('O maior é {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior é {}'.format(maior))
    elif op == 4:
        n1 = float(input('Digite um novo número: '))
        n2 = float(input('Digite outro novo número: '))
    elif op == 5:
        print('Programa finalizado.')
    else:
        print('{}Opção inválida. Tente novamente{}'.format('\033[31m','\033[m'))