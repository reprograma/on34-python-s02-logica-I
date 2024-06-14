"""
O usuário entrará com dois valores, e será necessário realizar o cálculo deles através destas funções:

"""
# Funções

# somar(x, y): recebe dois números e retorna a soma.
def somar (x, y):
    Resultado = x + y
    print (Resultado)

    impar (Resultado)

# subtrair(x, y): recebe dois números e retorna a subtração.
def subtrair (x, y):
    Resultado = x - y
    print (Resultado)

    impar (Resultado)

# multiplicar(x, y): recebe dois números e retorna a multiplicação.
def multiplicar (x, y):
    Resultado = x * y
    print (Resultado)

    impar (Resultado)

# dividir(x, y): recebe dois números e retorna a divisão do primeiro pelo segundo.
def dividir (x, y):
    Resultado = x / y
    print (Resultado)

    impar (Resultado)

# potenciação(x, y): receber dois números e elevar o primeiro pelo segundo.
def potenciacao (x, y):
    Resultado = x ** y
    print (Resultado)

    impar (Resultado)

# Função que verifica se o resultado é impar
def impar(Resultado):
    if Resultado % 2 == 0:
        print (Resultado, " É par")
    else:
        print (Resultado, " É impar")

# Entrada dos Valores
x = int(input("Digite um número"))
y = int(input("Digite outro número"))


