nasc = int(input('Digite o seu ano de seu nascimento:'))
idade = 2022 - nasc
if idade > 18:
    print('Você já deveria ter se alistado à {} ano(s)!!'.format(idade - 18))
elif idade < 18:
    print('Você ainda vai se alistar daqui à {} ano(s)'.format(18 - idade))
else:
    print ('Você deve se alistar!!')
