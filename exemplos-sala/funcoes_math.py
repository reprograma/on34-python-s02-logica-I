import math

print(math.ceil(10/3)) # arredonda pra cima
print(math.floor(10/3)) # arredonda pra baixo

numero_decimal = 7.999999
print(math.trunc(numero_decimal)) # "truncar" número, remover a parte decimal

x = 2*(4+8) # resultado é 24 (primeiro o valor dos parênteses é executado)
print(x)

y = 2*4+8 # resultado é 16
print(y)

'''
Exercício
'''
# eu ganho 10000
# minha esposa ganha 3000
# meu filho ganhe 900
# qual a renda mensal da minha casa?
# renda média (média de todos os salários)

renda_maiara = 10000
renda_esposa = 3000
renda_filho = 900

total_rendas = (renda_maiara+renda_esposa+renda_filho)
renda_media = total_rendas/3

print("A soma dos salários é R$", total_rendas, ", e a renda média é R$", renda_media)

# Precedência das operações

x = 4 * 2 + 5 
print(x)

x = (2**2 + 1) * 3 # ordem de execução dos operadores