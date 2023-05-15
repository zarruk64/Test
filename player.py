import pygame
import os

death = False

def idleAnimation(screen, character, size, place, plyrBtnSize, btnPlace, image):
    idle = []
    folder = os.listdir("data/Players/" + character + "/Idle")
    for i in range(1,len(folder)):
        idle.append(pygame.image.load("data/Players/" + character + "/Idle/" + str(i) + ".png"))
    if plyrBtnSize is not None:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerButton.png"), plyrBtnSize), btnPlace)
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerButton.png"), plyrBtnSize), btnPlace)
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerButton.png"), plyrBtnSize), btnPlace)
    screen.blit(pygame.transform.scale(idle[int(image)], size), place)

def walkAnimation(screen, character, size, place, image, right, left):
    walk = []
    folder = os.listdir("data/Players/" + character + "/Walk")
    for i in range(1,len(folder)):
        walk.append(pygame.image.load("data/Players/" + character + "/Walk/" + str(i) + ".png"))
    if right:
        screen.blit(pygame.transform.scale(walk[int(image)], size), place)
    elif left:
        screen.blit(pygame.transform.flip(pygame.transform.scale(walk[int(image)], size), True, False), place)

def runAnimation(screen, character, size, place, image, right, left):
    run = []
    folder = os.listdir("data/Players/" + character + "/Run")
    for i in range(1,len(folder)):
        run.append(pygame.image.load("data/Players/" + character + "/Run/" + str(i) + ".png"))
    if right:
        screen.blit(pygame.transform.scale(run[int(image)], size), place)
    elif left:
        screen.blit(pygame.transform.flip(pygame.transform.scale(run[int(image)], size), True, False), place)
    
def deadAnimation(screen, character, size, place, image, dead):
    dead = []
    folder = os.listdir("data/Players/" + character + "/Dead")
    for i in range(1,len(folder)):
        dead.append(pygame.image.load("data/Players/" + character + "/Dead/" + str(i) + ".png"))
    if dead:
        screen.blit(pygame.transform.scale(dead[4], size), place)
    else:
        screen.blit(pygame.transform.scale(dead[int(image)], size), place)