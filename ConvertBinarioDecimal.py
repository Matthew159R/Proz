#O programa abaixo converte um número decimal para binário e um binário de 8 digitos para decimal
DecimalOrBinario = int(input(' Digite[1] Para converter número binário em decimal. Digite[2] Para converter decimal em binário.'))
match DecimalOrBinario:
    case 1:
        print('==--------------------------------------==')
        print('Digite abaixo o nº binário linha por linha')
        print('==---------------------------------------==')
        print('Obs: Só digite números binários')
        numBinario = []
        for i in range(0, 8):
            number = int(input('[|Digite|]'))
            numBinario.append(number)
        decimal = pow(numBinario[7] * 2, 0) + pow(numBinario[6] * 2, 1) + pow(numBinario[5] * 2, 2) + pow(numBinario[4] * 2, 3) + pow(numBinario[3] * 2, 4) + pow(numBinario[2] * 2, 5) + pow(numBinario[1] * 2, 6) + pow(numBinario[0] * 2, 7)
        if numBinario[-1] == 0:
            print('O número decimal é: {}'.format(decimal - 1))
        else:
            print('O número decimal é: {}'.format(decimal))
    case 2:
        print('==-------------------------------------------------==')
        print('Digite abaixo o nº decimal que deseja ver em binário')
        print('==-------------------------------------------------==')
        def decimalParaBinario(valor):
            if valor <= 0:
                return '0'
            binario = ''
            while valor > 0:
                resto = int(valor % 2)
                valor = int(valor / 2)
                binario = str(resto) + binario
            return binario
        decimal = int(input('Digite...'))
        binario = decimalParaBinario(decimal)
        print(f'O número {decimal} é {binario} em bináro')
