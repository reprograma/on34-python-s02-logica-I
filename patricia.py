def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

def potenciacao(x, y):
    return x ** y

def eh_impar(numero):
    return numero % 2 != 0

# Entrada dos valores
x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))

# Realizar as operações
resultado_soma = somar(x, y)
resultado_subtracao = subtrair(x, y)
resultado_multiplicacao = multiplicar(x, y)
resultado_divisao = dividir(x, y)
resultado_potenciacao = potenciacao(x, y)

# Verificar se os resultados são ímpares
impar_soma = eh_impar(resultado_soma)
impar_subtracao = eh_impar(resultado_subtracao)
impar_multiplicacao = eh_impar(resultado_multiplicacao)
impar_divisao = eh_impar(resultado_divisao)
impar_potenciacao = eh_impar(resultado_potenciacao)

# Exibir os resultados
print(f"Soma: {resultado_soma} - Ímpar: {impar_soma}")
print(f"Subtração: {resultado_subtracao} - Ímpar: {impar_subtracao}")
print(f"Multiplicação: {resultado_multiplicacao} - Ímpar: {impar_multiplicacao}")
print(f"Divisão: {resultado_divisao} - Ímpar: {impar_divisao}")
print(f"Potenciação: {resultado_potenciacao} - Ímpar: {impar_potenciacao}")
