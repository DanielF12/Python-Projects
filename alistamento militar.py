from datetime import datetime

ano = int(input('Digite o ano que você nasceu: '))

now = datetime.now()

idade = now.year - ano
tempo = 18 - idade
tempo2 = idade - 18

if idade < 18:
    print('Você ainda não precisa se alistar')
    print('Daqui a {} anos você precisará!'.format(tempo))
elif idade == 18:
    print('Está na hora de você se alistar!')
else:
    print('Já passaram {} ano(s) que você precisou se alistar!'.format(tempo2))