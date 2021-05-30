#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption('Cross the River')
player1img = pygame.image.load('turtle1.png')
rect = player1img.get_rect()
player2img = pygame.image.load('turtle2.png')
rct = player2img.get_rect()
fishimg = pygame.image.load('fish.png')

# rct = fishimg.get_rect()

font = pygame.font.Font('freesansbold.ttf', 64)
font2 = pygame.font.Font('freesansbold.ttf', 20)
font3 = pygame.font.Font('freesansbold.ttf', 64)

player1_score = 0
player2_score = 0

rect.centerx = 610
rect.centery = 963
rct.centerx = 610
rct.centery = 38

player1ch = 0
player1cha = 0

FPS = 120
screen.fill((82, 219, 255))
speed = 2

# colors here

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (10, 255, 154)


# print player

def player1(x, y):
    screen.blit(player1img, (x, y))


def player2(x, y):
    screen.blit(player2img, (x, y))


# list for coordinates of fishermen

fish_list = []
fish_list.append((200, 740))
fish_list.append((600, 740))
fish_list.append((900, 740))

fish_list.append((350, 560))
fish_list.append((800, 560))

# x y

fish_list.append((130, 380))
fish_list.append((400, 380))
fish_list.append((1000, 380))

fish_list.append((350, 200))
fish_list.append((700, 200))

shark_list = [None] * 7
shark_y = [None] * 7


# print fisherman

def fish():
    i = 0
    while i < 10:
        screen.blit(fishimg, fish_list[i])
        i = i + 1


# class for moving plastic"sharks"

