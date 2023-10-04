num1 = int(input('Escolha um numero:'))
num2 = int(input('Escolha outro valor:'))
menu = 0
while menu != 5:
    print('''[1] SOMAR 
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    menu = int(input('Escolha a sua função'))
    if menu == 1:
        print('A soma dará {}'.format(num1 + num2))
    elif menu == 2:
        print('O maior número será {}'.format(num1 * num2))
    elif menu == 3 and num1 > num2:
        print('O maior número é o {}'.format(num1))
    elif menu == 3 and num2 > num1:
         print(' O maior numero sera o {}'.format(num2))
    elif menu == 4:
        num1 = int(input('Digite um valor novamente:'))
        num2 = int(input('Digite o segundo valor novamente:'))
    elif menu == 5:
        print('Finalizando')
    else:
        print('Valor invalido! Tente novamente...')
print('Obrigado!')








