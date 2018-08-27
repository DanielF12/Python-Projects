nome = str(input('Digite seu nome completo: ')).strip()  #strip elimina os espaços no fim e inicio
print(nome.upper())
print(nome.lower())
print('Numero de caracteres sem espaço: {}'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print(separa)
print(separa[0])
print('{} possui {} letras'.format(separa[0],len(separa[0])))
