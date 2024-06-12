# Calculadora

import math

str(input ('Vamos calcular 🧮⬇️            '))

#Soma
x = float(input('Digite um número: '))
y = float(input('Digite outro número: '))
x = math.floor(x)
y = math.floor(y)
soma = x + y
print('Soma:\n', x, '+', y, '=', soma)

if soma % 2 == 0: print(soma, 'é um número par')
else: print(soma, 'é um número ímpar')

#Subtração
subtração = x - y
print('Subtração:\n', x, '-', y,'é igual a', subtração)

if subtração % 2 == 0: print(subtração, 'é um número par')
else: print(subtração, 'é um número ímpar')

#Multiplicação
multiplicação = x * y
print('Multiplicação:\n', x, '*', y,'=', multiplicação)

if multiplicação % 2 == 0: print(multiplicação, 'é um número par')
else: print(multiplicação, 'é um número ímpar.')

#Divisão
divisão = x / y
divisão = int (divisão)
print('Divisão:\n', x, '/', y,'=',divisão)

if divisão % 2 == 0: print(divisão, 'é um número par')
else: print(divisão, 'é um número ímpar')

#Potenciação
potenciação = x ** y
print('Potenciação:\n', x, '^', y,'=',potenciação)

if potenciação % 2 == 0: print(potenciação, 'é um número par')
else: print(potenciação, 'é um número ímpar')