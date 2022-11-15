//Esse algoritmo foi feito por um iniciante em programação
let lanches = [
    {
        nome: 'pizza',
        valor: 15
    },
    {
        nome: 'hamburger',
        valor: 10
    },
    {
        nome: 'Cachorro quente',
        valor: 6
    }
]
let bebidas = [
    {
        nome: 'Refrigerante',
        valor: 5
    },
    {
        nome: 'Suco de maracujá',
        valor: 3
    },
    {
        nome: 'Café',
        valor: 2
    }
]
//!----------Algorítimo da Pizza----------!
alert('Bem vindo à ProgrammerFoods. Clique em [OK]')
alert('A Seguir veja nosso cardápio especial para hoje')
let lanche = prompt('[1]Para pizza / [2]Para hamburger / [3]Para cachorro quente')
if(lanche == 1){
            let quantidaDePizzas = prompt('Quantas pizzas você vai querer? Cada uma custa R$15')
            let valorPizza = quantidaDePizzas *= lanches[0].valor
            let bebida = prompt('Deseja adcionar alguma bebida? [S] [N]')
                if(bebida == 'S'){
                    let bebidas = prompt('Escolha: [1] Refrigerante / [2] Suco de maracujá / [3] Café.')
                    //!--------------------Refrigerante--------------------!
                        if(bebidas == 1){
                            let quantidadeRefrigerante = prompt(`Cada garrafa contém 1L do refrigerante  e custa R$ 5, quantas garrafas você vai querer?`)
                            let valorRefigerante = quantidadeRefrigerante *= 5
                            let final = prompt(`Seu total ficou R$${valorPizza + valorRefigerante}, sendo R$${valorPizza} da pizza e R$${valorRefigerante} do refrigerante. Deseja continuar? [S] [N]`)
                                if(final == 'S'){
                                    alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                               🍕🥤')
                                }else if(final == 'N'){
                                    alert('PEDIDO CANCELADO!!! X🍕🥤X')
                                }else{
                                    alert('Caracter não identificado')
                                }   
                    //!-------------------Suco de maracujá------------------!
                        }else if(bebidas == 2){
                            let quantidadeSucoDeMaracuja = prompt('Cada copo contém 500ML de  suco de maracujá e custa R$ 3, quantos copos você vai querer?')
                            let valorSucoDeMaracuja = quantidadeSucoDeMaracuja *= 3
                            let final = prompt(`Seu total ficou R$${valorPizza + valorSucoDeMaracuja}, sendo R$${valorPizza} da pizza e R$${valorSucoDeMaracuja} do suco de maracujá. Deseja continuar? [S] [N]`)
                                if(final == 'S'){
                                    alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                                🧃🍕')
                                }else if(final == 'N'){
                                    alert('PEDIDO CANCELADO!!! X🍕🧃X')
                                }else{
                                    alert('Caracter não identficada')
                                }
                    //!---------------------Café-----------------------------!
                        }else if(bebidas == 3){
                            let quantidadeCafe = prompt('Cada xícara custa R$ 2, quantas você vai querer?')
                            let valorCafe = quantidadeCafe *= 2
                            let final = prompt(`Seu total ficou R$${valorPizza + valorCafe}, sendo R$${valorPizza} da pizza e R$${valorCafe} do café. Deseja continuar? [S] [N]`)
                                if(final == 'S'){
                                    alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                                 ☕🍕')
                                }else if(final == 'N'){
                                    alert('PEDIDO CANCELADO!!! X🍕☕X')
                                }else{
                                    alert('Caracter não identificado')
                                }
                        }                      
                }else{
                    alert('OK')
                }
            let final = prompt(`Seu total ficou R$${valorPizza}. Deseja continuar? (Para sim)[S] (Para não)[N]`)
    if(final == 'S'){
        alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                               🍕')
    }else if(final == 'N'){
        alert('PEDIDO CANCELADO!!! X🍕X')
    }else{
        alert('Reinicie o algorítimo...')
    }
//!----------Algorítimo do Hamburger----------!
}else if(lanche == 2){
            let quantidadeDeHamburgers = prompt('Quantos hamburgers você vai querer? Cada um custa R$10')
            let valorHamburger = quantidadeDeHamburgers *= lanches[1].valor
            let bebida = prompt('Deseja adcionar alguma bebida? [S] [N]')
                if(bebida == 'S'){
                    let bebidas = prompt('Escolha: [1] Refrigerante / [2] Suco de maracujá / [3] Café.')
                    //!--------------------Refrigerante--------------------!
                        if(bebidas == 1){
                            let quantidadeRefrigerante = prompt(`Cada garrafa contém 1L do refrigerante  e custa R$ 5, quantas garrafas você vai querer?`)
                            let valorRefigerante = quantidadeRefrigerante *= 5
                            let final = prompt(`Seu total ficou R$${valorHamburger + valorRefigerante}, sendo R$${valorHamburger} do hamburger e R$${valorRefigerante} do refrigerante. Deseja continuar? [S] [N]`)
                                if(final == 'S'){
                                    alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                               🍔🥤')
                                }else if(final == 'N'){
                                    alert('PEDIDO CANCELADO!!! X🍔🥤X')
                                }else{
                                    alert('Caracter não identificado')
                                }   
                     //!-------------------Suco de maracujá------------------!
                        }else if(bebidas == 2){
                            let quantidadeSucoDeMaracuja = prompt('Cada copo contém 500ML de  suco de maracujá e custa R$ 3, quantos copos você vai querer?')
                            let valorSucoDeMaracuja = quantidadeSucoDeMaracuja *= 3
                            let final = prompt(`Seu total ficou R$${valorHamburger + valorSucoDeMaracuja}, sendo R$${valorHamburger} do hamburger e R$${valorSucoDeMaracuja} do suco de maracujá. Deseja continuar? [S] [N]`)
                                if(final == 'S'){
                                    alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                                🧃🍔')
                                }else if(final == 'N'){
                                    alert('PEDIDO CANCELADO!!! X🍔🧃X')
                                }else{
                                    alert('Caracter não identficada')
                                }
                     //!---------------------Café-----------------------------!
                        }else if(bebidas == 3){
                            let quantidadeCafe = prompt('Cada xícara custa R$ 2, quantas você vai querer?')
                            let valorCafe = quantidadeCafe *= 2
                            let final = prompt(`Seu total ficou R$${valorHamburger + valorCafe}, sendo R$${valorHamburger} do hamburger e R$${valorCafe} do café. Deseja continuar? [S] [N]`)
                                if(final == 'S'){
                                    alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                                 ☕🍔')
                                }else if(final == 'N'){
                                    alert('PEDIDO CANCELADO!!! X🍔☕X')
                                }else{
                                    alert('Caracter não identificado')
                                }
                        }                      
                }else{
                    alert('OK')
                }
            let final = prompt(`Seu total ficou R$${valorHamburger}. Deseja continuar? (Para sim)[S] (Para não)[N]`)
    if(final == 'S'){
        alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                                🍔')
    }else if(final == 'N'){
        alert('PEDIDO CANCELADO!!! X🍔X')
    }else{
        alert('Reinicie o algorítimo...')
    }
//!---------Algorírimo do Hot Hog----------!
    }else if(lanche == 3){
            let quantidadeHotDog = prompt('Quantos Hot dogs você vai querer pedir? Cada um custa R$6')
            let valorHotdog = quantidadeHotDog *= lanches[2].valor
            let bebida = prompt('Deseja adcionar alguma bebida? [S] [N]')
            if(bebida == 'S'){
                let bebidas = prompt('Escolha: [1] Refrigerante / [2] Suco de maracujá / [3] Café.')
                //!--------------------Refrigerante--------------------!
                    if(bebidas == 1){
                        let quantidadeRefrigerante = prompt(`Cada garrafa contém 1L do refrigerante  e custa R$ 5, quantas garrafas você vai querer?`)
                        let valorRefigerante = quantidadeRefrigerante *= 5
                        let final = prompt(`Seu total ficou R$${valorHotdog + valorRefigerante}, sendo R$${valorHotdog} do cachorro quente e R$${valorRefigerante} do refrigerante. Deseja continuar? [S] [N]`)
                            if(final == 'S'){
                                alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                               🍕🥤')
                            }else if(final == 'N'){
                                alert('PEDIDO CANCELADO!!! X🍕🥤X')
                            }else{
                                alert('Caracter não identificado')
                            }  
                        }
                //!-------------------Suco de maracujá------------------! 
                    }else if(bebidas == 2){
                        let quantidadeSucoDeMaracuja = prompt('Cada copo contém 500ML de  suco de maracujá e custa R$ 3, quantos copos você vai querer?')
                        let valorSucoDeMaracuja = quantidadeSucoDeMaracuja *= 3
                        let final = prompt(`Seu total ficou R$${valorHotdog + valorSucoDeMaracuja}, sendo R$${valorHotdog} do cachorro quente e R$${valorSucoDeMaracuja} do suco de maracujá. Deseja continuar? [S] [N]`)
                            if(final == 'S'){
                                alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                                🧃🌭')
                            }else if(final == 'N'){
                                alert('PEDIDO CANCELADO!!! X🍕🧃X')
                            }else{
                                alert('Caracter não identficada')
                            }
                //!---------------------Café-----------------------------!
                    }else if(bebidas == 3){
                        let quantidadeCafe = prompt('Cada xícara custa R$ 2, quantas você vai querer?')
                        let valorCafe = quantidadeCafe *= 2
                        let final = prompt(`Seu total ficou R$${valorHotdog + valorCafe}, sendo R$${valorHotdog} do cachorro quente e R$${valorCafe} do café. Deseja continuar? [S] [N]`)
                            if(final == 'S'){
                                alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                                 ☕🌭')
                            }else if(final == 'N'){
                                alert('PEDIDO CANCELADO!!! X🌭☕X')
                            }else{
                                alert('Caracter não identificado')
                            }
                    }                      
            }else{
                alert('OK')
            }
        let final = prompt(`Seu total ficou R$${valorHotdog}. Deseja continuar? (Para sim)[S] (Para não)[N]`)
if(final == 'S'){
    alert('----------SEU PEDIDO ESTÁ A CAMINHO----------                               🌭')
}else if(final == 'N'){
    alert('PEDIDO CANCELADO!!! X🌭X')
}else{
    alert('Reinicie o algorítimo...')
}


















/*             
                                         
                                         ,','
                                        ; ;
                                        `.`.
                                          ) ;
                                     ,,,-','
                      _____,,,,---''",,,-'
            ___,,--'""_____,,,,--''""
    __,,--'"__,,--'"""
 ,-"_,,--'""
; ,'               .,------,....___
; ;               /       ;        """`---.._
`.``-.._____,,,,,/       ;                   ""``.
  ``--...___;;;;/-"""""-;                         
            ```;        ;                         ;;
              ;        ;                         / ;
             ;"----....;___                     ; ;;
             ;-,,,,,___    ""`"--..._         ,' ; ;
             ;         """"``---...__""-...,-' ,'  ;
             ;                       "`-....,-'   /
             `-._     _-------_                 ,'
                 "`--'"""""""""``--..        ,,'
                                     ""`---'"
*/






















































//Feito por Matheus Batista. Proz Educação. Professor: Kleberson
