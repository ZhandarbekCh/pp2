import pygame
from random import randrange

pygame.init()
level=1
mon=800
size=50
fps=60
bg = pygame.image.load("bk.jpg")
bg=pygame.transform.scale(bg,(800,800)) 
x,y= 300,300
length=1
snake=[(x,y)]

buttons={
    'w':True,
    'a':True,
    'd':True,
    's':True
}

front=pygame.font.SysFont('Ariel',26,True)
count=0

walls={ #levels of wall,
    1:[(0,0),(50,0),(100,0),(150,0),(200,0),(250,0),(300,0),(350,0),(400,0),(450,0),(500,0),(550,0),(600,0),(650,0),(700,0),(0,50),(0,100),(0,150),(0,200),(0,250),(0,300),(0,350),(0,400),(0,450),(0,500),(0,550),(0,600),(0,650),(0,700)],
    2:[(700,700),(650,700),(700,650),(600,700),(700,600),(700,550),(650,550),(650,500)],
    3:[(50,50),(50,100),(50,150),(50,200),(150,0),(200,0),(250,0),(500,500),(550,500),(500,550),(600,500),(650,500)]
}

speed=7 #speed for clock
sup=10 #for 44,45 and also for 124 lines needed, for range to get does score go to range
score=2# point for every fruit
dx,dy=0,0 #direction 

clock=pygame.time.Clock()
time=50 

apple=randrange(50,mon,size),randrange(0,mon,size) #fruit spawn
while apple in walls:
    apple=randrange(50,mon,size),randrange(0,mon,size)

level1=9 #range 
level2=20

screen=pygame.display.set_mode([mon,mon])

score_font = pygame.font.SysFont("Verdana", 20)

working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False

        if event.type == pygame.KEYDOWN :# whole direction 
            if event.key == pygame.K_w and buttons['w']: # if ypu clicked w snake will move up, or dy will be equal to -1
                #а buttonsp['w'] needed when you you push s  you could not move up
                buttons={
                    'w':True,
                    'a':True,
                    'd':True,
                    's':False
                }
                dx,dy=0,-1
            elif event.key == pygame.K_s and buttons['s']:
                dx,dy=0,1
                buttons={
                    'w':False,
                    'a':True,
                    'd':True,
                    's':True
                }
            elif event.key == pygame.K_a and buttons['a']:
                dx,dy=-1,0
                buttons={
                    'w':True,
                    'a':True,
                    'd':False,
                    's':True
                }
            elif event.key == pygame.K_d and buttons['d']:
                dx,dy=1,0
                buttons={
                    'w':True,
                    'a':False,
                    'd':True,
                    's':True #sw
                }
    screen.blit(bg,(0,0)) #drawing background

    if snake[-1] in walls[level]: # if the coordinates of the head are in the coordinates of the walls, the game stops
        pygame.quit()

    if apple in walls[level]:#needed to check if the apple appeared inside the walls
        apple=randrange(50,mon,size),randrange(0,mon,size)

    [(pygame.draw.rect(screen,pygame.Color('blue'),(i,j,size-2,size-2))) for i, j in snake] #drawing snake 

    pygame.draw.rect (screen, pygame.Color('red'), (*apple, size-2,size-2))# drawing fruit

    for i in walls[level]:#we draw walls of a certain level
        pygame.draw.rect(screen,(0,0,0),(i[0],i[1],48,48))
    render_score=front.render(f'SCORE:{count}',1,pygame.Color('white'))#writing score
    screen.blit(render_score,(5,5))#drawing score

    if time ==0:#time for the case when the time for eating an apple has expired
        apple=randrange(50,mon,size),randrange(0,mon,size)
        time=50

    x+=dx*size#continuous movement
    y+=dy*size

    time-=1# every 50 speed we update the location of the apples, we need it for 111 lines
    snake.append((x,y))#coordinates of snake
   
    snake=snake[-length:]#in order for us to take only the snake, and not the places where it walked

    if count in range(level1,level2):#it is needed to transfer to the next level, as well as to increase the reward for the apple, speed,
        level1+=sup
        level2+=sup
        sup+=20
        level+=1
        score+=1
        speed+=2
        if level==4:level=1

    if snake[-1]==apple: #if the coordinate of the apples and the snake's head coincided
        count+=score
        length+=1
        time=50
        apple=randrange(50,mon,size),randrange(0,mon,size)

    if x<0 or x> mon-size or y<0 or y >mon-size or len(snake) != len(set(snake)): #going out of bounds or the snake enters itself
        working=False

    pygame.display.flip()
    clock.tick(speed)
