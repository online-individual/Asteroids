import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    black = (0, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)
        
        #redraw screen
        pygame.display.flip()

        #set FPS to 60 and convert to seconds
        dt = clock.tick(60) /1000
        
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
