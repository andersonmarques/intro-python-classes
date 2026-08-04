# Lista de Exercícios de Algoritmos

### Autores:
* Professor Anderson Soares, PhD.
* Professor Odlaniger Lourenço D. Monteiro, M.Sc.

📄 [Acessar o PDF original](https://1drv.ms/b/c/8723dc973c70e2d7/IQDX4nA8l9wjIICHBmoAAAAAASJ88mLHkX8wTTEUTmLFC_U?e=YxoncY)

Material convertido de `Lista_Exercicios_TecnicasProgramacaoI.pdf`, mantendo a numeração e a organização temática do documento original. Fórmulas foram representadas em LaTeX quando a extração permitiu; tabelas e matrizes permanecem em formato textual para preservar o enunciado.

### 1. Qual o resultado das proposições? (Adote: [ / ] divisão normal (quociente); [

% ] resto da divisão; [div] valor inteiro do quociente da divisão; <>
−𝑏+√𝑏2−4𝑎𝑐
diferente; a = 10; b = 25; c = π; d = √2; 𝑥 = ; y = cos30; w =
2𝑎
Falso; z = !Falso).

a) Verdadeiro e 12>99

b) 12 % 3 < -100/50 e Verdadeiro

c) 0,5 = ½ ou 12-(-10/2) > 1

d) 23 – (-23) + [-50 % -(+25)] + 2 >= 200-{-25-[50 div (50 div 3)]} e Falso

e) 27-18 < 10 e 15 < 4 e 100-{-25-[50 div (40 div 3)]} >2

f) Não (27-18 < 10 e 15 < 4) e 100-{-25-[50 div (40 div 3)]} < 99,9

g) Não (10>9) e Não Verdadeiro

h) a+c > x

i) a > b ^ b < a v d > a

j) !(b > c) v d + a < 100

k) !(x < π) AND d < a

l) -22 > -22,1

m) !(a – x) OR b > d

n) y > c ^ d < y

o) !(y > c) ^ !(d < y)

p) !( (-23) + [-50 % -(+25)] + 2) ^ !z

q) !w = z

r) !z <> z

s) !(z =!z) <> w

t) ![!(z e !z) <> w] e ![!(z ou !z) e w]

u) !{![!(z e !z) ou w] e ![!(z ou !z) e w]} ou 200-{-25-[-15,2 div (45,5 div 3)]} <> 10

v) !(!(x < π) AND d > a) ou !w = z

w) !{!w e !(!z e !w)}

x) d > b ou !(z e !(!z))

y) w e !{23 – (-23) + [-50 % -(+25)] + 2 >= 200-{-25-[50 div (50 div 3)]} }

z) z ou !{ (27-18 < 10 e 15 < 4) e 100-{-25-[50 div (40 div 3)]} > b}

### 2. Assinale os dados que são do tipo real:

a) “45,2”

b) -803

c) “dez”

d) Verdadeiro

e) 0,56

f) 78,12579

g) “numero”

h) Falso

i) -1,58

### 3. Assinale os dados que são do tipo inteiro:

a) 002

b) “56”

c) Verdadeiro

d) 4000

e) “Bom dia”

f) -85

g) Falso

h) 2,56

i) “-741”

### 4. Assinale os dados que são do tipo caracter:

a) “12,8”

b) -745

c) “média”

d) Verdadeiro

e) 0,56

f) -23,5983

g) “eu & você”

h) Falso

i) 200

### 5. Assinale os dados que são do tipo lógico:

a) “76978”

b) Verdadeiro

c) “Rua 7 de Setembro”

d) 4569

e) 0,056

f) -3,687

g) “preço $”

h) Falso

i) 100

### 6. Assinale os nomes válidos para variáveis:

a) 1nome

b) RUA

c) (Y)

d) Programmierung

e) “ano”

f) fone14

g) A*B

h) &resposta

i) KM/H

j) média

k) data_nascimento

l) X

m) V5J

n) endereço

o) valor$

p) COD

## Algoritmos simples

### 7. Elabore um algoritmo/programa que imprima a frase "Esse é meu

primeiroexercício".

### 8. Elabore um algoritmo/programa que imprima as frases "É possível usar

múltiplas linhas" e "em um programa". Cada frase deve ficar em uma linha
diferente.

### 9. Elabore um algoritmo/programa que imprima os seus dados pessoais,

conforme exemplo abaixo:
- Nome: <mostre seu nome aqui>
- Endereço: <mostre seuendereço aqui>
- Telefone: <mostre seutelefone aqui>

### 10. Elabore um algoritmo/programa para calcular e mostrar o valor da

conversão de uma quantia em dólares para reais. Crie variáveis para
guardar o valor da cotação do dólar do dia, o valor em dólares e o valor do
resultado da conversão. Use a fórmula:
quantiaEmReais = quantiaEmDolares * cotacaoDoDolar

### 11. Elabore um algoritmo/programa que calcule e mostre a taxa de consumo

em km/l que um carro tem em um deslocamento. Devem ser criadas
variáveis para a distância percorrida (em kilômetros), a quantidade de litros
consumidos e o valor da taxa de consumo (em km/l). O cálculo é feito pela
fórmula:
taxaDeConsumo = distancia / litros

### 12. Escreva um algoritmo para imprimir as seguintes palavras, seguindo o

formato:
Avô
Pai
Neto

### 13. Escreva um algoritmo para escrever seu nome completo. Imprima cada

nome em uma nova linha.

### 14. Escreva um algoritmo para calcular e exibir o valor de e [e = (2*x)-

(y%7)+(z*5)]. (x = 10; y = 49 e z = 25);

### 15. Escreva um algoritmo para solucionar e exibir o resultado da seguinte

questão: um pendrive pode armazenar 8GB de dados, sabendo que ele já

está armazenando 3584MB, quanto esse pendrive ainda pode armazenar
em GB?

### 16. Quais são os valores atribuídos a z, se adicionarmos as instruções:

1) z := x / y ;
2) z := x DIV y;
3) z := x % y; (O símbolo % representa o resto da divisão)
ALGORITMO Exercicio;
VAR
INTEIRO x, y;
REAL z;
INCIO
x := 15;
y := 2;
//instrução 1 aqui
//instrução 2 aqui
//instrução 3 aqui
FIM.

### 17. Crie um algoritmo/programa que receba três nomes quaisquer e os mostre

na tela na ordem inversa da que foi fornecida.
Exemplo de entrada: Ana, Bruno e Caio
Exemplo de saída: Caio, Bruno e Ana

### 18. Crie um algoritmo/programa que receba os valores de x, y e z (todos reais)

do usuário, calcule e mostre o resultado da seguinte expressão e:
e = (2*x)-(y/7)+(z*5)

### 19. Crie um algoritmo/programa que receba os valores do nome, idade e

telefone de uma pessoa e mostre-os no seguinte formato:
- Nome: <mostre o nome aqui>
- Idade: <mostre a idade aqui>
- Telefone: <mostre otelefone aqui>

### 20. Qual o valor de saída para x nos pseudocódigos abaixo?

