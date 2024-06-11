import math

print(math.floor(10/30)) #arredonda para baixo
print(math.ceil(10/30)) #arredonda para cima

numero_decimal = 7.9999
print(math.trunc(numero_decimal)) #truncar o numero

x = 2 * (4+8)
print(x)

salario_pessoa1 = 10000
salario_pessoa2 = 3000
salario_pessoa3 = 900

media_salario = (salario_pessoa1+salario_pessoa2+salario_pessoa3)/3
print("A media salario é: ", round(media_salario, 2))

#Convertendo para string

nome ="Williane"
sobrenome = "Fernandes"
conteudo = "Meu ano de nascimento é" + str(1999)

print(nome + " " + sobrenome + ", " + conteudo)
