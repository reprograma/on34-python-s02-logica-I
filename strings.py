nome = "Madu "
sobrenome = "Justino"

print(nome+sobrenome)

conteudo = "Meu ano de nascimento é " + str(2004)  
#converte para string
print(conteudo)

ano_nascimento = 2004 
idade = 2024 - ano_nascimento
print("Minha idade é: ", idade, " anos")

#salario = input("Digite o seu salário: ")
#salario = int(salario)
#salario_ano = salario*12
#print(salario_ano)

# Exercício da aula

num1 =  int(input("Digite o primeiro número: "))
num2 =  int(input("Digite o segundo número: "))

soma = (num1) +  (num2)
mult = num1 * num2
potencia= num1**num2

print("Soma é: ", soma, ", a ultiplicação é: ", mult, "e a potência é: ", potencia)

# Segundo exercício

numero = int(input("Digite um número para descobrirmos se é par ou impar: "))
eh_impar= numero%2
print("O número", numero, "é impar?", bool(eh_impar))
if numero % 2 == 0: 
    print("O número", numero, "é par")
else:
    print("O número", numero, "é impar")