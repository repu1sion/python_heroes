#!/usr/bin/python3

import pygame

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
