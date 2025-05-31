# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots ,updatable, drawable)


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
          updatable.update(dt)

          for ast in asteroids:
               if ast.is_colliding(player):
                    print("Game over!")
                    sys.exit()
               for shot in shots:
                    if ast.is_colliding(shot):
                         ast.split()
                         shot.kill()

          screen.fill((0,0,0))          
          for spr in drawable:
               spr.draw(screen)

          pygame.display.flip()
          dt = clock.tick(60) / 1000

if __name__ == "__main__":
        main()