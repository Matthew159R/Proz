i = 0
qtdDados = int(input('Qual a quantidade de dados precisa calcular?'))
valores = []
for i in range(0, qtdDados):
    dados = int(input('Digite um dado...'))
    valores.append(dados)
media = sum(valores) / len(valores)
tipo = input('Que que o dado tenha casas decimais? [S] / [N]')
if tipo == 'S' or tipo == 's':
    print('A média é {}'.format(media))
else:
    print(f'A media é {int(media)}')


