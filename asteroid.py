import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        # if small radius, then return
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        # otherwise, generate two new smaller and faster asteroids

        # generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50) 
        
        # new asteroids will move in different directions
        velocity_pos = self.velocity.rotate(random_angle)
        velocity_neg = self.velocity.rotate(-random_angle)

        # calculate new radius of asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # generate first new asteroid and update its velocity
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = velocity_pos * 1.2

        # generate second new asteroid and update its velocity
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = velocity_neg * 1.2
