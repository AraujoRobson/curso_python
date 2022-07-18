hora = input('Informe a Hora: ')

try:
    hora = int(hora)
except:
    print('Numero inválido.')

if (hora >= 0) and (hora <= 11):
    print('Bom dia!')
elif hora <= 17:
    print('Boa tarde!')
elif hora <= 23:
    print('Boa noite!') 
else:
    print('Hora inválida')