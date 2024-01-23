import pygame
pygame.init()
import random
# crash_sound = pygame.mixer.Sound("./s.mp3")
# pygame.mixer.Sound.play(crash_sound)
# pygame.mixer.music.stop()

clock = pygame.time.Clock()
running = True
screen = pygame.display.set_mode((400, 520))
rect1 = pygame.Rect(80, 80, 40, 40)
rect2 = pygame.Rect(130, 20, 40, 40)
rect3 = pygame.Rect(180, 140, 40, 40)
rect4 = pygame.Rect(220, 190, 40, 40)
crash_sound = pygame.mixer.Sound("idk/s.mp3")

dt = 0
move_letf = False

border_closing_event = pygame.USEREVENT + 1
timer_interval = 350  # Adjust this value to control the speed of the borders closing
pygame.time.set_timer(border_closing_event, timer_interval)

class MoveRect:
    def __init__(self, rect) -> None:
        self.rect = rect
        self.move_left = False
        self.speed = 1

rects = {
    "rect1": MoveRect(rect1),
    "rect2": MoveRect(rect2),
    "rect3": MoveRect(rect3),
    "rect4": MoveRect(rect4)
}
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for rect_name, rect in rects.items():
        print(rect_name, rect.rect.x, rect.rect.y, rect.move_left)
        rect.rect.clamp_ip(screen.get_rect())
        window_size = pygame.display.get_window_size()

        if rect.rect.x <= 0:
            
            pygame.mixer.Sound.play(crash_sound)
            pygame.mixer.music.stop()
            rect.move_left = False
            rect.speed = random.randint(1, 10)
            
        if rect.rect.x >= window_size[0]-40:
            pygame.mixer.Sound.play(crash_sound)
            pygame.mixer.music.stop()
            rect.move_left = True
            rect.speed = random.randint(1, 10)

        
        if rect.move_left:
            rect.rect.x -= rect.speed



        if rect.move_left is False:
            rect.rect.x += rect.speed

        
        if event.type == border_closing_event:
            if window_size[0] > 150:
                pygame.display.set_mode((window_size[0]-0.1,window_size[1]-0.1))


    screen.fill("black")
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)
    pygame.draw.rect(screen, (0, 0, 255), rect3)
    pygame.draw.rect(screen, (255, 255, 255), rect4)



     

    pygame.display.flip()


    dt = clock.tick(60) / 1000
