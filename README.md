<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Variáveis, tipos, operadores e funções

Turma Online On34 | Python | Semana 02 | 2024 | <a href="https://www.linkedin.com/in/maiarar/" target="_blank" rel="noopener noreferrer">Professora Maiara Rodrigues</a>

## <a name='Instrues'></a>Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)

## <a name='Resumo'></a>Resumo
<!-- vscode-markdown-toc -->
- [Variáveis, tipos, operadores e funções](#variáveis-tipos-operadores-e-funções)
  - [Instruções](#instruções)
  - [Resumo](#resumo)
  - [Conteúdo](#conteúdo)
    - [⚙️ Configurando o ambiente](#️-configurando-o-ambiente)
    - [1. Tipos de variáveis](#1-tipos-de-variáveis)
    - [2. Interação com o usuário](#2-interação-com-o-usuário)
    - [3. Operadores](#3-operadores)
      - [Operadores Aritméticos](#operadores-aritméticos)
      - [Operadores Comparativos](#operadores-comparativos)
      - [Operadores de Atribuição:](#operadores-de-atribuição)
      - [Operadores Lógicos:](#operadores-lógicos)
      - [Demais operadores](#demais-operadores)
    - [5. Funções de Conversão de Tipo](#5-funções-de-conversão-de-tipo)
    - [6. Módulo math](#6-módulo-math)
    - [7. Funções](#7-funções)
    - [8. Comentários](#8-comentários)
  - [📚 Estudando](#-estudando)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Contedo'></a>Conteúdo

### <a name='Configurandooambiente'></a>⚙️ Configurando o ambiente
1. **Instalar a Extensão Python**
- Abra o VSCode
- Clique no ícone de extensões na barra lateral (ou pressione Ctrl+Shift+X)
- Pesquise por "Python" e instale a extensão oficial da Microsoft

2. **Abrir o Terminal**
- Clique em "Exibir" na barra de menu superior
- Selecione "Terminal"
- Para quem usa Windows: selecionar *Git Bash*

### <a name='Tiposdevariveis'></a>1. Tipos de variáveis
| Tipo    | Descrição                                              | Exemplo           |
| ------- | ------------------------------------------------------ | ----------------- |
| `int`   | Números inteiros (positivos, negativos e zero)         | `idade = 30     ` |
| `float` | Números com casas decimais (ponto flutuante)           | `altura = 1.75  ` |
| `str`   | Sequência de caracteres (texto)                        | `nome = "Ada" `   |
| `bool`  | Valores lógicos: True (verdadeiro) ou False    (falso) | `aprovado = True` |

### <a name='Interaocomousurio'></a>2. Interação com o usuário
- `print()`: Exibe informações na tela.
```   
print("Olá, mundo!")
print(idade, altura)  # Exibe múltiplos valores
```
- `input()`: Lê dados digitados pelo usuário (sempre como string).
```
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))  # Converte para int
```

### <a name='OperadoresAritmticos'></a>3. Operadores

#### Operadores Aritméticos
Usados para realizar operações matemáticas básicas.
| Operador | Descrição       | Exemplo |
| -------- | --------------- | ------- |
| +        | Soma            | 5 + 3   |
| -        | Subtração       | 10 - 2  |
| *        | Multiplicação   | 4 * 6   |
| /        | Divisão         | 15 / 3  |
| **       | Potenciação     | 2** 3   |
| %        | Módulo (resto)  | 10 % 3  |
| //       | Divisão Inteira | 10 // 3 |

#### Operadores Comparativos
Usados para comparar dois valores e retornar um resultado booleano (`True` ou `False`).
| Operador | Descrição        | Exemplo (resultado) |
| -------- | ---------------- | ------------------- |
| ==       | Igual a          | 5 == 5 (True)       |
| !=       | Diferente de     | 5 != 3 (True)       |
| >        | Maior que        | 10 > 8 (True)       |
| <        | Menor que        | 3 < 7 (True)        |
| >=       | Maior ou igual a | 6 >= 6 (True)       |
| <=       | Menor ou igual a | 2 <= 1 (False)      |


#### Operadores de Atribuição:
Usados para atribuir valores a variáveis.
| Operador | Descrição                    | Exemplo | Equivalente a |
| -------- | ---------------------------- | ------- | ------------- |
| =        | Atribuição simples           | x = 5   | x = 5         |
| +=       | Adição e atribuição          | x += 3  | x = x + 3     |
| -=       | Subtração e atribuição       | x -= 2  | x = x - 2     |
| *=       | Multiplicação e atribuição   | x *= 4  | x = x * 4     |
| /=       | Divisão e atribuição         | x /= 2  | x = x / 2     |
| //=      | Divisão inteira e atribuição | x //= 3 | x = x // 3    |
| %=       | Módulo e atribuição          | x %= 5  | x = x % 5     |
| **=      | Exponenciação e atribuição   | x **= 2 | x = x ** 2    |

#### Operadores Lógicos:

Usados para combinar expressões booleanas e retornar um resultado booleano.

| Operador | Descrição                                                     | Exemplo        | Resultado |
| -------- | ------------------------------------------------------------- | -------------- | --------- |
| and      | Retorna True se ambas as expressões forem verdadeiras.        | True and False | False     |
| or       | Retorna True se pelo menos uma das expressões for verdadeira. | True or False  | True      |
| not      | Inverte o resultado da expressão.                             | not True       | False     |

#### Demais operadores
Temos demais operadores ([bit a bit](https://ealexbarros.medium.com/opera%C3%A7%C3%B5es-bit-a-bit-bitwise-em-python-e75624ce0611), [de associação](https://prensali.substack.com/p/como-usar-operadores-de-associacao-no-python), [de identidade](https://prensali.substack.com/p/como-usar-operadores-de-identidade-no-python)), mas não vamos passar por eles por enquanto 🐍

### <a name='FunesdeConversodeTipo'></a>5. Funções de Conversão de Tipo
- `int(x):` Converte x para um número inteiro (se possível).
- `float(x):` Converte x para um número de ponto flutuante (se possível).
- `str(x):` Converte x para uma string (texto).
- `bool(x):` Converte x para um valor booleano (True ou False).


### <a name='Mdulomath'></a>6. Módulo math
Fornece funções matemáticas, como:
- `math.sqrt(x):` Calcula a raiz quadrada de x.
- `math.pi`: Constante com o valor de pi (π).
- `math.sin(x)`, `math.cos(x)`, `math.tan(x):` Funções trigonométricas.
- `math.log(x)`, `math.log10(x):` Funções logarítmicas.
Exemplo:
```
raiz = math.sqrt(16)
print(raiz)  # Saída: 4.0
```

### <a name='Funes'></a>7. Funções
Blocos de código reutilizáveis que executam tarefas específicas. Veja o exemplo:
```
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Alice")  # Chama a função
```

### <a name='Comentrios'></a>8. Comentários
Usados para explicar o código e são ignorados pelo interpretador do Python.
- Comentário de linha única: `# Isto é um comentário`
- Comentário de múltiplas linhas:
```
    '''
    Este é um comentário
    de várias linhas
    '''
```

## <a name='Sugestesdemyateriais'></a>📚 Estudando
Para ver dicas de materiais, e de estudo, veja esse arquivo com materiais de dicas!
- [Dicas para estudo!](./material/estudo.md)


<p align="center">
Desenvolvido com :purple_heart:
</p>