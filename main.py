import pygame
import sys
import os
from GLOBALS import *

# This line is needed for pyinstaller to properly package the program.
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# Center the window, since that's the nice way to do it.
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Initialize Pygame
pygame.init()
# Initialize the sound module
pygame.mixer.init()

# Name the window screen
pygame.display.set_caption(GAME_CAPTION)
# Initialize the clock to limit the frames per second
CLOCK = pygame.time.Clock()
# Initialize a screen to reference later
SCREEN = pygame.display.set_mode(SCREEN_SIZE, 0)


def main_menu():
    pass


def game():
    pass
