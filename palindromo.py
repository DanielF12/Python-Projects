frase = str(input('Digite uma frase: ')).upper().replace(" ", "")

print('Sua frase: {}'.format(frase))
print('Frase inversa: {}'.format(frase[::-1]))
if frase == (frase[::-1]):
    print('{}É PALÍNDROMO'.format('\033[34m'))
else:
    print('{}NÃO É PALÍNDROMO'.format('\033[31m'))