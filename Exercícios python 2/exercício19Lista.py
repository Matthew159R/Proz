votos = []

Windows = 0
Unix = 0
Linux = 0
Netware = 0
MacOs = 0
Outro = 0
total = 0

print('Abaixo digite qual o melhor sistema operacional para servidor')
print('1.Windows Server / 2.Unix / 3. Linux / 4.Netware / 5.Mac Os / 6.Outro')

while True:
    voto = int(input('Digite'))

    if voto == 0:
        print('Programa encerrado')
        break

    if voto < 1 or voto > 6:
        print('Voto inválido. Digite novamente.')
        continue

    votos.append(voto)

def calculoPercetual (qtdVotos):
    percentual = ((qtdVotos * 100) / len(votos))
    return percentual

for i in range(len(votos)):
    if votos[i] == 1:
        Windows += 1
        total += 1
    elif votos[i] == 2:
        Unix += 1
        total += 1
    elif votos[i] == 3:
        Linux += 1
        total += 1
    elif votos[i] == 4:
        Netware += 1
        total += 1
    elif votos[i] == 5:
        MacOs += 1
        total += 1
    elif votos[i] == 6:
        Outro += 1
        total += 1

percentualW = calculoPercetual(Windows)
percentualU = calculoPercetual(Unix)
percentualN = calculoPercetual(Netware)
percentualL = calculoPercetual(Linux)
percentualM = calculoPercetual(MacOs)
percentualO = calculoPercetual(Outro)


print('Sistema Operacional     Votos   %')
print('-------------------     -----   ---')
print(f'Windows Server           {Windows}   {percentualW:.1f}%')
print(f'Unix                     {Unix}   {percentualU:.1f}%')
print(f'Linux                    {Linux}   {percentualL:.1f}%')
print(f'Netware                  {Netware}   {percentualN:.1f}%')
print(f'Mac Os                   {MacOs}   {percentualM:.1f}%')
print(f'Outro                    {Outro}   {percentualO:.1f}%')
print('-------------------     -----')
print(f'Total                    {total}')