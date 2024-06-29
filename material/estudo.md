# 📚 Estudando

## <a name='Sumrio'></a>Sumário
<!-- vscode-markdown-toc -->
- [📚 Estudando](#-estudando)
  - [Sumário](#sumário)
  - [Exemplos vistos em sala](#exemplos-vistos-em-sala)
  - [Leitura e exercícios](#leitura-e-exercícios)
  - [Playlists](#playlists)
  - [Exercício EXTRA](#exercício-extra)
    - [Sistema de uma empreiteira](#sistema-de-uma-empreiteira)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->


## <a name='Exemplosvistosemsala'></a>Exemplos vistos em sala
- [📂 Pastinha com os exemplos vistos em sala](../exemplos-sala/)

## <a name='Leituraeexerccios'></a>Leitura e exercícios
São indicações de plataformas gerais, legais para passar.
Sempre que encontrarem mais materiais e plataformas, divulguem entre si 🙌

- W3Schools Python: https://www.w3schools.com/python/
- Python Brasil: https://wiki.python.org.br/ListaDeExercicios
- Codecademy Python: https://www.codecademy.com/learn/learn-python-3

## Playlists
Para quem gosta de estudar através de videoaulas, recomendo as seguintes:
Aqui estão algumas playlists do YouTube para estudar Python. Vale escolher uma delas, e assistir 💪

- [Curso de Python 3 - Mundo 1: Fundamentos](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6) - Curso em Vídeo
- [Aulas Python](https://www.youtube.com/playlist?list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe) - Ignorância Zero
- [Curso Python p/ Iniciantes](https://www.youtube.com/playlist?list=PLj7gJIFoP7jdirAFg-fHe9HKOnGLGXSHZ) - Refatorando
- [Curso de Python](https://www.youtube.com/playlist?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR) - CFBCursos
- [Curso Completo de Python](https://www.youtube.com/playlist?list=PLLVddSbilcul-1bAKtMKoL6wOCmDIPzFJ) - Jefferson Lobato


## <a name='Listadeexerccios'></a>Exercício EXTRA
Para quem achou tranquila a atividade para casa, tem esse exercício EXTRA (baseado nos da Wiki de Python) 🙂
Quem quiser fazer, posso corrigir 🙌

### Sistema de uma empreiteira

Crie um conjunto de funções, dessa vez para uma empreiteira. Ele deve contemplar os seguintes requisitos:
- Funções, cada uma delas contendo uma operação
- As saídas devem conter o que o usuário selecionou, mais o resultado final
- As funções devem ser:
1. Conversor de metros para centímetros
   1. Aqui, ele vai poder digitar na sequência a entrada em metros, para ser mostrado depois o valor em centímetros
   2. Mostre a saída informando qual foi o valor de entrada, e qual o de saída
2. Calculadora de área de círculo
   1. Será pedido o raio de um círculo, e depois exibida sua área
3. Calculadora de área de um terreno quadrado 
   1. Aqui, deve se calcular a área do terreno
   2. Também deve se calcular o dobro da área
4. Cálculo de temperatura do local da obra - FaFahrenheit para Celsius
   1.  Peça a entrada em Fahrenheit, e mostre a saída em Celsius
    > C = 5 * ((F-32) / 9). 
5. Cálculo da temperatura do local da obra - Celsius para Fahrenheit
6. Calculadora das horas de trabalho totais dos obreiros
   1. Deve se informar a quantidade de trabalhadores para a obra, quanto cada um ganha por hora, e as horas trabalhadas por mês
   2. Calcule o valor bruto do salário final de um obreiro, e o custo total de salários de todos os obreiros para o mês referido
7. Calculadora do salário líquido de um obreiro
   1. Pergunte quanto um obreiro ganha por hora e o número de horas trabalhadas no mês
   2. De acordo com a [tabela do IR de 2024](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2024), e considerando que a **contribuição ao INSS é de 8%**, e ao **Sindicato é 5%**, retorne na saída:
    ```
    + Salário Bruto : R$ XXXX.XX
    - IR (X%) : R$ XXXX.XX
    - INSS (8%) : R$ XXXX.XX
    - Sindicato ( 5%) : R$ XXXX.XX
    = Salário Liquido : R$ XXXX.XX
    ```
   3. Substitua o que está em X pelo valor adequado
   4. Caso o trabalhador não tenha a renda mínima para o IR, printe o valor em `R$ 0.00`