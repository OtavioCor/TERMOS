# 🐍 Guia de Aulas: Lógica de Programação com Python & Versionamento com GitHub

Bem-vindos ao nosso laboratório de desenvolvimento! Este documento servirá como mapa para aprender a pensar de forma estruturada com **Python** e a proteger, organizar e compartilhar seu trabalho utilizando o **Git** e o **GitHub**.

---

## 📅 1. Jornada de Aprendizado (Conteúdo das Aulas)

O conteúdo é estruturado em ciclos semanais onde a lógica de programação e as boas práticas de versionamento caminham juntas.

*   **Ciclo 1: Primeiros Passos e Ambiente**: O que é um algoritmo, configuração do Python e introdução ao Git.
*   **Ciclo 2: Estruturas de Decisão e Fluxo**: Como o computador faz escolhas e como salvar essas versões do código.
*   **Ciclo 3: Laços de Repetição e Automação**: Repetindo tarefas eficientemente e trabalhando em equipe com repositórios remotos.
*   **Ciclo 4: Organização de Dados e Funções**: Listas, dicionários e modularização de código para projetos organizados.

---

## 💻 2. Domínio da Lógica com Python

Abaixo estão os blocos lógicos fundamentais explicados de forma direta através da sintaxe do Python.

### 🔹 Variáveis e Tipos de Dados
Espaços na memória para armazenar informações. O Python identifica o tipo automaticamente (Tipagem Dinâmica).
*   `int`: Números inteiros (ex: `idade = 21`)
*   `float`: Números com casas decimais (ex: `preco = 49.90`)
*   `str`: Textos e palavras entre aspas (ex: `nome = "Ana"`)
*   `bool`: Verdadeiro (`True`) ou Falso (`False`)

### 🔹 Estruturas Condicionais (`if`, `elif`, `else`)
Permitem que o programa tome decisões com base em testes e operadores lógicos.

```python
# Verificação de acesso ao sistema
idade_usuario = 18

if idade_usuario >= 18:
    print("Acesso concedido.")
else:
    print("Acesso bloqueado: menor de idade.")
```

### 🔹 Estruturas de Repetição (`while` e `for`)
Executam o mesmo bloco de código repetidas vezes sem necessidade de duplicar linhas.

```python
# Loop 'for' percorrendo uma lista de tarefas
tarefas = ["Estudar Python", "Criar repositório", "Dar Commit"]

for tarefa in tarefas:
    print(f"Pendente: {tarefa}")
```

### 🔹 Funções e Modularização
Blocos isolados que realizam tarefas específicas. Evitam repetição e deixam o projeto limpo.

```python
def saudar_aluno(nome_aluno):
    return f"Olá, {nome_aluno}! Bons estudos hoje."

print(saudar_aluno("Carlos"))
```

---

## 🐙 3. Versionamento e Colaboração com GitHub

O GitHub funciona como o portfólio e a máquina do tempo do programador. Aqui aprendemos a salvar o histórico de evolução do código.

### 🔹 Conceitos Chave
*   **Git**: O sistema local que grava as alterações do seu código.
*   **GitHub**: A plataforma na nuvem onde você hospeda seus repositórios e colabora com outros desenvolvedores.
*   **Repositório (Repo)**: A pasta do seu projeto monitorada pelo Git.

### 🔹 Fluxo de Trabalho Essencial (Terminal/Prompt)

Para cada alteração ou nova funcionalidade criada em Python, seguimos o ciclo de comandos abaixo:

1.  **Inicializar o projeto localmente** (Feito apenas uma vez por projeto):
    ```bash
    git init
    ```
2.  **Verificar o status dos arquivos** (Saber o que foi modificado):
    ```bash
    git status
    ```
3.  **Preparar os arquivos** (Adicionar para a lista de salvamento):
    ```bash
    git add nome_do_arquivo.py
    # Ou para adicionar todos os arquivos da pasta:
    git add .
    ```
4.  **Criar um ponto de restauração** (Fotografar o estado atual com uma mensagem explicativa):
    ```bash
    git commit -m "Adiciona a lógica de aprovação do aluno"
    ```
5.  **Enviar para a nuvem (GitHub)**:
    ```bash
    git push origin main
    ```

### 🔹 Boas Práticas para Alunos
*   **Mensagens de Commit Claras**: Evite mensagens como "ajuste" ou "teste". Prefira "Corrige bug no loop while" ou "Cria função de cálculo".
*   **Arquivo README.md**: Todo repositório deve ter um arquivo Markdown explicando o que o projeto faz e como executá-lo.
*   `.gitignore`: Arquivo para listar o que o Git deve ignorar (como arquivos temporários do sistema ou senhas).
