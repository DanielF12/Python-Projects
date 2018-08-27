frase = 'Curso em Vídeo Python'
print(frase[2::2])
print(frase[::-1])
print(frase.count('o'))
print(len(frase))
frase = frase.replace('Python','Descubra')
print(frase)
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.upper().count('U'))
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[0][2])
print('\n')
print("""Bem vindo ao python, use essas três aspas no começo e se for um texto muito grande,
para usar em tópico, ou algo assim, é só colocar as três aspas no começo e terminar com elas no
fim""")