from GLOBALS import *
import pygame
import os
from pygame.locals import *


class PartyController(object):
    global EVENT_QUEUE

    def __init__(self):
        self.characters = []
        self.center = SCREEN_CENTER
        self.step_speed = 5

    def update(self):
        for event in EVENT_QUEUE:
            if event[0] == "CLICK":
                engaged = False
                for character in self.characters:
                    if character.location.collidepoint(event[1]):
                        engaged = True
                if event[1] is not None and not engaged:
                    x = 0
                    for character in self.characters:
                        character.set_target(self.get_offset(event[1], x))
                        x += 1
        for character in self.characters:
            character.update()

    def get_offset(self, location, position):
        offset = location
        if position == 0:
            offset = (location[0], location[1]-32)
        elif position == 1:
            offset = (location[0]+32, location[1]-32)
        elif position == 2:
            offset = (location[0]-32, location[1])
        elif position == 3:
            offset = (location[0]+64, location[1])
        elif position == 4:
            offset = (location[0]+32, location[1]+32)
        elif position == 5:
            offset = (location[0], location[1]+32)
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
    global EVENT_QUEUE

    def __init__(self, sprite_size=(32, 64), image=None, location=None):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_size = sprite_size
        if location is not None:
            self.location = location
        else:
            self.location = pygame.rect.Rect(0, 0, self.sprite_size[0], self.sprite_size[0])
        if image is not None:
            self.surface = pygame.image.load(os.path.join('data/art', image))
        else:
            self.surface = pygame.Surface(self.location[0], self.location[1])
        self.surface.set_colorkey(self.surface.get_at((0, 0)))
        self.sprite = pygame.Surface(sprite_size)
        self.sprite.fill(RED)
        self.sprite.set_colorkey(RED)
        self.location.width = self.sprite_size[0]
        self.location.height = self.sprite_size[0]
        self.direction = "RIGHT"
        self.target = None
        self.move_speed = 3

    def update(self):
        clicked = False
        for event in EVENT_QUEUE:
            if event[0] == "CLICK" and self.location.collidepoint(event[1]):
                clicked = True
        if clicked:
            self.target = None
            top = self.sprite_size[1] - self.location.height
            EVENT_QUEUE.append(("MENU", (self.location.midtop[0], self.location.midtop[1] - top)))
        if self.target is not None:
            self.move()

    def set_target(self, location):
        self.target = location

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
        top = self.sprite_size[1] - self.location.height
        return self.location.topleft[0], self.location.topleft[1] - top
