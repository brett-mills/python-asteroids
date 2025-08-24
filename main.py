# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize pygame
    pygame.init()

    # set the size for the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # configure clock to specify a consistent drawing sped
    clock = pygame.time.Clock()
    dt = 0

    # groups allow us to more efficiently update the objects in the game
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add groups to Player as a static variable
    # any players created are automatically added to the groups
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # instantiate a player and the asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update all player objects
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with_player(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with_shot(shot):
                    shot.kill()
                    asteroid.split()
        
        # fill screen with black
        screen.fill("black")

        # draw all player objects
        for object in drawable:
            object.draw(screen)

        # update the screen
        pygame.display.flip()
        

        # increment the clock - call once per frame
        # the 60 value limits us to 60 frames per second
        # tick returns the time since the last call - divide by 1000 to get milliseconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