I)
ALGORITMO Valor_X;
VAR
REAL x;
INICIO
IMPRIMA “Valor de x”;
x <- ((25 + 100 / 2) ^ 2 ) - 1;
x <- x * x / 2;
IMPRIMA x;
FIM
II)
ALGORITMO Valor_X2;
VAR
REAL x;
INICIO
x <- (8 ^ 2) % 3;// O símbolo % representa o resto da divisão
x <- x + 2;
IMPRIMA x;
FIM
III)
ALGORITMO Valor_X3;
VAR
REAL x;
INICIO
x <- 8;
x <- x - 1;
x <- x * 2;
x <- x / 2;
x <- x + 1;
IMPRIMA x;
FIM

### 21. Crie um algoritmo/programa que receba a largura e o comprimento de um

lote de terra e mostre a área total existente. Não se esqueça de mostrar os
valores de todas as variáveis usadas no algoritmo/programa. Use a fórmula:
areaDoLote = largura * comprimento

### 22. Faça um algoritmo/programa que receba a quantidade e o valor de três

produtos, no seguinte formato: Quantidade1, Valor1, Quantidade2, Valor2,
Quantidade3, Valor3. O algoritmo/programa deve calcular esses valores
seguindo a fórmula total = Quantidade1 x Valor1 + Quantidade2 x Valor2 +
Quantidade3 x Valor3. O valor total deve ser apresentado no final da
execução do algoritmo/programa.

### 23. Crie um algoritmo/programa que receba quatro valores quaisquer e mostre

a média entre eles, o somatório entre eles e o percentual de cada um em
relação ao somatório.

### 24. Uma determinada pessoa que trabalha com a construção de piscinas precisa

de um algoritmo/programa que calcule o valor das construções solicitadas
pelos clientes, sabendo-se que os clientes sempre fornecem o comprimento,
a largura e a profundidade da piscina a ser construída. Leve em
consideração que o valor da construção é cobrado por m3 de água e o preço
é de R$ 75,00 por m3.

### 25. Faça um algoritmo/programa que receba duas notas de um aluno e seus

respectivos pesos, calcule e mostre a média ponderada dessas notas.
m é d i a p o n d e r a d a =
(
n o t a 1 * p( e
p
s
e
o
s
1
o
)
1
+
+
(
n
p
o
e
t a
s o
2
2
*) p e s o 2
)

### 26. Faça um algoritmo/programa que receba o valor de um depósito e o valor

da taxa de juros. Calcule e mostre o valor do rendimento e o valor total
depois do rendimento.

### 27. Faça um algoritmo/programa que receba um número inteiro, calcule e

mostre a tabuada de multiplicação desse número.

### 28. Faça um algoritmo/programa que receba o valor do salário de um

funcionário e o valor do salário mínimo. Calcule e imprima quantos salários
mínimos ganha esse funcionário.

### 29. Faça um algoritmo/programa que receba a idade de uma pessoa em anos,

calcule e imprima essa idade em:Meses, Dias, Horas e Minutos.

### 30. Faça um algoritmo/programa que receba uma determinada hora (hora e

minutos separados por ponto em forma de um valor fracionário), calcule e
imprima essa hora em minutos.

### 31. Faça um algoritmo/programa que receba o salário de um funcionário,

calcule e imprima o valor do imposto de renda a ser pago, sabendo que o
imposto equivale a 5% do salário.

### 32. Faça um algoritmo/programa que receba o salário de um funcionário,

calcule e imprima o novo salário sabendo-se que este sofreu um aumento de
25%.

### 33. Sabe-se que o quilowatt de energia custa 2% do salário mínimo. Faça um

algoritmo/programa que receba o valor do salário mínimo e a quantidade
de quilowatts gasta por uma residência. Calcule e imprima:
- o valor, em reais, de cada quilowatt;
- o valor, em reais, a ser pago por essa residência;
- o novo valor à ser pago por essa residência, se for dado um desconto
de 15%

### 34. Faça um algoritmo/programa que receba o peso de uma pessoa, em kg,

calcule e imprima:
- o peso dessa pessoa em gramas;
- se essa pessoa engordar 5%, qual será seu novo peso em gramas

### 35. Faça um algoritmo/programa que receba o ano de nascimento de uma

pessoa e o ano atual (ambos com 4 dígitos). Calcule e imprima:
- a idade dessa pessoa;
- essa idade convertida em semanas.

### 36. Faça um algoritmo/programa que receba os coeficientes a, b e c de uma

equação do 2º grau ax²+bx+c=0, calcule e mostre os valores de delta e das
raízes da equação.
- delta = b² - 4*a*c
−(𝑏)+√𝑑𝑒𝑙𝑡𝑎
- 𝑟𝑎𝑖𝑧 1 =
2∗𝑎
−(𝑏)−√𝑑𝑒𝑙𝑡𝑎
- 𝑟𝑎𝑖𝑧 2 =
2∗𝑎

### 37. Faça um algoritmo/programa que receba dois números, calcule e imprima

um elevado ao outro.

### 38. Faça um algoritmo (pseudocódigo) que leia o nome do automóvel e o preço

de fábrica e escreva o nome do automóvel e o preço final.
- Considere que o preço de um automóvel é calculado pela soma do
preço de fábrica com o preço dos impostos (45% do preço de
fábrica) e a percentagem do revendedor (28% do preço de fábrica).

### 39. Faça um algoritmo/programa que receba um número inteiro, calcule e

imprima:
- a raiz quadrada desse número;
- esse número elevado ao quadrado.

### 40. A conversão de graus Fahrenheit para Centígrados é obtida por c = 5/9*(f-

32). Faça um algoritmo/programa que calcule e escreva uma tabela de graus
Centígrados e graus Fahrenheit, que variam de 50 a 65 de 1 em 1.

### 41. Faça um algoritmo/programa que calcule a área de um triângulo.

𝑏𝑎𝑠𝑒∗𝑎𝑙𝑡𝑢𝑟𝑎
á𝑟𝑒𝑎 =
2

### 42. Faça um algoritmo/programa que calcule e imprima a área de um quadrado.

á𝑟𝑒𝑎 = 𝑙𝑎𝑑𝑜²

### 43. Faça um algoritmo/programa que calcule e imprima a área de um círculo.

á𝑟𝑒𝑎 = 𝜋∗𝑟𝑎𝑖𝑜2

### 44. Faça um algoritmo/programa que calcule e imprima a área de um trapézio.

𝑏𝑎𝑠𝑒 𝑚𝑎𝑖𝑜𝑟+𝑏𝑎𝑠𝑒 𝑚𝑒𝑛𝑜𝑟
á𝑟𝑒𝑎 = ∗𝑎𝑙𝑡𝑢𝑟𝑎
2

### 45. Faça um algoritmo/programa que calcule e imprima a área de um retângulo.

á𝑟𝑒𝑎 = 𝑏𝑎𝑠𝑒∗𝑎𝑙𝑡𝑢𝑟𝑎

### 46. Faça um algoritmo/programa que calcule e imprima a área de um losango.

