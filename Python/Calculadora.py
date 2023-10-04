while True:
    print('Calculadora usando Python:\n'
'Escolha uma função\n '
      '(1) Adição'
      '(2) Subtração'
      '(3) Divisão'
      '(4) Multiplicação')
    p = int(input('Digite o numero da função:'))
    if p == 1:
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite outro numero:'))
        print('A adição sera {} '.format(n1 + n2))
    elif p == 2:
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite outro número:'))
        print('A Subtração dos dois números dará o resultado {}'.format(n1-n2))
    elif p == 3:
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite outro número:'))
        print('A Divisão desses dois números dará {}'.format(n1/n2))
    elif p == 4:
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite outro número:'))
        print('A multiplicação desses dois números dará {}'.format(n1*n2))
    else:
        print('Opção errada por favor insira novamente:')
    opcao = (input('Deseja reiniciar a calculadora(Sim/Não)'))
    if opcao.lower() != 'sim':
        break








