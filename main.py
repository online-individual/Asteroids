import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    black = (0, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)
        
        pygame.display.flip()

    pygame.quit()

    print(
            f"""
            Starting Asteroids!
            Screen width: {SCREEN_WIDTH}
            Screen height: {SCREEN_HEIGHT
            }"""
            )


if __name__ == "__main__":
    main()
