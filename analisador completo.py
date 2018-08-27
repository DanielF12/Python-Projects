soma = 0
cont = 0
cont2 = 0
maioridhomem = 0
nomevelho = ''

for c in range(1,6):
    nome = str(input('({}) - Digite seu nome: '.format(c)))
    idade = int(input('({}) - Digite sua idade: '.format(c)))
    sexo = str(input('({}) - Digite seu Sexo: [F] [M]: '.format(c))).strip().upper()
    soma += idade
    if c == 1 and sexo == 'M':
        maioridhomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridhomem:
            maioridhomem = idade
            nomevelho = nome
    if idade < 20 and sexo == 'F':
            cont2 = cont2 + 1

media = soma/4
print('A média de idade do grupo é: {}'.format(media))
print('A maior idade masculina é do {} que possui {} anos'.format(nomevelho,maioridhomem))
print('Tem {} mulhere(s) menores de 20 anos'.format(cont2))

