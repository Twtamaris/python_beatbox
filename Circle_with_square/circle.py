import turtle
import pygame
pygame.init()
x = 0 

t = turtle.Turtle()
hero = True
timer = pygame.time.Clock()


while hero:
    timer.tick()
    t.forward(100)
    t.right(90)
    x += 1
    if x % 4 == 0:
        t.right(7)
    
        
    

    
    
    