a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if(abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b):
    print('Podem formar triângulo!')
else:
    print('Não podem formar triângulo')