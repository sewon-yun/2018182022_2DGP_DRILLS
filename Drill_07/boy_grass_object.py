from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    pass

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image_small = load_image('ball21x21.png')
        self.image_big = load_image('ball41x41.png')
        self.discrimination = random.randint(0, 1)
        self.speed = random.randint(3, 10)
    def update(self):
        self.y += self.speed
        
    def draw(self):
        if self.discrimination == 0:
            self.image_small.clip_draw(0, 0, 21, 21, self.x, self.y)
        elif self.discrimination == 1:
            self.image_big.clip_draw(0, 0, 41, 41, self.x, self.y)
    pass
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

team = [Boy() for i in range(11)]

balls = [Ball() for i in range(20)]

grass = Grass()

running = True
# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)
# finalization code
close_canvas()