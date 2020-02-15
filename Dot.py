import pygame

import math



GREEN = (20, 255, 140)

GREY = (210, 210 ,210)

WHITE = (255, 255, 255)

RED = (255, 0, 0)

PURPLE = (255, 0, 255)

BLUE = (0, 0, 255)

BLACK = (0, 0, 0)





class Dot(pygame.sprite.Sprite):

    # This class represents a car. It derives from the "Sprite" class in Pygame.



    def __init__(self, color, width, height):

        # Call the parent class (Sprite) constructor

        super().__init__()



        # Pass in the color of the car, and its x and y position, width and height.

        # Set the background color and set it to be transparent

        self.image = pygame.Surface([width, height])

        self.image.fill(WHITE)

        self.image.set_colorkey(WHITE)

        self.color = color

        self.width = width

        self.height = height

        self.movement = []



        

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


        self.rect = self.image.get_rect()

    def update(self):
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        
       


    def up(self):
        self.rect.y -= 5

    def down(self):
        self.rect.y += 5

    def left(self):
        self.rect.x -= 5

    def right(self):
        self.rect.x += 5



