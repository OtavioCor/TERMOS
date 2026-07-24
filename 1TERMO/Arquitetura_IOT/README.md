# 🚀 Guia de Aulas: Arquitetura IoT na Prática

Bem-vindos ao nosso ecossistema de aprendizagem em Internet das Coisas! Este documento serve como nossa bússola para entender como conectar o mundo físico ao digital, transformando dados brutos em soluções inteligentes.

---

## 📅 1. Nossa Jornada de Aprendizado (Conteúdo Programático)
Nossas aulas são estruturadas como um sistema IoT real: começamos na captura do dado e vamos até a nuvem.

*   **Fundamentos e Conceitos**: O que é IoT além do termo técnico? Modelos de arquitetura e mercado atual.
*   **A Borda (Edge)**: Como os sensores conversam com o mundo físico e coletam informações.
*   **A Conexão**: Como os dados viajam. Vamos desmistificar protocolos como MQTT e HTTP.
*   **O Destino (Cloud & Dashboards)**: Para onde vão os dados? Criação de telas e análise de informações.
*   **Segurança**: Como garantir que ninguém invada ou manipule nossos dispositivos.

---

## 🤖 2. Desbravando o Ecossistema Arduino
O Arduino será nossa principal ferramenta para dar vida aos projetos. Aqui, o foco não é apenas decorar comandos, mas entender o comportamento do hardware.

*   **Escolha do Hardware**: Diferenças práticas entre o Arduino clássico (para lógica local) e placas com Wi-Fi nativo (como o ESP32) para IoT.
*   **Dominando a IDE**: Configuração do ambiente de trabalho e instalação de bibliotecas para acelerar o desenvolvimento.
*   **Pensamento Sequencial**: Entendendo a dinâmica do `setup()` (o nascimento do circuito) e do `loop()` (o coração pulsante do código).
*   **Eletrônica Sem Medo**: Como controlar a energia através de pinos digitais e ler variações do mundo real com pinos analógicos.

---

## 💻 3. C++: O Motor do Nosso Hardware
Para fazer o hardware responder instantaneamente, usamos o C++. Vamos focar no que realmente importa para microcontroladores, sem complicação acadêmica excessiva.

*   **Gerenciamento de Memória**: Por que os tipos de dados (`int`, `float`, `bool`) importam tanto quando temos pouca memória disponível.
*   **Tomada de Decisão**: Criando inteligência local no dispositivo para ele decidir o que fazer sozinho (`if`, `switch`).
*   **Otimização de Código**: Por que devemos evitar a função `delay()` e como criar códigos que realizam múltiplas tarefas ao mesmo tempo.

### 🛠️ Código de Bolso: Piscar sem travar o sistema
Este exemplo mostra como criar um temporizador inteligente sem congelar o processador do Arduino:

```cpp
const int ledPin = 2;              // Pino onde o LED está conectado
unsigned long tempoAnterior = 0;   // Guarda o último momento em que o LED mudou de estado
const long intervalo = 1000;       // Tempo de espera (1 segundo)

void setup() {
  pinMode(ledPin, OUTPUT);         // Configura o pino como saída de energia
}

void loop() {
  unsigned long tempoAtual = millis(); // Conta o tempo desde que a placa ligou

  // Se passou o tempo necessário, inverte o estado do LED
  if (tempoAtual - tempoAnterior >= intervalo) {
    tempoAnterior = tempoAtual;
    digitalWrite(ledPin, !digitalRead(ledPin));
  }
}
```

---

## 🐍 4. Python: A Ponte para a Nuvem e Inteligência
Enquanto o C++ roda no chip monitorando o sensor, o Python entra em cena em computadores ou gateways (como o Raspberry Pi) para tratar volumes maiores de dados e enviá-los para a internet.

*   **Produtividade**: Sintaxe limpa, rápida e manipulação simplificada de dados no formato JSON.
*   **Integração de Sistemas**: Como ler as informações que o Arduino envia pela porta USB (Comunicação Serial).
*   **Comunicação em Rede**: Criando conexões rápidas e leves usando o protocolo padrão da indústria (MQTT).

### 🛠️ Código de Bolso: Escutando o Arduino e postando na internet
Este script roda no computador, recebe a leitura do sensor feita pelo Arduino e a joga diretamente em um servidor IoT:

```python
import serial
import paho.mqtt.client as mqtt
import time

# Configurando a porta USB correta e a velocidade de conversa
porta_serial = serial.Serial('/dev/ttyUSB0', 9600)

# Configurando nossa conexão com a nuvem (Broker MQTT gratuito)
cliente_iot = mqtt.Client()
cliente_iot.connect("hivemq.com", 1883, 60)

print("Sincronização iniciada. Aguardando dados do sensor...")

while True:
    if porta_serial.in_waiting > 0:
        # Lê a linha enviada pelo Arduino e limpa os espaços vazios
        dados_sensor = porta_serial.readline().decode('utf-8').rstrip()
        print(f"Monitorado localmente: {dados_sensor}")
        
        # Publica o dado em um tópico exclusivo na internet
        cliente_iot.publish("minha_turma/iot/sensores", dados_sensor)
```
