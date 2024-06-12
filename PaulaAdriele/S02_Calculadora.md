## Exercício para casa: Calculadora

#separador para organização
espaco = "________________________"

# Somar(x, y): recebe dois números e retorna a soma.

print(espaco)

#Calculadora Soma
print("Esta é a nossa calculadora de soma")
numero1 = int(input("Digite o número 1:"))
numero2 = int(input("Digite o número 2:"))
soma = ((numero1) + (numero2))
print("O valor total da sua soma é:", soma)
if soma %2==0:
  print("A sua soma é um número par.")
else:
  print("A sua soma é um número ímpar.")

print(espaco)

#subtrair(x, y): recebe dois números e retorna a subtração.

#Calculadora Subtração
print("Esta é a nossa calculadora de subtração")
numero3 = int(input("Digite o número 1:"))
numero4 = int(input("Digite o número 2:"))
soma2 = ((numero3) - (numero4))
print("O valor total da sua subtração é:", soma2)
if soma2 %2==0:
  print("A sua subtração é um número par.")
else:
  print("A sua subtração é um número ímpar.")

print(espaco)

#multiplicar(x, y): recebe dois números e retorna a multiplicação.

#Calculadora multiplicação
print("Esta é a nossa calculadora de multiplicação")
numero5 = int(input("Digite o número 1:"))
numero6 = int(input("Digite o número 2:"))
soma3 = ((numero5) * (numero6))
print("O valor total da sua multiplicação é:", soma3)
if soma3 %2==0:
  print("A sua multiplicação é um número par.")
else:
  print("A sua multiplicação é um número ímpar.")

print(espaco)

#dividir(x, y): recebe dois números e retorna a divisão do primeiro pelo segundo

#Calculadora divisão
print("Esta é a nossa calculadora de divisão")
numero7 = int(input("Digite o número 1:"))
numero8 = int(input("Digite o número 2:"))
soma4 = ((numero7) / (numero8))
print("O valor total da sua divisão é:", soma4)
if soma4 %2==0:
  print("A sua divisão é um número par.")
else:
  print("A sua divisão é um número ímpar.")

print(espaco)

#potenciação(x, y)

#Calculadora potenciação
print("Esta é a nossa calculadora de potenciação")
numero9 = int(input("Digite o número 1:"))
numero10 = int(input("Digite o número 2:"))
soma5 = ((numero9) ** (numero10))
print("O valor total da sua potenciação é:", soma5)
if soma5 %2==0:
  print("A sua potenciação é um número par.")
else:
  print("A sua potenciação é um número ímpar.")

print(espaco)

#trazer se o número resultante de cada operação é ímpar

#Descobrindo se o número é par ou ímpar
print("Descubra se seu número é par ou ímpar")
numero11 = int(input("Digite um número"))
impar = numero11%2
impar = bool(impar)
print("O número ", numero11, "é ímpar?", impar)

