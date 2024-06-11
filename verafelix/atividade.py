# somar(x, y): recebe dois números e retorna a soma.
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
soma = (x+y)
eh_impar = soma%2
eh_impar = bool (eh_impar)
print("O resultado da soma", soma, "é ímpar?", eh_impar)

# subtrair(x, y): recebe dois números e retorna a subtração.
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
subtrair = (x-y)
eh_impar = subtrair%2
eh_impar = bool (eh_impar)
print("O resultado da subtração", subtrair, "é ímpar?", eh_impar)

# multiplicar(x, y): recebe dois números e retorna a multiplicação.
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
multiplicacao = (x*y)
eh_impar = multiplicacao%2
eh_impar = bool (eh_impar)
print("O resultado da multiplicação", multiplicacao, "é ímpar?", eh_impar)

# dividir(x, y): recebe dois números e retorna a divisão do primeiro pelo segundo
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
divisao = (x/y)
eh_impar = divisao%2
eh_impar = bool (eh_impar)
print("O resultado da divisão", divisao, "é ímpar?", eh_impar)

# potenciação(x, y)
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
potenciacao = (x**y)
eh_impar = potenciacao%2
eh_impar = bool (eh_impar)
print("O resultado da potenciação", potenciacao, "é ímpar?", eh_impar)