𝑑𝑖𝑎𝑔𝑜𝑛𝑎𝑙 1∗𝑑𝑖𝑎𝑔𝑜𝑛𝑎𝑙 2
á𝑟𝑒𝑎 =
2

## Algoritmos com uso de condicional

### 47. Faça um algoritmo/programa que leia um número N e imprima “F1”, “F2” ou

“F3”, conforme a condição:
“F1”, se N < 10;
“F2”, se N = 10;
“F3”, se N >10.

### 48. Escreva um algoritmo/programa que, para uma conta bancária, leio o seu

número, o saldo, o tipo de operação a ser realizada (depósito ou retirada) e
o valor da operação. Após, determine e mostre o novo saldo.

### 49. Faça um algoritmo/programa que receba dois números e imprima o menor

dos dois.

### 50. Faça um algoritmo/programa que receba a idade de uma pessoa e imprima

mensagem de maior idade ou não.

### 51. Ler o nome de 2 times e o número de gols marcados na partida (para cada

time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser
impressa a palavra EMPATE.

### 52. Faça um algoritmo que leia a hora de início e a hora de fim de um jogo de

Xadrez (considere apenas horas inteiras, sem os minutos e em formato de
24hrs) e calcule a duração do jogo em horas, sabendo-se que o tempo
máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um
dia e terminar no dia seguinte.
Exemplo 1
Hora de início: 13
Hora de término: 18
Duração: 5
Exemplo 2
Hora de início: 13
Hora de término: 10
Duração: 21

### 53. Faça um algoritmo/programa para ler: a descrição do produto (nome), a

quantidade adquirida e o preço unitário. Calcular e escrever o total (total =
quantidade adquirida * preço unitário), o desconto e o total a pagar (total a
pagar = total - desconto), sabendo-se que:
- Se quantidade <= 5 o desconto será de 2%;
- Se quantidade > 5 e quantidade <=10 o desconto será de 3%;
- Se quantidade > 10 o desconto será de 5%;

### 54. Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:

VALOR DA COMPRA VALOR DA VENDA
Valor < R$ 10,00 Lucro de 70%
R$ 10,00  Valor < R$ 30,00 Lucro de 50%
R$ 30,00  Valor < R$ 50,00 Lucro de 40%
Valor  R$ 50,00 Lucro de 30%
Criar o algoritmo/programa que possa entrar com nome do produto e valor
da compra e imprimir o nome do produto e valor de venda.

### 55. Faça um algoritmo/programa que receba um número, verifique se este

número é par ou ímpar e imprima a mensagem.
- Para verificar se um número é par, use a operação resto da divisão
por 2, se der zero, o número é par.

### 56. Elabore um algoritmo/programa que receba uma senha do usuário e

compare com a senha padrão “ASDFG”. Se os valores forem iguais, o seu
algoritmo/programa deve informar a mensagem “Acesso liberado”, em caso
contrário, a mensagem a aparecer é “Acesso negado”.

### 57. Faça um algoritmo/programa que receba quatro notas de um aluno, calcule

e imprima a média aritmética das notas e a mensagem de aprovado para
média superior ou igual a 7.0 ou a mensagem de reprovado para média
inferior a 7.0.

### 58. Uma empresa decide dar um aumento de 30% aos funcionários cujo salário

é inferior a 850 reais. Escreva um algoritmo/programa que receba o salário
de um funcionário e imprima o valor do salário reajustado ou uma
mensagem caso o funcionário não tenha direito ao aumento.

### 59. Faça um algoritmo/programa que receba dois números e diga se o primeiro

é maior que o segundo, se são iguais ou se o segundo é maior que o
primeiro.

### 60. Faça um algoritmo/programa que receba cinco números e diga a

quantidade de números negativos.

### 61. Faça um algoritmo/programa que receba os coeficientes a, b e c de uma

equação do 2º grau ax²+bx+c=0, calcule e mostre os valores de delta e das

raízes da equação. O seu algoritmo/programa deverá informar a condição
de delta, se negativo, nulo ou positivo.
- delta = b² - 4*a*c
−(𝑏)+√𝑑𝑒𝑙𝑡𝑎
- 𝑟𝑎𝑖𝑧 1 =
2∗𝑎
−(𝑏)−√𝑑𝑒𝑙𝑡𝑎
- 𝑟𝑎𝑖𝑧 2 =
2∗𝑎

### 62. Faça um algoritmo/programa que calcule e imprima o salário reajustado de

um funcionário de acordo com a seguinte regra:
- salários até 1200, reajuste de 50%
- salários maiores que 1200, reajuste de 30%

### 63. Faça um algoritmo de conversão de temperatura. O usuário deve escolher se

a conversão será de (1) grau Celsius para Fahrenheit ou de (2) Fahrenheit
para Celsius, e em seguida deve entrar com uma temperatura. Utilize a
estrutura de decisão SE e SENÃO. As fórmulas de conversão estão descritas
abaixo:
F : Temperatura em Fahrenheit; C :Temperatura em Celsius
Celsius-Fahrenheit :F = (9 * C + 160) / 5;
Fahrenheit-Celsius: C = (F - 32) * (5 / 9);

### 64. Faça um algoritmo/programa que receba a altura (H) e o sexo de uma

pessoa, calcule e imprima o seu peso ideal, utilizando as seguintes fórmulas:
- para homens: (72.7 * H) - 58
- para mulheres: (62.1 * H) - 44.7

### 65. Faça um algoritmo/programa que receba o código de um produto e seu

valor. Baseado na tabela de aumento abaixo, o seu algoritmo/programa
deverá dizer qual é o novo preço do produto.
Código Percentual de aumento %
1 15
3 20
4 35
8 40

### 66. Faça um algoritmo/programa que receba a idade de um nadador e imprima

a sua categoria seguindo as regras:
Categoria Idade
Infantil A 5 - 7 anos
Infantil B 8 - 10 anos
Juvenil A 11 - 13 anos
Juvenil B 14 - 17 anos
Sênior maiores de 18 anos

### 67. No curso de computação, a nota final do estudante é calculada a partir de 3

notas atribuídas respectivamente a um trabalho de laboratório, a uma
avaliação semestral e a um exame final. As notas variam de 0 a 10 e a nota
final é a média ponderada das 3 notas mencionadas. A tabela a seguir
fornece os pesos das notas:
Laboratório peso 2
Av. semestral peso 3
Exame final peso 5
Faça um algoritmo/programa que receba as 3 notas do estudante, calcule e
imprima a média final e o conceito desse estudante.
O conceito segue a tabela abaixo:
Média final Conceito
8.0 |__| 10.0 A
7.0 |__ 8.0 B
6.0 |__ 7.0 C
5.0 |__ 6.0 D
< 5.0 E

### 68. Faça um algoritmo/programa que receba o preço de um produto e o seu

código de origem e imprima a sua procedência. A procedência obedece a
seguinte tabela:
Código de origem Procedência
1 Sul
2 Norte
3 Leste
4 Oeste
5 Nordeste
6 Sudeste
7 Centro-oeste
8 Nordeste

### 69. O cardápio de uma lanchonete é o seguinte:

