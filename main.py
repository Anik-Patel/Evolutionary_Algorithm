import pygame
from Dot import Dot
import random
import math
import time


GREEN = (20, 255, 140)

GREY = (210, 210 ,210)

WHITE = (255, 255, 255)

RED = (255, 0, 0)

PURPLE = (255, 0, 255)

BLUE = (0, 0, 255)



SCREENWIDTH = 1000

SCREENHEIGHT = 1000

pygame.font.init()

font = pygame.font.Font('freesansbold.ttf', 32) 

text = font.render('Generation:', True, GREEN, WHITE) 

textRect = text.get_rect()  

textRect.center = (100, 100)


size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Genetic Algorithm")

population = pygame.sprite.Group()

goal = pygame.sprite.Group()

obstacles = pygame.sprite.Group()



obstacle = Dot(GREEN, 550 ,20)
obstacle.rect.x = 0
obstacle.rect.y = 700
obstacles.add(obstacle)


obstacle = Dot(GREEN, 550,20)
obstacle.rect.x = 500
obstacle.rect.y = 300
obstacles.add(obstacle)
obstacle = 0



g = Dot(RED, 20, 20)
g.rect.x = 500
g.rect.y = 100
goal.add(g)

for i in range(1000):
    dot = Dot(BLUE, 20, 20)
    dot.rect.x = 500
    dot.rect.y = 900

    population.add(dot)
    dot = 0


clock = pygame.time.Clock()




carryOn = True


for dot in population:
    for i in range(3500):
        gh = random.randint(1, 4)
        if gh == 1:
            dot.movement.append(1)

        if gh == 2:
            dot.movement.append(2)

        if gh == 3: 
            dot.movement.append(3)

        if gh == 4:
            dot.movement.append(4)

    #print(len(dot.movement))




def execxute_moves(count):
    
    #o = obstacles.sprites()[0]
    for dot in population:
        for o in obstacles:
            if o.rect.colliderect(dot.rect):
                dot.kill()
        
        x = dot.movement[count]
        if x == 1:
            dot.up()
        if x == 2:
            dot.down()
        if x == 3:
            dot.left()
        if x == 4:
            dot.right()

        


def calculate_fitest():
    best_fitness = 0
    global fitness
    
    best_move_set = []
    count = 0
    for dot in population:
        x1 = dot.rect.x
        y1 = dot.rect.y
        x2 = goal.sprites()[0].rect.x
        y2 = goal.sprites()[0].rect.y
        dist = math.hypot(x1-x2, y1-y2)
        g = goal.sprites()[0]
        o = obstacles.sprites()[0]
        if g.rect.colliderect(dot.rect):
            fitness += 100
           
                            
        
        else:
            fitness = 2000/dist
        
        if fitness > best_fitness:
            best_fitness = fitness
            best_move_set = dot.movement


        count += 1

    return best_move_set


def mutate(array):
    new_array = []
    #print(array)
    for i in array:
        if random.randint(0, 15) == 1:
            new_array.append(random.randint(0, 4))

        else:
            new_array.append(i)

    #print(new_array)
    return new_array


def create_new_population():
    global population
    best = calculate_fitest()
    mutated = []

    for i in population:
        population = pygame.sprite.Group()

    for i in range(500):
        dot = Dot(BLUE, 20, 20)
        dot.rect.x = 500
        dot.rect.y = 900
        mutated = mutate(best)
        dot.movement = mutated
        #print(dot.movement)

        population.add(dot)



gen = 0
name = "Generation: "+str(gen)
text = font.render(name, True, GREEN, WHITE)

screen.blit(text, textRect)

while carryOn:
    name = "Generation: "+str(gen)
    text = font.render(name, True, GREEN, WHITE)
    screen.blit(text, textRect)

    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            carryOn = False

    

    c = 0
    n = population.sprites()[0]
    length = len(n.movement)
    #print(length)
    for i in range(length):
        execxute_moves(c)
        
    
        if c % 10 == 0:
            goal.update()
            population.update()
            obstacles.update()
            screen.fill(WHITE)
            population.draw(screen)
            goal.draw(screen)
            obstacles.draw(screen)
            screen.blit(text, textRect)
            pygame.display.flip()
            clock.tick(60)

        c+= 1

    
    

    
    create_new_population()
    
    
    gen += 1



   



pygame.quit()





