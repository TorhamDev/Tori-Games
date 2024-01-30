import pygame as pg 
from random import randint

pg.init()


clock = pg.time.Clock()

class Thing:
    def __init__(self, rect) -> None:
        self.rect = rect
        self.weight = randint(1, 5)

screen = pg.display.set_mode((800, 500))
end = False
things = []

def create_obj(x, y):
    things.append(Thing(rect=pg.Rect(x, y, 40, 40)))

dt = 0 
while not end:
    screen.fill("black")
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            end = True 
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event)
                print("YES")
                create_obj(*event.pos)
    
    for thing in things:
        thing.rect.clamp_ip(screen.get_rect())
        pg.draw.rect(screen, (255, 0, 0), thing.rect)
        thing.rect.y += thing.weight * 0.5



    pg.display.flip()
    dt = clock.tick(60) / 1000