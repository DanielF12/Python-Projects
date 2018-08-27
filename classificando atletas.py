from datetime import datetime

ano = int(input('Digite o ano que você nasceu: '))

now = datetime.now()

idade = now.year - ano
print('{} anos'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')