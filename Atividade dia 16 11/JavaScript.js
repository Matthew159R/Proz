//1
let lado = prompt('Informe o valor de um dos lados')
let perimetro = lado * 4
let area = lado * lado
    alert('O perímetro é: ' + perimetro +'cm' + ' e a área: ' + area + 'cm')
//2
let tempF = prompt('Qual é a temperatura em Fahrenheit?')
let tempC = (tempF - 32) / 1.8
    alert('Em celcius ela seria: ' + tempC)
//3
let cateto1 = prompt('Digite o primeiro cateto')
let cateto2 = prompt('Digite o segundo cateto')
let hipotenusa = cateto1**2 + cateto2**2
    alert('A hipotenusa é: ' + hipotenusa)
//4
let Dolar = prompt('Digite a cotação em dolar')
let Reais = Dolar * 5.31 
    alert('A sua cotação em reais é: ' + 'R$ ' + Reais)
//5
let distancia = prompt('Qual a distância do local em que você pretende chegar?')
let km = prompt('Você va dirigir a quantos km/h ?')
let tempo = distancia / km
    if(km < distancia){
        alert(`O tempo a ser dirigido é ${tempo} minutos`)
   }else if(tempo == 1){
        alert(`O tempo a ser dirigido é ${tempo} hora`)
   }else{
        alert(`O tempo a ser dirigido é ${tempo} horas`)
   }

