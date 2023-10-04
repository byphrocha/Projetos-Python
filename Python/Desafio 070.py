t = p = 0
while True:
    nome = str(input('Digite o nome do produto:'))
    preço = int(input('Digite o preço do produto:'))
    t+= 1
    preçot = t + preço
    if preço > 1000:
        p += 1




    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
            break

