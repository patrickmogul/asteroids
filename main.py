import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init()

def main():
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Set groups as containers for Player
    Player.containers = (updatable, drawable)
    
    # Set containers for Asteroid and AsteroidField
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    # Create player in the center of the screen
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    # Create asteroid field
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        # Update all updatable objects
        updatable.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return
        
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Delta time in seconds.
        
if __name__ == "__main__":
    main()
