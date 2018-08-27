frase = str(input('Digite a frase: ')).strip().upper()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece primeiro na posição: {}'.format(frase.find('A')))
print('A última letra A aparece na posição: {}'.format(frase.rfind('A')))


