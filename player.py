import pygame
import os

def idleAnimation(screen, character, size, place, plyrBtnSize, btnPlace):
    images = os.listdir("data/Players/" + character + "/Idle")
    for i in range(1,len(images)):
        if plyrBtnSize is not None:
            screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerButton.png"), plyrBtnSize), btnPlace)
            screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerButton.png"), plyrBtnSize), btnPlace)
            screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerButton.png"), plyrBtnSize), btnPlace)
        screen.blit(pygame.transform.scale(pygame.image.load("data/Players/" + character + "/Idle/" + str(i) + ".png"), size), place)

"""character = "Man/Man_2"
running = True
size = (250, 250)
place = (575, 225)
plyrBtnSize = (250, 400)
btnPlace = (575, 150)
pygame.init()
screen = pygame.display.set_mode((1400, 750))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    images = os.listdir("data/Players/" + character + "/Idle")
    for i in range(10,(len(images) * 10)):
            screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerButton.png"), plyrBtnSize), btnPlace)
            screen.blit(pygame.transform.scale(pygame.image.load("data/Players/" + character + "/Idle/" + str(i//10) + ".png"), size), place)
    pygame.display.update()"""