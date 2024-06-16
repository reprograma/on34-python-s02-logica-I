import math
def conversor_cm(metros):
    centimetros = metros * 100
    print(f"{metros} metros é igual a {centimetros} centímetros")
conversor_cm(float(input("Digite o valor em metros que você quer converter para centímetros: ")))

def area_circulo(raio):
    area = raio ** 2 * math.pi
    print(f"Um círculo de raio igual a {raio} tem área igual a {area}")
area_circulo(float(input("Para calcular a área do círculo, digite o valor do raio: ")))

def area_terreno_quadrado(comprimento, largura):
    area = comprimento * largura
    dobro_area = 2 * area
    print(f"A área de um terreno com comprimento {comprimento} e largura {largura} é {area}")
    print(f"O dobro da área de um terreno com comprimento {comprimento} e largura {largura} é {dobro_area}")
comprimento = float(input("Digite o valor do comprimento do terreno cuja área você quer calcular: "))
largura = float(input("Digite o valor da largura do terreno cuja área você quer calcular: "))
area_terreno_quadrado(comprimento, largura)

def temperatura_obra(temp_fahrenheit):
    temp_celsius = 5 * ((temp_fahrenheit-32) / 9)
    print(f"{temp_fahrenheit}°F é igual a {temp_celsius}°C")
temperatura_obra(float(input("Digite o valor da temperatura do local da obra em Fahrenheit para que seja convertida para Celsius: ")))

def salario_obreiros(qtde_trabalhadores, salario_hora, horas_mes):
    salario_bruto_obreiro = salario_hora * horas_mes
    custo_total_salarios = qtde_trabalhadores * salario_bruto_obreiro
    print(f"O salário bruto mensal de um obreiro é igual a R${salario_bruto_obreiro}")
    print(f"O custo total mensal com salários dos obreiros é igual a R${custo_total_salarios}")
qtde_trabalhadores = int(input("Informe a quantidade de trabalhadores para a obra: "))
salario_hora = float(input("Informe o salário por hora de cada trabalhador: "))
horas_mes = float(input("Informe a quantidade de horas trabalhadas por mês: "))
salario_obreiros(qtde_trabalhadores, salario_hora, horas_mes)

def salario_liquido(salario_hora, horas_mes):
    salario_bruto = salario_hora * horas_mes
    contribuicao_inss = 0.08 * salario_bruto
    contribuicao_sindicato = 0.05 * salario_bruto
    if salario_bruto <= 2259.20:
        sal_liq = salario_bruto - contribuicao_inss - contribuicao_sindicato
        print(f"""+ Salário Bruto : R$ {salario_bruto}
- IR (X%) : R$ 0.00
- INSS (8%) : R$ {contribuicao_inss}
- Sindicato ( 5%) : R$ {contribuicao_sindicato}
= Salário Liquido : R$ {sal_liq}""")
    elif 2259.21 <= salario_bruto <= 2826.65:
        contribuicao_ir = 0.075 * salario_bruto
        sal_liq = salario_bruto - contribuicao_ir - contribuicao_inss - contribuicao_sindicato
        print(f"""+ Salário Bruto : R$ {salario_bruto}
- IR (X%) : R$ {contribuicao_ir}
- INSS (8%) : R$ {contribuicao_inss}
- Sindicato ( 5%) : R$ {contribuicao_sindicato}
= Salário Liquido : R$ {sal_liq}""")
    elif 2826.66 <= salario_bruto <= 3751.05:
        contribuicao_ir = 0.15 * salario_bruto
        sal_liq = salario_bruto - contribuicao_ir - contribuicao_inss - contribuicao_sindicato
        print(f"""+ Salário Bruto : R$ {salario_bruto}
- IR (X%) : R$ {contribuicao_ir}
- INSS (8%) : R$ {contribuicao_inss}
- Sindicato ( 5%) : R$ {contribuicao_sindicato}
= Salário Liquido : R$ {sal_liq}""")
    elif 3751.06 <= salario_bruto <= 4664.68:
        contribuicao_ir = 0.225 * salario_bruto
        sal_liq = salario_bruto - contribuicao_ir - contribuicao_inss - contribuicao_sindicato
        print(f"""+ Salário Bruto : R$ {salario_bruto}
- IR (X%) : R$ {contribuicao_ir}
- INSS (8%) : R$ {contribuicao_inss}
- Sindicato ( 5%) : R$ {contribuicao_sindicato}
= Salário Liquido : R$ {sal_liq}""")
    else:
        contribuicao_ir = 0.275 * salario_bruto
        sal_liq = salario_bruto - contribuicao_ir - contribuicao_inss - contribuicao_sindicato
        print(f"""+ Salário Bruto : R$ {salario_bruto}
- IR (X%) : R$ {contribuicao_ir}
- INSS (8%) : R$ {contribuicao_inss}
- Sindicato ( 5%) : R$ {contribuicao_sindicato}
= Salário Liquido : R$ {sal_liq}""")
salario_hora = float(input("Informe o salário por hora do obreiro: "))
horas_mes = float(input("Informe a quantidade de horas trabalhadas por mês pelo obreiro: "))
salario_liquido(salario_hora, horas_mes)