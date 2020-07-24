#!/usr/bin/python3

import sys
import pygame
import random

from ui import Gem, Ship, Enemy

# global variables
screen = None
enemy = None
gem = None

# key - hero, value - probability (part of total sum, not percent)
heroes = {'knight': 6, 'archer': 6, 'mage': 6, 
          'grunt': 6, 'berserk': 6, 'shaman': 6,
          'puma': 6, 'archeress': 6, 'druid': 6,
          'skeleton': 6, 'skeleton_archer': 6, 'acolyte': 6,
          'horse_knight': 3, 'ballista': 3,
          'ogre': 3, 'catapult': 3,
          'ent': 3, 'elf_ballista': 3,
          'flesheater': 3, 'fleshthrower': 3,
          'paladin': 1, 'iron_maiden': 1,
          'thrall': 1, 'grim': 1,
          'elain': 1, 'taradrim': 1,
          'nerzul': 1, 'gorgoroth': 1
}

# class without objects, keeps settings
class Set:
    d_width = 1024
    d_height = 768
    bg_color = (120, 0, 60)
    screen = None


# FUNCTIONS --------------------------------------------------------------------a

# we pass max value in our range (our summ of all probabilities)
def rand(summ):
    rv = random.randrange(0, summ, 1)    # range from 1 to our summ, with step 1
    return rv


# init func --------------------------------------------------------------------
def init():
    global screen
    global enemy
    global gem

    print("init()")
    # randomizer init
    random.seed()

    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((Set.d_width, Set.d_height))

    # game objects init
    enemy = Enemy(screen)
    gem = Gem(screen)


# main loop --------------------------------------------------------------------
def run():
    global screen
    global enemy
    global gem

    # main loop
    while True:
        # events processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # screen redraw
        screen.fill(Set.bg_color)
        enemy.draw()
        gem.draw()
        pygame.display.flip()


# main func --------------------------------------------------------------------
if __name__ == "__main__":
    init()

    # randomizer -----
    i = 0
    # get sum of values in heroes dict
    h_values = heroes.values()
    h_sum = sum(h_values)
    print('sum of all heroes values:', h_sum)

    # print available heroes
    print(heroes)

    while (i < 100):
        r = rand(h_sum)
        #print('rand value is:', r)
        # go through dict to find our hero
        current_sum = 0
        for key, value in heroes.items():
            current_sum += value
            if (r < current_sum):
                print(key, '->', current_sum, 'random:', r)
                break
        i += 1
    # end randomizer -----


    run()
    
