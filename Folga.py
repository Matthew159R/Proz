print('Hoje é dia de folga, abaixo você vai decidir qual opção preferir')
print('Escolha a opção pelo seu número da lista')
folga = int(input('1.Ficar em casa e pedir um lanche no ifood / 2. Ir ao cinema para assistir um filme'))
pizza = 15
hotDog = 5
hamburguer = 12
if folga == 1:
    print('Certo, ta afim de ser sedentário hoje, né. Abaixo, escolha o lanche:')
    lanche = int(input('[1] para pizza🍕 / [2] para cachoro quente🌭 / [3] Hamburguer🍔'))
    if lanche == 1:
        print('A pizza vai sair por R$15 cada uma')
        quantidaPizza = int(input('Quantas você vai querer?'))
        valorTotal = quantidaPizza * pizza
        print('Seu pedido total ficou em R$', valorTotal)
        desejaContinuar = input('Deseja continuar [S] / [N]')
        if desejaContinuar == 'S':
            print('Seu pedido está a caminho...')
            print('🍕' * quantidaPizza)
            avalição = int(input('Obrigado por usar nosso sistema! Nos dê sua avaliação, isso é algo importantíssimo para o nosso crescimento. Digite sua quantidade de estrelas até 5'))
            estrelas = avalição * '⭐'
            print('Muito obrigado!', estrelas)
            if estrelas > 5:
                print('Muito obrigado, mas o máximo da avalização é 5', '⭐' * 5)
        elif desejaContinuar == 'N':
            print('Pedido cancelado, por favor reinicie o algorítimo...')
        else:
            print('Caracter não identificada... Por favor, reinicie o algorítimo')
    elif lanche == 2:
        print('Cada cachorro quente custa R$5')
        quantiCachorroQuente = int(input('Quantos você vai querer?'))
        valorTotalHotDog = quantiCachorroQuente * hotDog
        print('Seu pedido ficou em R$', valorTotalHotDog)
        desejaContinuar = input('Deseja continuar [S] / [N]')
        if desejaContinuar == 'S':
            print('Seu pedido está a caminho...')
            print('🌭' * quantiCachorroQuente)
            avalição = int(input('Obrigado por usar nosso sistema! Nos dê sua avaliação, isso é algo importantíssimo para o nosso crescimento. Digite sua quantidade de estrelas até 5'))
            estrelas = avalição * '⭐'
            print('Muito obrigado!', estrelas)
            if estrelas > 5:
                print('Muito obrigado, mas o máximo da avalização é 5', '⭐' * 5)
        elif desejaContinuar == 'N':
            print('Pedido cancelado, por favor reinicie o algorítimo...')
        else:
            print('Caracter não identificada... Por favor, reinicie o algorítimo')
    elif lanche == 3:
        print('Cada hamburguer custa R$12')
        quantidadeHamburguer = int(input('Quantos você vai querer?'))
        valorTotalHamburguer = quantidadeHamburguer * hamburguer
        print('Seu pedido ficou em R$', valorTotalHamburguer)
        desejaContinuar = input('Deseja continuar [S] / [N]')
        if desejaContinuar == 'S':
            print('Seu pedido está a caminho...')
            print('🍔' * quantidadeHamburguer)
            avalição = int(input('Obrigado por usar nosso sistema! Nos dê sua avaliação, isso é algo importantíssimo para o nosso crescimento. Digite sua quantidade de estrelas até 5'))
            estrelas = avalição * '⭐'
            print('Muito obrigado!', estrelas)
            if estrelas > 5:
                print('Muito obrigado, mas o máximo da avalização é 5', '⭐' * 5)
        elif desejaContinuar == 'N':
            print('Pedido cancelado, por favor reinicie o algorítimo...')
        else:
            print('Caracter não identificada... Por favor, reinicie o algorítimo')
                           #!!!----------------------------Algorítimo do cinema---------------------------!!!
elif folga == 2:
    print('Ótimo, decidiu assitir um filme hoje!')
    print('Escolha um dos filmes disponíveis para hoje abaixo:')
    filme = int(input('[1] Interestelar /  [2] hobbit'))
    if filme == 1:
        print('Filme escolhido: interestelar')
        sinopse = input('Deseja ver a sinopse? [S] / [N]')
        if sinopse == 'S':
            print('As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a população mundial, possibilitando a continuação da espécie. Cooper é chamado para liderar o grupo e aceita a missão sabendo que pode nunca mais ver os filhos. Ao lado de Brand, Jenkins e Doyle, ele seguirá em busca de um novo lar.')
        elif sinopse == 'N':
            print('Ok, você já deve conhecer o filme')
        pipoca = input('Deseja comprar uma pipoca para acompanhar? [S] / [N]')
        if pipoca == 'S':
            print('Bom filme!🍿')
        else:
            print('Bom filme!')
    elif filme == 2:
        print('Filme escolhido: Hobbit')
        sinopse = input('Deseja ver a sinopse? [S] / [N]')
        if sinopse == 'S':
            print('Como a maioria dos hobbits, Bilbo Bolseiro leva uma vida tranquila até o dia em que recebe uma missão do mago Gandalf. Acompanhado por um grupo de anões, ele parte numa jornada até a Montanha Solitária para libertar o Reino de Erebor do dragão Smaug.')
        elif sinopse == 'N':
            print('Ok, você já deve conhecer o filme')
        pipoca = input('Deseja comprar uma pipoca para acompanhar? [S] / [N]')
        if pipoca == 'S':
            print('Bom filme!🍿')
        else:
            print('Bom filme!')   
