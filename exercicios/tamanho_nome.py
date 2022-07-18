nome = input('Informe seu nome: ')

numCaracteres = len(nome)

if numCaracteres <= 4:
    print('Seu nome é curto')
elif numCaracteres <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')