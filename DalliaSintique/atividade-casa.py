valor1 = int(input("Digite aqui seu primeiro valor:"))
valor2 = int(input("Digite aqui seu segundo valor:"))

def somar (x,y):
    return x + y 

resultado_soma = somar(valor1,valor2)
print(" O resultado da soma é:" , resultado_soma)
if (resultado_soma%2)==1:
    print(" O valor resultante da soma é impar")
else:
    print(" O valor resultante da soma é par")

def subtrair(x,y):
    return x-y
resultado_subtrair = subtrair(valor1,valor2)
print(" O resultado da subtração é:" , resultado_subtrair)
if (resultado_subtrair % 2)==1:
    print("O valor resultante da subtração é impar")
else:
    print("O valor resultante da subtração é par")

def multiplicar(x,y):
    return x * y
resultado_multiplicar = multiplicar(valor1,valor2)
print("O valor da multiplicação é:" , resultado_multiplicar )
if (resultado_multiplicar %2) ==1:
    print(" O valor resultante da multiplicação é impar")
else:
    print("O valor resultante da multiplicação é par")

def dividir(x,y):
    return x / y
resultado_divisão = dividir(valor1,valor2)
print(" O resultado da divisão é:" , resultado_divisão)
if (resultado_divisão %2) ==1:
    print("O resultado da divisão é impar")
else:
    print("O resultado da divisão é par")

def potencia(x,y):
    return x**y
resultado_potencia = potencia(valor1,valor2)
print("O valor da potenciação é:" , resultado_potencia)
if (resultado_potencia %2) ==1:
    print(" O valor resultante da potenciação é impar")
else:
    print("O valor resultante da potenciação é par")



    