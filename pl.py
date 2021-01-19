import pygame
import random

FPS = 50


def hit(x1, y1, x2, y2, db1, db2):
    if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db1 and y1 < y2 + db2:
        return 1
    else:
        return 0


def start_screen():
    intro_text = ["               В погоне за звёздами", "",
                  "        Правила игры:",
                  "Управление кораблём осуществляется",
                  "с помощью клавиш W, A, S, D, выстрел -",
                  "- с помощью клавиши пробела. При",
                  "столкновении с астероидом игра",
                  "завершается."]

    fon = pygame.transform.scale(pygame.image.load('bg_st.png'), (400, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 28)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, 1, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return 1  # начинаем игру
        pygame.display.flip()


def stop_screen():
    intro_text = [" GAME OVER"]
    fon = pygame.transform.scale(pygame.image.load('bg_st.png'), (400, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font('font.ttf', 70)
    text_coord = 150
    for line in intro_text:
        string_rendered = font.render(line, 1, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру заново
        pygame.display.flip()


pygame.init()

screen = pygame.display.set_mode((400, 600))
window = pygame.Surface((400, 600))
player = pygame.Surface((60, 60))
aim = pygame.Surface((60, 60))
bullet = pygame.Surface((20, 40))

count = 0
myfont = pygame.font.SysFont('monospase', 40)

player.set_colorkey((0, 0, 0))
aim.set_colorkey((0, 0, 0))
bullet.set_colorkey((0, 0, 0))

img_p = pygame.image.load('p.png')
img_a = pygame.image.load('a3.png')
img_b = pygame.image.load('b.png')
img_bg = pygame.image.load('bg.png')

down = True
done = False

p_x = 180
p_y = 500

a_x = random.randint(0, 340)
a_y = 0

b_x = 1000
b_y = 1000
strike = False

st_sc = 0
stop_sc = 0

while done == False:
    if st_sc == 0:
        st_sc = start_screen()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if i.type == pygame.KEYDOWN and i.key == pygame.K_w:
            p_y -= 10
            if p_y < - 60:
                p_y = 600
        if i.type == pygame.KEYDOWN and i.key == pygame.K_s:
            p_y += 10
            if p_y > 600:
                p_y = - 60
        if i.type == pygame.KEYDOWN and i.key == pygame.K_a:
            p_x -= 10
            if p_x < - 60:
                p_x = 400
        if i.type == pygame.KEYDOWN and i.key == pygame.K_d:
            p_x += 10
            if p_x > 400:
                p_x = - 60
        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            if strike == False:
                strike = True
                b_x = p_x + 20
                b_y = p_y - 40

    if strike:
        b_y -= 5
        if b_y < 0:
            strike = False
            b_x = 1000
            b_y = 1000

    if hit(b_x, b_y, a_x, a_y, 20, 40):
        count += 1
        strike = False
        b_x = 1000
        b_y = 1000
        a_y = 0
        a_x = random.randint(0, 340)

    if down:
        if count < 10:
            a_y += 0.5
        elif count < 30:
            a_y += 0.7
        elif count < 60:
            a_y += 1
        elif count < 100:
            a_y += 1.5
        elif count < 150:
            a_y += 2
        else:
            a_y += 2.5
        if a_y > 600:
            a_y = 0
            a_x = random.randint(0, 340)
            if count < 3:
                count = 0
            else:
                count -= 2

    if hit(p_x, p_y, a_x, a_y, 60, 60):
        count = 0
        strike = False
        b_x = 1000
        b_y = 1000
        a_y = 0
        a_x = random.randint(0, 340)
        stop_screen()
        p_x = 180
        p_y = 500

    string = myfont.render('Счёт: ' + str(count), 0, (255, 255, 255))
    screen.fill((102, 153, 204))
    screen.blit(img_bg, (0, 0))
    player.blit(img_p, (0, 0))
    aim.blit(img_a, (0, 0))
    bullet.blit(img_b, (0, 0))
    screen.blit(player, (p_x, p_y))
    screen.blit(aim, (a_x, a_y))
    screen.blit(bullet, (b_x, b_y))
    window.blit(screen, (0, 0))
    screen.blit(string, (5, 5))
    pygame.display.update()

pygame.quit()
