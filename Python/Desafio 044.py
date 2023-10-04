pnormal = float(input('Digite o valor do produto sem acrescimos:'))
print('''FORMAS DE PAGAMENTO:
      [1] : Pagamento à vista(dinheiro/cheque)
      [2] : Pagamento no cartão à vista
      [3] : Pagamento até 2x no cartão
      [4] : Pagamento 3x ou mais no cartão''')
pagamento = int(input('Digite a forma de pagamento:'))
if pagamento == 1:
    total = pnormal - (pnormal * 10 / 100)
elif pagamento == 2:
    total = pnormal - (pnormal * 5 / 100)
elif pagamento ==3:
    total = pnormal
elif pagamento == 4:
    qtdp = int(input('Digite a quantidade de parcelas:'))
    total = pnormal + (pnormal * 20 / 100)
    parcela = total / qtdp
    print('A sua compra custará {} e cada parcela sairá por {}'.format(total, parcela))
else:
    total = pnormal
    print('\033[1:31m FORMA DE PAGAMENTO INVALIDA!!\033[m')

print('O total será de {}'.format(total))


