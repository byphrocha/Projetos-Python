nome = str(input('Qual é o seu nome ?'))
if nome == 'Gustavo':
    print('Puta nome feio')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome')
print('Tenha um bom dia, {}!'.format(nome))
