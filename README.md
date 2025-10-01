# Escape-the-maze

Um mini game de console desenvolvido em **Python**, como projeto da disciplina de **Matemática Aplicada à Computação**.  
O objetivo do jogo é escapar de um labirinto representado por uma **matriz**, escolhendo a dificuldade desejada no menu inicial. O jogador deve encontrar a saída no **menor tempo possível**.  

Se o tempo limite for ultrapassado, o jogador perde a partida.  

---

## Funcionalidades

- Menu inicial com opções de dificuldade (fácil, médio, difícil).  
- Cada dificuldade possui **labirintos pré-definidos**.  
- Seleção aleatória de um labirinto dentre os disponíveis da dificuldade escolhida.  
- Timer que inicia junto com a partida.  
- Condição de vitória (chegar na saída dentro do tempo).  
- Condição de derrota (tempo excedido).  
- Interface via console (modo texto).  

---

## Tecnologias Utilizadas

- **Python 3.10+**  
- **Bibliotecas Python**:
  - `time` → controle de tempo e cronômetro.  
  - `os` → limpar tela e melhorar visualização no console.  
  - `random` → selecionar um labirinto da dificuldade escolhida.  
  - `sys` → saída do programa em algumas partes do menu.  

---

## Como Executar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/escape-do-labirinto.git
2. Acesse o diretório do projeto:
   ```bash
   cd escape-do-labirinto 
3. Execute o jogo:
   ```bash
   python main.py

---

## Estrutura do Projeto

  ```bash
  escape-do-labirinto/
  ├── main.py           # Arquivo principal, inicia o jogo
  ├── labirintos.py     # Conjunto de matrizes dos labirintos (pré-definidos)
  ├── menu.py           # Funções do menu inicial
  ├── utils.py          # Funções auxiliares (timer, limpar tela, etc.)
  └── README.md         # Documentação do projeto
  ```

---

## Autores

**[Artur Peres dos Santos](https://github.com/Artur-Peres)**

[Jonatham Alves Araujo](https://github.com/JonathamAraujo)

[Nome do Integrante 3]

