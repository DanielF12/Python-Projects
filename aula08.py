from math import sqrt          #poderia ser import math
num = int(input('Digite um numero: '))
raiz = sqrt(num)   #com import math, teria que ser math.sqrt(num)

print('A raiz de {} = {:.2f}'.format(num,raiz))
