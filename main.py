import pygame
import time
import screens

running = True
playing = False
dead = False
mapa = 1
maxWaves = {"1": 5, "2": 5, "3": 10, "4": 10, "5": 15, "6": 15, "7": 20, "8": 20}
wave = 1
enemies = 5
gender = ""
character = ""
numChar = 1
num = 1
time_1 = 0
displayScreen = "main"
btn = 1
prevBtn = 0
pygame.init()
pygame.font.init()
font = pygame.font.Font("data/Other/Font/evil_empire/Evil_Empire.otf", 50)
screen = pygame.display.set_mode((1400, 750))
pygame.display.set_caption("I Don't Know")
icon = pygame.image.load("data/IDK.png")
backgrounds = {"nature_1": "", "nature_2": "", "nature_3": "", "nature_4": "", "nature_5": "", "nature_6": "", "nature_7": "", "nature_8": ""}
for background in backgrounds:
    path = "data/Nature/" + background + "/origbig.png"
    backgrounds[background] = pygame.image.load(path)
pygame.display.set_icon(icon)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if displayScreen == "main":
                if btn == 1:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_w:
                        btn = 2
                    elif event.key == pygame.K_RETURN:
                        displayScreen = "gender"
                elif btn == 2:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_w:
                        btn = 1
                    elif event.key == pygame.K_RETURN:
                        running = False
            elif displayScreen == "gender":
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    if btn == 1:
                        btn = 2
                    elif  btn == 2:
                        btn = 1
                elif event.key == pygame.K_DOWN:
                    prevBtn = btn
                    btn = 3
                elif event.key == pygame.K_UP and prevBtn != 0:
                    if prevBtn == 1:
                        btn = 1
                    else:
                        btn = 2
                elif event.key == pygame.K_RETURN:
                    if btn == 1:
                        gender = "Woman"
                        displayScreen = "character"
                    elif btn == 2:
                        gender = "Man"
                        displayScreen = "character"
                    else:
                        displayScreen = "main"
                        btn = 1
            elif displayScreen == "character":
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if num > 1:
                        num -= 1
                    else:
                        num = 3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if num < 3:
                        num += 1
                    else:
                        num = 1
                elif event.key == pygame.K_RETURN:
                    if btn == 1 or btn == 2 or btn == 3:
                        character = gender + "/" + gender + "_" + str(num)
                        displayScreen = "game"
                    else:
                        displayScreen = "gender"
                        btn = 1
            elif displayScreen == "game":
                if event.key == pygame.K_q:
                    if wave >= maxWaves[str(mapa)]:
                        if mapa >= 8:
                            mapa = 1
                        else:
                            mapa += 1
                        wave = 1
                    else:
                        wave += 1
                elif event.key == pygame.K_e:
                    dead = True
                    displayScreen = "dead"
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
        if displayScreen == "main":
            screens.mainScreen(screen, font, backgrounds, num, btn)
        elif displayScreen == "gender":
            screens.genderChooseScreen(screen, font, btn)
        elif displayScreen == "character":
            screens.characterChooseScreen(screen, font, gender)
        elif displayScreen == "game":
            screens.gameScreen(screen, font, backgrounds, mapa, wave, enemies, character)
        elif displayScreen == "dead":
            screens.deadScreen(screen, font, character)
    pygame.display.update()