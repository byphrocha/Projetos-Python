maior = 0
menor = 0
lista = []
for v in range(0,5):
    lista.append(int(input('Digite um valor:')))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        elif lista[v] < menor:
            menor = lista[v]
print(f'O maior numero será o {maior} e o menor numero sera o {menor}, e a lista é a {lista} ')
for c, i in enumerate(lista):
    if i == maior:
        print(f'O maior numero está na posição {c}')
for c, i in enumerate(lista):
    if i == menor:
        print(f'O menor numero está na posição {c}')
