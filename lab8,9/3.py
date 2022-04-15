from math import sqrt
import pygame
from random import randint

pygame.init()

#Global Variables:
WIDTH, HEIGHT = 800, 600


#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

#Initializing:
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

drawing = False

color = BLACK

#Functions for each drawing:
def drawRect(color, pos, width, height):  
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4) 

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

def square(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)

def r_triangle(color, z,x): #on the notebook I drew a graph of a right triangle, and from there, 
                            #thanks to this, I deduced the formula for the triangle itself
    x1=z[0]                 
    x2=x[0]                 
    y1=z[1]
    y2=x[1]
    pygame.draw.line(screen,color,z,x,2)
    pygame.draw.line(screen,color,(x1,y1),(x1,y2),2)
    pygame.draw.line(screen,color,(x1,y2),(x2,y2),2)


def romb(color, z,x):    #for rhombus, I could not find the formula thanks to the method of selecting each option, I roughly wrote the formula
    x1=z[0]
    x2=x[0]
    delta=(abs(x1-x2)//2)//sqrt(3)
    y1=z[1]
    y2=x[1]
    pygame.draw.line(screen,color,(x1,y1),(x1-(delta),y2),2)
    pygame.draw.line(screen,color,(x1-(delta),y2),(x2-(delta),y2),2)
    pygame.draw.line(screen,color,(x1,y1),(x2,y1),2)
    pygame.draw.line(screen,color,(x2-(delta),y2),(x2,y1),2)


def e_triangle(color,z,x):               #так же произошли трудности с правильным треугольником, +- вывел формулу и подставил  в pygame.draw.line
    x1=z[0]
    x2=x[0]
    y1=z[1]
    y2=x[1]

    pygame.draw.line(screen,color,z,x,2)
    
    deltax=abs(x2-x1)
    deltay=abs(y2-y1)
    x4=(deltax+x1)
    y4=(deltay+y1)
    
    y4+=deltax

    pygame.draw.line(screen,color,(x4,y4),x,2)
    pygame.draw.line(screen,color,z,(x4,y4),2)
RAD = 30


screen.fill(WHITE)
# the beggining and the end of the triangle during drawing
start_pos = 0
end_pos = 0

#Mode changes:
# 0 - Rect
# 1 - Circle
# 2 - Eraser
mode = 0

#List which contains 20 colours - to change colour
all_colors = []

for _ in range(20):
    all_colors.append((randint(0,255), randint(0,255), randint(0,255)))


while not finished:

    pos = pygame.mouse.get_pos() #the position where the cursor is located 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit from programm
            finished = True
        
        #Colour choose:
        if event.type == pygame.MOUSEBUTTONDOWN:#mouse was pressed
            drawing = True
            start_pos = pos #the beggining of mouse press

            if pos[0] > 20 and pos[0] < 720 and pos[1] > 20 and pos[1] < 40: #colour choose 
                color = screen.get_at(pos)
       
        if event.type == pygame.MOUSEBUTTONUP: #pressing of mouse stopped 
            drawing = False
            end_pos = pos# recording the end of the mouse click

            rect_x = abs(start_pos[0] - end_pos[0]) #x pressed
            rect_y = abs(start_pos[1] - end_pos[1]) #y pressed
            
            if mode == 0:                              #mode choose
                 drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)
            elif mode==3:
                if rect_x<rect_y:rect_x=rect_y
                square(color, start_pos, rect_x, rect_x)
            elif mode==4:
                r_triangle(color, start_pos,end_pos)
            elif mode==5:
                e_triangle(color, start_pos,end_pos)
            elif mode==6:
                romb(color, start_pos,end_pos)

        if event.type == pygame.MOUSEMOTION and drawing:  #eraser 
            if mode == 2:
                eraser(pos, RAD)
        
        if event.type == pygame.KEYDOWN:               #when you click on space, we will move on to the next mod
            if event.key == pygame.K_SPACE:             #and if we press the space bar again on mod 6, then we will be thrown to mod 1(0)
                mode += 1
                if mode==7:mode=0
            if event.key == pygame.K_BACKSPACE:      #when you click on the backspace, the entire screen is cleared
                screen.fill(WHITE)

    w = 30  # the size of the quadrilaterals that store all of our 20 colors
   
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * w, 20, w, 20)) #colours
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
