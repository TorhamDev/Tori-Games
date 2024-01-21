import pygame
from constants import WINDOW_SIZE, LIFES, PLAYER_SPEED, GREEN_CIRCLE_SPEED,RED_CIRCLE_SPEED, CIRCLE_Y
import random

pygame.init()
pygame.font.init()

defalt_font = pygame.font.Font('./assets/fonts/Pixeboy-z8XGD.ttf', 30)
screen = pygame.display.set_mode(WINDOW_SIZE)
bg = pygame.image.load("./assets/bg.png")
PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("./assets/bird.png"), (80, 80)).convert_alpha()
PLAYER_RECT = PLAYER_IMAGE.get_rect()
PLAYER_RECT.y = 600



dt = 1
clock = pygame.time.Clock()
running = True
GREEN_CIRCLE = pygame.transform.scale(pygame.image.load("./assets/green.png"), (40, 40)).convert_alpha()
GREEN_CIRCLE_RECT = GREEN_CIRCLE.get_rect()
GREEN_CIRCLE_RECT.x += 200
RED_CIRCLE = pygame.transform.scale(pygame.image.load("./assets/red.png"), (40, 40)).convert_alpha()
RED_CIRCLE_RECT = GREEN_CIRCLE.get_rect()
is_over = False
score = 0

while running:

    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not is_over:
        if LIFES <= 0:
            is_over = True
        
        one = pygame.transform.scale2x(defalt_font.render(f'{score}', False, (0, 0, 0)))
        two =  pygame.transform.scale2x(defalt_font.render(f'{score}', False, (255, 255, 255)))
        screen.blit(one, (350, 10))
        screen.blit(two, (349, 10))
        screen.blit(PLAYER_IMAGE, PLAYER_RECT)
        screen.blit(GREEN_CIRCLE, GREEN_CIRCLE_RECT)
        screen.blit(RED_CIRCLE, RED_CIRCLE_RECT)
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            PLAYER_RECT.y -= PLAYER_SPEED + dt
        if keys[pygame.K_s]:
            PLAYER_RECT.y += PLAYER_SPEED + dt
        if keys[pygame.K_a]:
            PLAYER_RECT.x -= PLAYER_SPEED + dt
        if keys[pygame.K_d]:
            PLAYER_RECT.x += PLAYER_SPEED + dt

        # draw to gold duck lifes
        space = 0
        for _ in range(LIFES):
            gold_duck = pygame.transform.scale(pygame.image.load("./assets/gold_duck.png"), (40, 40)).convert_alpha()
            gold_duck_rect = gold_duck.get_rect()
            gold_duck_rect.x += space
            screen.blit(gold_duck, gold_duck_rect)
            space += 25


        PLAYER_RECT.clamp_ip(screen.get_rect())
        
        if PLAYER_RECT.colliderect(GREEN_CIRCLE_RECT):
                GREEN_CIRCLE_SPEED -= 0.5
                PLAYER_SPEED += 0.4
                score += 1
                GREEN_CIRCLE_RECT.x = random.randint(0, 680)
                GREEN_CIRCLE_RECT.y = CIRCLE_Y

        if PLAYER_RECT.colliderect(RED_CIRCLE_RECT):
                RED_CIRCLE_SPEED -= 0.5
                PLAYER_SPEED += 0.4
                score -= 1
                RED_CIRCLE_RECT.x = random.randint(0, 680)
                RED_CIRCLE_RECT.y = CIRCLE_Y
                LIFES -= 1


        if GREEN_CIRCLE_RECT.y <= 900:
                GREEN_CIRCLE_RECT.y -= GREEN_CIRCLE_SPEED
        if RED_CIRCLE_RECT.y <= 900:
                RED_CIRCLE_RECT.y -= RED_CIRCLE_SPEED

        if GREEN_CIRCLE_RECT.y >= 900:
                GREEN_CIRCLE_RECT.x = random.randint(0, 680)
                GREEN_CIRCLE_RECT.y = CIRCLE_Y
                LIFES -= 1

        if RED_CIRCLE_RECT.y >= 900:
                RED_CIRCLE_RECT.x = random.randint(0, 680)
                RED_CIRCLE_RECT.y = CIRCLE_Y
        
    else:
        over_text = pygame.transform.scale2x(defalt_font.render('GAME OVER', False, (255, 255, 255)))
        one = pygame.transform.scale2x(defalt_font.render(f'{score}', False, (0, 0, 0)))
        two =  pygame.transform.scale2x(defalt_font.render(f'{score}', False, (255, 255, 255)))
        screen.blit(one, (350, 10))
        screen.blit(two, (349, 10))
        screen.blit(over_text, (250, 400))

    
    pygame.display.flip()


    dt = clock.tick(60) / 1000
