i = 1
Upper = 0
Lower = 0
negativos = 0
while i != 0:
    valor = int(input('Digite um número'))
    if valor == 0:
        print(f'O maior foi {Upper}, o menor foi {Lower} e a soma dos negativos foram {negativos}')
        break
    elif valor < 0:
        negativos = valor + negativos
    elif valor > Upper:
        Upper = valor
        print(f'O maior é {valor}')
    else:
        Lower = valor
        print(f'O menor é {Lower}')
#Calcula qual foi o maior, menor e a soma de todos os negativos
#Basta digitar 0 para finalizar