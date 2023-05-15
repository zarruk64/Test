import pygame
import time
import screens
import os

running = True
playing = False
dead = False
rightMove = False
leftMove = False
run = False
doing = ""
stage = 1
mapa = 1
maxWaves = {"1": 5, "2": 5, "3": 10, "4": 10, "5": 15, "6": 15, "7": 20, "8": 20}
wave = 1
enemies = 5
gender = ""
character = "Man/Man_2"
health = 100
stamina = 100
lowStamina = False
numChar = 1
num = 1
time_1 = 0
displayScreen = "main"
btn = 1
prevBtn = 0
image = 1
posX = 100
posY = 600
vel = 3
pygame.init()
pygame.font.init()
font = pygame.font.Font("data/Other/Font/evil_empire/Evil_Empire.otf", 50)
screen = pygame.display.set_mode((1400, 750))
pygame.display.set_caption("I Don't Know")
icon = pygame.image.load("data/Icon.png")
backgrounds = {"nature_1": "", "nature_2": "", "nature_3": "", "nature_4": "", "nature_5": "", "nature_6": "", "nature_7": "", "nature_8": ""}
for background in backgrounds:
    path = "data/Nature/" + background + "/origbig.png"
    backgrounds[background] = pygame.image.load(path)
pygame.display.set_icon(icon)
while running:
    if rightMove or leftMove or dead:
        doing = "Walk"
        if run:
            doing = "Run"
        if dead:
            doing = "Dead"
    else:
        doing = "Idle"
    if stamina <= 30:
        lowStamina = True
    else:
        lowStamina = False
    if image >= len(os.listdir("data/Players/" + character + "/" + doing)) - 1:
        image = 1
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
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    prevBtn = btn
                    btn = 3
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and prevBtn != 0:
                    if prevBtn == 1:
                        btn = 1
                    else:
                        btn = 2
                elif event.key == pygame.K_RETURN:
                    if btn == 1:
                        gender = "Woman"
                        displayScreen = "character"
                        image = 1
                    elif btn == 2:
                        gender = "Man"
                        displayScreen = "character"
                        image = 1
                    else:
                        displayScreen = "main"
                        btn = 1
            elif displayScreen == "character":
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if btn > 1:
                        btn -= 1
                    else:
                        btn = 3
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if btn < 3:
                        btn += 1
                    else:
                        btn = 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    prevBtn = btn
                    btn = 4
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and prevBtn != 0:
                    if prevBtn == 1:
                        btn = 1
                    elif prevBtn == 2:
                        btn = 2
                    else:
                        btn = 3
                elif event.key == pygame.K_RETURN:
                    if btn == 1 or btn == 2 or btn == 3:
                        character = gender + "/" + gender + "_" + str(btn)
                        displayScreen = "game"
                        image = 1
                    else:
                        displayScreen = "gender"
                        btn = 1
                        image = 1
            elif displayScreen == "game":
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    leftMove = True
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        run = True
                    image = 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    rightMove = True
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        run = True
                    image = 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if health < 100: 
                        health += 10
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if health > 0: 
                        health -= 10
                if event.key == pygame.K_q:
                    if wave >= maxWaves[str(mapa)]:
                        if mapa >= 8:
                            stage += 1
                            mapa = 1
                        else:
                            mapa += 1
                        wave = 1
                    else:
                        wave += 1
                elif event.key == pygame.K_e:
                    displayScreen = "dead"
                    image = 1
            elif displayScreen == "dead":
                if event.key == pygame.K_RETURN:
                    if btn == 1:
                        stage = 1
                        mapa = 1
                        wave = 1
                        enemies =5
                        displayScreen = "game"
                        image = 1
                    elif  btn == 2:
                        displayScreen = "main"
                if image >= 5:
                    dead = True
        if event.type == pygame.KEYUP:
            if displayScreen == "game":
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    leftMove = False
                    image = 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    rightMove = False
                    image = 1
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        run = False
    for waves in maxWaves:
        maxWaves[waves] = maxWaves[waves] * stage
    if not playing:
        keys = pygame.key.get_pressed()
        if displayScreen == "game":
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and rightMove == False:
                posX -= vel
                if (keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]) and stamina > 0:
                    stamina -= .85
                    posX -= vel * 1.2
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and leftMove == False:
                posX += vel
                if (keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]) and stamina > 0:
                    stamina -= .85
                    posX += vel * 1.2
            if stamina <= 0:
                stamina = 0
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
            screens.genderChooseScreen(screen, font, btn, image)
        elif displayScreen == "character":
            screens.characterChooseScreen(screen, font, btn, gender, image)
        elif displayScreen == "game":
            screens.gameScreen(screen, font, backgrounds, stage, mapa, wave, enemies, character, (posX, posY), image, dead, rightMove, leftMove, run, health, stamina)
        elif displayScreen == "dead":
            screens.deadScreen(screen, font, character, image, dead)
        if stamina < 100 and (lowStamina == False or run == False):
            stamina += .35
    if displayScreen == "gender":
        image += .3
    elif displayScreen == "character":
        image += .5
    elif displayScreen == "game":
        image += .15
    elif displayScreen == "dead":
        image += .02
    pygame.display.update()