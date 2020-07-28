#!/usr/bin/python3

import sys
import pygame
import random

from ui import Gem, Ship, Enemy, Msg, Label

# global variables
screen = None
enemy = None
gem = None
msg = None
label_gems = None
label_gems_cnt = None
label_team = None

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

class Player:
    gems = 5
    own_heroes = []

# FUNCTIONS --------------------------------------------------------------------

# we pass max value in our range (our summ of all probabilities)
def rand(summ):
    rv = random.randrange(0, summ, 1)    # range from 1 to our summ, with step 1
    return rv

def get_hero():
    global heroes
    global msg

    h_values = heroes.values()
    h_sum = sum(h_values)
    r = rand(h_sum)
    current_sum = 0
    for key, value in heroes.items():
        current_sum += value
        if (r < current_sum):
            print(key, '->', current_sum, 'random:', r)
            hero_name = key
            Player.own_heroes.append(hero_name)         # add hero to player's own list of heroes
            msg = Msg(screen, hero_name)
            print('Now you have in collection:', Player.own_heroes)
            break

# gem click
def check_gem_clicked(gem, mouse_x, mouse_y):
    global label_gems_cnt 

    if gem.rect.collidepoint(mouse_x, mouse_y):
        print('[Gem clicked]')
        if Player.gems > 0:
            Player.gems -= 1
            label_gems_cnt = Label(screen, str(Player.gems), 150, 20, 16, (241, 196, 15))
            get_hero()
            print('Opened a gem. Gems remained:', Player.gems)
        else:
            print('No more gems to open!')


# init func --------------------------------------------------------------------
def init():
    global screen
    global enemy
    global gem
    global label_gems
    global label_gems_cnt 
    global label_team

    print("init()")
    # randomizer init
    random.seed()

    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((Set.d_width, Set.d_height))

    # game objects init
    enemy = Enemy(screen)
    gem = Gem(screen)
    label_gems = Label(screen, 'Gems:', 100, 20, 16, (241, 196, 15))
    label_gems_cnt = Label(screen, str(Player.gems), 150, 20, 16, (241, 196, 15))
    label_team = Label(screen, 'TEAM', 100, 200, 16, (241, 196, 15))

# main loop --------------------------------------------------------------------
def run():
    global screen
    global enemy
    global gem
    global msg
    global label_gems
    global label_gems_cnt 
    global label_team

    # main loop
    while True:
        # events processing
        for event in pygame.event.get():
            # keys
            if event.type == pygame.QUIT:
                sys.exit()
            # mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_gem_clicked(gem, mouse_x, mouse_y)

        # screen redraw
        screen.fill(Set.bg_color)

        enemy.draw()
        gem.draw()
        label_gems.draw()
        label_gems_cnt.draw()
        label_team.draw()
        if (msg):
            msg.draw()

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

    '''
    while (i < 100):
        r = rand(h_sum)
        current_sum = 0
        for key, value in heroes.items():
            current_sum += value
            if (r < current_sum):
                print(key, '->', current_sum, 'random:', r)
                break
        i += 1
    '''
    run()




