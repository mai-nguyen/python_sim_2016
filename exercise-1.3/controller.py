from ellipse import Ellipse
import random

class Controller:
    def __init__(self):
        self.obj_list = list()
        for i in range(0, 20):
            newellipse = Ellipse(PVector(width/2, height/2), PVector(50, 80), PVector(random.random(), random.random()))
            self.obj_list.append(newellipse)
     
    def draw(self):
        background(99, 168, 191, 150)
        for ellipse in self.obj_list:
            ellipse.draw()
            ellipse.move()
       
