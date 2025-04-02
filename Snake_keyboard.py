import pygame
import random
pygame.init()      # Initializes all required pygame modules
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game')
FPS=30
fpsClock=pygame.time.Clock()  # Controls the game loop speed (FPS management).
background_color = (0,139,0)
snake_color=(0,0,255)
snake_posn_x = 400
snake_posn_y = 300
snake_height = 20
snake_width = 20
display.fill(background_color)
to_continue = True
SPEED = 5
'''
1 - left
2 - right
3 - up
4 - down
'''
what_direction =  2

def update_snake(x,y,dir):
    if(dir==1):
        new_x = x - SPEED
        new_y = y
    elif(dir==2):
        new_x = x + SPEED
        new_y = y
    elif(dir==3):
        new_x = x
        new_y = y - SPEED
    else :
        new_x = x
        new_y = y + SPEED
    if(new_x > 800):
        new_x = 0
    if(new_x < 0 ):
        new_x = 800
    if(new_y > 600):
        new_y = 0
    if(new_y < 0 ):
        new_y = 600
    return new_x,new_y

def give_food_posn():
    food_x = random.randint(0,800)
    food_y = random.randint(0,600)
    return food_x,food_y

food_x,food_y = give_food_posn()
food_radius = 7
food_color = [255,0,0]
is_food_present = True
pygame.draw.circle(display,food_color,(food_x,food_y),food_radius)

def is_snake_near_food(snake_x,snake_y,food_x,food_y):
    distance = ((food_x - snake_x)**2 + (food_y - snake_y)**2)**(0.5)
    #isme ** vo square ke liye use hota hai
    if(distance < 20):
        return True
    else:
        return False

while to_continue:
    display.fill(background_color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            to_continue=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                what_direction = 2
            if event.key == pygame.K_LEFT:
                what_direction = 1
            if event.key == pygame.K_UP:
                what_direction = 3
            if event.key == pygame.K_DOWN:
                what_direction = 4
    snake_posn_x,snake_posn_y =     update_snake(snake_posn_x,snake_posn_y,what_direction)
    if(is_snake_near_food(snake_posn_x,snake_posn_y,food_x,food_y)==True):
        food_x,food_y = give_food_posn()
    pygame.draw.rect(display, snake_color, [snake_posn_x, snake_posn_y, snake_width, snake_height])
    pygame.draw.circle(display, food_color, (food_x, food_y), food_radius)
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
quit()
