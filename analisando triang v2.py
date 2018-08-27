a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b):
    print('Pode constituir um triângulo ', end='')
    if a == b and a == c and b == c:
        print('EQUILATERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('{}NÃO se pode constituir um triângulo'.format('\033[31m'))
