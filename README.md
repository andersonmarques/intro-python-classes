# Aulas de Python — Técnicas de Programação

Repositório com exemplos, exercícios e notebooks usados nas disciplinas de **Técnicas de Programação**, **Técnicas de Programação I** e **Técnicas de Programação II**.

O material acompanha a introdução à programação com Python, partindo dos conceitos básicos e avançando para estruturas de decisão, repetição e resolução de problemas.

## Conteúdos abordados

- comandos de saída e entrada com `print()` e `input()`;
- variáveis, atribuição e tipagem dinâmica;
- tipos `int`, `float`, `str`, `bool`, `complex`, `list`, `tuple`, `dict` e `set`;
- conversão de tipos e inspeção com `type()`;
- operadores aritméticos, relacionais e lógicos;
- estruturas condicionais com `if`, `elif`, `else` e `match-case`;
- estruturas de repetição com `for` e `while`;
- controle de laços com `break` e `continue`;
- funções, parâmetros, retorno e anotações de tipo;
- somatórios, produtos, fatoriais e cálculos matemáticos;
- exercícios com cálculos financeiros, equação do segundo grau, saldo bancário e classificação de valores.

Os exemplos contextualizados incluem situações de qualidade da água, ocupação de reservatório, qualidade do ar e classificação de solo.

## Organização do repositório

```text
.
├── src
│   ├── aulas
│   │   ├── intro_python_03_08_26.py
│   │   └── tipos_dados.py
│   ├── exercicios
│   │   ├── q22.py
│   │   ├── q36.py
│   │   ├── q47.py
│   │   ├── q48.py
│   │   ├── q81.py
│   │   ├── q82.py
│   │   └── q88.py
│   └── notebooks
│       ├── aula01.ipynb
│       └── notebook_com_python.ipynb
├── LICENSE
└── README.md
```

### Aulas

Os arquivos em `src/aulas` apresentam os conceitos fundamentais da linguagem, com exemplos executáveis e comentários explicativos.

- `intro_python_03_08_26.py`: introdução à linguagem, tipos básicos, operadores, funções e iteração sobre listas;
- `tipos_dados.py`: declaração explícita de tipos e uso de `type()`.

### Exercícios

Os arquivos em `src/exercicios` são programas independentes, executados pelo terminal e geralmente dependentes de dados informados pelo usuário:

| Arquivo | Tema principal |
| --- | --- |
| `q22.py` | total de três produtos a partir de preço e quantidade |
| `q36.py` | delta e raízes de uma equação do segundo grau |
| `q47.py` | classificação de um número em três faixas |
| `q48.py` | depósito e saque em uma conta bancária |
| `q81.py` | contagem de 1 a 100.000 |
| `q82.py` | contagem de números ímpares |
| `q88.py` | contagem de valores entre 100 e 200 até a entrada de zero |

### Notebooks

Os notebooks em `src/notebooks` apoiam as aulas práticas e combinam explicações em Markdown com células de código:

- `aula01.ipynb`: saída, variáveis, tipos de dados, entrada, condicionais, `match-case`, laços, somatórios, produto/fatorial, `break` e `continue`;
- `notebook_com_python.ipynb`: introdução a Python para a disciplina de Técnicas de Programação II.

## Como executar

### Pré-requisitos

- Python 3.10 ou superior, recomendado;
- Jupyter Notebook ou JupyterLab, caso queira executar os arquivos `.ipynb`.

Não há dependências externas específicas: os exemplos usam a biblioteca padrão do Python.

### Executar um arquivo `.py`

Na raiz do repositório, execute:

```bash
python src/aulas/intro_python_03_08_26.py
python src/aulas/tipos_dados.py
python src/exercicios/q22.py
```

Os exercícios que usam `input()` solicitarão os valores no terminal.

> `intro_python_03_08_26.py` contém um exemplo de laço interativo para demonstrar repetição. Responda `n` para encerrá-lo.

O exercício `q81.py` imprime 100.000 números e pode gerar uma saída extensa no terminal.

### Abrir os notebooks

```bash
jupyter notebook
```

Depois, abra um dos arquivos em `src/notebooks` e execute as células na ordem.

## Objetivo didático

Este repositório serve como apoio às aulas e como espaço de experimentação. A recomendação é executar os exemplos, modificar os valores de entrada e observar como cada estrutura da linguagem altera o resultado do programa.

## Licença

Consulte o arquivo [LICENSE](LICENSE) para conhecer os termos de uso deste material.
