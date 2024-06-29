'''
EXERCÍCIO EXTRA
Descrição do exercício: https://github.com/reprograma/on34-python-s02-logica-I/blob/main/material/estudo.md#exerc%C3%ADcio-extra
'''

import math

def metros_para_centimetros():
    # converte metros para centímetros e exibe o resultado
    metros = float(input("📏 digite o valor em metros: "))
    centimetros = metros * 100
    print(metros, "metros equivalem a", centimetros, "centímetros 📏")

def area_circulo():
    # calcula e exibe a área de um círculo a partir do raio
    raio = float(input("⭕ digite o raio do círculo: "))
    area = math.pi * raio**2
    print("a área do círculo com raio", raio, "é", format(area, ".2f") + " ⭕")

def area_terreno_quadrado():
    # calcula e exibe a área de um terreno quadrado e o dobro da área
    lado = float(input("🟩 digite o lado do terreno quadrado: "))
    area = lado**2
    dobro_area = 2 * area
    print("a área do terreno é", format(area, ".2f"), "e o dobro da área é", format(dobro_area, ".2f") + " 🟩")

def fahrenheit_para_celsius():
    # converte temperatura de fahrenheit para celsius e exibe o resultado
    fahrenheit = float(input("🌡️ digite a temperatura em fahrenheit: "))
    celsius = 5 * ((fahrenheit - 32) / 9)
    print(fahrenheit, "graus fahrenheit equivalem a", format(celsius, ".2f"), "graus celsius 🌡️")

def celsius_para_fahrenheit():
    # converte temperatura de celsius para fahrenheit e exibe o resultado
    celsius = float(input("🌡️ digite a temperatura em celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(celsius, "graus celsius equivalem a", format(fahrenheit, ".2f"), "graus fahrenheit 🌡️")

def calcular_salarios():
    # calcula os salários brutos e líquidos dos trabalhadores
    num_trabalhadores = int(input("👷 digite o número de trabalhadores: "))
    valor_hora = float(input("💰 digite o valor da hora trabalhada: "))
    horas_trabalhadas = float(input("🕒 digite o número de horas trabalhadas por mês: "))

    salario_bruto = valor_hora * horas_trabalhadas
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05

    # Cálculo do IR (tabela simplificada para 2024)
    if salario_bruto <= 2259.2:
        ir = 0
    elif salario_bruto <= 2826.65:
        ir = salario_bruto * 0.075 - 169.44
    elif salario_bruto <= 3751.05:
        ir = salario_bruto * 0.15 - 381.44
    elif salario_bruto <= 4664.68:
        ir = salario_bruto * 0.225 - 662.7
    else:
        ir = salario_bruto * 0.275 - 896.36

    salario_liquido = salario_bruto - ir - inss - sindicato

    print("\n💼 cálculo de salário:")
    print("+ salário bruto: R$", format(salario_bruto, ".2f"))
    print("- ir (", format(ir/salario_bruto, ".1%"), "): R$", format(ir, ".2f"))
    print("- inss (8%): R$", format(inss, ".2f"))
    print("- sindicato (5%): R$", format(sindicato, ".2f"))
    print("= salário líquido por trabalhador: R$", format(salario_liquido, ".2f"))

    custo_total = salario_bruto * num_trabalhadores
    print("\ncusto total de salários: R$", format(custo_total, ".2f"))

# Loop principal do programa
while True:
    print("\n----------------------------------------------------------"
          +"\n👷 SISTEMA PARA EMPREITEIRA CANTINHO DA CONSTRUTORA! 🚧\n"
          +"----------------------------------------------------------")
    print("Escolha uma opção:")
    print("1. Metros Para Centímetros 📏")
    print("2. Área Do Círculo ⭕")
    print("3. Área Do Terreno Quadrado 🟩")
    print("4. Fahrenheit Para Celsius 🌡️")
    print("5. Celsius Para Fahrenheit 🌡️")
    print("6. Calcular Salários 💼")
    print("0. Sair 👋")

    opcao = input("opção: ")

    if opcao == '1':
        metros_para_centimetros()
    elif opcao == '2':
        area_circulo()
    elif opcao == '3':
        area_terreno_quadrado()
    elif opcao == '4':
        fahrenheit_para_celsius() 
    elif opcao == '5': 
        celsius_para_fahrenheit()
    elif opcao == '6':
        calcular_salarios()
    elif opcao == '0':
        print("até mais! 🤝")
        break
    else:
        print("opção inválida ❌")