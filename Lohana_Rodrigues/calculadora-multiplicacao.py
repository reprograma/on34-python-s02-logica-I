x = (int(input("Por favor, digite o primeiro número: ")))
y = (int(input("Por favor, digite o segundo número: ")))
resultado_da_multiplicacao= x * y
numero_impar= resultado_da_multiplicacao % 2
print("O resultado da multiplicação é: ", resultado_da_multiplicacao)
if numero_impar == 1:
    print("O valor calculado é um número ímpar")
else:
    print("O valor calculado não é um número ímpar")