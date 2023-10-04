from random import randint
n = randint(0,10)
attempts = 1
choice = int(input('Digite um numero de 0 a 10:'))
while choice != n:
    attempts += 1
    choice = int(input('Digite outro numero!'))
    if choice == n:
        print('Parabens você acertou')
print('O numero sorteado foi o {} e você acertou em {} tentativas!'.format(n, attempts))
      