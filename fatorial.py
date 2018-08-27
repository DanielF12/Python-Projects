##fat = num = int(input('Digite um número: '))

##if num == 1 or num == 0:
  ##  print('Fatorial de {} = 1'.format(num))
##else:
  ##  for c in range(1,num):
    ##    num = c * num
##print('{}! = {}'.format(fat,num))'''

numero = int(input('Digite um número: '))
numeroinicial = numero
fator = 1

if numero == 0:
    print('{}! = 1'.format(numero))

else:
    while numero >= 1:
        fator = numero * fator
        numero = numero - 1
    print('{}! = {}'.format(numeroinicial, fator))