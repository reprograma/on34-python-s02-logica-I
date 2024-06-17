import math

# Exercício Semanal Pricila Magalhães

print("\n------------------------------------------")
print("CALCULADORA")
print("------------------------------------------")

print("\n Vamos calcular?")
print("Antes insira dois numeros:")

numero1= float(input("Insira o primeiro número: "))
numero2= float(input("Insira o segundo número: "))

#soma
soma = numero1+ numero2
print("A soma dos dois valores inseridos é: ", soma)
if soma % 2 == 1:
    print(f"O número {soma} é ímpar.")
else:
    print(f"O número {soma} é par.")

#outra opcao- usando bloco math
#somar: (numero1, numero2)
#print("A soma dos dois valores inseridos é: ", soma)

#subtrair
subtracao = numero1- numero2
print("A subtração dos dois valores inseridos (primeiro pelo segundo) é: ", subtracao)
if subtracao % 2 == 0:
    print(f"O número {subtracao} é par.")
else:
    print(f"O número {subtracao} é impar.")

#multiplicar
multiplicacao= numero1*numero2
print("A multiplicação dos dois valores inseridos (primeiro pelo segundo) é: ", multiplicacao)
if multiplicacao % 2 == 0:
    print(f"O número {multiplicacao} é par.")
else:
    print(f"O número {multiplicacao} é ímpar.")

#dividir
divisao= numero1/numero2
print("A divisão dos dois valores inseridos (primeiro pelo segundo) é: ", divisao)
if divisao % 2 == 0:
    print(f"O número {divisao} é par.")
else:
    print(f"O número {divisao} é ímpar.")

#potenciar
potenciacao= numero1**numero2
print("A potenciação dos dois valores inseridos (primeiro pelo segundo) é: ", potenciacao)
if potenciacao % 2 == 0:
    print(f"O número {potenciacao} é par.")
else:
    print(f"O número {potenciacao} é ímpar.")

#tentando outros resultados

resultado = math.pow(numero1, 3) + numero2
print("resultado da equação: ", numero1, "elevado a 3 + ", numero2, "é igual a: ", resultado)

print("\n Viu que calcular pode ser divertido?")
