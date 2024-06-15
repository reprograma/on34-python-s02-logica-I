print("Calculadora")
print ("O usuário entrará com dois valores, e após a entrada, serão realizados os cálculos através das funções")

x = input("Informe o primeiro valor = ", )
y = input("informe segundo valor = ", )

x=float(x)
y=float(y)

soma = x + y
subtrair = x - y
dividir = x/y
multiplicar = x*y
potenciação = x**y
if soma % 2 == 0:
    print("O valor da conta é par.")
else:
    print("O valor da conta é ímpar.")

if soma % 2 == 0:
    print(f"O resultado da soma ({soma}) é par.")
else:
    print(f"O resultado da soma ({soma}) é ímpar.")


if subtrair % 2 == 0:
    print(f"O resultado da subtração ({subtrair}) é par.")
else:
    print(f"O resultado da subtração ({subtrair}) é ímpar.")


if multiplicar % 2 == 0:
    print(f"O resultado da multiplicação ({multiplicar}) é par.")
else:
    print(f"O resultado da multiplicação ({multiplicar}) é ímpar.")

if potenciação % 2 == 0:
    print(f"O resultado da potenciação ({potenciação}) é par.")
else:
    print(f"O resultado da potenciação ({potenciação}) é ímpar.")


