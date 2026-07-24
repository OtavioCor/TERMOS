# 📋 Plano de Ensino: Engenharia de Requisitos

Bem-vindos ao nosso guia de aulas focado em **Levantamento e Análise de Requisitos**. Este documento detalha as etapas, técnicas e entregáveis necessários para descobrir, documentar e validar o que um sistema de software realmente deve fazer.

---

## 📅 1. Cronograma e Conteúdo das Aulas

O aprendizado é dividido em quatro fases lógicas que simulam o ciclo de vida real de um projeto de software.

*   **Fase 1: Fundações**: O papel do analista e a diferença gritante entre o desejo do cliente e a real necessidade do negócio.
*   **Fase 2: Técnicas de Elicitação**: Como extrair informações usando metodologias ágeis e tradicionais.
*   **Fase 3: Modelagem e Documentação**: Transformando conversas e anotações em diagramas e especificações técnicas formais.
*   **Fase 4: Validação e Feedback**: Ferramentas visuais para validar as regras com o cliente antes de iniciar o desenvolvimento.

---

## 🎯 2. Requisitos Funcionais vs. Não Funcionais

A base de qualquer especificação técnica reside em separar o comportamento do sistema de suas restrições operacionais.

### Requisitos Funcionais (RF)
*   **O que é**: Define as ações que o sistema deve executar (o "o quê").
*   **Foco**: Recursos, fluxos de dados, cálculos e interações diretas do usuário.
*   **Exemplo**: *RF-01: O sistema deve permitir que o cliente filtre produtos por faixa de preço.*

### Requisitos Não Funcionais (RNF)
*   **O que é**: Define os critérios de qualidade e limites de operação (o "como").
*   **Foco**: Desempenho, segurança, usabilidade, confiabilidade e compatibilidade tecnológica.
*   **Exemplo**: *RNF-01: O sistema deve criptografar todas as senhas de usuários usando o algoritmo SHA-256.*

---

## 🧠 3. Técnicas de Elicitação e Descoberta

Nesta etapa, aprendemos a extrair o conhecimento que muitas vezes nem o próprio cliente consegue expressar claramente.

### 🌪️ Brainstorming (Tempestade de Ideias)
*   **Objetivo**: Estimular a criatividade da equipe e do cliente no início do projeto.
*   **Regra de Ouro**: Foco na quantidade de ideias, proibindo críticas ou julgamentos precoces.
*   **Dinâmica**: Uso de mapas mentais e post-its virtuais para agrupar conceitos e descobrir dores ocultas.

### 🗣️ Entrevistas Estruturadas e Não Estruturadas
*   **Objetivo**: Coleta aprofundada de dados diretamente com os tomadores de decisão (Stakeholders).
*   **Preparação**: Elaboração de roteiros com perguntas abertas (ex: *"Como você realiza essa tarefa manualmente hoje?"*).
*   **Execução**: Técnicas de escuta ativa e registro detalhado para evitar vieses do analista.

---

## 🎨 4. Prototipagem: Validando Ideias Visualmente

Antes de escrever uma única linha de código, materializamos os requisitos em modelos visuais para mitigar riscos de desalinhamento.

*   **Baixa Fidelidade (Wireframes)**: Esboços em papel ou ferramentas simples para validar o fluxo de navegação e a disposição dos elementos na tela.
*   **Alta Fidelidade**: Protótipos interativos e clicáveis (criados em ferramentas como Figma ou Adobe XD) para testar a usabilidade e a experiência do usuário (UX).
*   **Ciclo de Feedback**: Apresentação ao cliente para aprovação do fluxo de trabalho e ajuste rápido de requisitos mal interpretados.

---

## 📊 5. Diagramas e Modelagem de Requisitos

A modelagem visual traduz regras de negócio complexas em diagramas compreensíveis por desenvolvedores e arquitetos de software.

*   **Diagrama de Casos de Uso (UML)**: Mapeamento visual de *quem* (Atores) faz *o quê* (Casos de Uso) dentro dos limites do sistema.
*   **Diagrama de Fluxo de Dados (DFD)**: Visualização do caminho que a informação percorre, identificando processos, depósitos de dados e entidades externas.
*   **Diagrama de Atividades**: Representação gráfica do passo a passo algorítmico e decisões lógicas de um processo de negócio.

---

## 📝 6. Relatórios Técnicos e Documentação

O entregável final desta disciplina é o artefato que serve como contrato técnico entre a equipe de desenvolvimento e o cliente.

*   **Documento de Especificação de Requisitos de Software (SRS)**: Estrutura padronizada (baseada nas normas IEEE) contendo escopo, restrições e premissas.
*   **Matriz de Rastreabilidade**: Tabela dinâmica que conecta cada requisito à sua técnica de elicitação de origem e ao seu respectivo caso de teste.
*   **Critérios de Aceite**: Definição clara e testável de quando um requisito é considerado oficialmente concluído e funcional.
