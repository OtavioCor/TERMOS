# 💻 Guia de Aulas: Lógica de Programação Multiamplataforma (Windows, Linux & iOS)

Bem-vindos ao curso! Este documento serve como guia para compreender o raciocínio lógico de programação enquanto desenvolvemos a habilidade de configurar ambientes, manipular arquivos e rodar scripts nos três ecossistemas líderes de mercado: **Windows**, **Linux** e **iOS/macOS**.

---

## 📅 1. Cronograma e Conteúdo das Aulas

O conteúdo une conceitos puros de lógica com a prática de comandos em terminais distintos, preparando o aluno para qualquer mercado de desenvolvimento.

*   **Módulo 1: Anatomia dos Sistemas Operacionais**: Interface de linha de comando (CLI), sistemas de arquivos estruturados e variáveis de ambiente em cada plataforma.
*   **Módulo 2: Fundamentos da Lógica**: Alocação de memória (variáveis e constantes), tipos primitivos de dados e operadores de comparação.
*   **Módulo 3: Estruturas de Seleção**: Tomada de decisão (`if/else`) com base em estados e permissões do sistema operacional.
*   **Módulo 4: Estruturas de Repetição**: Loops (`while` e `for`) aplicados à varredura e automação de arquivos nas pastas do sistema.
*   **Módulo 5: Modularização**: Criação de funções reutilizáveis e parametrização para execução de scripts multiplataforma.

---

## 🔧 2. Terminais e Comandos Essenciais por Sistema

A lógica se traduz através do terminal. Cada sistema possui caminhos e comandos nativos para interagir com o código.

### 🪟 Ambiente Windows (CMD / PowerShell)
*   **Caminhos**: Usa barras invertidas (ex: `C:\Users\Aluno\Documentos`).
*   **Comandos de Navegação**:
    *   `cd [caminho]`: Entra em uma pasta específica.
    *   `dir`: Lista os arquivos e subpastas locais.
    *   `mkdir [nome]`: Cria um novo diretório.

### 🐧 Ambiente Linux (Bash / Terminal)
*   **Caminhos**: Usa barras normais (ex: `/home/aluno/documentos`). Diferencia maiúsculas de minúsculas (*case-sensitive*).
*   **Comandos de Navegação**:
    *   `cd [caminho]`: Entra em uma pasta específica.
    *   `ls`: Lista os arquivos do diretório (`ls -la` exibe os ocultos).
    *   `mkdir [nome]`: Cria um novo diretório.

### 🍏 Ambiente Apple iOS / macOS (Zsh / Terminals / Playgrounds)
*   **Terminal no Mac**: Baseado em Unix (comandos idênticos ao Linux, como `cd`, `ls` e `mkdir`).
*   **iOS (iPhone/iPad)**: Ambiente fechado (Sandbox). Para aprender lógica pura diretamente no ecossistema mobile, utilizamos o aplicativo **Swift Playgrounds** ou emuladores de terminal como o **iTerminal** ou **Ish** (que simula uma linha de comando Alpine Linux).

---

## 💻 3. Conceitos Estruturais de Lógica

A sintaxe muda entre linguagens, mas a estrutura lógica de desenvolvimento permanece universal nos três ambientes.

### 🔹 Entrada de Dados e Variáveis
Coleta de informações vindas do usuário para processamento em memória.

```text
ALGORITMO: Identificar Plataforma
DECLARE plataforma: TEXTO
ESCREVA "Digite o sistema operacional do seu dispositivo atual: "
LEIA plataforma
```

### 🔹 Estruturas Condicionais (Tomada de Decisão)
O programa avalia expressões lógicas e escolhe um caminho com base no sistema operacional detectado.

```text
SE plataforma == "Windows" ENTAO
    ESCREVA "Configurando variáveis via CMD..."
SENAO SE plataforma == "Linux" ENTAO
    ESCREVA "Configurando variáveis via Bash..."
SENAO SE plataforma == "iOS" ENTAO
    ESCREVA "Executando código via Sandbox Apple..."
SENAO
    ESCREVA "Sistema não reconhecido."
FIM_SE
```

### 🔹 Estruturas de Repetição (Laços/Loops)
Execução em massa de tarefas sequenciais baseadas em condições de parada.

```text
PARA cada aplicativo EM lista_de_apps FAÇA
    SE aplicativo.permissao == "Negada" ENTAO
        ESCREVA "Solicitando acesso ao usuário..."
    FIM_SE
FIM_PARA
```

---

## 🚀 4. Executando Algoritmos nos Três Ambientes

Passo a passo rápido de como o aluno coloca o código para rodar em cada cenário (exemplo utilizando um interpretador multiplataforma):

### No Windows 🪟
1. Abra o **Prompt de Comando** (`cmd`).
2. Acesse a pasta do arquivo: `cd C:\Projetos\Logica`
3. Execute o interpretador: `python meu_script.py` ou `node meu_script.js`

### No Linux 🐧
1. Abra o **Terminal** (`Ctrl + Alt + T`).
2. Acesse a pasta do arquivo: `cd /home/aluno/projetos/logica`
3. Execute o interpretador: `python3 meu_script.py` ou `node meu_script.js`

### No iOS 🍏
1. Abra o aplicativo **Swift Playgrounds** (ou um app de terminal mobile como o **iSh**).
2. Para Playgrounds: Crie um novo documento "Script" ou "Blank Page".
3. Digite o código de lógica na tela e toque no botão **Executar Código** (Run Code).
