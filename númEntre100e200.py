# Esse código mostra quantos números entre 100 e 200 foram digitados
entre100e200 = []
for i in range(0, 10):
    valor = int(input('({i}) Digite um número'))
    if valor > 100 or valor < 200:
        entre100e200.append(valor)
print('Foram digitados |{}| valores entre 100 e 200, sendo eles {}'.format(len(entre100e200), entre100e200))






