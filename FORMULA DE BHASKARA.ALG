Algoritmo "Fórmula de baskara"

Var
a, b, c: inteiro
xUm, xDois: real
delta: real

Inicio
escreval("Para resolvermos a sua equação siga os seguintes passos")
escreval("--------------------")
escreval("Escreva o coeficiente A")
leia(a)
escreval("Agora escreval o coeficiente B")
leia(b)
escreval("Por fim, escreva o C")
leia(c)
delta <- b^2 - 4 * a * c
xUm <- (-1 * b) + raizQ(delta) / 2 * a
xDois <- (-1 * b) - raizQ(delta) / 2 * a
limpatela
escreval("-------------------------------------")
escreval("O resultado foi da sua equação foi:")
escreval("X1 = ", xUm)
escreval("X2 = ", xDois)
escreval("Delta = ", delta)
escreval("-------------------------------------")



Fimalgoritmo