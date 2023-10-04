maior = 0
menor = 0
for p in range(1, 6):
    n = float(input('Digite o peso da {}ª:'.format(p)))
    if p == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('O menor peso foi o {} e o maior peso foi o {}'.format(menor, maior))

