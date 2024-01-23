import pygame


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((720, 900))

jet_f1 = pygame.image.load("./assets/jet/sprite_0.png")
jet_f2 = pygame.image.load("./assets/jet/sprite_1.png")
jet_f3 = pygame.image.load("./assets/jet/sprite_2.png")
jet_f4 = pygame.image.load("./assets/jet/sprite_3.png")
jets = [jet_f1, jet_f2, jet_f3, jet_f4]


dt = 1
clock = pygame.time.Clock()
running = True

s = 0
while running:

    screen.fill("black")
    jet = jets[s]
    print(jet)
    screen.blit(jet, jet.get_rect())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if s >= 3:
        s = 0
    else:
        s+=1
    pygame.display.flip()


    dt = clock.tick(60) / 1000
