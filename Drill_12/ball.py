import random
from pico2d import *
import game_world
import game_framework



class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(20, 1000), random.randint(20, 1000)
        self.hp = 100

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

