ano = int(input('Digite o ano: '))

if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('{}{}{} é ano bissexto'.format('\033[34m',ano,'\033[m'))
else:
    print('{}{}{} NÃO é bissexto'.format('\033[31m',ano,'\033[m'))
