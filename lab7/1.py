import pygame
from datetime import datetime
import math

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface,-angle,1)
    rotated_rect = rotated_surface.get_rect(center=(530,360))
    return rotated_surface, rotated_rect

def rotate2(surface2, angle2):
    rotated_surface2 = pygame.transform.rotozoom(surface2,-angle2,1)
    rotated_rect2 = rotated_surface2.get_rect(center=(540,370))
    return rotated_surface2, rotated_rect2

pygame.init()

W, H = 1080, 700

clock = pygame.time.Clock()
pygame.display.set_caption("mikey.jpg")
sc=pygame.display.set_mode((1080, 700))


mikey_surf = pygame.image.load("mikey.jpg")
mikey_rect = mikey_surf.get_rect(center=(W//2, H//2))

second = pygame.image.load("righthand1.png")
second_rect = second.get_rect(center=(500,280))
minute = pygame.image.load("lefthand1.png")
minute_rect2 = minute.get_rect(center=(500,280))

second=pygame.transform.scale(second,(500,400))
minute=pygame.transform.scale(minute,(500,500))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)
current_time = datetime.now()
second_now=current_time.second
minute_now=current_time.minute


angle = (5*second_now*1.2)-50
angle_min=(5*1.2*minute_now)+47

second_rotated,second_rotated_rect = rotate(second, angle)
minute_rotated2,minute_rotated_rect2 = rotate2(minute, angle_min)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(mikey_surf, mikey_rect)
    angle+=1.2
    angle_min+=0.02
    second_rotated,second_rotated_rect = rotate(second, angle)
    minute_rotated2,minute_rotated_rect2 = rotate2(minute, angle_min)
    sc.blit(second_rotated,second_rotated_rect)
    sc.blit(minute_rotated2,minute_rotated_rect2)

    pygame.display.flip()

    clock.tick(5)