Especificação Código Preço
Cachorro quente 100 3.00
Bauru simples 101 4.00
Bauru com ovo 102 4.50
Hambúrguer 103 3.00
Cheeseburguer 104 4.00
Refrigerante 105 2.50
Implemente um programa que leia o código do item pedido, a quantidade e
calcule o valor a ser pago por lanche. Considere que a cada execução será
calculado somente um item.

### 70. Sabendo que somente os municípios que possuem mais de 20.000 eleitores

aptos têm segundo turno nas eleições para prefeito caso o primeiro
colocado não tenha mais do que 50% dos votos, fazer um algoritmo que leia
o nome do município, a quantidade de eleitores aptos, o número de votos do
candidato mais votado e informar se ele terá ou não segundo turno em sua
eleição municipal.

### 71. Uma companhia de seguros tem três categorias de seguros baseadas na

idade ocupação do segurado. Somente pessoas com pelo menos 18 anos e
não mais de 70 anos podem adquirir apólices de seguros. Quanto às classes
de ocupações foram definidos três grupos de risco. A tabela a seguir fornece
as categorias em função da faixa de idade e do grupo de risco:
Idade Grupo de Risco

Baixo - Médio - Alto

18 a 24 7 8 9

25 a 40 4 5 6

41 a 70 1 2 3

Faça um algoritmo que receba a idade e o grupo de risco (b, m ou a) e
determine e imprima o código do seguro.

### 72. Um endocrinologista deseja controlar a saúde de seus pacientes, e para isso,

se utiliza o Índice de Massa Corporal (ICM). O IMC é calculado através da
seguinte fórmula:
𝑃𝑒𝑠𝑜
𝐼𝑀𝐶 =
𝐴𝑙𝑡𝑢𝑟𝑎2
Crie um algoritmo/programa que apresente o nome do paciente e sua faixa
de risco, de acordo com a tabela abaixo (peso é dado em kg e altura em m).
IMC FAIXA DE RISCO
Abaixo de 20 Abaixo do peso
A partir de 20 até 25 Normal
Acima de 25 Excesso de peso

### 73. Faça um algoritmo/programa que receba a idade de uma pessoa e

classifique-a seguindo o critério a seguir:
Idade Classificação
0 a 2 anos Recém-nascido
3 a 11 anos Criança
12 a 19 anos Adolescente
20 a 55 anos Adulto
Acima de 55 anos Idoso

### 74. Faça um algoritmo/programa que receba o código correspondente ao cargo

de um funcionário e imprima seu cargo e o percentual de aumento ao qual
este funcionário tem direito seguindo a tabela abaixo:
Código Cargo Percentual
1 Escriturário 50%
2 Secretário 35%
3 Caixa 20%
4 Gerente 10%
5 Diretor Não tem aumento

### 75. Faça um algoritmo/programa que mostre um menu com as seguintes

opções:
- soma
- raiz quadrada
- finalizar
O algoritmo/programa deve receber a opção desejada, receber os dados
necessários para a operação de cada opção, realizar a operação e imprimir o
resultado. Na opção finalizar o algoritmo/programa deverá encerrar-se.

### 76. Uma companhia de seguros tem três categorias de seguros baseadas na

idade e ocupação do segurado. Somente pessoas com pelo menos 18 anos e
não mais de 70 anos podem adquirir apólices de seguros. Quanto às classes
de ocupações foram definidos três grupos de risco. A tabela a seguir fornece
as categorias em função da faixa de idade e do grupo de risco:
Idade Grupo de Risco
Baixo Médio Alto
18 a 24 7 8 9
25 a 40 4 5 6
41 a 70 1 2 3
Faça um algoritmo/programa que receba a idade e o grupo de risco (b, m ou
a) e determine e imprima o código do seguro.

### 77. Faça um algoritmo/programa que receba o valor do salário mínimo, o

número de horas trabalhadas, o número de dependentes do funcionário e a
quantidade de horas extras trabalhadas. Calcule e imprima o salário a
receber do funcionário seguindo as regras abaixo:
- o valor da hora trabalhada é igual a 1/10 do salário mínimo;
- o salário do mês é igual ao número de horas trabalhadas vezes o
valor da hora trabalhada;
- para cada dependente acréscimo de 78 reais;
- para cada hora extra trabalhada o cálculo do valor da hora
trabalhada acrescida de 50%;
- o salário bruto é igual ao salário do mês mais os valores dos
dependentes mais os valores das horas extras;
O cálculo do valor do imposto de renda retido na fonte segue a tabela
abaixo:
IRRF Salário Bruto
Isento inferior a 600
10% de 600 até 900
20 % superior a 900
- o salário líquido é igual ao salário bruto menos IRRF;
- a gratificação segue a próxima tabela:
Salário Líquido Gratificação
Até 720 150 reais
Superior a 720 75 reais
O salário a receber do funcionário é igual ao salário líquido mais a
gratificação.

### 78. Dados três valores X, Y, Z, verifiquem se eles podem ser os comprimentos

dos lados de um triângulo e se forem escrever uma mensagem informando
se é se é um triângulo eqüilátero, isósceles ou escaleno.
Observações:
- O comprimento de um lado do triângulo é sempre menor do que a
soma dos outros dois.
- Eqüilátero> Todos lados iguais
- Isósceles > Dois lados iguais
- Escaleno > Todos os lados diferentes

### 79. A Secretaria do Meio Ambiente, que controla o índice de poluição, mantém 3

grupos de indústria que são altamente poluentes do meio ambiente. O
índice de poluição aceitável varia de 0.05 até 0.29. Se o índice sobe para 0.3
as indústrias do 1º grupo são intimadas a suspenderem suas atividades. Se o
índice crescer para 0.4 as indústrias do 1º e 2º grupo são intimadas a
suspenderem suas atividades e, se o índice atingir 0.5 todos os grupos
devem ser notificados a paralisarem suas atividades. Faça um algoritmo que
leia o índice de poluição medido e emita a notificação adequada aos
diferentes grupos de empresas.

### 80. Faça um algoritmo que mostre um menu com as seguintes opções:

1 - Soma
2 - Subtração
3 - Divisão inteira
4 - Exponencial
5 - Raiz quadrada
O algoritmo deve receber a opção desejada, receber os dados necessários
para a operação de cada opção, realizar a operação e imprimir o resultado.

## Algoritmos com uso de estrutura de repetição e/ou condicional

### 81. Escreva um algoritmo/programa que imprima os 100.000 primeiros

números inteiros positivos, ou seja, Z*+ = {1, 2, 3, 4, ..., 100.000}.

### 82. Escreva um algoritmo/programa que receba 10 números inteiros e imprima

a quantidade de números ímpares dentre os números que foram digitados.

### 83. Faça um algoritmo para calcular quantos números inteiros existem, de 1000

a 10000, que não são divisíveis nem por 5 nem por 7.

### 84. Faça um algoritmo para calcular quantos são os números naturais menores

que 98 e divisíveis por 5.

### 85. Um método que receba n valores inteiros e calcule a média aritmética entre

