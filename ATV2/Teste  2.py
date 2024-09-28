import math
""" 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a
soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
 informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

A=0
B=1
Proximo=A+B
I=0
#Apos isso B passa a ser o valor de Prox
# o numero deve atender as condições de Proximo para ser um numero de Fibonacci
print("0")
while I<20:# construindo uma sequencia de 10 numeros pertencentes a sequencia de Fibonacci
    Proximo=A+B
    A=B
    B=Proximo
    I+=1
    print(Proximo)

# verifica se é um quadrado perfeito saida em true ou false

def eh_quadrado_perfeito(x):
    s = int(math.sqrt(x))# atribui s a raiz quadrada de x
    return s * s == x # verifica se s vezes s é igual a x se sim é um quadrado perfeito

# verifica se é um número de Fibonacci através de duas condições se ao menos uma delas atender, o número pertence a sequencia Fibonacci
# aqui utilizo a formula de Binet para verificar se um numero qualquer pertence a sequencia de Fibonacci
def fibonacci(Num):
    # Verifica as duas condições mencionadas
    return eh_quadrado_perfeito(5 * Num *Num + 4) or eh_quadrado_perfeito(5 * Num * Num - 4)

# Teste
Numero =int(input('Digite um número: '))
if fibonacci(Numero):
    print(f"{Numero} pertence à sequência de Fibonacci.")
else:
    print(f"{Numero} não pertence à sequência de Fibonacci.")