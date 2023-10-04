somidade = 0
HV = 0
nomeHV = ''
qtdmH20 = 0
for p in range(1,5):
    print('-=-=-= {}ª pessoa -=-=-='.format(p))
    nome = str(input('Digite o seu nome:')).strip()
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Qual o seu sexo ?[M/F]')).strip()
    somidade += idade
    if p == 1 and sexo in 'Mm':
        HV = idade
        nomeHV = nome
    elif sexo in 'Mm' and idade > HV:
        HV = idade
        nomeHV = nome
    elif sexo in 'Ff' and idade < 20:
        qtdmH20 += 1

m = somidade / 4
print(m)
print('O homem mais velho é o {} com {} '.format(nomeHV, HV))
print('{} mulheres tem menos de 20 anos!'.format(qtdmH20))
