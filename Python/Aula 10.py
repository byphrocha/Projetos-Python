from random import choice
list = [1, 2, 3, 4, 5]
choice = choice(list)
Escolha = int(input('Tente adivinhar o numero'))
if Escolha == choice:
    print('Parabens você acertou')
else:
    print('Infelizmente você errou o número era {}'.format(choice))

