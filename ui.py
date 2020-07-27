#!/usr/bin/python3

import pygame
import pygame.font

class Gem:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/gem.jpeg')
        self.rect = self.image.get_rect()                   # var contains rectangle with image in memory
        self.screen_rect = screen.get_rect()

        # set coords of our rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Ship:
    def __init__(self, screen):
        self.screen = screen
        #self.image = pygame.image.load('images/ship.bmp')

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()                   # var contains rectangle with image in memory
        self.screen_rect = screen.get_rect()

        # set coords of our rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Msg:
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()                    # rectangle of full screen, 1024x768
        self.width, self.height = 200, 50
        self.text_color = (241, 196, 15)                        # gold
        self.font = pygame.font.SysFont(None, 14)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.prep_msg(msg)                                      # call prep_msg once

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        #self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
