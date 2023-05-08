import pygame
import time

def mainScreen(num):
    screen.fill((255, 255, 255))
    screen.blit(pygame.transform.scale(backgrounds["nature_" + str(num)], (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("Test/data/Other/Buttons/button.png"), (200, 100)), (900, 200))
    screen.blit(pygame.transform.scale(pygame.image.load("Test/data/Other/Buttons/button.png"), (200, 100)), (900, 500))
    play = font.render('Play', True, (90, 90, 90))
    quit = font.render('Quit', True, (90, 90, 90))
    screen.blit(play, (955, 225))
    screen.blit(quit, (955, 525))
    
def genderChooseScreen():
    screen.blit(pygame.transform.scale(pygame.image.load("Test/data/Other/Buttons/button.png"), (200, 100)), (400, 500))
    screen.blit(pygame.transform.scale(pygame.image.load("Test/data/Other/Buttons/button.png"), (200, 100)), (800, 500))
    female = font.render('Female', True, (90, 90, 90))
    male = font.render('Male', True, (90, 90, 90))
    screen.blit(female, (429, 525))
    screen.blit(male, (850, 525))

running = True
playing = False
num = 1
time_1 = 0
pygame.init()
pygame.font.init()
font = pygame.font.Font("Test/data/Other/Font/evil_empire/Evil_Empire.otf", 50)
screen = pygame.display.set_mode((1400, 750))
pygame.display.set_caption("I Don't Know")
icon = pygame.image.load("Test/data/IDK.png")
backgrounds = {"nature_1": "", "nature_2": "", "nature_3": "", "nature_4": "", "nature_5": "", "nature_6": "", "nature_7": "", "nature_8": ""}
for background in backgrounds:
    path = "Test/data/" + background + "/origbig.png"
    backgrounds[background] = pygame.image.load(path)
pygame.display.set_icon(icon)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not playing:
        if time_1 == 0:
            time_1 = time.time()
        time_2 = time.time()
        delta_time = time_2 - time_1
        if delta_time >= 5:
            time_1 = time.time()
            if num == 8:
                num = 1
            else:
                num += 1
        mainScreen(num)
    pygame.display.update()
