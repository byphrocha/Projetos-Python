n1 = float(input('Digite a nota do primeiro bim:'))
n2 = float(input('Digite a nota do segundo bim:'))
m = float(n1 + n2) / 2
if m < 5.0:
    print('REPROVADO!!')
elif m >= 5.0 and m < 7.0:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!!')

