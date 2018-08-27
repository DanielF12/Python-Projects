soma = 0
cont = 0
for c in range(1,500):
    if(c % 2 != 0):
        if(c % 3 == 0):
             soma += c
             cont = cont + 1
print('SOMA dos {}: {}'.format(cont, soma))
