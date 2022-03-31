import pygame
import sys
 
FPS = 60
W = 625  # ширина экрана
H = 625  # высота экрана
WHITE = (255, 255, 255)
RED = (255, 70, 0)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
UP="to the up"
DOWN="to the down"
 
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 25
 
motion = STOP
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            elif i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT,
                         pygame.K_RIGHT,
                         pygame.K_UP,
                         pygame.K_DOWN]:
                motion = STOP
 
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), r)
    pygame.display.update()
 
    if motion == LEFT and x>=40:
        x -= 20
    elif motion == RIGHT and x<=585:
        x += 20
    elif motion == UP and y>=40:
        y -= 20
    elif motion == DOWN and y<=585:
        y += 20    
 
    clock.tick(FPS)
