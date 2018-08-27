from math import radians, sin,cos,tan

angulo = float(input('Digite um ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Seno = {:.2f} cosseno = {:.2f} = tangente = {:.2f}'.format(seno,cosseno,tangente))

