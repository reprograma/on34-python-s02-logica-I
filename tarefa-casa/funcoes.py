# tarefa calculadora

# Solicitar dois números do usuário
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Função soma
def somar(x, y):
    return x + y

# Função subtração
def subtrair(x, y):
    return x - y

# Função  multiplicação
def multiplicar(x, y):
    return x * y

# Função divisão
def dividir(x, y):
        return x / y
    
# Função potenciação:
def potenciacao(x, y):
    return x ** y

# Função para verificar se um número é ímpar
def is_impar(numero):
    return numero % 2 != 0

# Calcular e exibir os resultados de todas as operações
print("### Resultados das Operações ###")
print("Soma:", somar(x, y), ", é ímpar:", is_impar(somar(x, y)))
print("Subtração:", subtrair(x, y), ", é ímpar:", is_impar(subtrair(x, y)))
print("Multiplicação:", multiplicar(x, y), ", é ímpar:", is_impar(multiplicar(x, y)))
print("Divisão:", dividir(x, y), ", é ímpar:", isinstance(dividir(x, y), float) and is_impar(dividir(x, y)))
print("Potenciação:", potenciacao(x, y), ", é ímpar:", is_impar(potenciacao(x, y)))