eles (𝑀é𝑑𝑖𝑎 = 𝑥1+𝑥2+⋯+𝑥𝑛 ).
𝑛

### 86. Tem-se um conjunto de dados contendo a altura e o sexo (M ou F) de 15

pessoas. Faça um algoritmo/programa que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- o número de homens.

### 87. Faça um algoritmo/programa que receba um número inteiro, calcule e

mostre a tabuada de multiplicação (até o 10) desse número, sendo esses
fornecidos pelo usuário, até encontrar como finalizador o valor -1.

### 88. Elabore um algoritmo/programa para ler vários números e informar

quantos números entre 100 e 200 foram digitados. Quando o valor 0 (zero)
for lido, o algoritmo deverá cessar sua execução.

### 89. Escreva um algoritmo/programa que receba a idade de 10 pessoas, calcule e

imprima a quantidade de pessoas maiores de idade (idade >= 18 anos).

### 90. Escreva um algoritmo/programa que receba a idade de 15 pessoas, calcule e

imprima:
- a quantidade de pessoas em cada faixa etária;
- a porcentagem de cada faixa etária em relação ao total de pessoas.
As faixas etárias são:
- 15 anos
- 16 30 anos
- 31 45 anos
- 46 60 anos
- >= 61 anos

### 91. Escreva um algoritmo/programa que receba um conjunto de valores

inteiros e positivos, calcule e imprima o maior e o menor valor do conjunto.
Para encerrar a entrada de dados, deve ser digitado o valor zero. Para
valores negativos, deve ser enviada uma mensagem. Esses valores (zero e
negativos) não entrarão nos cálculos.

### 92. Escreva um algoritmo/programa que receba um número inteiro e verifique

se o número fornecido é primo ou não. Imprima mensagem de número
primo ou número não primo.
Observação: um número é primo se este é divisível apenas pelo número um
e por ele mesmo.

### 93. Escreva um algoritmo/programa que receba 10 números inteiros e imprima

a quantidade de números primos dentre os números que foram digitados.

### 94. Em uma eleição presidencial, existem quatro candidatos. Os votos são

informados através de código. Os códigos utilizados são:
- 1,2,3,4 votos para os respectivos candidatos;
- 5 voto em branco;
- outros voto.nulo.
Escreva um algoritmo/programa que calcule e imprima:
- total de votos para cada candidato;
- total de votos nulos;
- total de votos em branco;
- porcentagem de votos nulos sobre o total de votos;
- porcentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos, tem-se o voto com valo zero.

### 95. Escreva um algoritmo/programa para calcular N! (fatorial de N), sendo que

o valor inteiro de N é fornecido pelo usuário.
- Sabe-se que: N!=1 *2*3*...*(N-1)*N;
- 0! = 1 , por definição.

### 96. Escreva um algoritmo/programa que leia um número indeterminado de

linhas contendo, cada uma, a idade de um indivíduo. A última linha, que não
entrará nos cálculos, contém o valor da idade igual a zero; calcule e escreva
a idade média deste grupo de indivíduos.

### 97. Elabore um algoritmo/programa que receba um texto de entrada e mostre o

mesmo texto na saída, só que com todas as posições dos caracteres
invertidas.
Exemplo Entrada: ODLANIGER Saída: REGINALDO

### 98. Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de

3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de
natalidade de 2% ao ano, calcular e imprimir o tempo necessário para que a
população do país A ultrapasse a população do país B.

### 99. Faça um algoritmo que calcule a média dos salários de uma empresa,

pedindo ao usuário o nome dos funcionários e os salários e devolvendo a
média, o salário mais alto e o salário mais baixo. Use 0 (zero) para encerrar
a leitura.

### 100. Faça um algoritmo/programa que receba, como entrada, uma lista de

números positivos ou negativos finalizada com o número zero e forneça,
como saída, a soma dos números positivos, a soma dos números negativos e
a soma das duas somas parciais.

### 101. Uma empresa decidiu fazer um levantamento em relação aos candidatos

que se apresentarem para preenchimento de vagas no seu quadro de
funcionários. Supondo que você seja o programador dessa empresa, faça um
algoritmo/programa que leia para cada candidato a idade, o sexo (M ou F) e
a experiência no serviço (S ou N). Para encerrar a entrada de dados, digite
zero para a idade. Calcule e escreva:
- o número de candidatos do sexo feminino;
- o número de candidatos do sexo masculino;
- a idade média dos homens que já têm experiência no serviço;
- a porcentagem dos homens com mais de 45 anos entre o total dos
homens;
- o número de mulheres com idade inferior a 35 anos e com
experiência no serviço;
- a menor idade entre as mulheres que já têm experiência no serviço.

### 102. Faça um algoritmo/programa que receba a idade e o peso de 15 pessoas.

Calcule e imprima as médias dos pesos das pessoas da mesma faixa etária.
As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e
maiores de 30 anos.

### 103. Faça um algoritmo/programa que receba duas notas de 6 alunos e calcule e

imprima:
- a média entre essas 2 notas de cada aluno;
- a mensagem de acordo com a tabela abaixo:
Média Mensagem
0 |__ 5 reprovado
5 |__ 7 exame final
7 |__| 10 aprovado
- o total de alunos aprovados e o total de alunos reprovados;
- a média geral da classe, isto é, a média entre as médias dos alunos.

### 104. Faça um algoritmo/programa que receba a idade e a altura de várias

pessoas. Calcule e imprima a média das alturas das pessoas com mais de 50
anos. Para encerrar a entrada de dados, digite idade <= zero.

### 105. Cada espectador de um cinema respondeu a um questionário no qual

constava sua idade e a sua opinião em relação ao filme: ótimo — 3, bom —
2, regular — 1. Faça um algoritmo/programa que receba a idade e a opinião
de 15 espectadores, calcule e imprima:
- a média das idades das pessoas que responderam ótimo;
- a quantidade de pessoas que responderam regular;
- a porcentagem de pessoas que responderam bom entre todos os
espectadores analisados.

### 106. Uma certa firma fez uma pesquisa de mercado para saber se as pessoas

gostaram ou não de um novo produto lançado. Para isso forneceu o sexo do
entrevistado e sua resposta (sim ou não). Sabendo que foram entrevistadas
10 pessoas, faça um algoritmo/programa que calcule e imprima:
- o número de pessoas que responderam sim;
- o número de pessoas que responderam não;
- o número de mulheres que responderam sim;
- a porcentagem de homens que responderam não entre todos os
homens analisados.

### 107. Faça um algoritmo/programa que receba 10 números, calcule e imprima a

soma dos números pares e a soma dos números primos.

### 108. Faça um algoritmo/programa que imprima na tela as tabuadas de 1 a 10.

### 109. Faça um algoritmo/programa que apresente um menu de opções para o

cálculo das seguintes operações entre dois números: adição, subtração,
multiplicação e divisão (no menu a opção 0 para sair). Possibilite ao usuário
escolher a operação desejada, mostrar o resultado e voltar ao menu de
opções.

### 110. Uma loja utiliza os seguintes códigos para as transações de cada dia:

