print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potenciação")

operacao = int(input("Selecione a operação "))
if (operacao > 0 and operacao <= 5):

    n1 = int(input("digite o primeiro número "))
    n2 = int(input("digite o segundo número "))

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

    def e_impar(x):
        resto = x % 2 

        if resto == 0: 
            return False
        else: 
            return True

    if operacao == 1:
        resultado = somar(n1, n2)
        print("O resultado é: ", resultado)
        if e_impar(resultado):
            print("O resultado é ímpar.")
        else:
            print("O resultado não é ímpar.") 
    if operacao == 2:
        resultado = subtrair(n1, n2)
        print("O resultado é: ", resultado)
        if e_impar(resultado):
            print("O resultado é ímpar.")
        else:
            print("O resultado não é ímpar.") 
    if operacao == 3:
        resultado = multiplicar(n1, n2)
        print("O resultado é: ", resultado)
        if e_impar(resultado):
            print("O resultado é ímpar.")
        else:
            print("O resultado não é ímpar.") 
    if operacao == 4:
        resultado = dividir(n1, n2)
        print("O resultado é: ", resultado)
        if e_impar(resultado):
            print("O resultado é ímpar.")
        else:
            print("O resultado não é ímpar.") 
    if operacao == 5:
        resultado = potenciacao(n1, n2)
        print("O resultado é: ", resultado)
        if e_impar(resultado):
            print("O resultado é ímpar.")
        else:
            print("O resultado não é ímpar.") 
else:
    print("Operação inválida.")
