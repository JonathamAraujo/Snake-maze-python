from labirintos import maze, screen, move, posPlayer


def play():
    screen()
    while True:
        command = input("Mover (WASD ou Q para sair):").strip().lower()

        if command=="q":
           print("Saindo do jogo...")
           break
        elif command=="w":
           move(-1,0)
        elif command=="s":
           move(1,0)
        elif command=="a":
           move(0,-1)
        elif command=="d":
           move(0,1)
        elif posPlayer==maze[-1][7]:
           print("Parabéns, você venceu o labirinto de nível [dificuldade]!")
           break
        else:
           print("ERRO! comando inválido!")
         
        screen()
play()