from random import randint
a = randint(1, 2)
n = str(input('Digite se quer PAR ou IMPAR:')).upper()
while True:
    if False:
        break
    if n == 'PAR':
        n = int(input('Digite seu numero:'))
        s = a + n
        if s % 2 == 0:
            print(f'Parabens vc ganhou {a}, {s}')
    else:
        n = int(input('Digite seu número:'))
        s = a + n
        if s % 2 != 0:
            print(f'Parabens vc ganhou {a}, {s}')











