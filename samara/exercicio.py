#soma
valor_1 = int(input("Digite primeiro número da soma: "))
valor_2= int(input("Digite segundo número da soma: "))

soma = valor_1 + valor_2
print(soma)

def eh_impar(num):
    return num % 2 != 0

if eh_impar(soma):
    print ("A soma é ", soma, "ímpar")
else:
    print ("A soma ", soma, "é par")

#subtração
valor_1 = int(input("Digite primeiro número da subtração: "))
valor_2= int(input("Digite segundo número da subtração: "))

subtracao = valor_1 - valor_2
print(subtracao)

def eh_impar(num):
    return num % 2 != 0

if eh_impar(subtracao):
    print ("A subtração é ", subtracao, "ímpar")
else:
    print ("A subtração ", subtracao, "é par")

#multiplicação
valor_1 = int(input("Digite primeiro número da multiplicação: "))
valor_2= int(input("Digite segundo número da multiplicação: "))

multiplicacao = valor_1 * valor_2
print(multiplicacao)

def eh_impar(num):
    return num % 2 != 0

if eh_impar(multiplicacao):
    print ("A multiplicação é ", multiplicacao, "ímpar")
else:
    print ("A multiplicação ", multiplicacao, "é par")

#divisão
valor_1 = float(input("Digite primeiro número da divisão: "))
valor_2= float(input("Digite segundo número da divisão: "))

divisao = valor_1 / valor_2
print(divisao)

def eh_impar(num):
    return num % 2 != 0

if eh_impar(divisao):
    print ("A divisão é ", divisao, "ímpar")
else:
    print ("A divisão ", divisao, "é par")

#potencia
valor_1 = int(input("Digite primeiro número da potência: "))
valor_2= int(input("Digite segundo número da potência: "))

potencia = valor_1 ** valor_2
print(potencia)

def eh_impar(num):
    return num % 2 != 0

if eh_impar(potencia):
    print ("A potência é ", potencia, "ímpar")
else:
    print ("A potência ", potencia, "é par")
