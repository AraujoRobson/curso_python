num1 = input("Informe um numero inteiro: ")

try:
    num1 = int(num1)
    valida = num1%2
    if valida == 0:
        print("Numero PAR.")
    else:
        print("Numero IMPAR.")
except:
    print('Não foi informado um número inteiro')