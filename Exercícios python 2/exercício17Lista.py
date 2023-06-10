
saltos = []
nomeAtleta = ''
soma = 0

print('Abaixo, digite os últimos 5 saltos do atleta e seu nome')
i = 5
while i > -1:
    
    if i == 0:
        nome = input('Digite o nome do atleta  ')
        nomeAtleta = nome
        
    else:
        try:
            salto = float(input(f'Digite o {i}° salto  '))
            saltos.append(salto)
            soma += salto
        except ValueError:
            i += 1
            print('O nome do atleta deve ser colocado no final dos saltos')
    i -= 1   
     
media = soma / len(saltos)

print('------------------')
print(f'Atleta: {nomeAtleta}')
print(f'Primeiro salto: {saltos[0]} m')
print(f'Segundo salto: {saltos[1]} m')
print(f'Terceiro salto: {saltos[2]} m')
print(f'Quarto salto: {saltos[3]} m')
print(f'Quinta salto: {saltos[4]} m')
print('------------------')
print('Resultado final:')
print(f'Atleta: {nomeAtleta}')
print(f'Saltos {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]}')
print(f'Média dos saltos: {media}')
print('------------------')