“v” para compras à vista
“p” para compras a prazo
É dada uma lista de transações contendo o valor de cada compra e o
respectivo código da transação. Faça um algoritmo/programa que calcule e
imprima:
- valor total das compras à vista;
- valor total das compras a prazo;
- valor total das compras efetuadas;
- valor a receber pelas compras a prazo, isto é, primeira parcela,
sabendo que estas serão pagas em três vezes.
Sabe-se que são efetuadas 25 transações por dia.

### 111. Crie um algoritmo para ler vários números até entrar o número -999. Para

cada número, imprimir seus divisores.

### 112. Elabore um algoritmo para entrar com sexo de várias pessoas e imprimir

quantas pessoas são do sexo masculino (considerar apenas M para
Masculino ou F para Feminino).

### 113. Foi f eita uma pesquisa de audiência de canal de TV em várias casas de uma

certa cidade, em um determinado dia. Para cada casa visitada foi fornecido o
número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo
a ele naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou
seja, esta casa não entraria na pesquisa. Faça um algoritmo/programa que:
- leia um número indeterminado de dados, isto é, o número do canal e
o número de pessoas que estavam assistindo;
- calcule e imprima a porcentagem de audiência em cada canal.
Para encerrar a entrada de dados, digite o número do canal zero.

### 114. Crie um algoritmo que leia a idade de várias pessoas e imprima:

- Total de pessoas com menos de 21 anos;
- Total de pessoas com mais de 50 anos;

### 115. Faça um algoritmo/programa que receba a idade, a altura e o peso de 15

pessoas. Calcule e imprima:
- a quantidade de pessoas com idade superior a 50 anos;
- a média das alturas das pessoas com idade entre 10 e 20 anos;
- a porcentagem de pessoas com peso inferior a 40 quilos entre todas
as pessoas analisadas.

### 116. Faça um algoritmo/programa para calcular a área de um triângulo. Este

algoritmo/programa não pode permitir a entrada de dados inválidos, por
exemplo, medidas menores ou iguais a zero. Cada entrada de dados deve ser
validada e caso o valor fornecido seja inválido, deverá ser feita uma nova
leitura para a variável.

### 117. Faça um algoritmo/programa que receba o valor e o código de várias

mercadorias vendidas em um determinado dia. Os códigos obedecem a
tabela abaixo:
- “L” — limpeza
- “A” — alimentação
- “H”— higiene
Calcule e imprima:
- o total vendido naquele dia, com todos os códigos juntos;
- o total vendido naquele dia em cada um dos códigos.
Para encerrar a entrada de dados. digite o valor da mercadoria zero.

### 118. Faça um algoritmo/programa que receba a idade e o estado civil (C - casado,

S - solteiro, V - viúvo e D - desquitado ou separado) de 20 pessoas. Calcule e
imprima:
- a quantidade de pessoas casadas;
- a quantidade de pessoas solteiras;
- a média das idades das pessoas viúvas;
- a porcentagem de pessoas desquitadas ou separadas dentre todas as
pessoas analisadas.

### 119. Criar um algoritmo que receba a idade e o estado civil (C-Casado, S-solteiro,

V-viúvo e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
- A quantidade de pessoas casadas;
- A quantidade de pessoas solteiras;
- A média das idades das pessoas viúvas;
- A porcentagem de pessoas desquitadas ou separadas dentre todas as
pessoas analisadas;
O algoritmo acaba quando se digita um número menor do que zero para
idade.

### 120. Faça um algoritmo/programa que receba a idade, o peso e o sexo de 10

pessoas. Calcule e imprima:
- total de homens;
- total de mulheres;
- média das idades dos homens;
- média dos pesos das mulheres.

### 121. Uma rainha requisitou os serviços de um monge e disse-lhe que pagaria

qualquer preço. O monge, necessitando de alimentos, perguntou à rainha se
o pagamento poderia ser feito com grãos de trigo dispostos em um tabuleiro
de xadrez, de tal forma que o primeiro quadro contivesse apenas um grão e
os quadros subsequentes, o dobro do quadro anterior. A rainha considerou
o pagamento barato e pediu que o serviço fosse executado, sem se dar conta
de que seria impossível efetuar o pagamento. Faça um algoritmo/programa
para calcular o número de grãos que o monge esperava receber.

### 122. Escreva um algoritmo/programa que imprima todas as possibilidades de

que no lançamento de dois dados tenhamos o valor 7 como resultado da
soma dos valores de cada dado.

### 123. Elabore um algoritmo/programa que imprima todos os números primos

existentes entre N1 e N2, em que N1 e N2 são números naturais fornecidos
pelo usuário.

### 124. Prepare um algoritmo/programa que calcule o valor de H, sendo que ele é

determinado pela série H = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.

### 125. Elabore um algoritmo/programa que determine o valor de S, em que: S =

1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... - 10/100.

### 126. Escreva um algoritmo/programa que calcule e escreva a soma dos dez

primeiros termos da seguinte série: 2/500 - 5/450 + 2/400 - 5/350 + ...

### 127. Uma agência de publicidade quer prestar serviços somente para as maiores

companhias — em número de funcionários — em cada uma das
classificações: grande, média, pequena e microempresa. Para tal, consegue
um conjunto de dados com o código, o número de funcionários e o porte da
empresa. Construa um algoritmo/programa que liste o código da empresa
com maiores recursos humanos dentro de sua categoria. Utilize como
finalizador o código de empresa igual a 0.

### 128. Foi realizada uma pesquisa sobre algumas características físicas da

população de uma certa região, a qual coletou os seguintes dados referentes
a cada habitante para análise:
- sexo (“M” — masculino ou “F” — feminino);
- cor dos olhos (“A” — azuis, “V” — verdes ou “C”— castanhos);
- cor dos cabelos (“L” — louros, “C” — castanhos ou “P”— pretos);
- idade.
Faça um algoritmo/programa que determine e escreva:
- a maior idade dos habitantes;
- a percentagem de indivíduos do sexo feminino cuja idade está entre
18 e 35 anos, inclusive, e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1 entrando
como idade.

### 129. Faça um algoritmo que leia informações de alunos (Matrícula, Nota1, Nota2,

Nota3) com o fim das informações indicado por Matrícula = 9999. Para cada
aluno deve ser calculada a média final de acordo com a seguinte fórmula:
[(2∗𝑁𝑜𝑡𝑎1)+ (3∗𝑁𝑜𝑡𝑎2 )+ (4∗𝑁𝑜𝑡𝑎3)]
𝑀é𝑑𝑖𝑎 𝐹𝑖𝑛𝑎𝑙 = ⁄
9
Se a média final for igual ou superior a 5, o algoritmo deve mostrar
Matrícula, Média Final e a mensagem “Aprovado”; se a média final for
inferior a 5, o algoritmo deve mostrar Matrícula, Média Final e mensagem
“Reprovado”.
Ao final devem ser mostrados o total de aprovados, o total de alunos da
turma e o total de reprovados.

### 130. Anacleto tem 1,50 metro e cresce 2 centímetros por ano, enquanto

