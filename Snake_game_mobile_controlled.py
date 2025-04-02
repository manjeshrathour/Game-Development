
import pygame
import random

import socket
import json
import pygame

# Pygame initialization
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game with Accelerometer')
FPS = 60
fpsClock = pygame.time.Clock()
background_color = (0, 139, 0)
snake_color = (0, 0, 255)
snake_posn_x = 400
snake_posn_y = 300
snake_height = 20
snake_width = 20
SPEED = 5

def update_snake(x, y, dx, dy):
    new_x = x + dx * SPEED
    new_y = y + dy * SPEED
    if new_x > 800:
        new_x = 0
    if new_x < 0:
        new_x = 800
    if new_y > 600:
        new_y = 0
    if new_y < 0:
        new_y = 600
    return new_x, new_y

def give_food_posn():
    return random.randint(0, 800), random.randint(0, 600)

def is_snake_near_food(snake_x, snake_y, food_x, food_y):
    return ((food_x - snake_x)**2 + (food_y - snake_y)**2)**0.5 < 20

food_x, food_y = give_food_posn()
food_radius = 7
food_color = [255, 0, 0]

dx, dy = 1, 0  # Initial movement direction

# UDP Server
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on port {UDP_PORT}...")

def onData(data):
    global dx, dy
    try:
        jsonData = json.loads(data.decode())
        if jsonData["type"] == "android.sensor.accelerometer":
            x, y, _ = jsonData["values"]
            if abs(x) > abs(y):  # Left or right movement
                dx = -1 if x < -1 else (1 if x > 1 else dx)
                dy = 0
            else:  # Up or down movement
                dy = -1 if y < -1 else (1 if y > 1 else dy)
                dx = 0
    except Exception as e:
        print(f"Error processing data: {e}")

# Game Loop
running = True
while running:
    display.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    try:
        data, _ = sock.recvfrom(1024)
        onData(data)
    except socket.error:
        pass
    snake_posn_x, snake_posn_y = update_snake(snake_posn_x, snake_posn_y, dx, dy)
    if is_snake_near_food(snake_posn_x, snake_posn_y, food_x, food_y):
        food_x, food_y = give_food_posn()
    pygame.draw.rect(display, snake_color, [snake_posn_x, snake_posn_y, snake_width, snake_height])
    pygame.draw.circle(display, food_color, (food_x, food_y), food_radius)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
sock.close()
