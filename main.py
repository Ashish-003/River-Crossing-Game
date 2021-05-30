#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
import time
from config import *
running = False
game_mode = False
screen = pygame.display.set_mode((1200, 1000))
player1ch = 0
player1cha = 0
flag1 = 0
flag2 = 0
flag = 0
pl1 = 1

count = 0
speed1 = 0
speed2 = 0
clc = pygame.time.Clock()
sharko()
setshark_list()
running = False
press = True
press1 = False
pl1 = 1
pl2 = 0
player1_score = 0
player2_score = 0
while press:
    for event in pygame.event.get():
        message()

        # time=(int)((pygame.time.get_ticks()) /1000)
        # key controls

        if event.type == pygame.QUIT:
            press = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = True
                press = False

        pygame.display.update()
tim1 = time.time()
while running:
    message()
    screen.fill((82, 219, 255))
    pygame.draw.rect(screen, green, [0, 930, 1200, 70])
    pygame.draw.rect(screen, green, [0, 740, 1200, 70])
    pygame.draw.rect(screen, green, [0, 560, 1200, 70])
    pygame.draw.rect(screen, green, [0, 380, 1200, 70])
    pygame.draw.rect(screen, green, [0, 200, 1200, 70])
    pygame.draw.rect(screen, green, [0, 0, 1200, 70])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fish()
    if pl1:  # player1 starts here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1ch = -1.2
            if event.key == pygame.K_RIGHT:
                player1ch = 2.5
            if event.key == pygame.K_UP:
                player1cha = -1.2
            if event.key == pygame.K_DOWN:
                player1cha = 2.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1ch = 0
            if event.key == pygame.K_RIGHT:
                player1ch = 0
            if event.key == pygame.K_UP:
                player1cha = 0
            if event.key == pygame.K_DOWN:
                player1cha = 0
        print_shark(speed1)  # prints shark
        ms1()  # prints start and end
        player1(rect.x, rect.y)  # prints player
        tim2 = time.time()
        player1_score = scorep(rect.y, pl1, pl2) - int(tim2 - tim1)
        flag1 = collide_fish(rect.centerx, rect.centery) # check for collision
        flag2 = collide_shark(rect.centerx, rect.centery) 
        pl2 = flag1 or flag2
        pl1 = not pl2
        if pl2 == 1:
            hit()
        rect.centerx += player1ch
        rect.centery += player1cha
        if rect.x <= 0:
            rect.x = 0
        elif rect.x >= 1133:
            rect.x = 1133
        if rect.y <= 0:
            rect.y = 0
        elif rect.centery >= 963:
            rect.centery = 963
        flag1 = 0
        flag2 = 0
        if rect.y <= 50:
            speed1 += 1
            pl1 = 0
            pl2 = 1
            success()  # prints success
        if pl2 == 1:
            rct.centerx = 610
            rct.centery = 38
            set0()
            player1ch = 0
            player1cha = 0

    if pl2:  # player2 starts here

        if event.type == pygame.KEYDOWN:  # for moving
            if event.key == pygame.K_a:
                player1ch = -1.2
            if event.key == pygame.K_d:
                player1ch = 2.5
            if event.key == pygame.K_w:
                player1cha = -1.2
            if event.key == pygame.K_s:
                player1cha = 2.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player1ch = 0
            if event.key == pygame.K_d:
                player1ch = 0
            if event.key == pygame.K_w:
                player1cha = 0
            if event.key == pygame.K_s:
                player1cha = 0
        print_shark(speed2)  # prints plastic
        player2(rct.x, rct.y)  # prints player
        ms2()  # prints end and start
        tim1 = time.time()
        player2_score = scorep(rct.y, pl1, pl2) - int(tim1 - tim2)  # score = score - time taken
        flag1 = collide_fish(rct.centerx, rct.centery)
        flag2 = collide_shark(rct.centerx, rct.centery)  # check for collision
        pl1 = flag1 or flag2
        if pl1 == 1:
            count += 1
            hit()  # prints crashed
        pl2 = not pl1

        rct.centerx += player1ch
        rct.centery += player1cha
        if rct.x <= 3:
            rct.x = 3
        elif rct.x >= 1133:

            rct.x = 1133
        if rct.y <= 0:
            rct.y = 0
        elif rct.centery >= 963:
            rct.centery = 963
        flag1 = 0
        flag2 = 0
        if rct.y >= 910:
            speed2 += 1
            count += 1
            pl1 = 1
            pl2 = 0
            success()
        if pl1 == 1:
            rect.centerx = 610
            rect.centery = 963
            set0()
            player1ch = 0
            player1cha = 0

    print_score1(player1_score)  # prints score1
    print_score2(player2_score)  # prints score2
    pygame.display.update()
    if count > 3:
        running = False
        press1 = True
    clc.tick(FPS)
while press1:

    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            press1 = False

        if player1_score >= player2_score:
            msg = font3.render('PLAYER 1 WINS', True, red)
            screen.blit(msg, (180, 450))
        else:
            msg = font3.render('PLAYER 2 WINS', True, red)
            screen.blit(msg, (180, 450))

        pygame.display.update()
        