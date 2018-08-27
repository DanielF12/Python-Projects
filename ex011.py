distancia = float(input('Digite a distância em metros: '))
km = distancia/1000
hm = distancia/100
dam = distancia/10
cm = distancia * 100
mm = distancia * 1000

print('{}km\n{}hm\n{}dam\n{:.0f}cm\n{:.0f}mm'.format(km,hm,dam,cm,mm))