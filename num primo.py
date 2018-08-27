num = int(input('Digite um número: '))
cont = 0

for c in range(1,num+1):
    if(num % c != 0):
        print('{}{}{}'.format('\033[31m',c,'\033[m'))
    else:
        print('{}{}{}'.format('\033[34m',c,'\033[m'))
        cont = cont + 1
print('Número de divisores: {}'.format(cont))
if (cont > 2):
    print('{} NÃO É PRIMO'.format(num))
else:
    print('{} É PRIMO'.format(num))