Felisberto tem 1,10 metro e cresce 3 centímetros por ano. Construa um
algoritmo/programa que calcule e imprima quantos anos serão necessários
para que Felisberto seja maior que Anacleto.

### 131. Realizou-se uma pesquisa para determinar o índice de mortalidade infantil

em um certo período. Construa um algoritmo/programa que leia o número
de crianças nascidas no período e, depois, em um número indeterminado de
vezes, o sexo de uma criança morta (“M” — masculino ou “F” — feminino) e
o número de meses de vida da criança.
Como finalizador, teremos a letra “X” no lugar do sexo da criança.
Determine e imprima:
- a porcentagem de crianças mortas no período;
- a porcentagem de crianças do sexo masculino mortas no período;
- a porcentagem de crianças que viveram dois anos ou menos no
período.

### 132. Em um prédio há três elevadores denominados A, B e C. Para otimizar o

sistema de controle dos elevadores, foi realizado um levantamento no qual
cada usuário respondia:
- o elevador que utilizava com mais freqüência;
- o período que utilizava o elevador, entre:
- “M” = matutino;
- “V” = vespertino;
- “N” = noturno.
Construa um algoritmo/programa que calcule e imprima:
- qual é o elevador mais frequentado e em que período se concentra o
maior fluxo;
- qual o período mais usado de todos e a que elevador pertence;
- qual a diferença percentual entre o mais usado dos horários e o
menos usado;
- qual a percentagem sobre o total de serviços prestados do elevador
de média utilização.

### 133. Uma agência de uma cidade do interior tem, no máximo, 10.000 clientes.

Crie um algoritmo que possa ler o número da conta, nome e saldo de cada
cliente. Imprima todas as contas, os respectivos saldos e uma das
mensagens: positivo ou negativo. A entrada de contas termina quando se
digita um valor negativo para número de conta ou quando ultrapassar
10.000 contas registradas. Ao final, deverá ser impresso o total de clientes
com saldo negativo, o total de clientes da agência e o saldo da agência.

### 134. Um m arciano chegou a uma floresta e se escondeu atrás de uma das 100

árvores quando viu um caçador. O caçador só tinha cinco balas em sua
espingarda. Cada vez que ele atirava, e não acertava, é claro, o marciano
dizia: estou mais à direita ou estou mais à esquerda. Se o caçador não
conseguir acertar o marciano, ele será levado para Marte. Implementar este
jogo para dois jogadores, onde um escolhe a árvore em que o marciano irá
se esconder, e o outro tenta acertar.

### 135. Um clube com capacidade máxima para 2000 pessoas em seu salão de

festas, organizou um baile em que foi permitida a entrada de sócios e não-
sócios cobrando os seguintes valores por cada ingresso:
1. SÓCIO : R$ 10,00
2. NÃO-SÓCIO : R$ 20,00
Criar um algoritmo que leia as informações sobre ingressos vendidos,
sabendo que no mínimo um ingresso foi vendido, até que seja digitado o
valor -999 ou que todos os ingressos sejam vendidos e imprima:
- A quantidade de ingressos vendidos para sócios e a para não-sócios;
- O percentual de ingressos para sócios em relação ao total geral de
ingressos vendidos;
- O valor em Reais recebido de sócios, de não-sócios e o total arrecadado no
baile.

### 136. Cons iderando alguns conceitos de física, elabore um algoritmo/programa

para mostrar que a diferença entre os níveis de decibéis 𝛽1 𝑒 𝛽2 de um som
está relacionada com a razão das distâncias r1 e r2 da fonte sonora por:
r1
β2−β1 = 20 log
r2
Seu algoritmo/programa deverá imprimir os valores de r1 variando de 2 em
2 metros até 40m e, considerando r2 = 10m, suas respectivas Diferenças de
Níveis de Intensidade.

### 137. A velocidade do som no ar em m/s depende da temperatura, de acordo com

a função abaixo aproximada:
𝑣 = 331,5+0,607∗𝑇
𝑐
- Onde Tc é a temperatura em Celsius.
No ar seco, a temperatura diminui cerca de 1° C a cada aumento de 150 m
de altitude. Suponha que essa mudança seja constante até 9000 m de
altitude. Encontre uma equação para a temperatura a partir da equação da
velocidade, que dependa do tempo. Considerando alguns conceitos de física,
elabore um algoritmo/programa que determine o intervalo de tempo que é
necessário para o som de um avião voando a 9000m chegar ao chão em um
dia em que a temperatura é de 30° C?
Seu algoritmo/programa deverá imprimir a variação do tempo, de 6 em 6
horas até 36h, e suas respectivas temperaturas para um avião voando a uma
altitude constante de 9000 m.

### 138. Você foi contratado por uma empresa que recentemente investiu em uma

fonte de energia limpa para sua linha de produção. Agora os gestores da
empresa precisam saber se há alguma relação entre o investimento
realizado e o faturamento da empresa. Como engenheiro responsável pela
implantação do novo sistema de energia da linha de produção, você foi
designado a responder o questionamento dos gestores.
Sua equipe lhe entregou o seguinte levantamento dos dados (ver Tabela 1 e
Figura 1):
Tabela 1 - Dados de Investimento x Faturamento.
Investimentos com energia Faturamento (em milhares
solar (em milhares de de reais)
reais)
2,4 225
1,6 184
2,0 220
2,6 240
1,4 180
1,6 184
2,0 186
2,2 215

Investimentos com energia solar (em milhares de
reais)
300
250
o
t 200
n
e
m 150
a
r
u
t 100
a
F
50
0
2,40 1,60 2,00 2,60 1,40 1,60 2,00 2,20
Investimento
Faturamento (em milhares de reais)
Figura 1 - Gráfico ilustrando a relação entre as duas variáveis.
Após analisar o gráfico da Figura 1, foi possível identificar a relação entre as
duas variáveis. Para reforçar a defesa da sua análise, sua resposta será
pautada em um critério estatístico. Para tal, considere a fórmula e o conceito
de estatística sobre coeficiente de correlação (r):
n∑xy− (∑x)(∑y)
r =
√(n∑x2 −(∑x)2)√(n∑y2 −(∑y)2)
Onde:
n: é a quantidade de dados;
Os demais termos são relativos às somatórias dos valores para x
(Investimentos com energia solar) e para y (Faturamento).
Sabendo que o valor máximo do coeficiente de correlação é 1, e o
mínimo é -1, sempre que for encontrado um coeficiente próximo de algum
dos extremos temos uma correlação forte entre as variáveis (x e y) - positiva
ou negativa, de acordo com o valor de r. Já um coeficiente 0 (zero) significa
que não existe relação entre as variáveis.
Ex: r = 0,9129 - correlação forte;
r = -0,9794 - correlação forte;
r = 0 - Não existe correlação.
Para ganhar produtividade em futuras análises, desenvolva um
algoritmo/programa que, dado uma lista de investimentos e seus
respectivos faturamentos, verifique se há relação entre os investimentos
com energia solar da empresa e seu faturamento.

## Algoritmos com o uso de recursão

### 139. Escre ver um algoritmo, utilizando um subalgoritmo recursivo, para calcular

