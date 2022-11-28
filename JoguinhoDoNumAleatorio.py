import random
number = random.randint(1, 10)
print('----Esse é um joguinho de advinhar o número----')
print('Você terá que chutar um número aleatório e o algoritmo vai dizer se você acertou ou não')
digite = int(input('Chute um número...'))
if digite == number:
  print(f'Você acertou, parabéns!! O número era: {number}')
else:
  tentetiva = 0
while number != digite and tentetiva < 5:
  if number < digite:
      print(f'O número aleatório é menor que {digite}')
      digite = int(input('Digite o número:'))
      tentetiva = tentetiva + 1
  else:
      print(f'O número aleatório é maior que {digite}')
      digite = int(input('Digite novamente...'))
      tentetiva = tentetiva + 1
if digite != number:
  resposta = input('Deseja ver qual número era? [S] / [N]')
  if resposta == 'S':
    print('O número era {}'.format(number))
  elif resposta == 'N':
    print('Ok...')
  else:
    print('Caracter não idetificado. O número era: {}'.format(number))