import pygame
from GLOBALS import *


class Button(object):
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 1, 1)
        self.surface = None

    def get_rect(self):
        return self.rect

    def get_surface(self):
        return self.surface

    def update(self):
        pass


class Menu(object):
    def __init__(self):
        self.banners = []
        self.buttons = []

    def update(self):
        pass


class ContextButton(object):
    global EVENT_QUEUE

    def __init__(self, position):
        context_font = pygame.font.Font('data/savate-regular.otf', 12)
        self.surface = context_font.render("TEST BUTTON", False, WHITE)
        self.rect = self.surface.get_rect()
        self.rect.center = position
        self.active = True

    def update(self):
        for event in EVENT_QUEUE:
            if event[0] == "CLICK":
                if self.rect.collidepoint(event[1]):
                    pass
                else:
                    self.active = False

    def click(self):
        pass

    def get_rect(self):
        return self.rect

    def get_surface(self):
        return self.surface
