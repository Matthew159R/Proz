Algoritmo "Menor de 3"


Var
a, b, c, menor: inteiro



Inicio
escreval("Primeiro número")
leia(a)
escreval("Segundo número")
leia(b)
escreval("Terceiro")
leia(c)
se (a < b) e (a < c) entao
  menor <- a
senao
  se b < c entao
  menor <- b
senao
  menor <- c


escreval("O menor número é ", menor)
fimse
fimse


Fimalgoritmo