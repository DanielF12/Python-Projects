valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = float(input('Digite quantos anos: '))

prestacao = (valor / anos) / 12
custos = salario *0.30

print('Sua prestação: R${} reais.'.format(prestacao))
print('30% do seu salário: R${} reais.'.format(custos))

if(prestacao > custos):
    print('Infelizmente você não poderá comprar esta casa.')
else:
    print('Você poderá comprar sua casa!')