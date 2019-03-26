import pygame
import sys
import os
import party
from GLOBALS import *
from pygame.locals import *

# This line is needed for pyinstaller to properly package the program.
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

# Center the window, since that's the nice way to do it.
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Initialize Pygame
pygame.init()
# Initialize the sound module
pygame.mixer.init()


import menus

# Name the window screen
pygame.display.set_caption(GAME_CAPTION)
# Initialize the clock to limit the frames per second
CLOCK = pygame.time.Clock()
# Initialize a screen to reference later
SCREEN = pygame.display.set_mode(SCREEN_SIZE, 0)


def main_menu():
    pass


def game():
    global EVENT_QUEUE
    # Create background
    background = pygame.Surface(SCREEN_SIZE)
    background.fill(GREY)
    font = pygame.font.Font('data/savate-regular.otf', 12)

    test_buttons = []

    test_text = font.render("USE THIS TEXT", False, WHITE)
    test_char = party.Character(image="Character.png")
    test_char1 = party.Character(image="Character.png")
    test_char2 = party.Character(image="Character.png")
    test_char3 = party.Character(image="Character.png")
    test_char4 = party.Character(image="Character.png")
    test_char5 = party.Character(image="Character.png")

    test_party = party.PartyController()
    test_party.add_character(test_char)
    test_party.add_character(test_char1)
    test_party.add_character(test_char2)
    test_party.add_character(test_char3)
    test_party.add_character(test_char4)
    test_party.add_character(test_char5)

    while True:

        for event in EVENT_QUEUE:
            if event[0] == "MENU":
                test_buttons.append(menus.ContextButton(event[1]))

        EVENT_QUEUE.clear()

        for event in pygame.event.get():
            if event.type is QUIT:
                pygame.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONUP:
                available = True
                for button in test_buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.click()
                        available = False
                if available:
                    EVENT_QUEUE.append(("CLICK", pygame.mouse.get_pos()))
            elif event.type is KEYUP:
                pass
            elif event.type is KEYDOWN:
                pass

        test_party.update()

        SCREEN.blit(background, (0, 0))
        # TODO: put the graphics update here:

        for i in test_party.characters:
            pygame.draw.rect(SCREEN, WHITE, i.location)

        drawlist = test_party.draw_party()
        for i in drawlist:
            SCREEN.blit(i[0], i[1])

        for button in test_buttons:
            button.update()
            if button.active:
                SCREEN.blit(button.get_surface(), button.get_rect())

        # update the screen and limit the FPS to game speed
        pygame.display.update()
        CLOCK.tick(GAME_SPEED)


if __name__ == "__main__":
    game()
