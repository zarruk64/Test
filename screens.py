import pygame
import player

pygame.init()
btnSize = (200, 100)
miniBtnSize = (100, 50)
plyrBtnSize = (250, 400)
hlSize = (210, 110)
miniHlSize = (104, 54)
plyrHlSize = (260, 410)
txtColor = (255, 215, 0)

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
    
def genderChooseScreen(screen, font, btn, image):
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_6/2.png"), (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_7/2.png"), (1400, 750)), (0, 0))
    player.idleAnimation(screen, "Man/Man_2", (250, 250), (775, 225), None, None, image)
    player.idleAnimation(screen, "Woman/Woman_3", (250, 250), (375, 225), None, None, image)
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

def characterChooseScreen(screen, font, btn, gender, image):
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_6/2.png"), (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Nature/nature_7/2.png"), (1400, 750)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/button.png"), miniBtnSize), (1200, 675))
    if btn == 1:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerHighlight.png"), plyrHlSize), (145, 145))
    elif btn == 2:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerHighlight.png"), plyrHlSize), (570, 145))
    elif btn == 3:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/playerHighlight.png"), plyrHlSize), (995, 145))
    elif btn == 4:
        screen.blit(pygame.transform.scale(pygame.image.load("data/Other/Buttons/Highlight.png"), miniHlSize), (1198, 673))
    player.idleAnimation(screen, gender + "/" + gender + "_1", (250, 250), (150, 225), plyrBtnSize, (150, 150), image)
    player.idleAnimation(screen, gender + "/" + gender + "_2", (250, 250), (575, 225), plyrBtnSize, (575, 150), image)
    player.idleAnimation(screen, gender + "/" + gender + "_3", (250, 250), (1000, 225), plyrBtnSize, (1000, 150), image)
    screen.blit(pygame.transform.scale(font.render('Back', True, txtColor), (80, 46)), (1210, 677))
    
def gameScreen(screen, font, backgrounds, stage, mapa, wave, enemies, character, position, image, dead, rightMove, leftMove, run, health, stamina):
    screen.blit(pygame.transform.scale(backgrounds["nature_" + str(mapa)], (1400, 750)), (0, 0))
    screen.blit(pygame.image.load("data/Other/IU/backplate.png"), (15, 15))
    screen.blit(pygame.transform.smoothscale(pygame.image.load("data/Players/" + character + "/profile.png"), (63, 49)), (90, 30))
    screen.blit(pygame.transform.smoothscale(pygame.image.load("data/Other/IU/health.png"), (health * 3.66, 36)), (32, 87))
    screen.blit(pygame.image.load("data/Other/IU/healthBar.png"), (30, 85))
    screen.blit(pygame.transform.smoothscale(pygame.image.load("data/Other/IU/stamina.png"), (stamina * 2.66, 36)), (32, 122))
    screen.blit(pygame.image.load("data/Other/IU/staminaBar.png"), (30, 120))
    screen.blit(pygame.image.load("data/Other/IU/bpTop.png"), (28, 85))
    screen.blit(font.render('Stage: ' + str(stage), True, txtColor), (1200, 25))
    screen.blit(font.render('Stage: ' + str(stage), True, txtColor), (1200, 25))
    screen.blit(font.render('Map: ' + str(mapa), True, txtColor), (1200, 75))
    screen.blit(font.render('Wave: ' + str(wave), True, txtColor), (1200, 125))
    if rightMove or leftMove:
        if run:
            player.runAnimation(screen, character, (150, 150), position, image, rightMove, leftMove)
        else:
            player.walkAnimation(screen, character, (150, 150), position, image, rightMove, leftMove)
    elif dead:
        player.deadAnimation(screen, character, (150, 150), position, image, dead)
    else:
        player.idleAnimation(screen, character, (150, 150), position, None, None, image)
    if enemies == 0:
        wave += 1
    
def deadScreen(screen, font, character, image, dead):
    screen.fill((64, 64, 64))
    player.deadAnimation(screen, character, (100, 200), (240, 200), image, dead)
    screen.blit(pygame.transform.scale(font.render('You Are Dead', True, txtColor, (255, 255, 255, 255)), (600, 100)), (400, 425))