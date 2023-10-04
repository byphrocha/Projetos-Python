n = s = c = 0
while True:
    n = int(input('Digite um número inteiro:'))
    c += 1
    if n == 999:
        break
    s += n
print(f'A quantidade de número digitados é {c} e a soma entre eles é {s}')


