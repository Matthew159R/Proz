Algoritmo "Menor de 3"


Var
a, b, c, menor: inteiro



Inicio
escreval("Primeiro n�mero")
leia(a)
escreval("Segundo n�mero")
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


escreval("O menor n�mero � ", menor)
fimse
fimse


Fimalgoritmo