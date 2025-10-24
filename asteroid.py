import pygame
import random
from circleshape import CircleShape
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Additional initialization for Asteroid can go here

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # This asteroid is destroyed when split
        self.kill()

        # If this is already the smallest kind, don't spawn more
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        # Choose a random split angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        # New radius is reduced by the minimum radius
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        # Spawn two smaller asteroids at this position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1 * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2 * 1.2