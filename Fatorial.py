numero = int(input('Digite o número que deseja calcular o fatorial'))
fatorial = 1
while numero > 1:
    fatorial = fatorial * numero                                      
    numero = numero - 1
print('O fatorial é {}'.format(fatorial))
