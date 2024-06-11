# ______________CALCULADORA______________--

entrada1 = input("Usuário, informe o primeiro valor: ")
entrada2 = input("Usuŕio, informe o segundo valor: ")

num01 = float(entrada1)
num02 = float(entrada2)

soma = (num01)+(num02)
print(soma)

if soma % 2 == 0:
    print("O resultado acima é par")
else:
    print("O resultado acima é ímpar")

sub = (num01)-(num02)
print(sub)

if sub % 2 == 0:
    print("O resultado acima é par")
else:
    print("O resultado acima é ímpar")

mult = (num01)*(num02)
print(mult)

if mult % 2 == 0:
    print("O resultado acima é par")
else:
    print("O resultado acima é ímpar")

divisao = (num01)/(num02)
print(divisao)

if divisao % 2 == 0:
    print("O resultado acima é par")
else:
    print("O resultado acima é ímpar")

pot = num01**(num02)
print(pot)

if pot % 2 == 0:
    print("O resultado acima é par")
else:
    print("O resultado acima é ímpar")


