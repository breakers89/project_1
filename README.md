# Testes básicos com `for`, `range` e `random`

Projeto simples em Python para praticar estruturas de repetição, geração de números aleatórios, pausas na execução e limpeza do terminal.

## 📌 Objetivo

Este script demonstra como:

- Repetir instruções usando `for`;
- Definir uma sequência de números com `range()`;
- Gerar um número inteiro aleatório com `random.randint()`;
- Pausar a execução com `time.sleep()`;
- Limpar o terminal usando `os.system("clear")` em sistemas Linux.

## 🧰 Tecnologias e módulos

- **Python 3**
- `random`: gera valores aleatórios;
- `time`: permite pausar a execução por um período;
- `os`: permite executar o comando de limpeza do terminal.

Os módulos utilizados fazem parte da biblioteca padrão do Python, então não é necessário instalá-los separadamente.

## 📁 Arquivo do projeto

```text
.
├── README.md
└── test1_for_range_random
```

> Salve o código do exemplo no arquivo `test1_for_range_random`. Se você usar outro nome, ajuste o comando de execução abaixo.

## ▶️ Como executar

No Ubuntu ou em outra distribuição Linux com Python 3 instalado, abra o terminal na pasta do projeto e execute:

```bash
python3 test1_for_range_random
```

Para verificar se o Python 3 está instalado:

```bash
python3 --version
```

## 💻 Código

```python
import random
import os
import time

print("TESTE DE FOR")

for i in range(10):
    print(i)

time.sleep(10)

print("TESTE RANGE")

for i in range(1, 10, 1):
    print(i)

time.sleep(10)

print("TESTE RANDOM")

numero = random.randint(1, 10)
print(numero)

time.sleep(10)
os.system("clear")
```

## 🧠 Entendendo o código

### 1. Laço `for`

```python
for i in range(10):
    print(i)
```

Repete o `print()` dez vezes e mostra os números de `0` a `9`. Em Python, a contagem de `range(10)` começa em zero e não inclui o limite final (`10`).

### 2. Função `range()`

```python
for i in range(1, 10, 1):
    print(i)
```

O `range()` recebe, neste exemplo:

- `1`: início da sequência;
- `10`: limite final, que não é incluído;
- `1`: passo, ou seja, o incremento a cada repetição.

Assim, são exibidos os números de `1` a `9`. Como o passo padrão é `1`, `range(1, 10)` produziria o mesmo resultado.

### 3. Número aleatório com `random.randint()`

```python
numero = random.randint(1, 10)
print(numero)
```

Gera e exibe um número inteiro aleatório entre `1` e `10`, incluindo os dois limites.

### 4. Pausa com `time.sleep()`

```python
time.sleep(10)
```

Interrompe a execução do programa por aproximadamente dez segundos antes de continuar. No script, isso permite observar cada etapa separadamente.

### 5. Limpeza do terminal com `os.system()`

```python
os.system("clear")
```

Executa o comando `clear`, comum em terminais Linux, para limpar a tela. Esse comando é específico do ambiente: no Windows, normalmente se usa `cls`.

## 🧪 Resultado esperado

A saída será semelhante a esta (o número aleatório pode mudar a cada execução):

```text
TESTE DE FOR
0
1
2
3
4
5
6
7
8
9

TESTE RANGE
1
2
3
4
5
6
7
8
9

TESTE RANDOM
7
```

Depois de mostrar o número aleatório, o programa espera mais dez segundos e limpa o terminal. Por isso, a saída anterior pode desaparecer ao final da execução.

## ⚠️ Observações

- O programa leva cerca de **30 segundos** em pausas: dez segundos após cada uma das três etapas.
- `random.randint(1, 10)` não garante um número diferente a cada execução; o valor é escolhido aleatoriamente.
- `os.system("clear")` depende de um terminal compatível com o comando `clear`.
- Não são necessárias bibliotecas externas.

## 🚀 Possíveis melhorias

- Permitir que o usuário escolha os limites do `range()`;
- Gerar vários números aleatórios;
- Substituir as pausas longas por um intervalo configurável;
- Detectar o sistema operacional antes de limpar o terminal;
- Adicionar testes automatizados.

## 📚 Conceitos praticados

`for` · `range()` · `random.randint()` · `time.sleep()` · `os.system()` · execução de scripts Python no terminal.
