# Gerenciamento de Pacotes com o PIP em Python

## <a name='Sumrio'></a>Sumário

<!-- vscode-markdown-toc -->
- [Gerenciamento de Pacotes com o PIP em Python](#gerenciamento-de-pacotes-com-o-pip-em-python)
  - [Sumário](#sumário)
  - [O que é o PIP?](#o-que-é-o-pip)
  - [Instalação do PIP](#instalação-do-pip)
    - [Windows:](#windows)
    - [Linux (Debian/Ubuntu):](#linux-debianubuntu)
  - [Como Usar o PIP](#como-usar-o-pip)
  - [Exemplos de Módulos Importantes](#exemplos-de-módulos-importantes)
  - [Boas Práticas: arquivo `requirements.txt`](#boas-práticas-arquivo-requirementstxt)
  - [Referências externas](#referências-externas)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->


## <a name='OqueoPIP'></a>O que é o PIP?
- PIP é o gerenciador de pacotes padrão para Python. Ele permite instalar, atualizar e remover bibliotecas e módulos externos que não fazem parte da biblioteca padrão da linguagem.
- Através dele, é possível adicionar funcionalidades ao seu projeto Python, como ferramentas para análise de dados, desenvolvimento web, machine learning, etc.

## <a name='InstalaodoPIP'></a>Instalação do PIP
### <a name='Windows:'></a>Windows:
- Certifique-se de ter o Python instalado (https://www.python.org/downloads/windows/)
- Abra o Prompt de Comando (cmd) como administrador
- Execute o comando `python -m ensurepip --upgrade`

### <a name='LinuxDebianUbuntu:'></a>Linux (Debian/Ubuntu):
- Abra o terminal
- Execute o comando `sudo apt install python3-pip`

## <a name='ComoUsaroPIP'></a>Como Usar o PIP
- Instalar um pacote: `pip install nome_do_pacote`
- Atualizar um pacote: `pip install --upgrade nome_do_pacote`
- Desinstalar um pacote: `pip uninstall nome_do_pacote`
- Listar pacotes instalados: `pip list`
- Procurar pacotes: `pip search termo_de_busca`
- Obter informações sobre um pacote: `pip show nome_do_pacote`

## <a name='ExemplosdeMdulosImportantes'></a>Exemplos de Módulos Importantes
| Módulo         | Descrição                                                                                     | Como importar                     | Como usar                                           |
| -------------- | --------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------------------------- |
| numpy          | Biblioteca para computação numérica com arrays multidimensionais.                             | `import numpy as np`              | `arr = np.array([1, 2, 3])`                         |
| pandas         | Biblioteca para análise e manipulação de dados, com estruturas como DataFrames e Series.      | `import pandas as pd`             | `df = pd.read_csv("dados.csv")`                     |
| matplotlib     | Biblioteca para criação de gráficos e visualizações.                                          | `import matplotlib.pyplot as plt` | `plt.plot([1, 2, 3], [4, 5, 6])`                    |
| requests       | Biblioteca para fazer requisições HTTP e interagir com APIs web.                              | `import requests`                 | `response = requests.get("https://www.google.com")` |
| beautifulsoup4 | Biblioteca para extrair dados de arquivos HTML e XML (web scraping).                          | `from bs4 import BeautifulSoup`   | `soup = BeautifulSoup(html_doc, 'html.parser')`     |
| scikit-learn   | Biblioteca para machine learning com algoritmos de classificação, regressão, clustering, etc. | `from sklearn import svm`         | `clf = svm.SVC()`                                   |

## <a name='BoasPrticas:arquivorequirements.txt'></a>Boas Práticas: arquivo `requirements.txt`
- Arquivo `requirements.txt`: Crie um arquivo `requirements.txt` para listar todas as dependências do seu projeto, facilitando a instalação em outras máquinas.

## <a name='Refernciasexternas'></a>Referências externas
- Documentação Oficial do PIP: https://pip.pypa.io/en/stable/
- Guia do Usuário de Empacotamento Python (incluindo PIP): https://packaging.python.org/en/latest/