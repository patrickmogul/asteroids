import pygame
import constants
from player import Player

pygame.init()

def main():
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create player in the center of the screen
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        # Draw the player
        player.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Delta time in seconds.
        
if __name__ == "__main__":
    main()
