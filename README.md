# Projeto de Aprendizado de Máquina com Redes Multicamadas 🧠
---
### Autor
- **Nome:** Gustavo Alves de Oliveira
- **Matrícula:** 12311ECP026
- **Disciplina:** Aprendizagem de Máquina
- **Faculdade:** Universidade Federal de Uberlândia


🤖📊🔍

>Este projeto utiliza técnicas de Aprendizado de Máquina para encontrar o mínimo global em funções complexas, chamadas funções
multimodais, no caso a função Rastrigin e a função Rosenbrock. Usamos a estratégia de Evolução Diferencial para encontrar a
combinação de valores paras N variáveis que essas funções possuem, de modo a minimizar seu valor.\
O algortimo desenvolvido para a evolução foi feito de modo geral, para adicionar funções para avaliadas pelo sistema, basta implementar
a função quando ela recebe um array contendo os valores das N variáveis, bem como os limites inferior e superior de cada variável.

### Algoritmos de Otimização

**O que são:** Os algoritmos de otimização são métodos computacionais utilizados para encontrar a melhor solução possível para um determinado problema, considerando um conjunto de restrições e critérios pré-definidos. Eles exploram um espaço de busca em busca da solução que otimiza uma determinada função objetivo.

**Exemplos de algoritmos conhecidos:**
- Algoritmo Genético
- Algoritmo de Enxame de Partículas (PSO)
- Algoritmo de Otimização por Enxame de Vagalumes (FA)
- Algoritmo de Otimização por Colônia de Formigas (ACO)
- Algoritmo de Otimização por Enxame de Abelhas (ABC)
- Algoritmo de Otimização por Enxame de Gafanhotos (GWO)

**Para que servem:** Os algoritmos de otimização são usados em uma variedade de áreas, incluindo otimização de funções matemáticas, engenharia de sistemas, otimização de roteamento, otimização de design, entre outros.

**Casos de uso:**
- Otimização de parâmetros em modelos matemáticos ou estatísticos.
- Otimização de rotas de veículos para reduzir custos de transporte.
- Otimização de layout de fábricas para aumentar a eficiência de produção.

### Computação Evolutiva: Evolução Diferencial

**O que é:** A Evolução Diferencial (DE) é uma técnica de otimização pertencente à família de algoritmos de computação evolutiva. Ela é inspirada no processo de seleção natural e evolução das espécies.

**Para que serve:** A Evolução Diferencial é usada para resolver problemas de otimização global, especialmente em espaços de busca contínuos e multi-dimensionais.

**Como funciona:** Na DE, uma população de soluções candidatas (vetores de parâmetros) é evoluída ao longo de várias gerações. Isso é feito através de operadores genéticos, como mutação, recombinação e seleção, para explorar e explorar o espaço de busca em busca da melhor solução.

**Vantagens:**
- Boa convergência para ótimos globais em espaços de busca complexos.
- Facilidade de implementação e ajuste de parâmetros.
- Eficiência computacional em problemas de alta dimensionalidade.

**Desvantagens:**
- Sensível à escolha de parâmetros.
- Pode ser computacionalmente intensivo para problemas de grande escala.

### [Função Rastrigin](https://www.sfu.ca/~ssurjano/rastr.html)

> <img src="data:image/jpeg;base64,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"
    />

**O que é:** A Função Rastrigin é uma função de teste comumente utilizada para avaliar o desempenho de algoritmos de otimização. Ela é não-convexa e multimodal, o que a torna desafiadora para muitos métodos de otimização.

**Para que serve:** A Função Rastrigin é usada principalmente como um benchmark para avaliar o desempenho de algoritmos de otimização em espaços de busca multi-modais e não-convexos.

**Fórmula matemática:**
A formulação da Função Rastrigin para um vetor $$ x $$ de dimensão $$ n $$ é dada por:

$$
    f(x) = An + \sum_{i=1}^{n} (x_i^2 - A\cos(2\pi x_i))
$$

Onde $$ A $$ é uma constante geralmente definida como $$ 10 $$.

### [Função Rosenbrock](https://www.sfu.ca/~ssurjano/rosen.html)

> <img src="https://slideplayer.com.br/slide/4832439/15/images/15/Fun%C3%A7%C3%A3o+de+Rosenbrock+Fun%C3%A7%C3%A3o+banana+%3A.jpg"
    width="480px"
    height="300px"
    />

> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Rosenbrock3.gif/300px-Rosenbrock3.gif">

**O que é:** A Função Rosenbrock, também conhecida como "vale de Rosenbrock" ou "vale de banana", é outra função de teste popular para avaliar algoritmos de otimização. Ela é caracterizada por uma longa e estreita depressão.

**Para que serve:** Assim como a Função Rastrigin, a Função Rosenbrock é usada como um benchmark para avaliar o desempenho de algoritmos de otimização, especialmente em problemas não-lineares e multimodais.

**Fórmula matemática:**
A formulação da Função Rosenbrock para um vetor $$ x $$ de dimensão $$ n $$ é dada por:


$$
    f(x) = \sum_{i=1}^{n-1} (100(x_{i+1} - x_i^2)^2 + (1 - x_i)^2) 
$$

A função Rosenbrock atinge seu mínimo global de $$ f(x) = 0 $$ em $$ x_i = 1 $$ para $$ i = 1, 2, ..., n $$.


> Visite o site da [SFU](https://www.sfu.ca/~ssurjano/optimization.html) para mais exemplos de funções para teste em algoritmos de otimização.

### Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **./src**: Contém os códigos-fonte;

### Dependências do Projeto

Para executar o projeto, é necessário instalar a seguinte biblioteca Python:

- Numpy: Biblioteca para criar e operar vetores de forma eficiente.

```bash
pip install numpy
```

### Como Executar o Projeto

1. Clone o repositório do projeto.
2. Instale as dependências listadas acima.
3. Execute o arquivo **main.py**

### Conclusões

> Através de alguns testes podemos constatar que o algoritmo consegue convergir para o conjunto de valores das variáveis independentes
usadas de modo a minimizar a função que está sendo avaliada. Não é surpresa que, a medida que aumentamos a quantidade de variáveis
independentes para compor as funções multimodais, mais alterações temos que fazer nos parâmetros da evolução diferencial, que são eles:
**aumentar o número de gerações que serão consideradas**, **aumentar a quantidade de indivíduos por geração**, **modificar a taxa de cruzamento** 
e **modificar o fator de escala para a criação do mutante**.

🚀🔍💡

---