class shark:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('shrak.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # print("ad")

    def hoo(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        self.screen.blit(self.image, self.rect)

    def move(self, x):
        self.rect.centerx += 3 + x

        # print ("sda")

        if self.rect.centerx > 1178:
            self.rect.centerx = 32


# initialze shark

def sharko():
    i = 0
    while i < 7:
        shark_list[i] = shark(screen)
        shark_y[i] = shark(screen)
        i += 1


# set shark coordinates

def setshark_list():
    i = 0
    a = 420
    while i < 7:
        shark_list[i].rect.centerx = a
        if i and 1 == 1:
            a += 420
            a = a % 1200
        else:
            a -= 200
            a = a % 1200
        i += 1
        shark_list[1].rect.centerx = 1030
        shark_y[0].rect.centery = 670
        shark_y[1].rect.centery = 670
        shark_y[2].rect.centery = 485
        shark_y[3].rect.centery = 320
        shark_y[4].rect.centery = 110
        shark_y[5].rect.centery = 110
        shark_y[6].rect.centery = 860


# prints shark oncreen and moves it

def print_shark(x):
    shark_list[0].hoo(shark_list[0].rect.centerx,
                      shark_y[0].rect.centery)
    shark_list[0].move(x)
    shark_list[1].hoo(shark_list[1].rect.centerx,
                      shark_y[1].rect.centery)
    shark_list[1].move(x)
    shark_list[2].hoo(shark_list[2].rect.centerx,
                      shark_y[2].rect.centery)
    shark_list[2].move(x)
    shark_list[3].hoo(shark_list[3].rect.centerx,
                      shark_y[3].rect.centery)
    shark_list[3].move(x)
    shark_list[4].hoo(shark_list[4].rect.centerx,
                      shark_y[4].rect.centery)
    shark_list[4].move(x)
    shark_list[5].hoo(shark_list[5].rect.centerx,
                      shark_y[5].rect.centery)
    shark_list[5].move(x)
    shark_list[6].hoo(shark_list[6].rect.centerx,
                      shark_y[6].rect.centery)
    shark_list[6].move(x)


# check for collision with fishermen

def collide_fish(x, y):

    i = 0
    ab = 0
    cd = 0

    while i < 10:
        ab = fish_list[i][0] + 32
        cd = fish_list[i][1] + 32
        if abs(ab - x) < 58 and abs(cd - y) < 58:
            return 1
        i += 1


# check for collision with sharks

def collide_shark(x, y):
    i = 0
    while i < 7:
        if abs(shark_list[i].rect.centerx - x) < 64 \
        and abs(shark_y[i].rect.centery - y) < 64:
            return 1
        i += 1


def message():
    msg = font.render('PRESS SPACE TO START', True, (255, 255, 255))
    screen.blit(msg, (180, 430))


def ms1():
    msg = font2.render('START', True, (0, 0, 0))
    screen.blit(msg, (50, 955))
    msg = font2.render('END', True, (0, 0, 0))
    screen.blit(msg, (50, 20))


def ms2():
    msg = font2.render('END', True, (0, 0, 0))
    screen.blit(msg, (50, 955))
    msg = font2.render('START', True, (0, 0, 0))
    screen.blit(msg, (50, 20))


# initialze all flags

surface_1_flag = 0
surface_2_flag = 0
surface_3_flag = 0
surface_4_flag = 0
surface_7_flag = 0

water_1_flag = 0
water_2_flag = 0
water_3_flag = 0
water_4_flag = 0
water_5_flag = 0
final1 = 0
final2 = 0
player1_score = 0
player2_score = 0


# sets all to zero

def set0():
    global player1_score
    global player2_score
    global water_1_flag
    global water_2_flag
    global water_3_flag
    global water_4_flag
    global water_5_flag
    global surface_1_flag
    global surface_2_flag
    global surface_3_flag
    global surface_4_flag
    global surface_7_flag
    global final1
    global final2

    surface_1_flag = 0
    surface_2_flag = 0
    surface_3_flag = 0
    surface_4_flag = 0
    surface_7_flag = 0
    water_1_flag = 0
    water_2_flag = 0
    water_3_flag = 0
    water_4_flag = 0
    water_5_flag = 0
    final1 = 0
    final2 = 0


def scorep(playerY, pl1, pl2):  # clalculating score
    global player1_score
    global player2_score
    global final1
    global final2
    global surface_1_flag
    global water_1_flag
    global water_2_flag
    global water_3_flag
    global water_4_flag
    global water_5_flag
    global surface_2_flag
    global surface_3_flag
    global surface_4_flag
    global surface_7_flag
    global winp1
    global winp2
    if pl1:
        if water_1_flag == 0:
            if playerY < 810:
                water_1_flag = 1
                player1_score += 10
        if surface_1_flag == 0:
            if playerY < 740:
                surface_1_flag = 1
                player1_score += 5
        if surface_2_flag == 0:
            if playerY < 560:
                surface_2_flag = 1
                player1_score += 5
        if water_2_flag == 0:
            if playerY < 630:
                water_2_flag = 1
                player1_score += 10
        if water_3_flag == 0:
            if playerY < 450:
                water_3_flag = 1
                player1_score += 10
        if water_4_flag == 0:
            if playerY < 270:
                water_4_flag = 1
                player1_score += 10
        if water_5_flag == 0:
            if playerY < 70:
                water_5_flag = 1
                player1_score += 10
        if surface_3_flag == 0:
            if playerY < 380:
                surface_3_flag = 1
                player1_score += 5
        if surface_4_flag == 0:
            if playerY < 200:
                surface_4_flag = 1
                player1_score += 5
        if surface_7_flag == 0:
            if playerY <= 55:
                winp1 = 1
        return player1_score
    if pl2:
        if water_1_flag == 0:
            if playerY > 900:
                water_1_flag = 1
                player2_score += 10
        if surface_1_flag == 0:
            if playerY > 810:
                surface_1_flag = 1
                player2_score += 5
        if surface_2_flag == 0:
            if playerY > 630:
                surface_2_flag = 1
                player2_score += 5
        if water_2_flag == 0:
            if playerY > 740:
                water_2_flag = 1
                player2_score += 10
        if water_3_flag == 0:
            if playerY > 560:
                water_3_flag = 1
                player2_score += 10
        if water_4_flag == 0:
            if playerY > 380:
                water_4_flag = 1
                player2_score += 10
        if water_5_flag == 0:
            if playerY > 180:
                water_5_flag = 1
                player2_score += 10
        if surface_3_flag == 0:
            if playerY > 450:
                surface_3_flag = 1
                player2_score += 5
        if surface_4_flag == 0:
            if playerY > 270:
                surface_4_flag = 1
                player2_score += 5
        if surface_7_flag == 0:
            if playerY >= 920:
                winp2 = 1
        return player2_score
    else:
        return 0


def print_score1(x):
    msg = font2.render('Player1 Score: ' + str(x), True, (0, 0, 0))
    screen.blit(msg, (970, 975))


def print_score2(y):
    msg1 = font2.render('Player2 Score: ' + str(y), True, (0, 0, 0))
    screen.blit(msg1, (970, 0))


def success():
    msg = font3.render('SUCCESS', True, white)
    screen.blit(msg, (280, 450))
    pygame.display.update()
    pygame.time.delay(400)


def hit():
    msg = font3.render('CRASHED', True, red)
    screen.blit(msg, (340, 450))
    pygame.display.update()
    pygame.time.delay(400)
