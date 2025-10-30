import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y)

    running = True
    while running:
        #set FPS to 60 and convert to seconds
        dt = clock.tick(60) /1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        
        updatable.update(dt)

        #render objs
        for sprite in drawable:
            sprite.draw(screen)
        
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

