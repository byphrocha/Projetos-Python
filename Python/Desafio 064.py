n = 0
c = 0
s = 0
n = int(input('Digite outro valor:'))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite outro valor:'))
print('Foram digitados {} e a soma entre eles será: {}'.format(c, s))