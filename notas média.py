n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print('{}REPROVADO'.format('\033[31m'))
elif media >= 5.0 and media < 7.0:
    print('{}RECUPERAÇÃO'.format('\033[33m'))
else:
    print('{}APROVADO'.format('\033[34m'))