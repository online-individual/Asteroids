import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    black = (0, 0, 0)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    running = True
    while running:
        #set FPS to 60 and convert to seconds
        dt = clock.tick(60) /1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(black)
        
        player.update(dt)

        #render player
        player.draw(screen)
        
        #redraw screen
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
