# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Crie um jogo da Forca em Python para praticar manipulação de strings, loops, condicionais e entrada de dados. O jogador deve descobrir uma palavra oculta antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Preparar a palavra e o progresso do jogo

#### Descrição
Escolha aleatoriamente uma palavra de uma lista predefinida e prepare a representação que será exibida ao jogador.

#### Requisitos
O programa concluído deve:

- Manter uma lista predefinida com pelo menos cinco palavras.
- Selecionar uma palavra aleatoriamente da lista.
- Exibir cada letra ainda não descoberta como `_`, mantendo as letras na posição correta.
- Definir e exibir o número inicial de tentativas disponíveis.

### 🛠️ Implementar os palpites e o encerramento

#### Descrição
Permita que o jogador tente adivinhar uma letra por vez até descobrir a palavra ou ficar sem tentativas.

#### Requisitos
O programa concluído deve:

- Solicitar um palpite de uma letra e revelar todas as ocorrências corretas na palavra.
- Reduzir as tentativas disponíveis quando o palpite não estiver na palavra.
- Atualizar e exibir o progresso após cada palpite.
- Encerrar quando a palavra for descoberta ou as tentativas acabarem.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra.
