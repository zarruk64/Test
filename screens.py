import pygame

pygame.init()
btnSize = (200, 100)
hlSize = (210, 110)
txtColor = (90, 90, 90)

def mainScreen(screen, font, backgrounds, num, btn):
    screen.blit(pygame.transform.scale(backgrounds["nature_" + str(num)], (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), btnSize), (900, 200))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), btnSize), (900, 500))
    if btn == 1:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), hlSize), (895, 195))
    elif btn == 2:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), hlSize), (895, 495))
    screen.blit(font.render('Play', True, txtColor), (955, 225))
    screen.blit(font.render('Quit', True, txtColor), (955, 525))
    
def genderChooseScreen(screen, font, btn):
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_6/2.png"), (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_7/2.png"), (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), btnSize), (400, 500))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), btnSize), (800, 500))
    if btn == 1:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), hlSize), (395, 495))
    elif btn == 2:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), hlSize), (795, 495))
    screen.blit(font.render('Female', True, txtColor), (429, 525))
    screen.blit(font.render('Male', True, txtColor), (850, 525))
    
def deadScreen(screen, font):
    screen.fill((64, 64, 64))
    #Dead picture of character
    screen.blit(pygame.transform.scale(font.render('You Are Dead', True, txtColor, (255, 255, 255, 255)), (600, 100)), (400, 425))