import math

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

def par_ou_impar(resultado):
    impar = (resultado%2==1)*("O resultado é ímpar")
    par = (not resultado%2==1)*("O resultado é par")
    print(impar + par)

soma = x + y
print("O resultado da soma é", soma)
par_ou_impar(soma)

subtracao = x - y
print("O resultado da subtração é", subtracao)
par_ou_impar(subtracao)

multiplicacao = x * y
print("O resultado da multiplicacao é", multiplicacao)
par_ou_impar(multiplicacao)

divisao = x / y
print("O resultado da divisão é", divisao)
par_ou_impar(divisao)

potenciacao = x ** y
print("O resultado da potenciacao é", potenciacao)
par_ou_impar(potenciacao)

raiz_quadrada_x = math.sqrt(x)
print("O resultado da raiz quadrada de x é", raiz_quadrada_x)
par_ou_impar(raiz_quadrada_x)

raiz_quadrada_y = math.sqrt(y)
print("O resultado da raiz quadrada de y é", raiz_quadrada_y)
par_ou_impar(raiz_quadrada_y)