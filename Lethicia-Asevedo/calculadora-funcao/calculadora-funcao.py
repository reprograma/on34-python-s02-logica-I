print("""
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
""")

print("Olá, seja bem vindo a calculadora! As operações seguem a seguinte ordem: ")
print("""\n
         1 - Soma\n
         2 - Subtração\n
         3 - Divisão\n
         4 - Multiplicação\n
         5 - Potenciação
      """)



#Essa função realiza a soma de dois valores digitados pelo usuário.
def soma(x,y):
    return x + y

x = (int(input("Digite o primeiro valor: ")))
y = (int(input("Digite o segundo valor: ")))
resultado = soma(x,y)
impar = resultado %2
print("O resultado da sua soma é", resultado)

#Essa condição criada ao pé de cada função indica se o valor resultante é ímpar ou não.
if resultado % 2 == 0:
    print("O valor resultante da sua operação não é um número ímpar")
else:
    print("O valor resultante da sua operação é ímpar")


#Essa função realiza a subtração de dois valores digitados pelo usuário.
def subtracao(x,y):
    return x - y 
x = (int(input("Digite o primeiro valor: ")))
y = (int(input("Digite o segundo valor: ")))
resultado = subtracao(x,y)
impar = resultado %2
print("O resultado da sua subtração é", resultado)

if resultado % 2 == 0:
    print("O valor resultante da sua operação não é um número ímpar")
else:
    print("O valor resultante da sua operação é ímpar")


#Essa função realiza a divisão de dois valores digitados pelo usuário.
def divisao(x,y):
    return x / y
x = (int(input("Digite o primeiro valor: ")))
y = (int(input("Digite o segundo valor: ")))
resultado = divisao(x,y)
impar = resultado %2
print("O resultado da sua divisão é", resultado)

if resultado % 2 == 0:
    print("O valor resultante da sua operação não é um número ímpar")
else:
    print("O valor resultante da sua operação é ímpar")


#Essa função realiza a multiplicação de dois valores digitados pelo usuário.
def multiplicacao(x,y):
    return x * y 
x = (int(input("Digite o primeiro valor: ")))
y = (int(input("Digite o segundo valor: ")))
resultado = multiplicacao(x,y)
impar = resultado %2
print("O resultado da sua multiplicação é", resultado)

if resultado % 2 == 0:
    print("O valor resultante da sua operação não é um número ímpar")
else:
    print("O valor resultante da sua operação é ímpar")

#Essa função recebe o primeiro valor digitado pelo usuário, e o eleva a 
#potência do segundo valor digitado pelo usuário. 
def potenciacao(x,y):
    return x ** y
x = (int(input("Digite o primeiro valor: ")))
y = (int(input("Digite o segundo valor: ")))
resultado = potenciacao(x,y)
impar = resultado %2
print("O resultado da sua potenciação é", resultado)

if resultado % 2 == 0:
    print("O valor resultante da sua operação não é um número ímpar")
else:
    print("O valor resultante da sua operação é ímpar")



print("""
███████╗██╗███╗░░░███╗
██╔════╝██║████╗░████║
█████╗░░██║██╔████╔██║
██╔══╝░░██║██║╚██╔╝██║
██║░░░░░██║██║░╚═╝░██║
╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝"
      """)
