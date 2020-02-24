import pygame
import math
from vector import Vector


#Colors:
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

SCREEN_SIZE = 400
NUMBER_OF_LINES = 20
FAT_LINE_WIDTH = 3
REG_LINE_WIDTH = 1
VECTOR_WIDTH = 3
VECTOR_CIRCLE_RADIUS = 4
LINES_COLOR = BLACK
BACKGROUND_COLOR = WHITE

class Draw_vector():
    """
    class Draw_vector:
        Description:
            Class used for visualising vectors in pygame
        Methods:
            setupGrid:
                Draws a coordinate system on the screen
            mainloop:
                Infinite loop, which runs until the QUIT event is picked up
            drawVector:
                Draws a vector on the cordinate system, with a circle in the start position
            map:
                Maps a number x in [a,b] linearly to [c,d]
    """
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
        self.setupGrid()

    def setupGrid(self):
        """
        setupGrid:
            Description:
                Draws a coordinate system on the screen
            Inputs:
                None
            Return Value:
                None
        """
        self.surface.fill(BACKGROUND_COLOR)
        for i in range(0,SCREEN_SIZE,NUMBER_OF_LINES):
            if i == SCREEN_SIZE / 2:
                pygame.draw.line(self.surface, LINES_COLOR, (0,i),(SCREEN_SIZE,i),FAT_LINE_WIDTH)
                pygame.draw.line(self.surface, LINES_COLOR, (i,0),(i,SCREEN_SIZE),FAT_LINE_WIDTH)
                continue
            pygame.draw.line(self.surface, LINES_COLOR, (0,i),(SCREEN_SIZE,i),REG_LINE_WIDTH)
            pygame.draw.line(self.surface, LINES_COLOR, (i,0),(i,SCREEN_SIZE),REG_LINE_WIDTH)
        pygame.display.update()
    
    def mainloop(self):
        """
        mainloop:
            Description:
                Infinite loop, which runs until the QUIT event is picked up
            Inputs:
                None
            Return Value:
                None
        """
        while(1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    def drawVector(self, vector, start, color):
        """
        mainloop:
            Description:
                Draws a vector on the cordinate system, with a circle in the start position
            Inputs:
                vector: Vector to be drawn
                start: Start position of the vector as a vector from origo
                color: RGB value the vector should be drawn in
            Return Value:
                None
        """
        start_x = self.map(start.x, -NUMBER_OF_LINES //2,NUMBER_OF_LINES//2, 0, SCREEN_SIZE)
        start_y = self.map(start.y, -NUMBER_OF_LINES //2,NUMBER_OF_LINES//2, 0, SCREEN_SIZE)

        vector_x = vector.x * NUMBER_OF_LINES
        vector_y = vector.y * -NUMBER_OF_LINES

        startPos = (start_x, start_y)
        endPos = (start_x + vector_x, start_y+vector_y)

        pygame.draw.line(self.surface, color, startPos, endPos, VECTOR_WIDTH)
        pygame.draw.circle(self.surface, color, startPos, VECTOR_CIRCLE_RADIUS)
        pygame.display.update()
        

    def map(self,x,a,b,c,d):
        """
        map:
            Description:
                Maps a number x in [a,b] linearly to [c,d]
            Inputs:
                x = Number to be mapped
                a = Start of set where x exists
                b = End of set where x exists
                c = Start of set where x is to be mapped
                d = End of set where x is to be mapped
            Return Value:
                A new number X where the relation (x-a)/(b-a) = (X-c)/(d-c)
        """
        return (x-a)/(b-a) * (d-c)+ c
        

if __name__ == "__main__":
    #Minor tests to draw vectors on the screen
    vec = Draw_vector()
    vec.drawVector(Vector(-2,-2),Vector(0,0), RED)
    vec.drawVector(Vector(-2,2),Vector(0,0), RED)
    vec.drawVector(Vector(2,-2),Vector(0,0), RED)
    vec.drawVector(Vector(2,2),Vector(0,0), RED)

    vec.drawVector(Vector(2,2),Vector(3,4), BLUE)
    vec.mainloop()

    

