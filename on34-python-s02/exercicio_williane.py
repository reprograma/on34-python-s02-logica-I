print("**Calculadora da Williane** \n \nPara começar, digite os dois números nos quais deseja realizar os cálculos :)")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 % 2 > 0: 
    print("\nO primeiro número que você digitou é ímpar")
else: 
    print("\nO primeiro número que você digitou é par")

if numero2 % 2 > 0: 
    print("O segundo número que você digitou é ímpar")
else: 
    print("O segundo número que você digitou é par")

def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def potenciacao(numero1, numero2):
    return numero1 ** numero2

def divisao(numero1, numero2):
    return numero1 / numero2

print("\nOperações disponíveis: \n \n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4-Potenciação \n 5-Divisão")

escolha = input("\nAgora, digite o número referente a operação a sua escolha (1-2-3-4-5): ")

if escolha == '1':
    resultado = soma(numero1, numero2)
    print("\nO resultado da soma é:", round(resultado, 2))
elif escolha == '2':
    resultado = subtracao(numero1, numero2)
    print("\nO resultado da subtração é:", round(resultado, 2))
elif escolha == '3':
    resultado = multiplicacao(numero1, numero2)
    print("\nO resultado da multiplicação é:", round(resultado, 2))
elif escolha == '4':
    resultado = potenciacao(numero1, numero2)
    print("\nO resultado da divisão é:", round(resultado, 2))
elif escolha == '5':
    resultado = divisao(numero1, numero2)
    print("\nO resultado da divisão é:",round(resultado, 2))
else:
    print("\nOpção inválida")

if resultado % 2 > 0: 
    print("O resultado do cálculo é impar")
else: 
    print("O resultado do cálculo é par")