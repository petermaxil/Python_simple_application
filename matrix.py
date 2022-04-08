import pygame
import random as rand
import cv2
import keyboard

pygame.init()

WIDTH,HEIGHT=1920,1080
alpha_value=rand.randrange(30,40,5)
res=(WIDTH,HEIGHT)
FONT_SIZE=20

chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z']
font=pygame.font.SysFont('sans-serif',FONT_SIZE)
green_chars=[font.render(char,True,(0,255,0)) for char in chars]
screen=pygame.display.set_mode(res)
display_surface=pygame.Surface(res)

clock=pygame.time.Clock()

class Symbol:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=4
        self.value=rand.choice((green_chars))

    def draw(self):
        self.value=rand.choice(green_chars)
        self.y=self.y+self.speed if self.y <HEIGHT else -FONT_SIZE * rand.randrange(1,10)
        screen.blit(self.value,(self.x,self.y))

symbols=[Symbol(x,rand.randrange(-HEIGHT,0)) for x in range(0,WIDTH,FONT_SIZE)]

run=True

while run:
    screen.blit(display_surface,(0,0))
    display_surface.fill(pygame.Color('black'))
    [symbol.draw() for symbol in symbols]
    pygame.display.update()

    clock.tick(200)

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False

    if keyboard.is_pressed('q') or keyboard.is_pressed('esc'):  # if key 'q' is pressed
        print('You have been killed the task')
        break
