import time
import pygame
import os
pygame.font.init()



[width, height] = [800, 500]
[spaceship_width, spaceship_height] = [40, 40]


SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (width, height))

health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('comicsans', 100)


WIN = pygame.display.set_mode((width, height))

pygame.display.set_caption('Hello Brother')
pygame.display.set_mode((width, height))

fps = 60
vel = 5
bullet_vel = 7
max_bullet = 1000

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2



yellow_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
red_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

small_y_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship, (spaceship_width, spaceship_height)), 90) 
small_r_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (spaceship_width, spaceship_height)), 270) 



white = (25, 31, 84)
black = (0, 0 , 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
WHITE = (5, 252, 44)


border = pygame.Rect(width/2-5, 0, 10, height)

 
 

def game_window(yellow_x, red_x, yellow_y, red_y, r_bullets, y_bullets,red_health, yellow_health,):
    
    WIN.blit(SPACE, (0,0))
    
    
    WIN.blit(small_y_spaceship, (yellow_x, yellow_y))
    WIN.blit(small_r_spaceship, (red_x, red_y))
    pygame.draw.rect(WIN, black, border)
    

    
    for i in y_bullets:
        if i.x < width and y_bullets.index(i)%2 == 0:
    
            i.x += bullet_vel
        
            
            pygame.draw.rect(WIN,yellow, i)
            
        if i.x < width and y_bullets.index(i)%2 != 0:
    
            i.x += bullet_vel
        
            
            pygame.draw.rect(WIN,white, i)
 
        
                

    for i in r_bullets:
        
        if i.x > 0 and r_bullets.index(i)%2 == 0:
            i.x -= bullet_vel
            pygame.draw.rect(WIN,red, i)
            
        if i.x > 0 and r_bullets.index(i)%2 != 0:
            i.x -= bullet_vel
            pygame.draw.rect(WIN,white, i)
            
        
        
            
                
    for i in r_bullets:
        for j in y_bullets:
            if i.colliderect(j):
                i.x = 0
                j.x = width
    
    
    red_health_text = health_font.render('Health: ' + str(red_health), 1, WHITE )
    yellow_health_text = health_font.render('Health: ' + str(yellow_health), 1, WHITE )
    WIN.blit(red_health_text, ((3*width)/4 - red_health_text.get_width()/2, 10))
    WIN.blit(yellow_health_text, (width/4 - yellow_health_text.get_width()/2, 10))
              

    pygame.display.update()
    

def main():
    yellow_x = 200
    red_x = 600
    yellow_y = 250
    red_y = 250
   
    
    r_bullets = []
    y_bullets = []
    red_health = 200
    yellow_health = 200
    
    
    
    
    
    clock = pygame.time.Clock()
    real = True
    z = 0

    while real:
        
        clock.tick(fps)
        keys_pressed = pygame.key.get_pressed()
        
        y_bullet = pygame.Rect(yellow_x+spaceship_width, yellow_y+spaceship_height/2 -2, 20, 5)
        r_bullet = pygame.Rect(red_x - 10, red_y + spaceship_height/2 -2, 15, 5)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                real = yy
                pygame.quit()
                
                
            
                
                
        winner_text =''
        if red_health <= 0:
            winner_text = 'Yellow Wins!'
            
        if yellow_health <= 0:
            winner_text = 'Red Wins'
            
        if winner_text != '':
            draw_text = winner_font.render(winner_text, 1, WHITE)
            WIN.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            main()
        
        
        
            
                
                
            
                
                
                

                
        #for red movement        
        if keys_pressed[pygame.K_a] and yellow_x > 0:
            yellow_x -= vel
        if keys_pressed[pygame.K_d] and yellow_x + spaceship_width < border.x:
            yellow_x += vel
        if keys_pressed[pygame.K_w] and yellow_y > 0:
            yellow_y -= vel
        if keys_pressed[pygame.K_s] and yellow_y + 40 < height :
            yellow_y += vel
            
            
        #for yellow movement
        if keys_pressed[pygame.K_UP] and red_y > 0 :
            red_y -= vel
        if keys_pressed[pygame.K_DOWN] and red_y + 40 < height:
            red_y += vel
        if keys_pressed[pygame.K_LEFT] and red_x > border.x + 10:
            red_x -= vel
        if keys_pressed[pygame.K_RIGHT] and red_x + 40 < width:
            red_x += vel

            
        if keys_pressed[pygame.K_ESCAPE]:
            real = False
            
            #bullet moving
        if keys_pressed[pygame.K_LCTRL]:
            
            if len(y_bullets) < max_bullet*2:
                y_bullets.append(y_bullet)
  
        if keys_pressed[pygame.K_RCTRL]:
            if len(r_bullets) < max_bullet*2:
                r_bullets.append(r_bullet)
                
        for i in y_bullets:
            if i.x < width and y_bullets.index(i)%2 == 0:
                if i.x + 25 > red_x  and i.x+ 15 < red_x + width and i.y > red_y and i.y +5 < red_y + spaceship_height:
                    red_health -= 1
                    y_bullets.remove(i)
                     
                    
        for i in r_bullets:
            if i.x > 0 and r_bullets.index(i)%2 == 0:
                if i.x  < yellow_x + spaceship_width + 5 and i.x + 15 > yellow_x and i.y + 5 > yellow_y and i.y + 5 < yellow_y + spaceship_height:
                    yellow_health -= 1
                    r_bullets.remove(i)
        
        
        
                    
        
                    
                
            
        
                
                
        
                    
        game_window(yellow_x, red_x, yellow_y, red_y, r_bullets, y_bullets,red_health, yellow_health)
        
                    
                
            
        
        pygame.display.update()
    
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    main()
    
    

    
