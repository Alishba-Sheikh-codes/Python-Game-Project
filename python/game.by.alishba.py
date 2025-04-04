#libraries
import pygame
import random
import math

#initialization
pygame.init()

#screen, icon, caption
screen = pygame.display.set_mode ((800,600))
pygame.display.set_caption("Spaceship World")
ICON = pygame.image.load('spaceship.png')
pygame.display.set_icon(ICON)
score = 0
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)
game_over = False
clock = pygame.time.Clock()


#player 
Airplane = pygame.image.load('airplane.png')
Ax = 400
Ay = 400

#obstacle and clouds
Clouds = []
Cx = []
Cy = []
Obstacle = []
Ox = []
Oy = []
obstacleList = 6
obstaclespeed = 5

for i in range(obstacleList):
    Obstacle.append(pygame.image.load('obstacle.png')) 
    Ox.append(random.randint(0, 800))
    Oy.append(random.randint(-600, -50))

for i in range(obstacleList):
    cloud_img = pygame.image.load('cloud.png')
    cloud_img = pygame.transform.scale(cloud_img, (100, 100))  # Resize to 100x100 pixels
    Clouds.append(cloud_img)
    Cx.append(random.randint(0, 800))
    Cy.append(random.randint(-600, -50))    

def airplane(x, y):
    screen.blit(Airplane, (x, y))

def obstacle(x, y, i):
    screen.blit(Obstacle[i], (x, y))

def Cloud(x, y, i):
    screen.blit(Clouds[i], (x,y))     
    

def display_score(score):
    precaution = font.render("Keep the airplane safe from obstacles!!", True, (0,0,0))
    text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(precaution, (200, 10))
    screen.blit(text, (10, 10))

    

def display_game_over():
    photo = pygame.image.load('gameover.jpg')
    photo = pygame.transform.scale(photo, (800, 600))
    SCORE = large_font.render(f"Score = {score}", True, (0, 0,0) )
    screen.blit(photo, (0,0))
    screen.blit(SCORE, (275, 30))

def collision(Ox, Oy, Ax, Ay):
    distance = math.sqrt((math.pow(Ax - Ox, 2)) + (math.pow(Ay - Oy, 2)))
    if distance < 37:
        return True 
    else:
        return False

#game loop, where everything which we want to continue resides 
running = True
while running:
    screen.fill((0,191,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Ax -= 10
            if event.key == pygame.K_RIGHT:
                Ax += 10
            if event.key == pygame.K_UP:
                Ay -= 5
                obstaclespeed += 0.25  

        for i in range(obstacleList):
            Oy[i] += obstaclespeed 

            Cy[i] += obstaclespeed   
        #respawn obstacles if gets out of screen
            if Oy[i] > 600:
                Ox[i] = random.randint(0, 800)
                Oy[i] = random.randint(-600, -50)
                score += 1
            if Cy[i] > 600:
                Cx[i] = random.randint(0, 800)
                Cy[i] = random.randint(-600, -50)  
            Collision = collision(Ox[i], Oy[i], Ax, Ay)
            if Collision:
               game_over = True 
            
            Cloud(Cx[i], Cy[i], i)
            obstacle(Ox[i], Oy[i], i)

            display_score(score)
                
        airplane(Ax, Ay)
               
    else:
        display_game_over()

    pygame.display.update()
    clock.tick(60)       