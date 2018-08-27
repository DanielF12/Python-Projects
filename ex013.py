from math import pow,sqrt

op = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))

hip = pow(op,2) + pow(adj,2)
print('A hipotenusa desse triângulo vale: {:.2f}'.format(sqrt(hip)))