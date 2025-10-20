import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize timer
    timer = pygame.time.Clock()

    # Create two groups to manage drawable and updatale objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    # Checks if the user has closed their window and exits the game if so
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
            
        screen.fill("black", rect=None, special_flags=0)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limit framerate to 60FPS
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
