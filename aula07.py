nome = input('Qual o seu nome?')
print('Prazer em conhecer você,{:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outr valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma vale {} \no produto vale {}\n a divisao vale {}\n'.format(s,m,d), end=' ')
print('a divisao inteira vale {} \na potencia vale {}'.format(di,e))