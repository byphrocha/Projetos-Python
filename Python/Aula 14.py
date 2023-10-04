n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de pares foram {} o calculo é {} e de impares foi {} e o calculo é {}'.format(par, par + n, impar, impar + n))
