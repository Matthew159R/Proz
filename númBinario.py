# Esse algoritmo lê 8 números binários linha por linha e mostra o valor em decimal
print('==--------------------------------------==')
print('Digite abaixo o nº binário linha por linha')
print('==---------------------------------------==')
print('Obs: Só digite números binários')
numBinario = []
for i in range(0, 8):
    number = int(input('[|Digite|]'))
    numBinario.append(number)
decimal = pow(numBinario[7] * 2, 0) + pow(numBinario[6] * 2, 1) + pow(numBinario[5] * 2, 2) + pow(numBinario[4] * 2, 3) + pow(numBinario[3] * 2, 4) + pow(numBinario[2] * 2, 5) + pow(numBinario[1] * 2, 6) + pow(numBinario[0] * 2, 7)
if numBinario[-1] == 0:
    print('O número decimal é: {}'.format(decimal - 1))
else:
    print('O número decimal é: {}'.format(decimal))

