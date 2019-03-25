from GLOBALS import *
import pygame
import os
from pygame.locals import *


class PartyController(object):
    def __init__(self):
        self.characters = []
        self.center = SCREEN_CENTER
        self.step_speed = 5

    def update(self, direction=None, location=None):
        if direction is not None:
            if direction == "Left":
                direction = (self.center[0] - self.step_speed, self.center[1])
            elif direction == "Right":
                direction = (self.center[0] + self.step_speed, self.center[1])
            elif direction == "Up":
                direction = (self.center[0], self.center[1] - self.step_speed)
            elif direction == "Down":
                direction = (self.center[0], self.center[1] + self.step_speed)
            else:
                direction = self.center
            x = 0
            for character in self.characters:
                character.update(self.get_offset(direction, x))
                x += 1
        elif location is not None:
            x = 0
            print("location is: " + str(location))
            for character in self.characters:
                character.update(self.get_offset(location, x))
                x += 1
        else:
            for character in self.characters:
                character.update()

    def get_offset(self, location, position):
        offset = location
        if position == 0:
            offset = (location[0]+32, location[1]-16)
        elif position == 1:
            offset = (location[0]+64, location[1]-16)
        elif position == 2:
            offset = (location[0]+16, location[1])
        elif position == 3:
            offset = (location[0]+80, location[1])
        elif position == 4:
            offset = (location[0]+64, location[1]+16)
        elif position == 5:
            offset = (location[0]+32, location[1]+16)
        return offset

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        x = 0
        remove = False
        for i in self.characters:
            if i is character:
                remove = True
                break
            x += 1
        if remove:
            self.characters.pop(x)

    def draw_party(self):
        party_list = []
        for character in self.characters:
            party_list.append((character.get_draw_frame(), character.get_location()))
        return party_list


class Character(pygame.sprite.Sprite):
    def __init__(self, sprite_size=(32, 64), image=None, location=None):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_size = sprite_size
        if location is not None:
            self.location = location
        else:
            self.location = pygame.rect.Rect(SCREEN_CENTER[0], 0, self.sprite_size[0], self.sprite_size[1])
        if image is not None:
            self.surface = pygame.image.load(os.path.join('data/art', image))
        else:
            self.surface = pygame.Surface(self.location[0], self.location[1])
        self.surface.set_colorkey(self.surface.get_at((0, 0)))
        self.sprite = pygame.Surface(sprite_size)
        self.sprite.fill(RED)
        self.sprite.set_colorkey(RED)
        self.location.width = self.surface.get_width()
        self.location.height = self.surface.get_height()
        self.direction = "RIGHT"
        self.target = None
        self.move_speed = 3

    def update(self, target=None):
        if target is not None:
            self.target = target
            print("target is: " + str(self.target))
        if self.target is not None:
            self.move()

    def move(self):
        if self.target[0] < self.location.centerx:
            self.direction = "LEFT"
            if self.target[0] < self.location.centerx - self.move_speed:
                self.location.centerx = self.location.centerx - self.move_speed
            else:
                self.location.centerx = self.target[0]
        elif self.target[0] > self.location.centerx:
            self.direction = "RIGHT"
            if self.target[0] > self.location.centerx + self.move_speed:
                self.location.centerx = self.location.centerx + self.move_speed
            else:
                self.location.centerx = self.target[0]

        if self.target[1] < self.location.centery:
            self.direction = "UP"
            if self.target[1] < self.location.centery - self.move_speed:
                self.location.centery = self.location.centery - self.move_speed
            else:
                self.location.centery = self.target[1]
        elif self.target[1] > self.location.centery:
            self.direction = "DOWN"
            if self.target[1] > (self.location.centery + self.move_speed):
                self.location.centery = self.location.centery + self.move_speed
            else:
                self.location.centery = self.target[1]

        if self.location.center == self.target:
            self.target = None

    def get_surface(self):
        return self.surface

    def get_draw_frame(self):
        self.sprite.fill(RED)
        if self.direction == "UP":
            self.sprite.blit(self.surface, (0, 0), (self.sprite_size[0], 0, self.sprite_size[0], self.sprite_size[1]))
        elif self.direction == "LEFT":
            self.sprite.blit(self.surface, (0, 0), (self.sprite_size[0]*2, 0, self.sprite_size[0], self.sprite_size[1]))
        elif self.direction == "RIGHT":
            self.sprite.blit(self.surface, (0, 0), (self.sprite_size[0]*3, 0, self.sprite_size[0], self.sprite_size[1]))
        else:
            self.sprite.blit(self.surface, (0, 0), (0, 0, self.sprite_size[0], self.sprite_size[1]))
        return self.sprite

    def get_location(self):
        return self.location
