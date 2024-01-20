import pygame
import random

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((720, 900))
clock = pygame.time.Clock()
running = True
player_sepeed = 5

enemy_speed = -2
enemy_y = 10
enemy_x = 0
player_pos =  pygame.Rect(500, 30, 60, 60)
enemy_rec = pygame.Rect(enemy_y, enemy_x, 20, 20)
lifes = 10
score = 0
screen_rec = screen.get_rect()
is_over = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")
    if not is_over:
        if lifes <= 0:
            is_over = True

        screen.blit(my_font.render(f'Lifes : {lifes}', False, (255, 0, 0)), (0,0))
        screen.blit(my_font.render(f'Score : {score}', False, (0, 255, 0)), (0,24))
        pygame.draw.rect(screen, "red", player_pos)
        pygame.draw.rect(screen, "blue", enemy_rec)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= player_sepeed
        if keys[pygame.K_s]:
            player_pos.y += player_sepeed
        if keys[pygame.K_a]:
            player_pos.x -= player_sepeed
        if keys[pygame.K_d]:
            player_pos.x += player_sepeed
    

        player_pos.clamp_ip(screen_rec)

        if player_pos.colliderect(enemy_rec):
            enemy_speed -= 0.5
            player_sepeed += 0.4
            score += 1
            enemy_rec.x = random.randint(0, 680)
            enemy_rec.y = enemy_y

        if enemy_rec.y <= 900:
            enemy_rec.y -= enemy_speed

        if enemy_rec.y >= 900:
            enemy_rec.x = random.randint(0, 680)
            enemy_rec.y = enemy_y
            lifes -= 1
    else:
        screen.blit(my_font.render('GAME OVER', False, (255, 0, 0)), (screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(my_font.render(f'SCORE: {score}', False, (0, 255, 0)), (screen.get_width() // 2, (screen.get_height() // 2) + 24))

    

    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()