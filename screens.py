import pygame

pygame.init()
btnSize = (200, 100)
miniBtnSize = (100, 50)
hlSize = (210, 110)
miniHlSize = (104, 54)
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
    screen.blit(pygame.image.load("data/Players/Man/Man_2/Idle.png"), (825, 275), (96, 96, 240, 240))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), btnSize), (400, 500))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), btnSize), (800, 500))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), miniBtnSize), (1200, 675))
    if btn == 1:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), hlSize), (395, 495))
    elif btn == 2:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), hlSize), (795, 495))
    elif btn == 3:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), miniHlSize), (1198, 673))
    screen.blit(pygame.transform.scale(font.render('Choose The Gender\nOf Your Character', True, txtColor), (600, 100)), (400, 50))
    screen.blit(font.render('Male', True, txtColor), (850, 525))
    screen.blit(font.render('Female', True, txtColor), (429, 525))
    screen.blit(pygame.transform.scale(font.render('Back', True, txtColor), (80, 46)), (1210, 677))

def characterChooseScreen(screen, font, gender):
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_6/2.png"), (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_7/2.png"), (1400, 750)), (0, 0))
    
def gameScreen(screen, font, backgrounds, mapa, wave, enemies, gender):
    screen.blit(pygame.transform.scale(backgrounds["nature_" + str(mapa)], (1400, 750)), (0, 0))
    screen.blit(font.render('Wave: ' + str(wave), True, txtColor), (1200, 25))
    if enemies == 0:
        wave += 1
    
def deadScreen(screen, font, charcter):
    screen.fill((64, 64, 64))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Players/" + charcter + "/Dead.png"), (240, 1200)), (100, 200))
    screen.blit(pygame.transform.scale(font.render('You Are Dead', True, txtColor, (255, 255, 255, 255)), (600, 100)), (400, 425))