def calculo_imc(altura, peso):
    imc = peso/(altura**2)
    formatado = "{:.2f}".format(imc)
    print(formatado) #duas casas decimais

print(calculo_imc(1.60, 80)) #chama a função


def gorjeta_garcom(conta):
    gorjeta = conta/10
    return gorjeta
