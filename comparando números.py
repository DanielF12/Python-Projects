v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if v1 > v2:
    print('Entre {} e {} O primeiro valor é maior: {}'.format(v1,v2,v1))
elif v2 > v1:
    print('Entre {} e {} O segundo valor é maior: {}'.format(v1, v2,v2))
else:
    print('Não existe valor maior, {} e {} são iguais'.format(v1,v2))