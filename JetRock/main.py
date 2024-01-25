import pygame


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((720, 900))

jet_f1 = pygame.transform.scale(pygame.image.load("./assets/jet/sprite_0.png"), (80, 80)).convert_alpha()
jet_f2 = pygame.transform.scale(pygame.image.load("./assets/jet/sprite_1.png"), (80, 80)).convert_alpha()
jet_f3 = pygame.transform.scale(pygame.image.load("./assets/jet/sprite_2.png"), (80, 80)).convert_alpha()
jet_f4 = pygame.transform.scale(pygame.image.load("./assets/jet/sprite_3.png"), (80, 80)).convert_alpha()
jets = [jet_f1, jet_f2, jet_f3, jet_f4]


dt = 1
clock = pygame.time.Clock()
running = True
ANIMATION_SPEED = pygame.USEREVENT
pygame.time.set_timer(ANIMATION_SPEED, 200)
s = 0
x = 1
bullets = []
def shoot(screen, x, y):
    bullet = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x + 42, y, 1, 20))
    bullets.append(bullet)
score = 0
while running:

    screen.fill("black")
    jet = jets[s]
    jet_rect = jet.get_rect()
    jet_rect.x = x
    jet_rect.y = 800
    jet_rect.clamp_ip(screen.get_rect())
    screen.blit(jet, jet_rect)
    enemy = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(42, 4, 40, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shoot(screen, jet_rect.x, jet_rect.y)
                
        if event.type == ANIMATION_SPEED:
                if s >= 3:
                    s = 0
                else:
                    s+=1
    
    if x == 0:
        x = 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 5 + dt
    if keys[pygame.K_d]:
        x += 5 + dt

    print(jet_rect.x)

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)
        bullet.y -= 4
        if bullet.colliderect(enemy):
            print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            score += 1
            bullets.remove(bullet)
        if bullet.y <= 10:
            bullets.remove(bullet)
        print(bullet.y)

    print(f"{score=}")
    pygame.display.flip()


    dt = clock.tick(60) / 1000
