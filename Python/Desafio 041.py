ano = int(input('Digite o seu ano de nascimento:'))
idade = int(2022 - ano)
if idade >= 0 and idade <= 9:
    print('Você é da categoria MIRIM!')
elif idade > 9 and idade <= 14:
    print('Você é da categoria INFANTIL!')
elif idade > 14 and idade <= 18:
    print('Você é da categoria JUNIOR!')
elif idade > 18 and idade == 20:
    print('Você é da categoria SÊNIOR!')
else:
    print('Você é da MASTER!!')