a soma dos 'n' primeiros inteiros positivos, sendo 'n' um valor fornecido
pelo usuário.

### 140. Escre ver um algoritmo, utilizando um subalgoritmo recursivo, que eleve um

número inteiro qualquer a uma potência. Devem ser fornecidos o número e

a potência.

### 141. Há 2 0 funcionários em uma equipe e quatro deles serão convidados para

uma promoção. Não faz diferença entre quem é convidado em primeiro
lugar, em segundo ou assim por diante. Considere a fórmula da combinação
de n elementos em um grupo de p:
𝑛!
𝐶 = ,𝑠𝑒𝑛𝑑𝑜 𝑛 ≥ 𝑝
𝑛,𝑝 (𝑛−𝑝)!𝑝!
Faça um algoritmo para encontrar a quantidade de agrupamentos formados
em uma combinação simples.

### 142. Elabore um algoritmo/programa para descobrir o número de anagramas da

palavra CONJUNTO que começam por C e terminam por T.
Possíveis respostas:
A) 15
B) 30
C) 180
D) 360
E) 720

### 143. Escre ver um algoritmo, utilizando um subalgoritmo recursivo, para calcular

o N-esimo termo da série de Fibonacci.

## Algoritmos com o uso de vetores/matrizes

### 144. Crie um algoritmo/programa que receba dez nomes do usuário, armazene-

os em um vetor e ao final mostre a listagem, indicando a posição de cada
nome.

### 145. Elabore um algoritmo/programa que crie um vetor com 10 posições inteiras

e receba seus valores do usuário. Ao final o seu algoritmo/programa deverá
mostrar somente os valores acima da média.

### 146. Elabore um algoritmo/programa que crie um vetor de 15 posições com

valores aleatórios reais. Ao final o algoritmo/programa deverá mostrar o
maior e o menor valor.

### 147. Elabore um algoritmo/programa que crie um vetor com 5 textos para

guardar os nomes de pessoas. O vetor deve ser preenchido pelo usuário e ao
final deve ser feita uma consulta com um novo nome para saber se ele está
ou não cadastrado.

### 148. Elabore um algoritmo/programa que crie uma matriz 3x4 com valores

aleatórios reais. Ao final o algoritmo/programa deverá:
- Mostrar os valores da matriz;
- Mostrar a soma dos valores.

### 149. Elabore um algoritmo/programa que crie uma matriz 3x6 com valores

aleatórios reais. Ao final o algoritmo/programa deverá:
- Mostrar os valores da matriz;
- Pedir um valor real do usuário;
- Multiplicar todos os valores pelo valor fornecido pelo usuário;
- Mostrar novamente os valores da matriz.

### 150. Elabore um algoritmo/programa que crie uma matriz 4x4 com valores

aleatórios reais. Ao final o algoritmo/programa deverá:
- Mostrar os valores da matriz;
- Mostrar o valor e a posição do maior elemento;
- Mostrar o valor e a posição do menor elemento.

### 151. Elabore um algoritmo/programa que crie um vetor com 20 valores int

aleatórios (entre 0 e 999). O seu algoritmo/programa deverá:
- Mostrar os valores do vetor original;
- Classificar em ordem crescente os valores do vetor;
- Mostrar os valores do vetor já classificado.

### 152. Elabore um algoritmo/programa que crie um vetor com 10 valores int

preenchidos pelo usuário. O seu algoritmo/programa deverá:
- Mostrar todos os valores do vetor;
- Mostrar o valor da média dos elementos;
- Mostrar quantos valores são maiores que a média.

### 153. Elabore um algoritmo/programa que crie dois vetores:

- Um para guardar os nomes de cinco pessoas;
- Um para guardar as notas das cinco pessoas;
O seu algoritmo/programa deverá receber o nome e anota de cada pessoa
(guardando em cada vetor correspondente) e ao final fornecer:
- A listagem com posição, nome e nota de cada aluno;
- O nome do aluno com maior nota;
- O nome do aluno com menor nota.

### 154. Elabore um algoritmo/programa que crie uma matriz 3x6, onde as linhas

representam os vendedores e as colunas representam os meses de Janeiro a
Junho. As células representam as vendas de cada vendedor em um
determinado mês. O exemplo abaixo representa uma amostra de como essa
matriz poderia ser preenchida.
Janeiro Fevereiro Março Abril Maio Junho
Vendedor 1 450,00 660,00 980,00 267,00 497,00 655,20
Vendedor 2 990,00 149,50 125,00 634,00 225,31 223,87
Vendedor 3 725,25 220,00 476,50 445,00 987,00 268,10
O seu algoritmo/programa deverá gerar aleatoriamente os valores de venda
para as células. Os valores podem ser de 0,00 a 1000,00. Ao final deverá
mostrar:
- A matriz de vendas;
- O total geral de vendas;
- O nome do vendedor que vendeu mais;
- O nome do mês que a loja mais vendeu;
- A média de vendas por vendedor;
- A média de vendas por mês.

### 155. Faça um algoritmo/programa para obter as matrizes A = (a )4x4 e B = (b )4x4, sabendo

ij ij
que suas leis de formação são a = 2i – 3j e b = 3i – j2. Seu algoritmo deve verificar se é
ij ij
possível calcular as seguintes operações AB, A+B, B-A. Caso seja possível o
algoritmo/programa deverá calcular as operações se não for possível o
algoritmo/programa deverá emitir uma mensagem justificando ao usuário o porque de
não ser possível efetuar o cálculo.

### 156. Faça um algoritmo/programa para obter as matrizes A = (a )4x4 e B = (b )4x4, sabendo

ij ij
que suas leis de formação são a = 2i – 3j e b = 3i – j2. Seu algoritmo/programa deverá
ij ij
calcular, e imprimir, o detA e o detB por Laplace.

### 157. Elabore um algoritmo/programa que determine a matriz X tal que

4 1 3 1 2 −1
   
2 6 2 −1 + X =3 0 2 1 . Seu algoritmo/programa deverá verificar se
   
   
−4 −3 −2 1 4 6
   
é possível calcular o det e a matriz inversa da matriz X. Imprima uma mensagem
indicando se é possível ou não efetuar tais cálculos.

### 158. Sendo

A =
 2
3
6
2
1
−
5
1
1
7
0
8
− 1 −

7
3
2
2

B =
 −
1
4
5
1 2
0
2
4
−
9
3
2
6
−
3
−
3
1
5

C =
 4
2
5
6
−
1
7
7
1
1
3
9
1
5
−
6
9
4
3 
,
faça um algoritmo/programa que calcule a matriz X de modo que:
3(X - A) = 2(B + X)+ 6C.
Seu algoritmo/programa deverá verificar se é possível calcular o det da matriz X, se
sim, seu algoritmo/programa deverá calcular e imprimir seu determinante por Laplace.

---

_Conversão realizada a partir do PDF original. Recomenda-se conferir visualmente as expressões matemáticas dos exercícios 1, 16, 20, 25, 36, 61, 67, 124-126, 136-138 e 155-158._
