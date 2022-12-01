i = 1
maior = 0
menor = 0
negativos = 0
while i != 0:
    valor = int(input('Digite o número'))
    if valor == 0:
        print(f'O maior foi {maior}, o menor foi {menor} e a soma dos negativos foram {negativos}')
        break
    elif valor < 0:
        negativos = valor + negativos
    elif valor > maior:
        maior = valor
        print(f'O maior é {valor}')
    else:
        menor = valor
        print(f'O menor é {menor}')

soma = 0
i = 1
qtdNum = int(input('Quantos dados de media?'))
for i in range(0, qtdNum):
    numbers = int(input('Digite um número'))
    if qtdNum == qtdNum:
        soma = soma + numbers
        media = soma / qtdNum
        print(media)
    