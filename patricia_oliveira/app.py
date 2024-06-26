def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Divisão por zero não é permitida"
    return x / y

def potenciacao(x, y):
    return x ** y

def eh_impar(numero):
    return numero % 2 != 0

def main():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    resultado_soma = somar(x, y)
    resultado_subtracao = subtrair(x, y)
    resultado_multiplicacao = multiplicar(x, y)
    resultado_divisao = dividir(x, y)
    resultado_potenciacao = potenciacao(x, y)

    operacoes = {
        "soma": resultado_soma,
        "subtração": resultado_subtracao,
        "multiplicação": resultado_multiplicacao,
        "divisão": resultado_divisao,
        "potenciação": resultado_potenciacao
    }

    for operacao, resultado in operacoes.items():
        if isinstance(resultado, (int, float)):  # Verifica se o resultado é um número
            impar = eh_impar(resultado)
            print(f"O resultado da {operacao} ({resultado}) é {'ímpar' if impar else 'par'}")
        else:
            print(f"O resultado da {operacao} não pode ser calculado: {resultado}")

if __name__ == "__main__":
    main()
