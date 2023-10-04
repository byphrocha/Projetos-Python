totmaior = 0
totmenor = 0
for p in range(1,8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(p)))
    if 2022 - n >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(' No total tivemos {} maiores e {} menores'.format(totmaior, totmenor))