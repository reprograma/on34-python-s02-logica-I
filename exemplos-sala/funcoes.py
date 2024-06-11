def calculo_imc(altura, peso):
    imc = peso/(altura**2)
    # print(imc)

def calculo_imc_retorno(altura, peso):
    imc = peso/altura**2
    return imc

# calculo_imc(1.60, 80)
# print(calculo_imc_retorno(1.60, 80))

retorno_funcao = calculo_imc(1.60, 40)
print(retorno_funcao)

retorno_funcao = calculo_imc_retorno(1.60, 40)
print(retorno_funcao)

#########

def desconto_salario(salario):
    salario = (salario/10)*3
    print("O desconto será de", salario)

# quando eu for chamar
desconto_salario(1200)

# -----

def gorjeta_garcom(conta): #nome funcao
    gorjeta = conta/10 
    return gorjeta

# quando eu for chamar
print(gorjeta_garcom(456))