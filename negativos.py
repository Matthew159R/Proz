# Mostra quantos e quais números negativos foram digitados
negativos = []
for i in range(0, 5):
    valor = int(input('Digite'))
    if valor < 0:
        negativos.append(valor)
if len(negativos) == 1:
    print('Foi digitado apenas 1 valor, sendo ele {}'.format(negativos))
else:
    print(f'Foram digitados {len(negativos)} valores negativos, sendo eles: {negativos}')







