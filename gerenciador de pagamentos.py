valor = float(input('Digite o valor: '))
print('Escolha a forma de pagamento:\n À vista dinheiro :1\n À vista no cartão :2\n 2x no cartão :3\n 3x ou mais no cartão :4')
op = int(input('Sua opção: '))

if op == 1:
    preco = valor - (valor * 0.10)
    print('Será cobrado R${} reais'.format(preco))
elif op == 2:
    preco = valor - (valor * 0.05)
    print('Será cobrado R${} reais'.format(preco))
elif op == 3:
    total = valor / 2
    print('Serão duas parcelas de R${:.2f} reais'.format(total))
    print('Será cobrado o preço normal de R${} reais'.format(valor))
elif op == 4:
    parcela = int(input('Quantas parcelas? '))
    preco = valor + (valor * 0.20)
    parcelado = preco / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} reais com juros'.format(parcela,parcelado))
    print('Será cobrado R${:.2f} reais'.format(preco))
else:
    print('Opção inválida. Tente novamente')