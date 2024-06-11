print('Iniciando nova aba')
import math

print(pow(3, 2)) #ou **

# impar ou par
print(10%3)

valor = 21/4
valor_arredondado = round(valor, 2)
print(valor_arredondado)

valor = 20/6
print(math.floor(valor))
print(math.ceil(valor))

numero_decimal = 7.483
print(math.trunc(numero_decimal)) #remove a parte decimal

x = 21*3+9
print(x)

sal1= 10000
sal2= 3000
sal3= 90

renda_total = sal1+sal2+sal3
renda_per_capita = (renda_total/3)

print("A renda per capita da família é: R$", round(renda_per_capita,2))