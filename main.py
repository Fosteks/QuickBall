import random
import pygame
import time

from objects import Balls, Coins, Tiles, Particle, Message, Button

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
CENTER = WIDTH // 2, HEIGHT // 2

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption('')

clock = pygame.time.Clock()
FPS = 90

# COLORS **********************************************************************

color_list = [(70, 70, 70)]
r, g, b = 30, 30, 30
for i in range(185):
    b += 1
    color_list.append((r, g, b))
for i in range(185):
    g += 1
    color_list.append((r, g, b))
for i in range(185):
    r += 1
    color_list.append((r, g, b))
for i in range(185):
    b -= 1
    color_list.append((r, g, b))
for i in range(185):
    g -= 1
    color_list.append((r, g, b))
for i in range(185):
    r -= 1
    color_list.append((r, g, b))
for i in range(185):
    b += 1
    color_list.append((r, g, b))
for i in range(185):
    r += 1
    color_list.append((r, g, b))
for i in range(185):
    b -= 1
    color_list.append((r, g, b))
for i in range(185):
    r -= 1
    color_list.append((r, g, b))
list_colors = color_list.extend(list(reversed(color_list)))

RED = (255, 0, 0)
LIGHT_GREEN = (0, 255, 0)
GREEN = (200, 255, 153)
BLUE = (30, 144, 255)
ORANGE = (252, 76, 2)
YELLOW = (254, 221, 0)
PURPLE = (155, 38, 182)
AQUA = (0, 103, 127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (25, 25, 25)
BROWN = (153, 76, 0)
DARK_GREEN = (0, 102, 0)

colors_x = {BROWN: '2', DARK_GREEN: '2.5', YELLOW: '3', LIGHT_GREEN: '3.5', ORANGE: '4', PURPLE: '4,5', RED: '5', 'rainbow': '10'}

color_index = 0
color_play = color = BLUE

# SHOP ********************************************************************

blue_img = pygame.image.load('Assets/blue.jpg')
brown_img = pygame.image.load('Assets/brown.jpg')
dark_green_img = pygame.image.load('Assets/dark_green.png')
yellow_img = pygame.image.load('Assets/yellow.jpg')
light_green_img = pygame.image.load('Assets/light_green.jpg')
orange_img = pygame.image.load('Assets/orange.jpg')
purple_img = pygame.image.load('Assets/purple.jpg')
red_img = pygame.image.load('Assets/red.jpg')
rainbow_img = pygame.image.load('Assets/rainbow.jpg')

blue_btn = Button(blue_img, (50, 50), WIDTH // 4 - 33, HEIGHT - 370)
brown_btn = Button(brown_img, (50, 50), WIDTH // 4 + 47, HEIGHT - 370)
dark_green_btn = Button(dark_green_img, (50, 50), WIDTH // 4 + 127, HEIGHT - 370)
yellow_btn = Button(yellow_img, (50, 50), WIDTH // 4 - 33, HEIGHT - 260)
light_green_btn = Button(light_green_img, (50, 50), WIDTH // 4 + 47, HEIGHT - 260)
orange_btn = Button(orange_img, (50, 50), WIDTH // 4 + 127, HEIGHT - 260)
purple_btn = Button(purple_img, (50, 50), WIDTH // 4 - 33, HEIGHT - 150)
red_btn = Button(red_img, (50, 50), WIDTH // 4 + 47, HEIGHT - 150)
rainbow_btn = Button(rainbow_img, (50, 50), WIDTH // 4 + 127, HEIGHT - 150)

brown_cost = Message(WIDTH // 4 + 70, 215, 15, 'x2-250', None, BROWN, win)
dark_green_cost = Message(WIDTH // 4 + 150, 215, 15, 'x2.5-500', None, DARK_GREEN, win)
yellow_cost = Message(WIDTH // 4 - 10, 320, 15, 'x3-1500', None, YELLOW, win)
light_green_cost = Message(WIDTH // 4 + 70, 320, 15, 'x3.5-3000', None, LIGHT_GREEN, win)
orange_cost = Message(WIDTH // 4 + 150, 320, 15, 'x4-5000', None, ORANGE, win)
purple_cost = Message(WIDTH // 4 - 10, 425, 15, 'x4.5-7500', None, PURPLE, win)
red_cost = Message(WIDTH // 4 + 70, 425, 15, 'x5-10000', None, RED, win)
rainbow_cost = Message(WIDTH // 4 + 150, 425, 15, 'x10-15000', None, WHITE, win)

# SOUNDS **********************************************************************

new_item_fx = pygame.mixer.Sound('Sounds/new_item.mp3')
flip_fx = pygame.mixer.Sound('Sounds/flip.mp3')
score_fx = pygame.mixer.Sound('Sounds/point.mp3')
dead_fx = pygame.mixer.Sound('Sounds/dead.mp3')
score_page_fx = pygame.mixer.Sound('Sounds/score_page.mp3')
brue_fx = pygame.mixer.Sound('Sounds/brue.mp3')
brue_fx.set_volume(0.2)

pygame.mixer.music.load('Sounds/bgm.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

# FONTS ***********************************************************************

title_font = "Fonts/Aladin-Regular.ttf"
score_font = "Fonts/DroneflyRegular-K78LA.ttf"
game_over_font = "Fonts/ghostclan.ttf"
final_score_font = "Fonts/DalelandsUncialBold-82zA.ttf"
new_high_font = "Fonts/BubblegumSans-Regular.ttf"

connected = Message(WIDTH // 2, 120, 55, "QuickBall", title_font, WHITE, win)
score_msg = Message(WIDTH // 2, 100, 60, "0", score_font, (150, 150, 150), win)
game_msg = Message(80, 150, 40, "GAME", game_over_font, BLACK, win)
over_msg = Message(210, 150, 40, "OVER!", game_over_font, WHITE, win)
final_score = Message(WIDTH // 2, HEIGHT // 2, 90, "0", final_score_font, RED, win)
new_high_msg = Message(WIDTH // 2, HEIGHT // 2 + 60, 20, "New Record", None, GREEN, win)
plus_coins = Message(WIDTH // 2, HEIGHT // 2 + 60, 20, '0', None, GREEN, win)
touch_msg = Message(WIDTH // 2, 80, 20, "Нажмите чтобы купить!", None, WHITE, win)
coins_msg = Message(WIDTH // 2, 40, 30, "0", final_score_font, RED, win)
monet_msg = Message(WIDTH // 2 + 65, 36, 30, "монет", None, RED, win)

# Button images

home_img = pygame.image.load('Assets/homeBtn.png')
shop_img = pygame.image.load('Assets/shopBtn.png')
replay_img = pygame.image.load('Assets/replay.png')
sound_off_img = pygame.image.load("Assets/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/soundOnBtn.png")
easy_img = pygame.image.load("Assets/easy.jpg")
hard_img = pygame.image.load("Assets/hard.jpg")

# Buttons ********************************************************************

easy_btn = Button(easy_img, (70, 24), WIDTH // 4 - 10, HEIGHT - 130)
hard_btn = Button(hard_img, (70, 24), WIDTH // 2 + 10, HEIGHT - 130)
home_btn = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT // 2 + 120)
home_btn2 = Button(home_img, (24, 24), WIDTH // 4 - 52, HEIGHT // 2 - 230)
replay_btn = Button(replay_img, (36, 36), WIDTH // 2 - 18, HEIGHT // 2 + 115)
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT // 2 + 120)
shop_btn = Button(shop_img, (60, 50), WIDTH // 4 + 40, HEIGHT - 90)

# Groups **********************************************************************

RADIUS = 70
ball_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
particle_group = pygame.sprite.Group()

ball = Balls((CENTER[0], CENTER[1] + RADIUS), RADIUS, 90, win)
ball_group.add(ball)
ball = Balls((CENTER[0], CENTER[1] - RADIUS), RADIUS, 270, win)
ball_group.add(ball)

# TIME ************************************************************************

start_time = pygame.time.get_ticks()
current_time = 0
coin_delta = 850
tile_delta = 2000

# VARIABLES *******************************************************************

clicked = False
new_coin = True
score = 0
file = open('player_info', 'r')
all_coins = int(file.readlines()[0].split('-')[1].strip())
file.close()

player_alive = True
score = 0
highscore = 0
sound_on = True
easy_level = True

home_page = True
shop_page = False
game_page = False
score_page = False
last_time = time.time()

running = True
while running:
    win.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or \
                    event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_page:
            if not clicked:
                clicked = True
                for ball in ball_group:
                    ball.dtheta *= -1
                    flip_fx.play()

        if event.type == pygame.MOUSEBUTTONDOWN and game_page:
            clicked = False

    if home_page:
        connected.update()

        pygame.draw.circle(win, BLACK, CENTER, 80, 20)
        ball_group.update(color)

        if easy_btn.draw(win):
            ball_group.empty()
            ball = Balls((CENTER[0], CENTER[1] + RADIUS), RADIUS, 90, win)
            ball_group.add(ball)

            home_page = False
            game_page = True
            easy_level = True

        if hard_btn.draw(win):
            ball_group.empty()
            ball = Balls((CENTER[0], CENTER[1] + RADIUS), RADIUS, 90, win)
            ball_group.add(ball)
            ball = Balls((CENTER[0], CENTER[1] - RADIUS), RADIUS, 270, win)
            ball_group.add(ball)

            home_page = False
            game_page = True
            easy_level = False

        if shop_btn.draw(win):
            win.fill(GRAY)

            file = open('player_info', 'r')
            items_have = [i.strip() for i in file.readlines()]
            items_have = list(sorted(items_have))
            file.close()
            all_items = ['blue', 'brown', 'dark_green', 'yellow', 'light_green', 'orange', 'purple', 'red', 'rainbow']
            gg_colors = [0] * 9
            for i in range(9):
                if all_items[i] in items_have:
                    gg_colors[i] = GREEN
                else:
                    gg_colors[i] = BLACK

            shop_page = True
            home_page = False
            game_page = False
            easy_level = False

    if shop_page:
        coins_msg = Message(WIDTH // 2 - 20, 40, 30, str(all_coins), final_score_font, RED, win)
        touch_msg.update()
        coins_msg.update()
        monet_msg.update()
        brown_cost.update()
        dark_green_cost.update()
        yellow_cost.update()
        light_green_cost.update()
        orange_cost.update()
        purple_cost.update()
        red_cost.update()
        rainbow_cost.update()

        for i in range(9):
            if all_items[i] in items_have:
                gg_colors[i] = GREEN
            else:
                gg_colors[i] = BLACK

        pygame.draw.rect(win, gg_colors[0], (28, 130, 70, 70))
        pygame.draw.rect(win, gg_colors[1], (108, 130, 70, 70))
        pygame.draw.rect(win, gg_colors[2], (188, 130, 70, 70))
        pygame.draw.rect(win, gg_colors[3], (28, 240, 70, 70))
        pygame.draw.rect(win, gg_colors[4], (108, 240, 70, 70))
        pygame.draw.rect(win, gg_colors[5], (188, 240, 70, 70))
        pygame.draw.rect(win, gg_colors[6], (28, 350, 70, 70))
        pygame.draw.rect(win, gg_colors[7], (108, 350, 70, 70))
        pygame.draw.rect(win, gg_colors[8], (188, 350, 70, 70))

        file = open('player_info', 'a+')
        color_buy = ''
        if blue_btn.draw(win):
            color_play = color = BLUE
        if brown_btn.draw(win):  # 2
            if all_coins >= 250 and 'brown' not in items_have:
                all_coins -= 250
                color_buy = 'brown'
            if 'brown' in items_have:
                color_play = color = BROWN
        if dark_green_btn.draw(win):  # 2.5
            if all_coins >= 500 and 'dark_green' not in items_have:
                all_coins -= 500
                color_buy = 'dark_green'
            if 'dark_green' in items_have:
                color_play = color = DARK_GREEN
        if yellow_btn.draw(win):  # 3
            if all_coins >= 1500 and 'yellow' not in items_have:
                all_coins -= 1500
                color_buy = 'yellow'
            if 'yellow' in items_have:
                color_play = color = YELLOW
        if light_green_btn.draw(win):  # 3.5
            if all_coins >= 3000 and 'light_green' not in items_have:
                all_coins -= 3000
                color_buy = 'light_green'
            if 'light_green' in items_have:
                color_play = color = LIGHT_GREEN
        if orange_btn.draw(win):  # 4
            if all_coins >= 5000 and 'orange' not in items_have:
                all_coins -= 5000
                color_buy = 'orange'
            if 'orange' in items_have:
                color_play = color = ORANGE
        if purple_btn.draw(win):  # 4.5
            if all_coins >= 7500 and 'purple' not in items_have:
                all_coins -= 7500
                color_buy = 'purple'
            if 'purple' in items_have:
                color_play = color = PURPLE
        if red_btn.draw(win):  # 5
            if all_coins >= 10000 and 'red' not in items_have:
                all_coins -= 10000
                color_buy = 'red'
            if 'red' in items_have:
                color_play = color = RED
        if rainbow_btn.draw(win):  # 10
            if all_coins >= 15000 and 'rainbow' not in items_have:
                all_coins -= 15000
                color_buy = 'rainbow'
            if 'rainbow' in items_have:
                color_play = color = 'rainbow'

        if color_buy:
            items_have.append(color_buy)
            file.write('\n' + color_buy)
            new_item_fx.play()
        file.close()

        if home_btn2.draw(win):
            home_page = True
            score_page = False
            game_page = False
            shop_page = False
            player_alive = True
            score = 0
            score_msg = Message(WIDTH // 2, 100, 60, "0", score_font, (150, 150, 150), win)

    if score_page:
        game_msg.update()
        over_msg.update()
        plus_coins.update()

        if score:
            final_score.update(score, color)
            if n:
                plus = ''
                print(all_coins)
                all_coins += score
                print(all_coins)
                file = open('player_info', 'r')
                all = file.readlines()
                file.close()
                file = open('player_info', 'w')
                all[0] = 'coins - ' + str(all_coins) + '\n'
                file.writelines(all)
                file.close()
            if color != BLUE and n:
                plus = f'+ {score}*{colors_x[color_play]} монет'
                all_coins -= score
                all_coins += int(score * float(colors_x[color_play]))
                file = open('player_info', 'r')
                all = file.readlines()
                file.close()
                file = open('player_info', 'w')
                all[0] = 'coins - ' + str(all_coins) + '\n'
                file.writelines(all)
                file.close()
            n = False
            plus_coins = Message(WIDTH // 2 - 20, HEIGHT // 2 + 90, 20, plus, None, RED, win)
        else:
            final_score.update("0", color)
        if score and (score >= highscore):
            new_high_msg.update(shadow=False)

        if home_btn.draw(win):
            home_page = True
            score_page = False
            game_page = False
            player_alive = True
            score = 0
            score_msg = Message(WIDTH // 2, 100, 60, "0", score_font, (150, 150, 150), win)

        if replay_btn.draw(win):
            home_page = False
            score_page = False
            game_page = True
            score = 0
            score_msg = Message(WIDTH // 2, 100, 60, "0", score_font, (150, 150, 150), win)

            if easy_level:
                ball = Balls((CENTER[0], CENTER[1] + RADIUS), RADIUS, 90, win)
                ball_group.add(ball)
            else:
                ball = Balls((CENTER[0], CENTER[1] + RADIUS), RADIUS, 90, win)
                ball_group.add(ball)
                ball = Balls((CENTER[0], CENTER[1] - RADIUS), RADIUS, 270, win)
                ball_group.add(ball)

            player_alive = True

        if sound_btn.draw(win):
            sound_on = not sound_on

            if sound_on:
                sound_btn.update_image(sound_on_img)
                pygame.mixer.music.play(loops=-1)
            else:
                sound_btn.update_image(sound_off_img)
                pygame.mixer.music.stop()

    if game_page:
        pygame.draw.circle(win, BLACK, CENTER, 80, 20)
        ball_group.update(color)
        coin_group.update(color)
        tile_group.update()
        score_msg.update(score)
        particle_group.update()

        if player_alive:
            time_now = time.time()
            if time_now - last_time > 2:
                score += 1
                last_time = time_now
            for ball in ball_group:
                if pygame.sprite.spritecollide(ball, coin_group, True):
                    score_fx.play()
                    score += 4
                    if highscore <= score:
                        highscore = score

                    x, y = ball.rect.center
                    for i in range(10):
                        particle = Particle(x, y, color, win)
                        particle_group.add(particle)

                if pygame.sprite.spritecollide(ball, tile_group, True):
                    x, y = ball.rect.center
                    for i in range(30):
                        particle = Particle(x, y, color, win)
                        particle_group.add(particle)

                    player_alive = False
                    dead_fx.play()
                    brue_fx.play()

            current_time = pygame.time.get_ticks()
            delta = current_time - start_time
            if coin_delta < delta < coin_delta + 100 and new_coin:
                y = random.randint(CENTER[1] - RADIUS, CENTER[1] + RADIUS)
                coin = Coins(y, win)
                coin_group.add(coin)
                new_coin = False

            if current_time - start_time >= tile_delta:
                y = random.choice([CENTER[1] - 80, CENTER[1], CENTER[1] + 80])
                type_ = random.randint(1, 3)
                t = Tiles(y, type_, win)
                tile_group.add(t)

                start_time = current_time
                new_coin = True

        if not player_alive and len(particle_group) == 0:
            score_page = True
            n = True
            game_page = False

            score_page_fx.play()

            ball_group.empty()
            tile_group.empty()
            coin_group.empty()

    pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT), 5, border_radius=10)
    clock.tick(FPS)
    if color_play == 'rainbow':
        color_index += 1
        if color_index >= 1350:
            color_index = 0
        color = color_list[color_index]
    pygame.display.update()

pygame.quit()