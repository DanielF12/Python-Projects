num = int(input('Digite um número para converter: '))
print('Digite 1 para converter para biário\nDigite 2 para converter para octal\nDigite 3 para converter em hexadecimal')
x = int(input('Sua opção: '))

if x == 1:
    print('{} convertido para BINARIO: {}'.format(num,bin(num)[2:]))
elif x == 2:
    print('{} convertido para OCTAL: {}'.format(num,oct(num)[2:]))
elif x == 3:
    print('{} convertido para HEXADECIMAL: {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida! Tente 1, 2 ou 3')



