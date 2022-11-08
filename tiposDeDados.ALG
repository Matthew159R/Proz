Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 08/11/2022
var
anoDeNascimento: inteiro
anoAtual: inteiro
idade:inteiro
nome: caracter
covid:caracter  //Covid está como string porque sendo lógico ele não funcionou
Inicio
anoAtual <- 2022
escreva("Digite o ano em que você nasceu")
leia(anoDeNascimento)
idade <- anoAtual - anoDeNascimento
escreva("Sua idade é", idade)
escreval("Qual seu nome?")
leia(nome)
escreval("Você tem covid? S/N")
leia(covid)
se covid ="S"entao
escreva("Não saia de casa, se você sair, vai tomar um tiro")
senao
escreva("Coloque máscara para se proteger")

fimse
Fimalgoritmo
