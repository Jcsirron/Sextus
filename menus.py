from pygame import Rect
from pygame import Surface
from pygame import sprite


class Button(sprite):
    def __init__(self):
        self.rect = Rect(0, 0, 1, 1)
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


class ContextButton(sprite):
    def __init__(self):
        self.rect = Rect(0, 0, 1, 1)
        self.context_rect = Rect(0, 0, 1, 1)
        self.surface = None

    def get_rect(self):
        return self.rect

    def get_surface(self):
        return self.surface
