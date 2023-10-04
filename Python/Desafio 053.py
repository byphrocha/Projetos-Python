f = str(input('Digite a palavra:')) .strip().upper()
s = f . split()
junto = '' .join(s)
inverso = ''
for c in range (len(junto) -1, -1, -1):
    inverso += junto[c]
    if inverso == junto:
        print('A palavra é um palindromo')
    else:
        print('A palavra não é um palindromo')



