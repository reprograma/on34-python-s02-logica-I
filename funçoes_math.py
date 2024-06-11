import math

print(math.floor(10/3)) #arredonda para cima
print(math.ceil(10/3)) #arredonda para baixo

numero_decimal = 7.1618
print(math.trunc(numero_decimal)) # "truncar" numero, remover a parte decimal

x = 2 * (4+8) # resultado = 24(primeiro o valor dos parenteses é executado)
print(x)

y = 2*4+8 #resultado 16
print(y)

# eu ganho 10000
# minha esposa ganha 3000
# meu filho ganha 900
# qual a renda mensal da minha casa?
# renda média (média de todos os salários)

valor_renda = (10000+3000+900)
valor_media = (valor_renda/3)
valor_media = round(valor_media, 2)

print("A soma dos salários é R$", valor_renda, ", e a renda média", valor_media)

# Precedência das operações