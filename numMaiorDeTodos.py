print('----------------------------------------------------------------------')
print('O algoritmo abaixo vai lhe dizer quais dos números digitados é o maior')
print('----------------------------------------------------------------------')
numeroMaior = 0
count = 1
while count != 0:
    numberDigitado = int(input('Digite um número'))
    if numberDigitado  == 0:
        break
    elif numberDigitado > numeroMaior:
        numeroMaior = numberDigitado
        print('Até agora {} é o maior'.format(numeroMaior))
    elif numberDigitado < numeroMaior:
        print('{} é menor que {}'.format(numberDigitado, numeroMaior))
    elif numberDigitado == numeroMaior:
        print('{} é igual a {}'.format(numberDigitado, numeroMaior))
        count = count + 1