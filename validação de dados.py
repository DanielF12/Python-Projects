sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo [M] / [F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Inválido. Digite novamente[M] / [F]: ')
print('Sexo {} registrado com sucesso.'.format(sexo))