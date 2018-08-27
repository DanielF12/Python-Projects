from datetime import datetime

now = datetime.now()
cont = 0
cont2 = 0
for c in range(1,8):
    ano = int(input('({}) - Digite seu ano de nascimento: '.format(c)))
    maioridade = now.year - ano
    if (maioridade >= 21):
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print('{}Quantidade de pessoas na maioridade: {}'.format('\033[34m', cont))
print('{}Quantidade de pessoas que NÃO estão na maioridade: {}'.format('\033[31m',cont2))