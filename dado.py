#O algoritmo abaixo simula um dado sendo jogado para cima 100 vezes e mostra quantas vezes cada face foi sorteada.
lado1 = []
lado2 = []
lado3 = []
lado4 = []
lado5 = []
lado6 = []
import random
for i in range(0, 100):
    dado = random.randint(1, 6)
    match dado:
        case 1:
            lado1.append(dado)
        case 2:
            lado2.append(dado)
        case 3:
            lado3.append(dado)
        case 4: 
            lado4.append(dado)
        case 5: 
            lado5.append(dado)
        case 6: 
            lado6.append(dado)
print('===-----------------------===')
print('Resultado das jogadas do dado')
print('LADO 1 |{}|'.format(len(lado1)))
print('LADO 2 |{}|'.format(len(lado2)))
print('LADO 3 |{}|'.format(len(lado3)))
print('LADO 4 |{}|'.format(len(lado4)))
print('LADO 5 |{}|'.format(len(lado5)))
print('LADO 6 |{}|'.format(len(lado6)))
print('===========')







