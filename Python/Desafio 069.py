t = tm = tf = 0
while True:
    idade = int(input('Digite a sua idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo(M/F):')).strip().upper()[0]
    if idade >= 18:
        t += 1
    if sexo == 'M':
        tm += 1
    if sexo == 'F' and idade < 20:
        tf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar:')).strip().upper()
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 é {t}')
print(f'O total de homens é {tm} e o total de mulher com mais de 20 é {tf}')

