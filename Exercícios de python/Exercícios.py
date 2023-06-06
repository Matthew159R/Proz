import math
import random
print('Esses são meus exercícios do site: https://wiki.python.org.br/ListaDeExercicios')
while True:
    escolha_De_Lista_Exercício = int(input('Qual lista de exercícios quer ver? [1]|Estrutura sequencial [2]|Estrutura de decisão [3]| Estrutura de repetição'))
    match escolha_De_Lista_Exercício:
        case 1:
            while True:
                escolha_De_Exercício = int(input('Qual exercício deseja ver? 1 até 18'))
                if escolha_De_Exercício < 1 or escolha_De_Exercício > 18:
                    print(f'O exercício {escolha_De_Exercício} não existe')
                match escolha_De_Exercício:
                    case 1:
                        print('1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.')
                        print('Alo mundo')
                    case 2:
                        print('2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]')
                        num = int(input('Digite um número'))
                        print(f'O número digitado foi {num}')
                    case 3:
                        print('3. Faça um Programa que peça dois números e imprima a soma.')
                        num1 = int(input('Digite o primeiro número'))
                        num2 = int(input('Digite o segundo número'))
                        print(f'A soma de {num1} com {num2} é {num1 + num2}')
                    case 4:
                        print('4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.')
                        nota1 = float(input('Digite a primeira nota: '))
                        nota2 = float(input('Digite a segunda nota: '))
                        nota3 = float(input('Digite a terceira nota: '))
                        nota4 = float(input('Digite a quarta nota: '))
                        media = (nota1 + nota2 + nota3 + nota4) / 4
                        print(f'A média é {media}')
                        #Abaixo esta o código escrito de uma forma mais avançada

                        quantidade = int(input('Quantos números você quer comparar?'))
                        soma = 0
                        for i in range(quantidade):
                            nota = float(input('Digite...'))
                            soma += nota
                        media = soma / quantidade
                        print(f'A média é {int(media)}')
                    case 5:
                        print('5. Faça um Programa que converta metros para centímetros.')
                        metros = float(input('Digite alguma medida em metros'))
                        centímetro = metros * 100
                        print(f'Em cm essa medida é {centímetro}cm')
                    case 6:
                        print('6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.')
                        raio = int(input('Digite o raio do círculo'))
                        pi = 3.14
                        area = pi * raio**2
                        perímetro = 2 * pi * raio
                        print(f'A área do círculo é {area} e o perímetro é {perímetro}')
                    case 7:
                        print('7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.')
                        lado = int(input('Informe a medida de um dos lados do quadrado'))
                        area = lado*lado
                        print(f'O dobro da area desse quadrado é {area*2} e o dobro do perímetro é {lado*4*2}')
                    case 8:
                        print('8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.')
                        salário_Hora = float(input('Quanto você ganha por hora?'))
                        horas_Trabalhadas = int(input('Quantas horas trabalhadas você tem esse mês?'))
                        salário = salário_Hora * horas_Trabalhadas
                        print(f'Seu salário esse mês é R${salário}')
                    case 9:
                        print('9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.')
                        temperatura_Fahrenheit = float(input('Informe a temperatura em graus fahrenheit'))
                        temperatura_Celsius = 5 * ((temperatura_Fahrenheit - 32) / 9)
                        print(f'{temperatura_Fahrenheit} em Celcius = {temperatura_Celsius:.2f}')
                    case 10:
                        print(f'10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.')
                        temperatura_Celsius = float(input('Informe a temperatuda em graus Celcius'))
                        temperatura_Fahrenheit = (temperatura_Celsius * 9 / 5) + 32
                        print(f'{temperatura_Celsius} em fahrenheit = {temperatura_Fahrenheit}')
                    case 11:
                        print('11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:')
                        print('A. o produto do dobro do primeiro com metade do segundo.')
                        print('B. a soma do triplo do primeiro com o terceiro.')
                        print('B. o terceiro elevado ao cubo.')
                        num1 = int(input('Digite o primeiro número'))
                        num2 = int(input('Digite o segundo número'))
                        num3 = float(input('Digite o terceiro número'))
                        print((num1 * 2) + (num2 / 2))
                        print(num1 * 3 + num3)
                        print(num3**3)
                    case 12:
                        print('12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58')
                        altura = float(input('Digite sua altura (h)'))
                        pesoIdeal = (72.7*altura) - 58
                        print(f'Seu peso ideal é {int(pesoIdeal)}Kg')
                    case 13:
                        print('13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:')
                        print('A. Para homens: (72.7*h) - 58')
                        print('B. Para mulheres: (62.1*h) - 44.7')
                        altura = float(input('Informe a sua altura (h)'))
                        sexo = input('Você é homen ou mulher?[h]/[m]')
                        if sexo == 'h':
                            print(f'Seu peso ideal é: {int((71.7*altura) - 58)}), senhor')
                        else:
                            print(f'Seu peso ideal é {int((62.1*altura) - 44.7)}')
                    case 14:
                        print('14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.')
                        peso = float(input('Coloque o peso'))
                        excesso = peso - 50
                        multa = excesso > 0
                        print(f'João o excesso foi {excesso}, caso a multa seja igual a True você terá que pagar 4 reais, caso seja igual a False, não.')
                        print(f'Multa = <{multa}>')
                    case 15:
                        print('15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:')

                        grana_Por_Hora = float(input('Quanto você ganha por hora?'))
                        horas_Trabalhadas = int(input('Quantas horas você trabalhou esse mês?'))
                        salário_Bruto = grana_Por_Hora * horas_Trabalhadas
                        IR = salário_Bruto * 11 / 100
                        INSS = salário_Bruto * 8 / 100
                        Sindicato = salário_Bruto * 5 / 100
                        salário_Líquido = salário_Bruto - IR - INSS - Sindicato
                        print(f'+ Salário bruto: R${salário_Bruto}')
                        print('--Descontos--')
                        print(f'- IR (11%): R${IR}')
                        print(f'- INSS (8%): R${INSS}')
                        print(f'- Sindicato (5%): R${Sindicato}')
                        print(f'Seu salário líquido é : R${salário_Líquido}')
                    case 16:
                        print('16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total')
                        tamanho = float(input('Informe o tamanho em M² da área a ser pintada'))
                        latas = tamanho / 54
                        preço = latas * 80
                        print(f'Será necessário {int(latas)} latas para pintar {tamanho}M².')
                        print(f'preço R${int(preço)}')
                    case 17:
                        print('wiouehfiuw3eg')
                    case 18:
                        print('18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).')
                        tamanho_Arquivo = float(input('Qual é o tamanho do arquivo em MB'))
                        Velocidade = float(input('Qual é a velocidade do link? Mbps'))
                        tempo = tamanho_Arquivo / Velocidade
                        if tempo >= 60:
                            tempo_Em_Minutos = int(tempo / 60)
                            if tempo_Em_Minutos == 1:
                                print(f'Aproximadamente <{tempo_Em_Minutos}> minuto')
                            else:
                                print(f'Aproximadamente <{tempo_Em_Minutos} minutos')
                        else:
                            print(f'Aproximadamente <{tempo} segundos>') 
                    

        case 2:    
            #Repetição dos exercícios de estrutura de decisão
            while True:
                escolha_De_Exercício = int(input('Qual exercício deseja ver? 1 até 28'))
                if escolha_De_Exercício < 1 or escolha_De_Exercício > 28:
                    print(f'O exercício {escolha_De_Exercício} não existe')
                match escolha_De_Exercício:
                    case 1:
                        print('1. Faça um Programa que peça dois números e imprima o maior deles.')
                        maior_Num_Exercício1 = 0
                        for i in range(0, 2):
                            num_Exercício_1 = int(input('Digite...'))
                            if num_Exercício_1 > maior_Num_Exercício1:
                                maior_Num_Exercício1 = num_Exercício_1
                        print(maior_Num_Exercício1)
                    case 2:
                        print('2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.')
                        num_Exercício_2 = int(input('Digite o número'))
                        if num_Exercício_2 < 0:
                            print('O número digitado é negativo')
                        else:
                            print('O número digitado é positivo')
                    case 3:
                        print('3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.')
                        sexo_Exercício1 = input('Digite o seu sexo [F]/[M]')
                        if sexo_Exercício1 == 'm' or sexo_Exercício1 == 'M':
                            print('Masculino')
                        elif sexo_Exercício1 == 'f' or sexo_Exercício1 == 'F':
                            print('Feminino')
                        else:
                            print('Sexo inválido')
                    case 4:
                        print('4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')
                        letra_exercício4 = input('Digite a letra')
                        if letra_exercício4 == 'a' or letra_exercício4 == 'e' or letra_exercício4 == 'i' or letra_exercício4 == 'o' or letra_exercício4 == 'u':
                            print('Vogal minúscola')
                        elif letra_exercício4 == 'A' or letra_exercício4 == 'E' or letra_exercício4 == 'I' or letra_exercício4 == 'O' or letra_exercício4 == 'U':
                            print('Vogal maiúscola')
                        elif letra_exercício4 == letra_exercício4.upper():
                            print('Consoante maiúscola')
                        else:
                            print('Consoante minúscola')
                    case 5:
                        print('5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez.')
                        nota1 = int(input('Digite a nota da primeira prova. Max. 10'))
                        nota2 = int(input('Digite a nota da segunda prova. Max. 10'))
                        media = (nota1 + nota2) / 2
                        if media >= 7:
                            print('Aprovado') 
                        elif media == 10:
                            print('Aprovado com distinção')   
                        else:
                            print('Reprovado')        
                    case 6:
                        print('6. Faça um Programa que leia três números e mostre o maior deles.')  
                        num_Maior_Ex6 = 0
                        for i in range(0, 3):
                            num_Exercício_6 = int(input('Digite...'))
                            if num_Exercício_6 > num_Maior_Ex6:
                                num_Maior_Ex6 = num_Exercício_6
                        print(f'O maior número digitado foi o: {num_Maior_Ex6}')
                    case 7:
                        print('7. Faça um Programa que leia três números e mostre o maior e o menor deles.')
                        num_Maior_Ex7 = 0
                        num_Menor_Ex7 = float('inf')
                        for i in range(0, 3):
                            num_Exercício_7 = int(input('Digite...'))
                            if num_Exercício_7 > num_Maior_Ex7:
                                num_Maior_Ex7 = num_Exercício_7
                            elif num_Exercício_7 < num_Menor_Ex7:
                                num_Menor_Ex7 = num_Exercício_7
                        print(f'O maior número digitado foi o: {num_Maior_Ex7} e o menor: {num_Menor_Ex7}')
                    case 8:
                        print('8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.')
                        celularApple = int(input('Qual o preço do celular da Apple?'))
                        celularSansung = int(input('Qual o preço so celular Sansung?'))
                        celularMotorola = int(input('Qual o preço so celular da Motorola'))
                        compra = 'Vou querer o '
                        if celularApple < celularSansung and celularApple < celularMotorola:
                            compra += 'celular da Apple'
                        elif celularSansung < celularApple and celularSansung < celularMotorola:
                            compra += 'celular da Sansung'
                        else:
                            compra += 'celular da Motorola'
                        print(compra)
                    case 9:     
                        num1 = int(input("Digite o primeiro número: "))
                        num2 = int(input("Digite o segundo número: "))
                        num3 = int(input("Digite o terceiro número: "))
                        if num1 > num2 and num1 > num3:
                            maior = num1
                        elif num2 > num1 and num2 > num3:
                            maior = num2
                        else:
                            maior = num3
                        if num1 < num2 and num1 < num3:
                            menor = num1
                        elif num2 < num1 and num2 < num3:
                            menor = num2
                        else:
                            menor = num3
                        print(maior)
                        if maior != num1 and menor != num1:
                            print(num1)
                        elif maior != num2 and menor != num2:
                            print(num2)
                        else:
                            print(num3)
                        print(menor)
                    case 10:
                        print('10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.')
                        horário = input('Em qual horário você estuda? M-matutino ou V-Vespertino ou N- Noturno.')
                        if horário == 'm' or horário == 'M':
                            print('Bom dia!')
                        elif horário == 'v' or horário == 'V':
                            print('Boa tarde!')
                        elif horário == 'n' or horário == 'N':
                            print('Boa noite!')
                        else:
                            print('Valor inválido')
                    case 11:
                        print('11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.')
                        print('Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:')
                        print('salários até R$ 280,00 (incluindo) : aumento de 20%')
                        print('salários entre R$ 280,00 e R$ 700,00 : aumento de 15%')
                        print('salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%')
                        print('salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:')
                        print('o salário antes do reajuste;')
                        print('o percentual de aumento aplicado;')
                        print('o valor do aumento;')
                        print('o novo salário, após o aumento.')
                        print(' ')
                        print(' ')
                        salário = float(input('Qual é o seu salário?'))
                        print(' ')
                        if salário <= 280:
                            percentual = 20
                            aumento = salário * percentual / 100
                            salário_Atual = aumento + salário 
                            print(f'Seu salário erá {280}. Foi aplicado um percentual de {percentual}%, R${aumento} de aumento. Agora seu salário é R${salário_Atual}')
                        elif salário > 280 and salário < 700:
                            percentual = 15
                            aumento = salário * percentual / 100
                            salário_Atual = aumento + salário 
                            print(f'Foi aplicado um aumento de {percentual}% R${aumento} de aumento. Agora seu salário é R${salário_Atual}')
                        elif salário >= 700 and salário < 1500:
                            percentual = 10
                            aumento = salário * percentual / 100
                            salário_Atual = aumento + salário 
                            print(f'Foi aplicado um aumento de {percentual}% R${aumento} de aumento. Agora seu salário é R${salário_Atual}')
                        elif salário >= 1500:
                            percentual = 15
                            aumento = salário * percentual / 100
                            salário_Atual = aumento + salário 
                            print(f'Foi aplicado um aumento de {percentual}% R${aumento} de aumento. Agora seu salário é R${salário_Atual}')
                    case 12:
                        print('12. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.')
                        dia = int(input('Digite o dia da semana'))
                        if dia == 1:
                            print('Domingo')
                        elif dia == 2:
                            print('Segunda')
                        elif dia == 3:
                            print('Terça')
                        elif dia == 4:
                            print('Quarta')
                        elif dia == 5:
                            print('Quinta')
                        elif dia == 6:
                            print('Sexta')
                        elif dia == 7:
                            print('Sábado')
                        else:
                            print('Valor inválido')
                    case 13:
                        print('13. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:')
                        print('  Média de Aproveitamento  Conceito')
                        print('Entre 9.0 e 10.0        A')
                        print('Entre 7.5 e 9.0         B')
                        print('Entre 6.0 e 7.5         C')
                        print('Entre 4.0 e 6.0         D')
                        print('Entre 4.0 e zero        E')
                        nota1 = float(input('Digite a primeira nota'))
                        nota2 = float(input('Digite a segunda nota'))
                        media = (nota1 + nota2) / 2
                        if media >= 9 and media <= 10:
                            print('A')
                            print('Aprovado!')
                        elif media >= 7.5 and media < 9:
                            print('B')
                            print('Aprovado!')
                        elif media >= 6 and media < 7.5:
                            print('C')
                            print('Aprovado!')
                        elif media >= 4 and media < 6:
                            print('D')
                            print('Reprovado')
                        else:
                            print('E')
                            print('Reprovado')
                    case 14:
                        lado1 = float(input('Digite o primeiro lado'))
                        lado2 = float(input('Digite o segundo lado'))
                        lado3 = float(input('Digite o terceiro lado'))
                        if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
                            if lado1 == lado2 == lado3:
                                print('Triângulo equilátero')
                            elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
                                print('Triângulo isósceles')
                            elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
                                print('Trângulo escaleno')
                        else:
                            print('Os valores digitados não formam um triângulo')
                    case 16:
                        print('15. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:')
                        print('a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;')
                        print('b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;')
                        print('c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;')
                        print('d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;')
                        a = int(input('Informe o valor de A: '))
                        if a == 0:
                            print('A equação não é do segundo grau')
                        else:
                            b = int(input('Informe o valor de B: '))
                            c = int(input('Informe o valor de C: '))
                            delta = b**2 - 4*a*c
                            if delta < 0:
                                print('A equação não possui raizes reais')
                            elif delta == 0:
                                x1 = (-b + math.sqrt(delta)) / (2 * a)
                                print('A equação possui apenas uma raiz real:', x1)
                            else:
                                x1 = (-b + math.sqrt(delta)) / (2 * a)
                                x2 = (-b - math.sqrt(delta)) / (2 * a)
                                print('A equação possui duas raízes reais:', x1, 'e', x2)
                    case 17:
                        print('17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.')
                        ano = int(input('Digite um ano'))
                        if ano % 4 == 0:
                            print(f'{ano} é um ano bissexto')
                        else:
                            print(f'{ano} não é um ano bissexto')
                    case 18:
                        print('18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.')
                        dia = int(input('Digite o dia'))
                        mês = int(input('Digite o mês'))
                        ano = input('Digite o ano')
                        if dia > 31:
                            print('Data inválida')
                        elif mês > 12:
                            print('Data inválida')
                        elif len(ano) == 4:
                            print(f'{dia}/{mês}/{int(ano)}')
                        else:
                            print('Data inválida')
                    case 19:
                        print('19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.')
                        number = int(input('Digite um número menor do que 1000'))
                        if number >= 1000:
                            print('Digite um número menor do que 1000...')
                        else:
                            centena = int(number / 100)
                            dezenas = int(number / 10)
                            unidade = number % 10
                            print(f'Centenas: {centena}')
                            print(f'Dezenas: {dezenas}')
                            print(f'Unidades: {unidade}')
                    case 20:
                        print('20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:')
                        print('A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;')
                        print(' A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;')
                        print('A mensagem "Aprovado com Distinção", se a média for igual a 10.')
                        nota1 = int(input('Digite a primeira nota'))
                        nota2 = int(input('Digite a segunda nota'))
                        nota3 = int(input('Digite a terceira nota'))
                        media = (nota1 + nota2 + nota3) / 3
                        if media >= 7:
                            print(f'Aprovado: {round(media)}')
                        elif media < 7:
                            print(f'Reprovado {round(media)}')
                        elif media == 10:
                            print(f'Aprovado com distinção {round(media)}')
                    case 21:
                        #Retornar
                        print('Retornar')
                    case 22:
                        print('22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).')
                        number = int(input('Digite o número'))
                        if number % 2 == 0:
                            print('Seu número é par')
                        else:
                            print('Seu número é ímpar')
                    case 23:
                        number = float(input("Insira um número: "))
                        if round(number) == number:
                            print("O número é inteiro")
                        else:
                            print("O número é decimal")

                    case 24:
                        print('23. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:')                      
                        print('par ou ímpar;')
                        print('positivo ou negativo;')
                        print('inteiro ou decimal.')
                        number1 = float(input('Digite o primeiro número'))
                        number2 = float(input('Agora digite o segundo número'))
                        operação = int(input('Qual operação deseja fazer? Adição[1] Subtração[2] Multiplicação[3] Divisão[4]'))
                        resultado = 0
                        mensagem = ''
                        if operação == 1:
                            resultado = number1 + number2
                        elif operação == 2:
                            resultado = number1 - number2
                        elif operação == 3:
                            resultado = number1 * number2
                        else:
                            resultado = number1 / number2
                        if resultado % 2 == 0:
                            mensagem += 'Seu número é par, '
                        else:
                            mensagem += 'Seu número é ímpar, '
                        if resultado < 0:
                            mensagem += 'negativo e '
                        else:
                            mensagem += 'positivo e '
                        if resultado % 1 != 0:
                            mensagem += 'decimal'
                        else:
                            mensagem += 'inteiro'
                        print(' ')
                        print(resultado)
                        print(mensagem)
                    case 25:
                        print('24. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são')
                        print('"Telefonou para a vítima?"')
                        print('"Esteve no local do crime?"')
                        print('"Mora perto da vítima?"')
                        print(' "Devia para a vítima?"')
                        print('"Já trabalhou com a vítima?"')
                        print('O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".')
                        resultado = 0
                        pergunta1 = input('Telefonou para a vítima? [s]/[n]')
                        if pergunta1 == 's' or pergunta1 == 'S':
                            resultado += 1
                        pergunta2 = input('Esteve no local do crime? [s]/[n]')
                        if pergunta2 == 's' or pergunta2 == 'S':
                            resultado += 1
                        pergunta3 = input('Mora perto da vítima? [s]/[n]')
                        if pergunta3 == 's' or pergunta3 == 'S':
                            resultado += 1
                        pergunta4 = input('Devia para a vítima? [s]/[n]')
                        if pergunta4 == 's' or pergunta4 == 'S':
                            resultado += 1
                        pergunta5 = input('Já trabalhou com a vítima? [s]/[n]')
                        if pergunta5 == 's' or pergunta5 == 'S':
                            resultado += 1
                        if resultado == 2:
                            print('Classificada como Suspeito')
                        elif resultado == 3 or resultado == 4:
                            print('Classificada como Cúmplice')
                        elif resultado == 5:
                            print('Classificada como Assassino')
                        else:
                            print('Inocente')
                    
                    case 26:
                        print('26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:')
                        print('Álcool:')
                        print('até 20 litros, desconto de 3% por litro')
                        print('acima de 20 litros, desconto de 5% por litro')
                        print('Gasolina:')
                        print('até 20 litros, desconto de 4% por litro')
                        print('acima de 20 litros, desconto de 6% por')
                        print('litro Escreva um algoritmo que leia o ')
                        print('número de litros vendidos, o tipo de combustível')
                        print('(codificado da seguinte forma: A-álcool, G-gasolina),')
                        print('calcule e imprima o valor a ser pago pelo cliente ')
                        print('sabendo-se que o preço do litro da gasolina é R$ 2,50 ')
                        print('o preço do litro do álcool é R$ 1,90.')
                        print(' ')
                        print('Álcool: até 20 litros, desconto de 3% por litro. Acima de 20 litros, desconto de 5% por litro. O  preço do litro do álcool é R$ 1,90. ')
                        print('Gasolina: até 20 litros, desconto de 4% por litro. acima de 20 litros, desconto de 6% por. O preço do litro da gasolina é R$ 2,50')
                        preçoAlcool = 1.90
                        preçoGasolina = 2.50
                        combustível = input('Escolha o combustivel: [A]Álcool / [G]Gasolina')
                        if combustível == 'A' or combustível == 'a':
                            litros = float(input('Quantos litros de alcool deseja por?'))
                            if litros <= 20:
                                desconto = litros * preçoAlcool * 3 / 100 
                                preço = litros * preçoAlcool - desconto
                                print('Seu preço a ser pago é R${}'.format(preço))
                            elif litros > 20:
                                desconto = litros * preçoAlcool * 5 / 100
                                preço = litros * preçoAlcool - desconto
                                print('Seu preço a ser pago é R${}'.format(preço))
                        else:
                            litros = float(input('Quantos litros de gasolina deseja por?'))
                            if litros <= 20:
                                desconto = litros * preçoGasolina * 4 / 100 
                                preço = litros * preçoGasolina - desconto
                                print('Seu preço a ser pago é R${}'.format(preço))
                            elif litros > 20:
                                desconto = litros * preçoGasolina * 6 / 100
                                preço = litros * preçoGasolina - desconto
                                print('Seu preço a ser pago é R${}'.format(preço))
                    case 27:
                        #retornar
                        print('27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:')
                    case 28:
                        #retornar
                        print(' ')
        case 3:
            while True:
                escolha_De_Exercício = int(input('Qual exercício deseja ver de 1 até 51?'))
                match escolha_De_Exercício:
                    case 1:
                        print('1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.')
                        while True:
                            nota = float(input('Digite a nota'))
                            if nota >= 0 and nota <= 10:
                                print('Nota aceita')
                                break
                            else:
                                print('Nota inválida')
                                print('Digite novamente')
                    case 2:
                        print('2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.')
                        nome = input('Digite o seu nome')
                        while True:
                            senha = input('Digite a sua senha')
                            if senha == nome or senha == nome.upper() or senha == nome.lower():
                                print('Sua senha não pode ser igual ao seu nome')
                                print('Digite novamente')
                            else:
                                print('Senha aceita')
                                break
                    case 3:
                        print('3. Faça um programa que leia e valide as seguintes informações:Nome: maior que 3 caracteres;')
                        informações = []
                        while True:
                            nome = input('Digite o seu nome')
                            if len(nome) < 3:
                                print('Seu nome precisa ser maior que 3 caracteres')
                            else:
                                informações.append(nome)
                                print('Nome aceito')
                                break
                        while True:
                            idade = int(input('Digite a sua idade'))
                            if idade > 0 and idade < 150:
                                informações.append(idade)
                                print('Idade aceita')
                                break
                            else:
                                print('Idade inválida')
                        while True:
                            salario = float(input('Digite seu salário'))
                            if salario > 0:
                                informações.append(salario)
                                print('Salário aceito')
                                break
                            else:
                                print('Seu salário precisa ser maior do que 0')
                        while True:
                            sexo = input('Qual é o seu sexo? [f]/[m]')
                            if sexo == 'f' or sexo == 'F' or sexo == 'm' or sexo == 'M':
                                informações.append(sexo)
                                print('Sexo aceito')
                                break
                            else:
                                print('Sexo inválido')
                        while True:
                            estado_Civil = input('Estado civil [s]/[c]/[v]/[d]')
                            if estado_Civil == 's' or estado_Civil == 'c' or estado_Civil == 'v' or estado_Civil == 'd':
                                informações.append(estado_Civil)
                                print('Estado civil aceito')
                                break
                            else:
                                print('Digite novamente. ')
                        if informações[3] == 'f':
                            print('Certo senhora, sua informações foram validadas com sucesso')
                            for i in range(len(informações)):
                                print(informações[i])
                        else:
                            print('Certo, senhor suas informações foram validadas com sucesso')
                            for i in range(len(informações)):
                                print(informações[i])
                    case 4:
                        print('4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3 por cento e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.')
                        populaçãoB = 200000
                        populaçãoA = 80000
                        taxa_PopulaçãoB = 1.5
                        taxa_PopulaçãoA = 3
                        anos = 0
                        while populaçãoA < populaçãoB:
                            populaçãoB += populaçãoB * taxa_PopulaçãoB / 100
                            populaçãoA += populaçãoA * taxa_PopulaçãoA / 100
                            anos += 1
                        print(f'Serão necessários {anos} para que a população A se iguale à população B')
                    case 5:
                        print('5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.')
                        while True:
                            populaçãoB = int(input('Digite o número de habitantes da população B'))
                            populaçãoA = int(input('Agora digite o número de habitantes da população A'))
                            taxa_PopulaçãoB = float(input('Informe a taxa de crescimento da população B'))
                            taxa_PopulaçãoA = float(input('Agora informe a taxa de crescimento da população A'))
                            anos = 0
                            while populaçãoA < populaçãoB:
                                populaçãoB +=  populaçãoB * taxa_PopulaçãoB / 100
                                populaçãoA += populaçãoA * taxa_PopulaçãoA / 100
                                anos += 1
                            print(f'Com os dados que você informou será necessário {anos} para que a população A se iguale à população B')
                    case 6:
                        print('6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.')
                        while True:
                            numbers = ''
                            escolha = int(input('Quer ver os números de que forma? [1]Lado a lado/ [2]Um embaixo do outro'))
                            if escolha == 2:
                                for i in range(1, 21):
                                    print(i)
                            else:
                                for i in range(1, 21):
                                    numbers += str(i) + ' '
                                print(numbers)
                    case 7:
                        print('5. Faça um programa que leia 5 números e informe o maior número.')
                        print("Digite os número abaixo")
                        maior = 0
                        for i in range(0, 5):
                            number = int(input('Digite...'))
                            if number > maior:
                                maior = number
                        print(f'O maior número digitado foi {maior}')
                    case 8:
                        print('8. Faça um programa que leia 5 números e informe a soma e a média dos números.')
                        print('Digite abaixo os 5 números')
                        soma = 0
                        for i in range(0, 5):
                            number = int(input('Digite'))
                            soma += number
                        media = soma / 5
                        print(f'A soma é {soma} e a media e {media}')
                    case 9:
                        print('9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.')
                        ínpares = []
                        while True:
                            number = int(input('Digite'))
                            if number % 2 != 0:
                                ínpares.append(number)
                            if number == 0:
                                break
                        print(f'Os ínpares foram: {ínpares}')
                    case 10:
                        print('10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.')
                        def intervalo(inicio, fim):
                            for i in range(inicio, fim+1):
                                print(i)
                            inicio = int(input('Digite o número inicial: '))
                            fim = int(input('Digite o número final: '))
                            intervalo(inicio, fim)
                    case 11:
                        #Retornar
                        print('11. ')
                    case 12:
                        number = int(input('Digite o número que seja ver a tabuada'))
                        for i in range(1, 11):
                            tabuada = f' |{number} X {i}| = {number * i}'
                            print(tabuada)
                    case 13:
                        print('13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.')    
                        base = int(input('Digite a base'))
                        expoente = int(input('Agora digite o expoente'))
                        resultado = 1
                        for i in range(expoente):
                            resultado = resultado * base
                        print(resultado)
                    case 14:
                        print('14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.')
                        ímpares = 0
                        pares = 0
                        for i in range(10):
                            number = int(input('Digite'))
                            if number % 2 == 0:
                                pares += 1
                            else:
                                ímpares += 1
                        print(f'Foram digitados {ímpares} números ímpares e {pares} númetos pares')
                    case 15:
                        print('15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo')
                        limite = int(input('Escolha o limite da sequência'))
                        a, b = 0, 1
                        while a <= limite:
                            print(a)
                            temp = b
                            b = a + b
                            a = temp
                    case 16:
                        print('16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.')
                        limite = 500
                        a, b = 0, 1
                        while a <= limite:
                            print(a)
                            temp = b
                            b = a + b
                            a = temp
                    case 17:
                        print('17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120')
                        num = int(input('Forneça o número'))
                        fatorial = 1
                        while num > 1:
                            fatorial = num * fatorial
                            num = num - 1
                        print(f'O fatorial é {fatorial}')
                    case 18:
                        print('18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.')
                        numbers = []
                        while True:
                            num = input("Insira um número (ou 'q' para encerrar): ")
                            if num == 'q':
                                break
                            try:
                                numbers.append(int(num))
                            except ValueError:
                                print("Insira um valor valido, numerico")
                                continue

                        min_val = min(numbers)
                        max_val = max(numbers)
                        sum_val = sum(numbers)

                        print("Menor valor:", min_val)
                        print("Maior valor:", max_val)
                        print("Soma dos valores:", sum_val)
                    case 19:
                        print('19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.')
                        #Retornar
                    case 20:
                        print('20.Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. ')
                        while True:
                            num = int(input('Forneça o número'))
                            if num >= 16 or num < 0:
                                print('Digite apenas números positivos e inteiro maiores que 16')
                            else:
                                fatorial = 1
                                while num > 1:
                                    fatorial = num * fatorial
                                    num = num - 1
                                print(f'O fatorial é {fatorial}')   
                    case 21:
                        print('21.Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.')
                        num = int(input('Digite um número'))
                        if num > 1:
                            for i in range(2, num):
                                condição = num % i == 0
                                if condição:
                                    print('Não é um número primo')
                                    break
                                else:
                                    print('É um número primo')
                                    break
                        else:
                            print('Não é um número primo')
                    case 22:
                        print('22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.')
                        num = int(input('Digite um número'))
                        if num > 1:
                            for i in range(2, num):
                                condição = num % i == 1
                                if condição:
                                    print('Não é um número primo')
                                    print('Ele é divisível por', i)
                                    
                                    break
                                else:
                                    print('É um número primo')
                                    break
                        else:
                            print('Não é um número primo')
                    case 23:
                        print('23.Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.')
                        num = int(input('Digite o número: '))
                        num_divisões = 0
                        for i in range(2, num):
                            primo = True
                            for j in range(2, i):
                                num_divisões += 1
                                if i % j == 0:
                                    primo = False
                                    break
                        if primo:
                                print(i)
                        print(f'Número de divisões feitas: {num_divisões}')
                    case 24:
                        print('24.Faça um programa que calcule o mostre a média aritmética de N notas.')
                        soma = 0
                        len = 0
                        while True:
                            entrada = int(input('Digite...'))
                            if entrada == 0:
                                break
                            soma += entrada
                            len += 1
                        media = soma / len
                        print('Media', media)
                    case 25:
                        print('25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.')
                        soma = 0
                        len = 0
                        while True:
                            entrada = int(input('Digite...'))
                            if entrada == 0:
                                break
                            soma += entrada
                            len += 1
                        media = soma / len
                        if media > 0 and media < 26:
                            print('Turma jovem')
                        elif media >= 26 and media < 60:
                            print('Turma adulta')
                        elif media > 60:
                            print('Turma idosa') 
                    case 26:
                        print('26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.')
                        
                        votos_candidato1 = 0
                        votos_candidato2 = 0
                        votos_candidato3 = 0
                        N_eleitores = int(input('Digite o número de eleitores'))
                        print('Candidato 1 [1] Candidato 2 [2] Candidato 3 [3]')
                        for i in range(N_eleitores):
                            votos = int(input('Vote'))  
                            if votos == 1:
                                votos_candidato1 += 1
                            elif votos == 2:
                                votos_candidato2 += 1
                            elif votos == 3:
                                votos_candidato3 += 1
                        if votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3:
                            print(f'O ganhador foi o candidato 1')
                        elif votos_candidato2 > votos_candidato1 and votos_candidato2 > votos_candidato3:
                            print(f'O ganhador foi o candidato 2')
                        elif votos_candidato3 > votos_candidato1 and votos_candidato3 > votos_candidato2:
                            print(f'O ganhador foi o candidato 3')
                    case 27:
                        print('27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.')
                        soma = 0
                        qtd_turmas = int(input('Informe a quantidade de tumas'))
                        for i in range(qtd_turmas):
                            qtd_alunos = int(input(f'Informe a quantidade de alunos da turma {i + 1}'))
                            soma += qtd_alunos
                        media = soma / qtd_turmas
                        print(f'Média de alunos por turma {media}')
                    case 28:
                        print('28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.')
                        qtd_cds = int(input('Informe a quantidade de cds comprados'))
                        soma = 0
                        for i in range(qtd_cds):
                            preço = int(input(f'Inform o preço do cd N° {i + 1}'))
                            soma += preço
                        media = soma / qtd_cds
                        print(f'O total investido em cds foi R${soma} e o valor médio foi R${media}')
                    case 29:
                        print('29.O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos.')
                        print('Lojas Quase Dois - Tabela de preços')
                        print('-----------------------------------')
                        for qtd_produtos in range(1, 51):
                            preco = qtd_produtos * 1.99
                            print(f'{qtd_produtos} - R$ {preco:.2f}')
                    case 30:
                        print('30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:')
                        preco_pao = float(input('Informe o preço do pão'))
                        print('Lojas Quase Dois - Tabela de preços')
                        print('-----------------------------------')
                        for i in range(0, 50):
                            preco = i * preco_pao
                            print(f'{i} - R$ {preco:.2f}')
                    case 31:
                        print('31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui  uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,  para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar  ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:')
                        while True:
                            total = 0
                            for i in range(999999):
                                produtos = float(input(f'Produto {i + 1} '))
                                total += produtos
                                if produtos == 0:
                                    break
                            dinheiro = float(input('Informe o dinheiro'))
                            Trouco = dinheiro - total
                            print('-----')
                            print(f'Total: {total} Trouco: {Trouco}')
                            print('-----')
                    case 32:
                        num = int(input('Informe o número: '))
                        fatorial = 1
                        i = 1
                        while i <= num:
                            fatorial *= i
                            i += 1
                        print(f'O fatorial de {num} é {fatorial}')
                    case 33:
                        print('33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.')
                        maior = 0
                        menor = 999999999
                        soma = 0
                        len = 0
                        while True:
                            temperatura = int(input('Digite...'))
                            if temperatura == 0:
                                break
                            soma += temperatura
                            len += 1
                            if temperatura > maior:
                                maior = temperatura
                            elif temperatura < menor:
                                menor = temperatura
                        media = soma / len 
                        print(f'Maior temperatura: {maior} Menor temperatura: {menor} Media: {media}')
                    case 34:
                        print('34. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.')                    
                        num = int(input('Digite um número'))
                        if num > 1:
                            for i in range(2, num):
                                condição = num % i == 0
                                if condição:
                                    print('Não é um número primo')
                                    print('Ele é divisível por', i)
                                    
                                    break
                                else:
                                    print('É um número primo')
                                    break
                        else:
                            print('Não é um número primo')
                    case 35:
                        print('35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.')
                        num_primos = []
                        entrada = int(input('Informe'))
                        for i in range(1, entrada):
                            if i % 2 == 0:
                                num_primos.append(i)
                        print(f'Os números primos são {num_primos}')
                    case 36:
                        print('36.Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:')
                        tabuada = int(input('Informe a tabuada'))
                        a_partir_de = int(input('A partir de qual número?'))
                        final = int(input('Digite o número final'))
                        if final > a_partir_de:
                            print('O número de início não pode ser menor que o número final')
                        while a_partir_de > final - 1:
                            print(f'{tabuada} X {a_partir_de} = {a_partir_de * tabuada}')
                            a_partir_de -= 1
                    case 37:
                        print('37.Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes')
                        clienteMaisAlto = 0
                        clienteMaisBaixo = 999
                        clienteMaisMagro = 999
                        clienteMaisGordo = 0
                        qtdPeso = []
                        qtdAltura = []

                        while True:
                            cod = 0
                            inputCodigo = int(input('Digite seu código'))
                            if inputCodigo == 0:
                                break

                            inputAltura = int(input('Digite sua altura em cm. Ex: 170'))

                            if inputAltura > clienteMaisAlto:
                                clienteMaisAlto = inputAltura
                            elif inputAltura < clienteMaisBaixo and inputAltura < clienteMaisAlto:
                                clienteMaisBaixo = inputAltura

                            qtdAltura.append(inputAltura)

                            inputPeso = int(input('Digite seu peso'))

                            if inputPeso > clienteMaisGordo:
                                clienteMaisGordo = inputPeso
                            elif inputPeso < clienteMaisMagro and inputPeso < clienteMaisGordo:
                                clienteMaisMagro = inputPeso

                            qtdPeso.append(inputPeso)

                        somaAltura = 0
                        somaPeso = 0
                        mediaPeso = 0
                        mediaAltura = 0
                        for i in range(len(qtdPeso)):
                            somaPeso += qtdPeso[i]
                            somaAltura += qtdAltura[i]
                        mediaPeso = somaPeso / len(qtdPeso)
                        mediaAltura = somaAltura / len(qtdAltura)

                        print(f'Cliente mais alto {clienteMaisAlto}')
                        print(f'Cliente mais baixo {clienteMaisBaixo}')
                        print(f'Cliente mais gordo {clienteMaisGordo}')
                        print(f'Cliente mais magro {clienteMaisMagro}')
                        print(f'Média de peso: {mediaPeso}')
                        print(f'Média de altura: {mediaAltura}')

                        

                            