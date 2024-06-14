
''' Inte e Float '''
print ("olá mundo")

print (3*3)

print (type(3.9))

numero1 = 1
print (numero1)
print ("O tipo de variavel numero é: ", type (numero1))

numero2 = 7.4
print (numero2)
print ("O tipo de variavel numero é: ", type (numero2))

soma = numero1+numero2
print (soma)
print ("O tipo de variavel numero é: ", type (soma))

# Booleano
trouxe_carteira = False
print ("O tipo de variavel numero é: ", type (trouxe_carteira))

# String
# texto = "valor com aspas duplas"
# texto = 'valor com aspas simples'
# texto = '''valor com 3 aspas simples'''

texto = "pipoca de cinema"
print(texto)
print ("O tipo de variavel numero é: ", type (texto))

#harry potther
texto = '"Palavras são , na minha nada opinião humilde, nossa inesgotável fonte de magia . Capazes de formar grandes sofrimentos e também de remediá-los - Alvo Dumbledore"'
print(texto)

# INPUTS
entrada = input("Digite um texto: ")
print("O valor do input é:", entrada)

#Nome das variáveis
'''exemplo1234= True --> Apenas nomes e números, começar por uma letra
No código (variável) não usa acento, nem utilizar caracteres especiais, exceto _
sempre descrever bem as variaveis'''

print('"olá,Giovana"')

entrada1 = input("o valor da entrada é:")
entrada2 = input("o valor da entrada é:")

print(type(entrada1))
print(type(entrada2))

concat = entrada1+entrada2
print(concat)
print("tipo do concat",type(concat))

print(1+3) #soma
print(30-90) #subtração
print(5*10) #multiplicação
print(10/3) #divisão

print(3**2) #exponenciação
print(pow(3, 2)) #exponenciação

print(10%3)

valor = 10/3
valor_arredondado = round(valor, 2)
print(valor_arredondado)

valor_arredondado_para_baixo = float(valor)
print(valor_arredondado_para_baixo)

import math

print(math.floor(10/3))

print(math.ceil(10/3)) #arredonda pra cima
print(math.floor(10/3)) #arredonda pra baixo

numero_decimal = 7.12334
print(math.trunc(numero_decimal)) #truncar número, remover a parte decimal)

x = 2*(4+8)
print(x)
#resultado: 24 (primeiro o valor dos p arenteses é executado)

#eu ganho 10000, minha esposa 3000, meu filho 900
#qual a renda média de todos salarios?

valor1 = 10000
valor2 = 3000
valor3 = 900
print((valor1+valor2+valor3/3))

renda_minha = 10000
renda_esposa = 3000
renda_filho = 900

total_rendas = (renda_minha+renda_esposa+renda_filho)
renda_media = total_rendas/3

print("A soma dos salários é R$", total_rendas, ", e a renda média é R$", renda_media)

#Strings
nome = "Giovana"
sobrenome = "Gomes"

print( nome +" " + sobrenome )

conteudo = "Meu ano de nascimento é " + str(1997)
#converte print pra string
print(conteudo)

ano_nascimento = 1997
idade = 2024 - ano_nascimento
print(" minha idade é: " + idade)

print(bool(0))
print(bool(1))
print(bool("conteudo")) #True
print(bool("")) #False
print(bool(-200)) #True


